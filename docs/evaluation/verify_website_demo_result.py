"""Measure how long a known screen state appears in a website demo."""

import argparse
import json
import math

import cv2


def verify(args):
    reference = cv2.imread(args.reference, cv2.IMREAD_GRAYSCALE)
    if reference is None:
        raise ValueError('Could not read the reference screenshot.')
    height, width = reference.shape
    left, top, right, bottom = args.crop
    if not (0 <= left < right <= width and 0 <= top < bottom <= height):
        raise ValueError('Crop must be inside the reference screenshot.')
    marker = reference[top:bottom, left:right]
    if marker.std() < 5:
        raise ValueError('Choose a crop with distinct text or graphics.')

    start, end = args.window
    numbers = (start, end, args.hold, args.threshold)
    if not all(math.isfinite(n) for n in numbers):
        raise ValueError('Window, hold and threshold values must be finite.')
    if not (0 <= start < end and 0 < args.hold <= end - start):
        raise ValueError('Choose a positive hold that fits inside the time window.')
    if not 0 < args.threshold <= 1:
        raise ValueError('Threshold must be between zero and one.')

    video = cv2.VideoCapture(args.video)
    try:
        fps = video.get(cv2.CAP_PROP_FPS)
        if not video.isOpened() or not math.isfinite(fps) or fps <= 0:
            raise ValueError('Could not read the video and its frame rate.')
        first_frame = math.ceil(start * fps)
        last_frame = math.ceil(end * fps)
        if first_frame >= last_frame or not video.set(cv2.CAP_PROP_POS_FRAMES, first_frame):
            raise ValueError('Could not seek to the requested time window.')

        peak = -1.0
        streak = longest = 0
        longest_start = None
        for frame_index in range(first_frame, last_frame):
            decoded, frame = video.read()
            if not decoded:
                raise ValueError('The requested window could not be fully decoded.')
            frame_height, frame_width = frame.shape[:2]
            if abs(frame_width * height / (frame_height * width) - 1) > 0.02:
                raise ValueError('Reference and export must have the same aspect ratio.')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            normalized = cv2.resize(gray, (width, height), interpolation=cv2.INTER_AREA)
            similarities = cv2.matchTemplate(normalized, marker, cv2.TM_CCOEFF_NORMED)
            _, score, _, _ = cv2.minMaxLoc(similarities)
            peak = max(peak, score)
            streak = streak + 1 if score >= args.threshold else 0
            if streak > longest:
                longest = streak
                longest_start = (frame_index - streak + 1) / fps
    finally:
        video.release()

    return {
        'pass': longest >= math.ceil(args.hold * fps),
        'frames_checked': last_frame - first_frame,
        'peak_similarity': round(peak, 3),
        'longest_match_seconds': round(longest / fps, 3),
        'longest_match_start_seconds': longest_start,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', help='Constant-frame-rate MP4 to check')
    parser.add_argument('reference', help='Trusted screenshot of the intended result')
    parser.add_argument('--crop', nargs=4, type=int, required=True,
                        metavar=('LEFT', 'TOP', 'RIGHT', 'BOTTOM'))
    parser.add_argument('--window', nargs=2, type=float, required=True,
                        metavar=('START', 'END'), help='Start and end times in seconds')
    parser.add_argument('--hold', type=float, default=1.0, help='Required continuous hold in seconds')
    parser.add_argument('--threshold', type=float, default=0.9, help='Minimum normalized similarity')
    args = parser.parse_args()
    try:
        result = verify(args)
    except (ValueError, cv2.error) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0 if result['pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
