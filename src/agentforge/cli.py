"""Command-line interface for AgentForge."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from . import __version__
from .adapters import ALL_TARGETS, TARGETS
from .core import data_root, generate, install, uninstall, validate_repository


def _csv(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentforge",
        description="Build, validate, and install portable AI-agent skills and specialist profiles.",
    )
    parser.add_argument("--version", action="version", version=f"AgentForge {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    listing = sub.add_parser("list", help="List skills, agents, or supported targets")
    listing.add_argument("category", nargs="?", choices=["skills", "agents", "targets"], default="skills")

    validate = sub.add_parser("validate", help="Validate skill metadata, catalogs, and project files")
    validate.add_argument("--strict", action="store_true", help="Enable additional repository checks")

    for command, help_text in [("install", "Install skills, agents, rules, and workflows"), ("generate", "Generate native agent profiles and project instruction files")]:
        cmd = sub.add_parser(command, help=help_text)
        cmd.add_argument("--agent", default="all", help="Comma-separated targets or 'all'")
        cmd.add_argument("--scope", choices=["project", "global"], default="project")
        cmd.add_argument("--destination", type=Path, help="Project destination (defaults to current directory)")
        cmd.add_argument("--force", action="store_true", help="Refresh AgentForge-managed paths only")
        cmd.add_argument("--dry-run", action="store_true", help="Preview operations without writing files")
        if command == "install":
            cmd.add_argument("--skill", action="append", help="Install only this skill; repeat to select multiple")
            cmd.add_argument("--components", default="skills,agents,rules,workflows", help="Comma-separated: skills,agents,rules,workflows")

    remove = sub.add_parser("uninstall", help="Remove unmodified AgentForge-managed files")
    remove.add_argument("--agent", default="all", help="Comma-separated targets or 'all'")
    remove.add_argument("--scope", choices=["project", "global"], default="project")
    remove.add_argument("--destination", type=Path, help="Project destination (defaults to current directory)")
    remove.add_argument("--skill", action="append", help="Remove only this skill; repeat to select multiple")
    remove.add_argument("--dry-run", action="store_true", help="Preview removals without writing files")

    sub.add_parser("doctor", help="Show target paths and detected agent command-line tools")
    return parser


def _print_messages(messages: list[str]) -> None:
    for message in messages:
        print(message)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = data_root()

    try:
        if args.command == "list":
            if args.category == "skills":
                catalog = json.loads((root / "catalog/skills.json").read_text(encoding="utf-8"))
                for item in catalog["skills"]:
                    print(f"{item['name']:<28} {item['description']}")
            elif args.category == "agents":
                catalog = json.loads((root / "catalog/agents.json").read_text(encoding="utf-8"))
                for item in catalog["agents"]:
                    print(f"{item['name']:<28} {item['description']}")
            else:
                for target_id in ALL_TARGETS:
                    target = TARGETS[target_id]
                    capability = "skills + custom agents" if target.supports_custom_agents else "skills + rules"
                    print(f"{target_id:<14} {target.display_name:<24} {capability}")
            return 0

        if args.command == "validate":
            errors = validate_repository(root, strict=args.strict)
            if errors:
                for error in errors:
                    print(error, file=sys.stderr)
                print(f"Validation failed with {len(errors)} issue(s).", file=sys.stderr)
                return 1
            print("Validation passed. Skills, agents, catalogs, and required project files are consistent.")
            return 0

        if args.command == "install":
            messages = install(
                agent_arg=args.agent,
                scope=args.scope,
                skills=args.skill,
                components=_csv(args.components),
                force=args.force,
                dry_run=args.dry_run,
                destination=args.destination,
            )
            _print_messages(messages)
            return 0

        if args.command == "generate":
            messages = generate(
                agent_arg=args.agent,
                scope=args.scope,
                force=args.force,
                dry_run=args.dry_run,
                root=args.destination,
            )
            _print_messages(messages)
            return 0

        if args.command == "uninstall":
            messages = uninstall(
                agent_arg=args.agent,
                scope=args.scope,
                skills=args.skill,
                destination=args.destination,
                dry_run=args.dry_run,
            )
            _print_messages(messages)
            return 0

        if args.command == "doctor":
            print(f"AgentForge {__version__}")
            print(f"Python: {sys.version.split()[0]} ({'supported' if sys.version_info >= (3, 10) else 'requires 3.10+'})")
            print("\nProject paths:")
            for target_id in ALL_TARGETS:
                target = TARGETS[target_id]
                skills_path = target.project_skills
                agents_path = target.project_agents or "(not generated)"
                print(f"- {target.display_name}: skills={skills_path}; agents={agents_path}")
            print("\nDetected tools:")
            for executable in ["claude", "codex", "copilot", "gemini", "agy", "gh"]:
                print(f"- {executable}: {shutil.which(executable) or 'not found'}")
            print("\nAgentForge does not configure credentials, MCP servers, or tool permissions.")
            return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
