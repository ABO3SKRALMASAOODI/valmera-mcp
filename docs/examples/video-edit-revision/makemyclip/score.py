"""Compare the four published exports. Run from the folder containing the MP4s."""
import json
import subprocess
from pathlib import Path

FRAME_SIZE = 96 * 96


def gray_frames(path):
    filters = r"fps=30,crop=min(iw\,ih):min(iw\,ih),scale=96:96:flags=area,format=gray"
    command = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", filters,
               "-f", "rawvideo", "-"]
    raw = subprocess.check_output(command)
    return [raw[i:i + FRAME_SIZE] for i in range(0, len(raw), FRAME_SIZE)]


def distance(first, second):
    return sum(abs(a - b) for a, b in zip(first, second))


def source_schedule(ranges):
    return [frame for start, stop in ranges for frame in range(start * 30, stop * 30)]


def main():
    record = json.loads(Path("comparison.json").read_text())
    source = gray_frames("original-source.mp4")
    first = source_schedule([(3, 7), (12, 16), (19, 23)])
    revised = source_schedule([(3, 7), (12, 14), (19, 23)])
    for item in record["scores"]:
        frames = gray_frames(item["file"])
        counts = {"nearFirst": 0, "nearRevised": 0, "ties": 0}
        for index in range(180, 300):
            a = distance(frames[index], source[first[index]])
            b = distance(frames[index], source[revised[index]])
            if a == b:
                counts["ties"] += 1
            elif a < b:
                counts["nearFirst"] += 1
            else:
                counts["nearRevised"] += 1
        print(item["label"], counts)
        if any(item[key] != count for key, count in counts.items()):
            raise SystemExit("Counts differ from the published run")


if __name__ == "__main__":
    main()
