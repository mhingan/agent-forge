#!/usr/bin/env python3
"""Format or verify every repository JSON file using AgentForge's canonical style."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".venv", "venv", "__pycache__", "build", "dist"}


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate object key: {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"invalid JSON constant {value!r}")),
    )


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"


def iter_json_files(root: Path):
    for path in sorted(root.rglob("*.json")):
        if not any(part in EXCLUDED_PARTS for part in path.parts):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Fail if any JSON file is invalid or not canonically formatted")
    mode.add_argument("--write", action="store_true", help="Rewrite JSON files using the canonical format (default)")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to scan")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2

    failures = 0
    checked = 0
    for path in iter_json_files(root):
        checked += 1
        try:
            value = load_json(path)
            formatted = canonical_json(value)
            current = path.read_text(encoding="utf-8")
            if current != formatted:
                if args.check:
                    print(f"NOT FORMATTED: {path.relative_to(root)}", file=sys.stderr)
                    failures += 1
                else:
                    path.write_text(formatted, encoding="utf-8", newline="\n")
                    print(f"FORMATTED: {path.relative_to(root)}")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            print(f"INVALID JSON: {path.relative_to(root)}: {exc}", file=sys.stderr)
            failures += 1

    if failures:
        print(f"Checked {checked} JSON file(s); found {failures} problem(s).", file=sys.stderr)
        return 1
    print(f"Checked {checked} JSON file(s); all are valid and canonically formatted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
