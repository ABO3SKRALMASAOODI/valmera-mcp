"""Retime a numbered UTF-8 SRT for one or more deletions on the original clock."""
import argparse
from pathlib import Path
import re
import sys

from check_srt_revision import milliseconds, read_cues


def source_time(value):
    """Read nonnegative seconds with at most millisecond precision."""
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,3})?", value):
        raise argparse.ArgumentTypeError("Use original seconds, e.g. 1.450")
    whole, _, fraction = value.partition(".")
    return 1000 * int(whole) + int(fraction.ljust(3, "0"))


def removed_ranges(pairs):
    merged = []
    for start, end in sorted(pairs):
        if end <= start:
            raise ValueError("Each removal needs an end later than its start")
        if merged and start <= merged[-1][1]:
            merged[-1] = merged[-1][0], max(end, merged[-1][1])
        else:
            merged.append((start, end))
    return merged


def new_time(time, cuts):
    return time - sum(max(0, min(time, end) - start) for start, end in cuts if start < time)


def stamp(time):
    seconds, ms = divmod(time, 1000)
    minutes, sec = divmod(seconds, 60)
    hours, minute = divmod(minutes, 60)
    return f"{hours:02d}:{minute:02d}:{sec:02d},{ms:03d}"


def retime(cues, cuts):
    blocks, changes = [], []
    for cue in cues:
        start, end = milliseconds(cue.start), milliseconds(cue.end)
        left, right = new_time(start, cuts), new_time(end, cuts)
        if right == left:
            changes.append(f"Dropped source cue {cue.number} (entirely inside a removal).")
            continue
        number = len(blocks) + 1
        if right - left < end - start:
            changes.append(f"Review source cue {cue.number} at output {stamp(left)} (cue {number}): a cut crosses its text.")
        blocks.append("\n".join([str(number), f"{stamp(left)} --> {stamp(right)}", *cue.lines]))
    return "\n\n".join(blocks) + ("\n" if blocks else ""), changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("srt", type=Path, help="Original numbered SubRip file")
    parser.add_argument("--remove", action="append", nargs=2, required=True, metavar=("START", "END"),
                        type=source_time, help="Removed interval in original seconds; repeat for additional cuts")
    args = parser.parse_args()
    try:
        cuts = removed_ranges(args.remove)
        output, changes = retime(read_cues(args.srt), cuts)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Could not retime subtitles: {error}\n")
    for message in changes:
        print(message, file=sys.stderr)
    sys.stdout.buffer.write(output.encode("utf-8"))


if __name__ == "__main__":
    main()
