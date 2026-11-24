#!/usr/bin/env python3
"""Check local video dependencies and their approved hashes in an MLT handoff."""

import argparse
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath, PureWindowsPath


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Path to the copied .mlt file")
    parser.add_argument("manifest", type=Path, help="Approved JSON mapping relative paths to SHA-256 hashes")
    args = parser.parse_args()
    root = args.project.resolve().parent

    try:
        project = ET.parse(args.project).getroot()
        approved = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, ET.ParseError, ValueError) as error:
        parser.exit(2, f"Cannot read the project and manifest: {error}\n")

    if project.tag != "mlt" or not isinstance(approved, dict) or not approved:
        parser.exit(2, "Expected an MLT project and a nonempty JSON path-to-hash mapping.\n")

    found = set()
    failures = []
    project_root = project.get("root")
    if project_root and project_root != ".":
        failures.append(f"Project root is not relative to this delivery: {project_root}")

    for node in project.iter():
        if node.tag not in {"producer", "chain"}:
            continue
        props = {prop.get("name"): prop.text for prop in node.findall("property")}
        if props.get("mlt_service") not in {"avformat", "avformat-novalidate"}:
            continue
        raw = props.get("resource") or ""
        slash_path = raw.replace("\\", "/")
        relative = PurePosixPath(slash_path)
        windows_path = PureWindowsPath(raw)
        if (
            not raw
            or relative.is_absolute()
            or windows_path.drive
            or ".." in relative.parts
            or any(":" in part for part in relative.parts)
        ):
            failures.append(f"Resource needs a path inside the delivery: {raw or '(empty)'}")
            continue

        name = relative.as_posix()
        if name in found:
            continue
        found.add(name)
        if name not in approved:
            failures.append(f"Unapproved video reference: {name}")
            continue

        try:
            candidate = root.joinpath(*relative.parts).resolve()
            if not candidate.is_relative_to(root):
                failures.append(f"Resource points outside the delivery: {name}")
                continue
            with candidate.open("rb") as media:
                digest = hashlib.sha256()
                for block in iter(lambda: media.read(1024 * 1024), b""):
                    digest.update(block)
        except (OSError, RuntimeError):
            failures.append(f"Missing or unreadable video: {name}")
            continue
        if digest.hexdigest() != approved[name]:
            failures.append(f"Wrong or changed video: {name}")

    for name in sorted(approved.keys() - found):
        failures.append(f"Approved video absent from project references: {name}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print(f"Verified {len(found)} video references and approved hashes in {args.project.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
