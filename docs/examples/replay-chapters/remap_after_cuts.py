"""Map source chapter starts to a straight-cut, normal-speed replay."""
import argparse
from pathlib import Path
import sys

from chapters import seconds


def cut_intervals(text, source_duration):
    ranges = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 2:
            raise ValueError(f"Cut line {line_number}: expected start and end times")
        start, end = map(seconds, fields)
        if not 0 <= start < end <= source_duration:
            raise ValueError(f"Cut line {line_number}: range lies outside the source or has no duration")
        ranges.append((start, end))

    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1]:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged


def format_clock(total):
    hours, minute_seconds = divmod(total, 3600)
    minutes, second = divmod(minute_seconds, 60)
    return f"{hours}:{minutes:02d}:{second:02d}" if hours else f"{minutes:02d}:{second:02d}"


def remap(chapter_text, cut_text, source_duration):
    cuts = cut_intervals(cut_text, source_duration)
    removed_seconds = sum(end - start for start, end in cuts)
    if not 0 <= removed_seconds < source_duration:
        raise ValueError("The replay must keep at least one second of the source")

    mapped = []
    review = []
    previous = -1
    for line_number, line in enumerate(chapter_text.splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split(maxsplit=1)
        if len(fields) != 2:
            raise ValueError(f"Chapter line {line_number}: expected start time and title")
        clock, title = fields
        current = seconds(clock)
        if not previous < current < source_duration:
            raise ValueError(f"Chapter line {line_number}: starts must be ordered and inside the source")
        previous = current
        if any(start <= current < end for start, end in cuts):
            review.append(f"Review removed chapter {clock} {title}")
            continue
        removed_before = sum(end - start for start, end in cuts if end <= current)
        mapped.append((current - removed_before, title))

    if not mapped:
        raise ValueError("No chapter starts survived. Choose new starts from the edited playback")
    if mapped[0][0] != 0:
        review.append("If the destination requires a 00:00 chapter, name it after inspecting the opening")
    return mapped, review, source_duration - removed_seconds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_chapters", type=Path, help="One source time and title per line")
    parser.add_argument("removed_ranges", type=Path, help="One source start and end per line")
    parser.add_argument("source_duration", help="Original runtime as MM:SS or H:MM:SS")
    args = parser.parse_args()
    try:
        mapped, review, duration = remap(
            args.source_chapters.read_text(encoding="utf-8-sig"),
            args.removed_ranges.read_text(encoding="utf-8-sig"),
            seconds(args.source_duration),
        )
    except (ValueError, OSError) as exc:
        parser.exit(2, f"{parser.prog}: {exc}\n")

    for start, title in mapped:
        print(f"{format_clock(start)} {title}")
    for item in review:
        print(item, file=sys.stderr)
    print(f"Replay duration before added title cards or endings: {format_clock(duration)}", file=sys.stderr)


if __name__ == "__main__":
    main()
