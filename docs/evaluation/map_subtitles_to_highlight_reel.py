"""Map SubRip cue times through a 1x-speed editorial cut map."""

import argparse
import csv
import re
import sys
from decimal import Decimal, DecimalException
from pathlib import Path


SOURCE_START = "Source start (seconds)"
SOURCE_END = "Source end (seconds)"
OUTPUT_START = "Output start (seconds)"
OUTPUT_END = "Output end (seconds)"
CLOCK = r"\d{2,}:[0-5]\d:[0-5]\d,\d{3}"
TIMING = re.compile(rf"({CLOCK})\s+-->\s+({CLOCK})")


def csv_milliseconds(value):
    milliseconds = Decimal(value) * 1000
    if not milliseconds.is_finite() or milliseconds < 0 or milliseconds % 1:
        raise ValueError(f"Expected non-negative seconds at millisecond precision: {value!r}")
    return int(milliseconds)


def read_cuts(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = csv.DictReader(handle)
        required = {SOURCE_START, SOURCE_END, OUTPUT_START, OUTPUT_END}
        if not required <= set(rows.fieldnames or []):
            raise ValueError("Cut map is missing a source or output time column.")
        cuts = []
        previous_end = 0
        for row in rows:
            output_start, output_end = (
                csv_milliseconds((row[column] or "").strip()) for column in (OUTPUT_START, OUTPUT_END)
            )
            if output_end <= output_start or output_start < previous_end:
                raise ValueError(f"Cut map row {rows.line_num} has an invalid or overlapping output range.")
            previous_end = output_end
            source = [(row[column] or "").strip() for column in (SOURCE_START, SOURCE_END)]
            if source == ["", ""]:
                continue
            source_start, source_end = map(csv_milliseconds, source)
            if source_end - source_start != output_end - output_start:
                raise ValueError(f"Cut map row {rows.line_num} requires a positive, 1x-speed mapping.")
            cuts.append((source_start, source_end, output_start))
        if not cuts:
            raise ValueError("Cut map has no source-backed cuts.")
        return cuts


def clock_milliseconds(value):
    hours, minutes, seconds, milliseconds = map(int, re.split("[:,]", value))
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + milliseconds


def format_clock(value):
    whole_seconds, milliseconds = divmod(value, 1000)
    whole_minutes, seconds = divmod(whole_seconds, 60)
    hours, minutes = divmod(whole_minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def read_cues(path):
    contents = path.read_text(encoding="utf-8-sig").strip()
    if not contents:
        return []
    cues = []
    for index, block in enumerate(re.split(r"\n[^\S\n]*\n+", contents), 1):
        lines = block.splitlines()
        match = TIMING.fullmatch(lines[1].strip()) if len(lines) >= 3 else None
        if not lines[0].strip().isdecimal() or match is None:
            raise ValueError(f"Cue {index} is not a standard numbered SubRip cue.")
        start, end = map(clock_milliseconds, match.groups())
        if end <= start:
            raise ValueError(f"Cue {index} must end after it starts.")
        cues.append((start, end, "\n".join(lines[2:])))
    return cues


def map_cues(cues, cuts):
    mapped = []
    affected = 0
    for start, end, body in cues:
        parts = []
        for cut_start, cut_end, output_start in cuts:
            kept_start, kept_end = max(start, cut_start), min(end, cut_end)
            if kept_start < kept_end:
                offset = output_start - cut_start
                parts.append((kept_start + offset, kept_end + offset, body))
        if len(parts) != 1 or parts[0][1] - parts[0][0] != end - start:
            affected += 1
        mapped.extend(parts)
    return sorted(mapped, key=lambda cue: cue[:2]), affected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_srt", type=Path)
    parser.add_argument("cut_map_csv", type=Path)
    arguments = parser.parse_args()
    try:
        cues = read_cues(arguments.source_srt)
        mapped, affected = map_cues(cues, read_cuts(arguments.cut_map_csv))
    except (OSError, ValueError, DecimalException, csv.Error) as error:
        parser.exit(2, f"{parser.prog}: {error}\n")
    for index, (start, end, body) in enumerate(mapped, 1):
        print(f"{index}\n{format_clock(start)} --> {format_clock(end)}\n{body}\n")
    print(f"{len(cues)} source cues, {len(mapped)} output cues. "
          f"{affected} source cues were clipped, split or removed.", file=sys.stderr)


if __name__ == "__main__":
    main()
