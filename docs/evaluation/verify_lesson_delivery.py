"""Verify an LMS delivery folder against its approved MP4 and SRT manifest."""

import argparse
import csv
import hashlib
import string
from pathlib import Path

COLUMNS = ("lesson_id", "mp4", "mp4_sha256", "srt", "srt_sha256")


def verify(manifest, folder):
    errors = []
    named = set()
    lessons = set()
    with manifest.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise ValueError(f"Expected columns: {', '.join(COLUMNS)}")
        for row in reader:
            lesson = row["lesson_id"]
            if None in row or not lesson or lesson in lessons:
                raise ValueError(f"Missing or duplicate lesson ID, or extra fields, at line {reader.line_num}.")
            lessons.add(lesson)
            for extension in ("mp4", "srt"):
                filename = row[extension] or ""
                checksum = (row[f"{extension}_sha256"] or "").lower()
                if Path(filename).name != filename or "\\" in filename or not filename.endswith(f".{extension}"):
                    raise ValueError(f"{lesson}: enter a .{extension} filename within the delivery folder.")
                if filename in named:
                    raise ValueError(f"{lesson}: {filename} is already used by another row.")
                if len(checksum) != 64 or any(char not in string.hexdigits for char in checksum):
                    raise ValueError(f"{lesson}: {filename} requires a 64-character SHA-256.")
                named.add(filename)
                file = folder / filename
                if file.is_symlink() or not file.is_file():
                    errors.append(f"{lesson}: missing regular file {filename}")
                    continue
                digest = hashlib.sha256()
                with file.open("rb") as media:
                    for chunk in iter(lambda: media.read(1024 * 1024), b""):
                        digest.update(chunk)
                if digest.hexdigest() != checksum:
                    errors.append(f"{lesson}: {filename} differs from the approved file.")

    if not lessons:
        raise ValueError("The manifest needs at least one approved lesson.")
    unlisted = {
        file.name for file in folder.iterdir()
        if file.suffix.lower() in {".mp4", ".srt"} and file.name not in named
    }
    errors.extend(f"Unlisted deliverable: {filename}" for filename in sorted(unlisted))
    return len(lessons), errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="reference CSV created from the approved files")
    parser.add_argument("folder", type=Path, help="candidate delivery folder")
    args = parser.parse_args()
    try:
        count, errors = verify(args.manifest, args.folder)
    except (ValueError, csv.Error, OSError) as error:
        parser.error(str(error))

    if errors:
        print("\n".join(errors))
        return 1
    lesson_label = "lesson" if count == 1 else "lessons"
    print(f"Verified {count} {lesson_label} against the approved MP4 and SRT files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
