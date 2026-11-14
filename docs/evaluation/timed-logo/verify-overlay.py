"""Measure the supplied timed-logo fixture against its original video."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import numpy as np

WIDTH, HEIGHT = 320, 180
REGION = (241, 7, 310, 30)
THRESHOLD = 5
BOUNDARIES = (89, 90, 659, 660)


def decode(path):
    command = [
        "ffmpeg", "-nostdin", "-v", "error", "-i", str(path), "-map", "0:v:0",
        "-vf", f"scale={WIDTH}:{HEIGHT}:flags=area", "-vsync", "0",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
    ]
    size = WIDTH * HEIGHT * 3
    with subprocess.Popen(command, stdout=subprocess.PIPE) as process:
        try:
            while data := process.stdout.read(size):
                if len(data) != size:
                    raise ValueError(f"Incomplete decoded frame in {path}")
                yield np.frombuffer(data, dtype=np.uint8).reshape(HEIGHT, WIDTH, 3)
            if process.wait():
                raise RuntimeError(f"Could not decode {path}")
        finally:
            process.stdout.close()


def measure(source, output):
    x0, y0, x1, y1 = REGION
    mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    mask[y0:y1, x0:x1] = True
    inside, background = [], []
    source_count = 0
    rendered = iter(decode(output))
    for original in decode(source):
        source_count += 1
        frame = next(rendered, None)
        if frame is None:
            continue
        difference = np.abs(frame.astype(np.int16) - original.astype(np.int16))
        inside.append(float(difference[mask].mean()))
        background.append(float(difference[~mask].mean()))
    if next(rendered, None) is not None:
        rendered.close()
        raise ValueError("Output extends beyond the matching source frames")
    if len(inside) <= max(BOUNDARIES):
        raise ValueError("Output is too short to inspect both logo boundaries")
    active = [i for i, difference in enumerate(inside) if difference > THRESHOLD]
    metrics = {
        "frames": len(inside), "activeCount": len(active),
        "firstActiveFrame": active[0] if active else None,
        "lastActiveFrame": active[-1] if active else None,
        "onlyExpectedFramesActive": active == list(range(90, 660)),
        "meanBackgroundDifference": round(float(np.mean(background)), 3),
        "maxBackgroundDifference": round(max(background), 3),
        "boundaryReadings": {str(i): round(inside[i], 3) for i in BOUNDARIES},
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
    }
    return {
        "sourceFrames": source_count, "probeWidth": WIDTH, "probeHeight": HEIGHT,
        "sampleRegionXYXY": REGION, "thresholdMeanChannelDifference": THRESHOLD,
        "outputs": {output.name: metrics},
        "sourceSha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(measure(args.source, args.output), indent=2))
