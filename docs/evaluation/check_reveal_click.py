"""Measure one click against the visual cut in Valmera's public swatch example."""

import argparse
import math
import struct
import subprocess

RATE = 48_000
FPS = 25


def decode(path, options):
    return subprocess.check_output([
        "ffmpeg", "-nostdin", "-v", "error", "-i", path, "-t", "4",
        *options, "-",
    ])


def audio(path):
    pcm = decode(path, [
        "-map", "0:a:0", "-ac", "1", "-ar", str(RATE), "-f", "f32le",
    ])
    samples = [value for value, in struct.iter_unpack("<f", pcm)]
    if len(samples) < 3 * RATE:
        raise ValueError("The example needs at least three seconds of audio.")
    return samples


def swatch_time(path):
    # One grayscale pixel per frame approximates the mean luma. These two
    # original 25 fps clips cut from dark graphics to a light swatch chart.
    luma = decode(path, [
        "-map", "0:v:0", "-vf", "scale=1:1:flags=area,format=gray",
        "-fps_mode", "passthrough", "-f", "rawvideo",
    ])
    if len(luma) != 4 * FPS:
        raise ValueError("Expected the 100-frame swatch example.")
    for i in range(1, len(luma)):
        if luma[i - 1] <= 120 < luma[i]:
            return i / FPS
    raise ValueError("No dark-to-light reveal found.")


def measure(source, path):
    mix = audio(path)
    start, end = round(0.3 * RATE), round(2.3 * RATE)
    bed = source[start:end]
    mixed_bed = mix[start:end]
    energy = sum(s * s for s in bed)
    if energy == 0:
        raise ValueError("Expected narration before the reveal.")
    gain = sum(s * m for s, m in zip(bed, mixed_bed)) / energy
    # Both renders share the same source and timebase. Subtract the matched
    # narration and find the strongest residual in the known cue window.
    start, end = round(2.45 * RATE), round(2.95 * RATE)
    residual = [abs(m - gain * s) for s, m in zip(source[start:end], mix[start:end])]
    peak = max(residual)
    noise = math.sqrt(sum((m - gain * s) ** 2 for s, m in zip(bed, mixed_bed)) / len(bed))
    if peak <= max(1e-5, 10 * noise):
        raise ValueError("No distinct click above the narration residual in this example.")
    hit = (start + residual.index(peak)) / RATE
    reveal = swatch_time(path)
    print(f"{path}: reveal {reveal:.3f} s, click {hit:.4f} s, offset {(hit - reveal) * 1000:+.1f} ms")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="The narrated swatch clip without a click")
    parser.add_argument("mix", nargs="+", help="One or both rendered previews")
    args = parser.parse_args()
    original = audio(args.source)
    for filename in args.mix:
        try:
            measure(original, filename)
        except ValueError as error:
            parser.exit(1, f"{filename}: {error}\n")
