"""Compare two short audio windows for Valmera's four-second filler-word trial."""
import argparse
import math
import struct
import subprocess

RATE = 16000


def decode(path):
    # Limit decoding to the trial's first four seconds, even for longer inputs.
    data = subprocess.check_output([
        "ffmpeg", "-nostdin", "-v", "error", "-i", path, "-t", "4",
        "-map", "0:a:0", "-ac", "1", "-ar", str(RATE), "-f", "s16le", "-",
    ])
    return [sample for sample, in struct.iter_unpack("<h", data)]


def window(audio, start_ms, length_ms):
    start, length = start_ms * RATE // 1000, length_ms * RATE // 1000
    segment = audio[start:start + length]
    if len(segment) != length:
        raise ValueError("Audio is too short for this trial window")
    mean = sum(segment) / length
    return [s - mean for s in segment]


def compare(source, edit, src_ms, edit_ms, length_ms):
    x = window(source, src_ms, length_ms)
    y = window(edit, edit_ms, length_ms)
    norm = math.sqrt(sum(s*s for s in x) * sum(s*s for s in y))
    return f"{sum(a*b for a, b in zip(x, y)) / norm:.3f}" if norm else "undefined (silent window)"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", help="Original four-second MP4")
    parser.add_argument("candidate", help="Reference cut or your exported edit")
    parser.add_argument(
        "--window", nargs=3, action="append", type=int,
        metavar=("SOURCE_MS", "EDIT_MS", "LENGTH_MS"),
        help="Compare these two positions within the first four decoded seconds. Repeat to check other positions.",
    )
    args = parser.parse_args()
    windows = [("Before cut", 350, 350, 400), ("After cut", 2400, 2080, 500)]
    if args.window:
        windows = []
        for src_ms, edit_ms, length_ms in args.window:
            if min(src_ms, edit_ms) < 0 or length_ms <= 0 or max(src_ms, edit_ms) + length_ms > 4000:
                parser.error("Choose a positive window within the first four seconds of both tracks.")
            windows.append((f"Source {src_ms} ms / edit {edit_ms} ms", src_ms, edit_ms, length_ms))
    source, edit = decode(args.original), decode(args.candidate)
    for label, src_ms, edit_ms, length_ms in windows:
        print(f"{label}: r = {compare(source, edit, src_ms, edit_ms, length_ms)}")
