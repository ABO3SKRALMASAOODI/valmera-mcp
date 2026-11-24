"""Map reviewed stream ranges onto one continuous recording and print an edit brief."""

import argparse
import csv
from pathlib import Path


def parse_time(value: str) -> int:
    parts = value.strip().split(":")
    if len(parts) not in (2, 3) or any(not part.isascii() or not part.isdecimal() for part in parts):
        raise ValueError(f"Use MM:SS or HH:MM:SS for {value!r}.")
    fields = [int(part) for part in parts]
    if fields[-1] >= 60 or (len(fields) == 3 and fields[-2] >= 60):
        raise ValueError(f"Seconds and H:MM:SS minutes must be under 60 in {value!r}.")
    if len(fields) == 2:
        fields.insert(0, 0)
    hours, minutes, seconds = fields
    return hours * 3600 + minutes * 60 + seconds


def clock(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ranges", type=Path, help="CSV with stream_in, stream_out and label columns")
    parser.add_argument("--anchor", action="append", nargs=2, required=True, type=parse_time,
                        metavar=("STREAM_TIME", "RECORDING_TIME"),
                        help="Matching visual frame in both files. Supply an early and a late anchor.")
    parser.add_argument("--duration", required=True, type=parse_time, help="Local recording duration")
    args = parser.parse_args()

    try:
        if len(args.anchor) != 2:
            raise ValueError("Supply exactly two matching anchor pairs.")
        (early_stream, early_local), (late_stream, late_local) = sorted(args.anchor)
        if early_stream >= late_stream or late_local > args.duration:
            raise ValueError("Choose two distinct stream anchors within the local recording.")
        offset = early_local - early_stream
        if late_local - late_stream != offset:
            raise ValueError("The offsets disagree. Check for pauses or missing frames and map each continuous section separately.")

        lines = []
        previous_end = early_stream
        with args.ranges.open(encoding="utf-8-sig", newline="") as handle:
            rows = csv.DictReader(handle)
            if not {"stream_in", "stream_out", "label"}.issubset(rows.fieldnames or []):
                raise ValueError("CSV header must contain stream_in, stream_out and label.")
            for row in rows:
                start, end = parse_time(row["stream_in"] or ""), parse_time(row["stream_out"] or "")
                label = " ".join((row["label"] or "").split())
                if not previous_end <= start < end <= late_stream or not label:
                    raise ValueError(f"Line {rows.line_num} needs a labeled, non-overlapping range in source order between the anchors.")
                lines.append(f"- {clock(start + offset)} to {clock(end + offset)} — {label}")
                previous_end = end
        if not lines:
            raise ValueError("Add at least one reviewed range to the CSV.")
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        parser.error(str(exc))

    print("Make one 16:9 highlight reel from the uploaded local recording.")
    print("Use these source ranges in order and retain the original audio.")
    print(*lines, sep="\n")
    print("Show the preview so I can check that each setup, payoff and reaction survives the cuts.")


if __name__ == "__main__":
    main()
