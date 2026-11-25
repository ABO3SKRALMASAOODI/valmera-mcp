"""Verify that an exported demo shows the supplied B-roll while retaining its narration."""

import argparse
import json
import math
from pathlib import Path
import struct
import subprocess
import tempfile

from compare_cutaway_export import AUDIO_RATE, correlation
from replay_existing_footage_evidence import download_assets


ASSETS = {
    "source": (
        "/examples/narrated-tutorial/source.mp4", 518298,
        "06f4c7c07bfd255ebb0d0c8883060f3a5d8196a4bb9631176e2024aced435544",
    ),
    "close_up": (
        "/examples/narrated-demo-b-roll/captions-guide-close-up.mp4", 263480,
        "f94b6aebab8668f4e979b7060ec58f3508fe3d881d79b312e398b941a47ee042",
    ),
    "preview": (
        "/examples/narrated-demo-b-roll/approval-preview.mp4", 1908551,
        "44f74f42866f3225a09de8ec9490970bdd846c59a80da86a57c2b0272e7dd98b",
    ),
    "final": (
        "/examples/narrated-demo-b-roll/final.mp4", 1738531,
        "efbf09c5ee069c7c17f7c41c836c912d8344e8a8b220dd3e16b329d2f8670629",
    ),
}
AUDIO_WINDOW_SECONDS = 1.5
TONE_HZ = 697
FRAME_SIZE = (320, 180)
CHECKPOINTS = ((3.57, "source"), (4.25, "source"), (5.10, "close_up"), (6.55, "source"))


def decode(path, timestamp, options):
    return subprocess.check_output([
        "ffmpeg", "-nostdin", "-v", "error", "-ss", str(timestamp), "-i", str(path),
        *options, "-",
    ])


def frame(path, timestamp):
    width, height = FRAME_SIZE
    pixels = decode(path, timestamp, [
        "-map", "0:v:0", "-frames:v", "1", "-vf", f"scale={width}:{height},format=gray",
        "-f", "rawvideo",
    ])
    if len(pixels) != width * height:
        raise ValueError(f"Missing picture at {timestamp:.2f} s")
    return pixels


def stereo_window(path, timestamp):
    pcm = decode(path, timestamp, [
        "-map", "0:a:0", "-t", str(AUDIO_WINDOW_SECONDS),
        "-ac", "2", "-ar", str(AUDIO_RATE), "-f", "f32le",
    ])
    if len(pcm) != round(AUDIO_WINDOW_SECONDS * AUDIO_RATE) * 8:
        raise ValueError(f"Missing audio from {timestamp:.2f} s")
    return tuple(zip(*struct.iter_unpack("<ff", pcm)))


def tone_dbfs(samples):
    in_phase = quadrature = window_size = 0.0
    for index, sample in enumerate(samples):
        window = (1 - math.cos(math.tau * index / (len(samples) - 1))) / 2
        phase = math.tau * TONE_HZ * index / AUDIO_RATE
        in_phase += sample * window * math.cos(phase)
        quadrature += sample * window * math.sin(phase)
        window_size += window
    amplitude = 2 * math.hypot(in_phase, quadrature) / window_size
    return round(20 * math.log10(max(amplitude, 1e-12)), 1)


def compare_audio(original, candidate, input_tone):
    channels = []
    for reference, measured in zip(original, candidate):
        try:
            similarity = float(correlation(reference, measured))
        except ValueError:
            similarity = None
        gain = sum(x * y for x, y in zip(reference, measured)) / sum(x * x for x in reference)
        residual = tone_dbfs([y - gain * x for x, y in zip(reference, measured)])
        gain_db = round(20 * math.log10(max(gain, 1e-12)), 1)
        channels.append({
            "narration_correlation": similarity,
            "narration_gain_db": gain_db,
            "residual_tone_dbfs": residual,
            "passed": similarity is not None and similarity >= .98
                and -6 <= gain_db <= 6 and residual <= input_tone - 25,
        })
    return channels


def compare_export(path, reference_frames, original_audio, input_tone):
    pictures = []
    for timestamp, expected in CHECKPOINTS:
        observed = frame(path, timestamp)
        distances = {
            name: round(sum(abs(a - b) for a, b in zip(observed, expected_frame)) / len(observed), 2)
            for name, expected_frame in reference_frames[timestamp].items()
        }
        pictures.append({
            "seconds": timestamp,
            "expected": expected,
            "mean_luma_error": distances,
            "passed": min(distances, key=distances.get) == expected and distances[expected] <= 9,
        })
    audio = compare_audio(original_audio, stereo_window(path, 4.65), input_tone)
    return {"picture": pictures, "audio": audio, "passed": all(check["passed"] for check in pictures + audio)}


def replay(directory, candidate):
    assets = {name: ASSETS[name] for name in ("source", "close_up")} if candidate else ASSETS
    files = download_assets(directory, assets)
    input_tone = max(map(tone_dbfs, stereo_window(files["close_up"], .15)))
    references = {
        timestamp: {
            "source": frame(files["source"], timestamp),
            "close_up": frame(files["close_up"], max(0, min(1.75, timestamp - 4.5))),
        }
        for timestamp, _ in CHECKPOINTS
    }
    audio = stereo_window(files["source"], 4.65)
    outputs = {"candidate": candidate} if candidate else {name: files[name] for name in ("preview", "final")}
    return {
        "input_tone_dbfs": input_tone,
        "exports": {name: compare_export(path, references, audio, input_tone) for name, path in outputs.items()},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, help="Compare a local export of the two published inputs.")
    args = parser.parse_args()
    if args.candidate is not None and not args.candidate.is_file():
        parser.error("--candidate must point to a local file")
    try:
        with tempfile.TemporaryDirectory(prefix="valmera-narrated-demo-") as tmp:
            report = replay(Path(tmp), args.candidate)
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        parser.exit(1, f"Could not verify the export: {error}\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if all(result["passed"] for result in report["exports"].values()) else 1)
