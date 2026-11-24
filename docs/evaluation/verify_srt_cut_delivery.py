"""Check delivered SubRip tracks against the original subtitles and a list of removed intervals."""

import argparse
from pathlib import Path

from check_srt_revision import milliseconds, read_cues
from retime_srt_after_cuts import new_time, removed_ranges, source_time, stamp


def expected_cues(path, cuts):
    expected = []
    for cue in read_cues(path):
        start = new_time(milliseconds(cue.start), cuts)
        end = new_time(milliseconds(cue.end), cuts)
        if end > start:
            expected.append((start, end, cue.lines))
    return expected


def delivered_cues(path, expected):
    if not expected and not path.read_text(encoding="utf-8-sig").strip():
        return []
    return [(milliseconds(cue.start), milliseconds(cue.end), cue.lines) for cue in read_cues(path)]


def check_pair(language, before, after, cuts):
    expected = expected_cues(Path(before), cuts)
    delivered = delivered_cues(Path(after), expected)
    if len(delivered) != len(expected):
        print(f"{language}: expected {len(expected)} cues, found {len(delivered)}.")
        return False

    matches = True
    for index, (reference, actual) in enumerate(zip(expected, delivered), start=1):
        start, end, lines = reference
        delivered_start, delivered_end, delivered_lines = actual
        if (start, end) != (delivered_start, delivered_end):
            print(f"{language} cue {index}: expected {stamp(start)} to {stamp(end)}, "
                  f"found {stamp(delivered_start)} to {stamp(delivered_end)}.")
            matches = False
        if lines != delivered_lines:
            print(f"{language} cue {index}: text differs.")
            matches = False
    if matches:
        print(f"{language}: {len(expected)} cues match the declared removals.")
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remove", action="append", nargs=2, required=True, type=source_time,
                        metavar=("START", "END"), help="Removed interval in original seconds")
    parser.add_argument("--pair", action="append", nargs=3, required=True,
                        metavar=("LANGUAGE", "ORIGINAL", "DELIVERED"),
                        help="Repeat for each language and its two subtitle files")
    args = parser.parse_args()
    try:
        cuts = removed_ranges(args.remove)
        results = [check_pair(language, before, after, cuts) for language, before, after in args.pair]
    except (OSError, ValueError) as error:
        parser.exit(2, f"Cannot check delivery: {error}\n")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
