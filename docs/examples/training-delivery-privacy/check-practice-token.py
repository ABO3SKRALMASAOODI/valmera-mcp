"""Find a fictional practice string in training delivery filenames, text and media tags."""
import argparse
import json
import subprocess
from pathlib import Path

TEXT_SUFFIXES = {".srt", ".vtt", ".txt", ".csv", ".json", ".md"}
MEDIA_SUFFIXES = {".mp4", ".mov", ".m4a", ".webm"}


def metadata_values(path):
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams",
         "-show_chapters", "-of", "json", str(path)],
        capture_output=True,
        check=True,
        text=True,
        timeout=30,
    )
    data = json.loads(probe.stdout)
    sections = [data.get("format", {}), *data.get("streams", []), *data.get("chapters", [])]
    for section in sections:
        yield from section.get("tags", {}).values()


def check(folder, marker):
    findings = []
    errors = []
    files = sorted(path for path in folder.rglob("*") if path.is_file())
    if not files:
        return findings, ["No files to inspect"]

    for path in files:
        relative = path.relative_to(folder).as_posix()
        if marker in relative.casefold():
            findings.append((relative, "filename"))
        try:
            suffix = path.suffix.lower()
            if suffix in TEXT_SUFFIXES and marker in path.read_text(encoding="utf-8-sig").casefold():
                findings.append((relative, "text"))
            if suffix in MEDIA_SUFFIXES and any(marker in value.casefold() for value in metadata_values(path)):
                findings.append((relative, "media metadata"))
        except (UnicodeError, OSError, subprocess.SubprocessError, ValueError):
            errors.append(f"Could not inspect {relative}")

    return findings, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("practice_token", help="A fictional value intentionally added to test material")
    args = parser.parse_args()
    marker = args.practice_token.strip().casefold()
    if not marker or not args.folder.is_dir():
        parser.error("Specify an existing delivery folder and a non-empty practice token")

    findings, errors = check(args.folder, marker)
    for path, location in findings:
        print(f"Found in {location}: {path}")
    for error in errors:
        print(error)
    if errors:
        return 2
    if findings:
        return 1
    print("Practice token absent from the checked filenames, text and media tags.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
