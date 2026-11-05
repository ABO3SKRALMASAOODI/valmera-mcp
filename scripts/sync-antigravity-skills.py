#!/usr/bin/env python3
"""Keep the self-contained Antigravity package aligned with the shared skills."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true", help="Fail if the bundled skill files differ")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
names = ("edit-video-with-valmera", "turn-long-video-into-shorts", "website-demo-video")
different = []
for name in names:
    source = root / "skills" / name / "SKILL.md"
    target = root / "plugins/antigravity/skills" / name / "SKILL.md"
    if not target.exists() or source.read_bytes() != target.read_bytes():
        different.append(name)
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
if args.check and different:
    raise SystemExit("Run python3 scripts/sync-antigravity-skills.py: " + ", ".join(different))
print("Antigravity skill bundle matches the three shared skills.")
