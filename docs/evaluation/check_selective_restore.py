"""Compare source ranges before and after a targeted edit revision."""

import argparse
import json
from decimal import Decimal, InvalidOperation


def read_ranges(value):
    ranges = json.loads(value, parse_float=Decimal, parse_int=Decimal)
    if not isinstance(ranges, list):
        raise ValueError("Use a JSON array of [start, end] pairs in source seconds.")
    previous_end = Decimal(0)
    for pair in ranges:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("Use a JSON array of [start, end] pairs in source seconds.")
        start, end = pair
        if not all(isinstance(point, Decimal) and point.is_finite() for point in pair):
            raise ValueError("Each range endpoint must be a finite number.")
        if not previous_end <= start < end:
            raise ValueError("List positive-length source ranges in order without overlap.")
        previous_end = end
    return [tuple(pair) for pair in ranges]


def merge_ranges(ranges):
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1]:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged


def format_ranges(ranges):
    return ", ".join(f"{start:f}–{end:f}" for start, end in ranges) or "(empty)"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", help="JSON retained ranges from the approved cut")
    parser.add_argument("after", help="JSON retained ranges from the candidate revision")
    parser.add_argument("start", help="start of the requested restore in source seconds")
    parser.add_argument("end", help="end of the requested restore in source seconds")
    args = parser.parse_args()

    try:
        before = read_ranges(args.before)
        after = read_ranges(args.after)
        start, end = Decimal(args.start), Decimal(args.end)
        if not (start.is_finite() and end.is_finite() and 0 <= start < end):
            raise ValueError("Provide a finite restore range with 0 <= start < end.")
    except InvalidOperation:
        parser.error("The restore endpoints must be numbers in source seconds.")
    except ValueError as error:
        parser.error(str(error))

    expected = merge_ranges(before + [(start, end)])
    actual = merge_ranges(after)
    added = sum(end - start for start, end in expected) - sum(end - start for start, end in before)
    print(f"Expected retained source seconds: {format_ranges(expected)}")
    print(f"Actual retained source seconds:   {format_ranges(actual)}")
    print(f"Expected newly restored seconds:  {added:f}")
    if actual != expected:
        print("Source coverage differs from the requested restoration.")
        return 1
    print("Source coverage matches. Review the rendered video, sound and captions separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
