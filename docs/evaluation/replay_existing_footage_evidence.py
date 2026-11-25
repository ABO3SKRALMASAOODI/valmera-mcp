"""Download and verify Valmera's public existing-footage buyer test."""

import hashlib
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
from urllib.request import urlopen

from check_reveal_click import decode
from compare_cutaway_export import AUDIO_RATE, FRAME_NUMBERS, correlation

HOST = "https://valmera.io"
ASSETS = {
    "source": (
        "/examples/filler-word-cut/original.mp4", 74834,
        "437fe11667dbe2d1c7bf4d14b6d3cedd95eaf76ffeb062e2f94dcdcb7d551630",
    ),
    "trim": (
        "/examples/filler-word-cut/first-sentence-removed.mp4", 587214,
        "865ee3b2c96b13bdc9d09b44ebc396eff2e778324f2eecf719d3b1671853fa6f",
    ),
    "preview": (
        "/examples/b-roll-cutaway/preview.mp4", 239255,
        "55dbd09c57d9bff28112b33fedca130c8bd12a30c08864a38386e166f8defa9e",
    ),
    "final": (
        "/examples/b-roll-cutaway/final.mp4", 318275,
        "798d484242fc63f25f756d940214701a0ca9b90cc65679721def30bf1dd729f8",
    ),
}

# These thresholds belong to the published fixture, with its dark waveform
# and light print swatches. They do not score the quality of another edit.
MIN_CORRELATION = 0.99
SWATCH_LUMA = 120


def download_assets(directory, assets=ASSETS):
    files = {}
    for name, (url, byte_count, expected_digest) in assets.items():
        with urlopen(HOST + url, timeout=20) as response:
            data = response.read(byte_count + 1)
        if len(data) != byte_count or hashlib.sha256(data).hexdigest() != expected_digest:
            raise ValueError(f"Published file changed: {url}")
        path = directory / f"{name}.mp4"
        path.write_bytes(data)
        files[name] = path
    return files


def audio(path):
    samples = decode(str(path), [
        "-map", "0:a:0", "-ac", "1", "-ar", str(AUDIO_RATE), "-f", "f32le",
    ])
    return [sample for sample, in struct.iter_unpack("<f", samples)]


def luminance(path):
    return decode(str(path), [
        "-map", "0:v:0", "-vf", "fps=25,scale=1:1:flags=area,format=gray",
        "-f", "rawvideo",
    ])


def verify_audio(label, expected, decoded):
    if len(decoded) != len(expected):
        raise ValueError(f"{label}: audio duration changed")
    measurement = correlation(expected, decoded)
    try:
        value = float(measurement)
    except ValueError as error:
        raise ValueError(f"{label}: {measurement}") from error
    if not value >= MIN_CORRELATION:
        raise ValueError(f"{label}: audio correlation {value:.6f}")
    return value


def verify_cutaway(label, path, source_audio):
    frames = luminance(path)
    if len(frames) != 100:
        raise ValueError(f"{label}: expected 100 program frames")
    levels = [frames[n] for n in FRAME_NUMBERS]
    if [level >= SWATCH_LUMA for level in levels] != [False, True, True, False]:
        raise ValueError(f"{label}: unexpected picture at cutaway boundaries: {levels}")
    return {
        "program_frames_at_25_fps": len(frames),
        "checkpoint_luminance": dict(zip(FRAME_NUMBERS, levels)),
        "four_second_audio_correlation": verify_audio(label, source_audio, audio(path)),
    }


def verify(files):
    source_audio = audio(files["source"])
    if len(source_audio) != 4 * AUDIO_RATE:
        raise ValueError("Source audio is not four seconds")
    cut_in = round(0.20 * AUDIO_RATE)
    cut_out = round(1.45 * AUDIO_RATE)
    expected_trim = source_audio[:cut_in] + source_audio[cut_out:]
    trimmed_frames = luminance(files["trim"])
    if len(trimmed_frames) != 69:
        raise ValueError("Trimmed export did not decode to 69 frames at 25 fps")
    return {
        "files": {name: {"url": HOST + info[0], "sha256": info[2]} for name, info in ASSETS.items()},
        "trim": {
            "video_frames_at_25_fps": len(trimmed_frames),
            "audio_seconds": len(expected_trim) / AUDIO_RATE,
            "audio_correlation_with_source_minus_0_20_to_1_45": verify_audio(
                "trim", expected_trim, audio(files["trim"]),
            ),
        },
        "preview": verify_cutaway("preview", files["preview"], source_audio),
        "final": verify_cutaway("final", files["final"], source_audio),
    }


if __name__ == "__main__":
    try:
        with tempfile.TemporaryDirectory(prefix="valmera-buyer-test-") as tmp:
            report = verify(download_assets(Path(tmp)))
        print(json.dumps(report, indent=2))
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        print(f"Could not verify the published example: {error}", file=sys.stderr)
        raise SystemExit(1)
