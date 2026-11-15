"""Build the three reference cuts from the credited 24 fps source excerpt."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def render_examples(source, output, ffmpeg):
    output.mkdir(exist_ok=True, parents=True)
    # All three timelines skip 90 source frames. Only the picture splice moves.
    samples_per_frame = 2000  # 48 kHz / 24 fps
    with tempfile.TemporaryDirectory() as tmp:
        sound = Path(tmp) / "dialogue.m4a"
        audio_filter = (
            f"[0:a]atrim=end_sample={63 * samples_per_frame},asetpts=PTS-STARTPTS[a];"
            f"[0:a]atrim=start_sample={153 * samples_per_frame}:"
            f"end_sample={228 * samples_per_frame},asetpts=PTS-STARTPTS[b];"
            "[a][b]concat=n=2:v=0:a=1[out]"
        )
        subprocess.run([ffmpeg, "-v", "error", "-i", str(source), "-filter_complex",
                        audio_filter, "-map", "[out]", "-c:a", "aac", "-b:a", "192k",
                        str(sound)], check=True)
        for name, splice in [("straight", 63), ("j-cut", 78), ("l-cut", 48)]:
            video_filter = (
                f"[0:v]trim=end_frame={splice},setpts=PTS-STARTPTS[a];"
                f"[0:v]trim=start_frame={splice + 90}:end_frame=228,setpts=PTS-STARTPTS[b];"
                "[a][b]concat=n=2:v=1:a=0[out]"
            )
            subprocess.run([ffmpeg, "-v", "error", "-y", "-i", str(source), "-i",
                            str(sound), "-filter_complex", video_filter, "-map", "[out]",
                            "-map", "1:a:0", "-c:a", "copy", "-c:v", "libx264",
                            "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                            str(output / (name + ".mp4"))], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Original 9.6-second Sintel excerpt")
    parser.add_argument("output", type=Path)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    args = parser.parse_args()
    render_examples(args.source, args.output, args.ffmpeg)
