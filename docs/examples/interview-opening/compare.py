"""Compare two exported clips on the decoded picture and sound clocks."""
import argparse
import hashlib
import subprocess


def ffmpeg_output(ffmpeg, path, arguments):
    return subprocess.check_output([ffmpeg, "-v", "error", "-i", path, *arguments, "-"])


def frame_hashes(ffmpeg, path):
    data = ffmpeg_output(ffmpeg, path, ["-map", "0:v:0", "-f", "framemd5"])
    return [row.rsplit(b",", 1)[-1].strip() for row in data.splitlines()
            if row and not row.startswith(b"#")]


def sound_hash(ffmpeg, path):
    data = ffmpeg_output(ffmpeg, path, ["-map", "0:a:0", "-f", "s16le", "-c:a", "pcm_s16le"])
    return hashlib.sha256(data).hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first")
    parser.add_argument("revision")
    parser.add_argument("--ffmpeg", default="ffmpeg")
    args = parser.parse_args()
    first = frame_hashes(args.ffmpeg, args.first)
    revision = frame_hashes(args.ffmpeg, args.revision)
    differences = [i for i, (a, b) in enumerate(zip(first, revision)) if a != b]
    print("Decoded frame counts:", len(first), len(revision))
    print("Changed frames on the shared clock:", len(differences))
    if differences:
        print("First and last changed frames (zero-based):", differences[0], differences[-1])
    print("Decoded PCM identical:", sound_hash(args.ffmpeg, args.first) == sound_hash(args.ffmpeg, args.revision))
