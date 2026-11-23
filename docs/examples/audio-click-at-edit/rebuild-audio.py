"""Build a three-second hard splice and an equal-length smoothed splice."""
import json
import math
from pathlib import Path
import struct
import wave

RATE = 48_000
JOIN = 72_000
HANDLE = 480
DURATION = 3
FULL_SCALE = 32_767


def tone_pair(position):
    t = (position - JOIN) / RATE
    common = 0.04 * math.sin(math.tau * 470 * t)
    shifted = 0.22 * math.cos(math.tau * 125 * t)
    return common + shifted, common - shifted


def make_samples():
    hard, smooth = [], []
    start, stop = JOIN - HANDLE, JOIN + HANDLE
    for sample in range(RATE * DURATION):
        outgoing, incoming = tone_pair(sample)
        exact = outgoing if sample < JOIN else incoming
        blended = exact
        if start <= sample < stop:
            progress = (sample - start) / (stop - start - 1)
            weight = (1 - math.cos(math.pi * progress)) / 2
            blended = outgoing * (1 - weight) + incoming * weight
        hard.append(round(exact * FULL_SCALE))
        smooth.append(round(blended * FULL_SCALE))
    assert hard[:start] == smooth[:start]
    assert hard[stop:] == smooth[stop:]
    return hard, smooth


def write_wav(path, samples):
    with wave.open(str(path), "wb") as file:
        file.setparams((1, 2, RATE, len(samples), "NONE", "not compressed"))
        file.writeframes(struct.pack(f"<{len(samples)}h", *samples))
    with wave.open(str(path), "rb") as file:
        assert file.getnframes() == len(samples)
        assert file.getframerate() == RATE
        return list(struct.unpack(f"<{len(samples)}h", file.readframes(len(samples))))


def measure(samples):
    start, stop = JOIN - HANDLE, JOIN + HANDLE
    neighborhood = samples[start - 1:stop + 1]
    max_step = max(abs(a - b) for a, b in zip(neighborhood, neighborhood[1:]))
    return {
        "adjacentStepAtJoinCounts": abs(samples[JOIN] - samples[JOIN - 1]),
        "maxAdjacentStepInWindowCounts": max_step,
        "maxAdjacentStepInWindowPercentFullScale": round(max_step / FULL_SCALE * 100, 4),
    }


def build(output):
    output.mkdir(parents=True, exist_ok=True)
    hard, smooth = make_samples()
    hard = write_wav(output / "hard-join.wav", hard)
    smooth = write_wav(output / "smoothed-join.wav", smooth)
    measurements = {
        "channels": 1,
        "sampleRateHz": RATE,
        "bitsPerSample": 16,
        "samplesPerFile": len(hard),
        "durationSeconds": DURATION,
        "joinSeconds": JOIN / RATE,
        "changedWindowSeconds": [(JOIN - HANDLE) / RATE, (JOIN + HANDLE) / RATE],
        "identicalOutsideWindow": hard[:JOIN - HANDLE] == smooth[:JOIN - HANDLE]
        and hard[JOIN + HANDLE:] == smooth[JOIN + HANDLE:],
        "hardJoin": measure(hard),
        "smoothedJoin": measure(smooth),
    }
    assert measurements["identicalOutsideWindow"]
    assert measurements["smoothedJoin"]["maxAdjacentStepInWindowCounts"] < 600
    (output / "measurements.json").write_text(json.dumps(measurements, indent=2) + "\n")


if __name__ == "__main__":
    import sys

    build(Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd())
