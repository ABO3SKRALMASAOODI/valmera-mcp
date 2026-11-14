"""Compare two UTF-8 numbered SRT files for a wording-only handoff."""

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Cue:
    number: int
    start: str
    end: str
    lines: tuple


STAMP = r"[0-9]{2,}:[0-5][0-9]:[0-5][0-9],[0-9]{3}"
TIMING = re.compile(rf"({STAMP})[ \t]+-->[ \t]+({STAMP})")


def milliseconds(stamp):
    hours, minutes, seconds, fraction = map(int, re.split("[:,]", stamp))
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + fraction


def read_cues(path):
    source = path.read_text(encoding="utf-8-sig").strip("\n")
    cues = []
    seen = set()
    for block in re.split(r"\n[ \t]*\n(?:[ \t]*\n)*", source):
        lines = block.split("\n")
        position = len(cues) + 1
        if len(lines) < 3 or not re.fullmatch(r"[0-9]+", lines[0]):
            raise ValueError(f"{path}: expected a numbered, nonempty cue at block {position}")
        timing = TIMING.fullmatch(lines[1])
        if not timing:
            raise ValueError(f"{path}: unsupported timestamp line in block {position}")
        start, end = timing.groups()
        number = int(lines[0])
        if number in seen or milliseconds(start) >= milliseconds(end):
            raise ValueError(f"{path}: repeated cue number or invalid duration at block {position}")
        # A missing blank separator can otherwise hide an entire cue inside text.
        if any(TIMING.fullmatch(line) for line in lines[2:]) or not any(line.strip() for line in lines[2:]):
            raise ValueError(f"{path}: missing separator or empty text at block {position}")
        seen.add(number)
        cues.append(Cue(number, start, end, tuple(lines[2:])))
    return cues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("revised", type=Path)
    args = parser.parse_args()
    try:
        original, revised = map(read_cues, (args.original, args.revised))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Cannot compare files: {exc}\n")
    if [cue.number for cue in original] != [cue.number for cue in revised]:
        print(f"Cue structure differs ({len(original)} original, {len(revised)} revised). "
              "Check cue numbers, splits, joins and ordering before comparing wording.")
        return 1

    text_changes = timing_changes = 0
    for before, after in zip(original, revised):
        if (milliseconds(before.start), milliseconds(before.end)) != (
            milliseconds(after.start), milliseconds(after.end)
        ):
            timing_changes += 1
            print(f"Cue {before.number} timing: {before.start} --> {before.end} "
                  f"became {after.start} --> {after.end}")
        if before.lines != after.lines:
            text_changes += 1
            print(f"Cue {before.number} text at {after.start}:")
            for prefix, lines in [("-", before.lines), ("+", after.lines)]:
                for line in lines:
                    print(f"  {prefix} {line!r}")
    print(f"{len(original)} cues compared. Text changed in {text_changes}. Timing changed in {timing_changes}.")
    return 1 if timing_changes else 0


if __name__ == "__main__":
    raise SystemExit(main())
