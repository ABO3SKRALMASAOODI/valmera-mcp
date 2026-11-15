"""Measure an export of the four-second print-swatch exercise against its reference."""

import argparse
import csv
import math
from pathlib import Path
import struct
import subprocess
import sys

from check_reveal_click import decode

FPS = 25
FRAME_BYTES = 32 * 16 * 3
FRAME_NUMBERS = (63, 64, 92, 93)
AUDIO_RATE = 16000


def picture(path):
    return decode(str(path), [
        "-map", "0:v:0", "-vf", "fps=25,scale=32:16:flags=area",
        "-pix_fmt", "rgb24", "-f", "rawvideo",
    ])


def voice(path):
    raw = decode(str(path), ["-map", "0:a:0", "-ac", "1", "-ar", str(AUDIO_RATE), "-f", "f32le"])
    first = round(2.625 * AUDIO_RATE)
    last = round(3.55 * AUDIO_RATE)
    if len(raw) < 4 * last:
        raise ValueError(f"{path} ends before the audio measurement window")
    return [value for value, in struct.iter_unpack("<f", raw[4 * first:4 * last])]


def correlation(left, right):
    a_mean = sum(left) / len(left)
    b_mean = sum(right) / len(right)
    a = [v - a_mean for v in left]
    b = [v - b_mean for v in right]
    energy = math.sqrt(sum(x*x for x in a) * sum(y*y for y in b))
    if not energy:
        return "undefined (silent or constant audio)"
    return f"{sum(x*y for x, y in zip(a, b)) / energy:.6f}"


def measure(source, reference, candidate):
    target = picture(reference)
    observed = picture(candidate)
    rows = []
    for frame in FRAME_NUMBERS:
        first = frame * FRAME_BYTES
        last = first + FRAME_BYTES
        if min(len(target), len(observed)) < last:
            raise ValueError(f"Missing picture for the {frame / FPS:.2f} s checkpoint")
        difference = sum(abs(x-y) for x, y in zip(target[first:last], observed[first:last]))
        rows.append(("mean_absolute_rgb_difference", f"{frame / FPS:.2f}", f"{difference / FRAME_BYTES:.2f}"))
    rows.append(("narration_correlation", "2.625-3.550", correlation(voice(source), voice(candidate))))
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Original four-second narration")
    parser.add_argument("reference", type=Path, help="Valmera's four-second cutaway preview")
    parser.add_argument("candidate", type=Path, help="Export from the editor under test, starting at source time zero")
    args = parser.parse_args()
    try:
        values = measure(args.source, args.reference, args.candidate)
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        parser.exit(1, f"Could not compare the files: {error}\n")
    writer = csv.writer(sys.stdout)
    writer.writerow(("measurement", "program_seconds", "value"))
    writer.writerows(values)
