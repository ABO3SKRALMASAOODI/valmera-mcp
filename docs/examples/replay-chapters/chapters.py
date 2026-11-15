"""Convert chapter starts from a finished replay into FFmpeg chapter metadata."""
import argparse
from pathlib import Path


def seconds(clock):
    parts = clock.split(":")
    if len(parts) not in (2, 3) or not all(p.isascii() and p.isdigit() for p in parts):
        raise ValueError(f"Expected MM:SS or H:MM:SS, got {clock!r}")
    if any(len(p) != 2 or int(p) >= 60 for p in parts[1:]):
        raise ValueError(f"Invalid clock {clock!r}")
    total = 0
    for part in parts:
        total = total * 60 + int(part)
    return total


def metadata(text, duration):
    chapters = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        fields = line.strip().split(maxsplit=1)
        if len(fields) != 2:
            raise ValueError(f"Line {line_no} needs a timestamp and chapter title")
        start = seconds(fields[0])
        if not chapters and start != 0:
            raise ValueError("The first chapter must start at 00:00")
        if chapters and start <= chapters[-1][0]:
            raise ValueError(f"Line {line_no} must start after the preceding chapter")
        if start >= duration:
            raise ValueError(f"Line {line_no} starts at or after the end of the file")
        chapters.append((start, fields[1]))
    if not chapters:
        raise ValueError("Supply at least one chapter")
    lines = [";FFMETADATA1"]
    ends = [start for start, _ in chapters[1:]] + [duration]
    for (start, title), end in zip(chapters, ends):
        escaped = "".join(("\\" + c) if c in "\\#;=" else c for c in title)
        lines.extend(("[CHAPTER]", "TIMEBASE=1/1000", f"START={1000 * start}",
                      f"END={1000 * end}", f"title={escaped}"))
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("list_file", type=Path, help="UTF-8 file of chapter starts and titles")
    parser.add_argument("duration", help="Final playback duration, to a whole second")
    args = parser.parse_args()
    try:
        print(metadata(args.list_file.read_text(encoding="utf-8-sig"), seconds(args.duration)))
    except (ValueError, OSError) as exc:
        parser.exit(2, f"{parser.prog}: {exc}\n")
