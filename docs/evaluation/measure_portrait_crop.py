"""Locate a full-height portrait crop within matching frames of a wide video."""
import argparse
from collections import Counter
from contextlib import ExitStack

import cv2


def measure(wide_path, portrait_path):
    positions = Counter()
    lowest_match = 1.0
    with ExitStack() as stack:
        videos = [cv2.VideoCapture(path) for path in (wide_path, portrait_path)]
        for video, path in zip(videos, (wide_path, portrait_path)):
            stack.callback(video.release)
            if not video.isOpened():
                raise ValueError(f"Could not open {path}")
        wide, portrait = videos
        if abs(wide.get(cv2.CAP_PROP_FPS) - portrait.get(cv2.CAP_PROP_FPS)) > 0.001:
            raise ValueError("Use two previews with matching frame rates.")
        while True:
            wide_ok, frame = wide.read()
            portrait_ok, crop = portrait.read()
            if wide_ok != portrait_ok:
                raise ValueError("The previews differ in decoded frame count.")
            if not wide_ok:
                break
            height, width = frame.shape[:2]
            crop_height, crop_width = crop.shape[:2]
            match_width = round(height * crop_width / crop_height)
            if not 0 < match_width < width:
                raise ValueError("Expected a narrower, full-height crop.")
            template = cv2.resize(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY),
                                  (match_width, height), interpolation=cv2.INTER_AREA)
            source = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            matches = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
            _, score, _, (left, _) = cv2.minMaxLoc(matches)
            positions[left] += 1
            lowest_match = min(lowest_match, score)
    if not positions:
        raise ValueError("No frames decoded.")
    return positions, lowest_match


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wide", help="Wide MP4 excerpt")
    parser.add_argument("portrait", help="Portrait MP4 of the same excerpt")
    args = parser.parse_args()
    offsets, minimum = measure(args.wide, args.portrait)
    print(f"Frames compared: {sum(offsets.values())}")
    print(f"Left edge in wide-preview pixels (x: frames): {dict(sorted(offsets.items()))}")
    print(f"Lowest normalized correlation: {minimum:.4f}")
