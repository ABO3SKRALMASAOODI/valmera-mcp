#!/usr/bin/env python3
"""Compare approved and delivered clip batches using exact MP4 file contents."""

import argparse
import filecmp
from pathlib import Path


def mp4_files(directory):
    return {
        path.name: path
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() == ".mp4"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("approved", type=Path, help="folder containing the approved MP4s")
    parser.add_argument("delivered", type=Path, help="folder containing the delivered MP4s")
    parser.add_argument("--revised", help="filename of the one clip expected to change")
    args = parser.parse_args()

    try:
        approved = mp4_files(args.approved)
        delivered = mp4_files(args.delivered)
        if not approved:
            parser.error("the approved folder contains no MP4 files")
        if args.revised is not None and args.revised not in approved:
            parser.error("--revised must name an MP4 in the approved folder")

        failed = False
        for name in sorted(approved.keys() | delivered.keys()):
            if name not in delivered:
                status = "MISSING"
            elif name not in approved:
                status = "UNEXPECTED FILE"
            else:
                changed = not filecmp.cmp(approved[name], delivered[name], shallow=False)
                if name == args.revised:
                    status = "REVISED, REVIEW THIS FILE" if changed else "REVISION FILE MATCHES ORIGINAL"
                else:
                    status = "UNEXPECTED CHANGE" if changed else "APPROVED FILE MATCHES"
            print(f"{status}: {name}")
            failed |= status not in {"APPROVED FILE MATCHES", "REVISED, REVIEW THIS FILE"}
        return int(failed)
    except OSError as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
