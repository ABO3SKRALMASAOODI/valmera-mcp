"""Render three captioned vertical clips of Michelle Thaller's 2017 mission interview."""
import argparse
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
# File name, on-screen question, source start, duration, clip-clock captions.
VERSIONS = [
    ("mission", "Where was OSIRIS-REx going?", "11.600", "10.080", "answer.srt"),
    ("asteroid", "Why study an asteroid?", "11.600", "10.080", "answer.srt"),
    ("shorter", "Why study an asteroid?", "16.840", "4.840", "shorter-opening.srt"),
]


def render(source, output, ffmpeg):
    source = source.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name, question, start, duration, captions in VERSIONS:
        # A 3-second closed GOP makes the common part independently decodable.
        vf = (
            "fps=25,scale=540:304,setsar=1,pad=540:960:0:280:color=0x10141b,"
            f"drawtext=text='{question}':font=Arial:fontsize=26:fontcolor=white:"
            "x=(w-tw)/2:y=178:enable='lt(n,75)',"
            f"subtitles={captions}:original_size=540x960:"
            "force_style='PlayResX=540,PlayResY=960,FontName=Arial,FontSize=26,"
            "MarginL=32,MarginR=32,MarginV=170,Outline=1,Shadow=0,Alignment=2'"
        )
        subprocess.run([
            ffmpeg, "-v", "error", "-nostdin", "-y", "-ss", start,
            "-i", str(source), "-t", duration, "-map", "0:v:0", "-map", "0:a:0",
            "-vf", vf, "-c:v", "libx264", "-qp", "20", "-pix_fmt", "yuv420p",
            "-x264-params", "keyint=75:min-keyint=75:scenecut=0:open-gop=0",
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
            str((output / (name + ".mp4")).resolve()),
        ], cwd=HERE, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Original NASA Thaller interview MP4")
    parser.add_argument("output", type=Path, help="Directory for the three rendered MP4s")
    parser.add_argument("--ffmpeg", default="ffmpeg")
    args = parser.parse_args()
    render(args.source, args.output, args.ffmpeg)
