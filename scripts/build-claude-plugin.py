#!/usr/bin/env python3
"""Build the standalone Claude upload ZIP from committed plugin components."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path, help="New ZIP path; existing files are never overwritten")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
files = {
    ".claude-plugin/plugin.json": ".claude-plugin/plugin.json",
    ".claude-plugin/icon.png": ".claude-plugin/icon.png",
    ".mcp.json": ".mcp.json",
    "LICENSE": "LICENSE",
    "README.md": "docs/CLAUDE-PLUGIN.md",
}
for name in ("edit-video-with-valmera", "turn-long-video-into-shorts", "website-demo-video"):
    path = f"skills/{name}/SKILL.md"
    files[path] = path

# Fixed timestamps, order and permissions make repeated builds comparable.
# Explicit component selection keeps other clients and maintenance scripts out.
contents = {}
for destination, source in sorted(files.items()):
    path = root / source
    if path.is_symlink() or not path.is_file():
        raise SystemExit(f"Expected a regular file: {source}")
    contents[destination] = path.read_bytes()
with ZipFile(args.output, "x", compression=ZIP_DEFLATED) as archive:
    for destination, content in contents.items():
        entry = ZipInfo(destination, date_time=(2026, 1, 1, 0, 0, 0))
        entry.compress_type = ZIP_DEFLATED
        entry.create_system = 3
        entry.external_attr = 0o100644 << 16
        archive.writestr(entry, content)

print(json.dumps({"path": str(args.output.resolve()), "version": manifest["version"],
                  "files": len(files), "bytes": args.output.stat().st_size,
                  "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}, indent=2))
