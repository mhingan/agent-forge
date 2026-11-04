#!/usr/bin/env python3
"""Synchronize canonical repository assets into the installable package data."""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "src" / "agentforge" / "data"
DIRECTORIES = [".github", "adapters", "agents", "catalog", "commands", "docs", "rules", "skills", "templates", "workflows"]
FILES = ["README.md", "LICENSE", "SECURITY.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "CONTRIBUTING.md", "CHANGELOG.md"]


def expected_files() -> dict[str, Path]:
    expected: dict[str, Path] = {}
    for name in FILES:
        path = ROOT / name
        if path.is_file():
            expected[name] = path
    for directory in DIRECTORIES:
        base = ROOT / directory
        if base.is_dir():
            for path in base.rglob("*"):
                if path.is_file():
                    expected[path.relative_to(ROOT).as_posix()] = path
    return expected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if packaged data differs from canonical assets")
    args = parser.parse_args()
    expected = expected_files()
    if args.check:
        actual = {p.relative_to(DEST).as_posix(): p for p in DEST.rglob("*") if p.is_file()} if DEST.exists() else {}
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        changed = sorted(name for name in set(expected) & set(actual) if not filecmp.cmp(expected[name], actual[name], shallow=False))
        if missing or extra or changed:
            for label, items in [("missing", missing), ("extra", extra), ("changed", changed)]:
                for item in items:
                    print(f"{label}: {item}", file=sys.stderr)
            return 1
        print(f"Package data is synchronized ({len(expected)} files).")
        return 0

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    for relative, source in expected.items():
        destination = DEST / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    print(f"Synchronized {len(expected)} files into {DEST.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
