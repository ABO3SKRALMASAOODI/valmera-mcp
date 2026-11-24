"""Compare the first decoded audio track in approved and alternate video exports."""

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


def audio_digest(video):
    if not video.is_file():
        raise ValueError("file is missing or is not a regular file")
    # WAV includes the audio sample rate and channel metadata. Strip input tags
    # so descriptive tags do not become part of the fingerprint.
    command = [
        "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-xerror",
        "-i", str(video.resolve()), "-map", "0:a:0", "-map_metadata", "-1",
        "-abort_on", "empty_output_stream", "-fflags", "+bitexact",
        "-c:a", "pcm_s24le", "-f", "wav", "pipe:1",
    ]
    with tempfile.TemporaryFile() as errors:
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=errors) as process:
            digest = hashlib.sha256()
            for block in iter(lambda: process.stdout.read(1024 * 1024), b""):
                digest.update(block)
            if process.wait():
                errors.seek(0)
                detail = errors.read(512).decode(errors="replace").strip()
                raise ValueError(detail or "FFmpeg could not decode the audio")
    return digest.hexdigest()


def compare(approved, variants):
    try:
        expected = audio_digest(approved)
    except OSError as error:
        print(f"Could not run FFmpeg: {error}", file=sys.stderr)
        return 2
    except ValueError as error:
        print(f"ERROR {approved}: {error}", file=sys.stderr)
        return 2

    status = 0
    for variant in variants:
        try:
            actual = audio_digest(variant)
        except (OSError, ValueError) as error:
            print(f"ERROR {variant}: {error}", file=sys.stderr)
            status = 2
            continue
        if actual == expected:
            print(f"MATCH {variant}")
        else:
            print(f"DIFFERENT {variant}")
            status = max(status, 1)
    return status


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("approved", type=Path, help="approved export")
    parser.add_argument("variant", nargs="+", type=Path, help="alternate export(s)")
    args = parser.parse_args()
    raise SystemExit(compare(args.approved, args.variant))
