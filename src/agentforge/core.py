"""Core validation, generation, installation, and safe uninstall logic."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from .adapters import ALL_TARGETS, TARGETS, parse_frontmatter, render_agent, render_antigravity_rule, render_contexts

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_SKILL_NAMES = {"anthropic", "claude"}
VALID_COMPONENTS = {"skills", "agents", "rules", "workflows"}


def data_root() -> Path:
    """Return canonical assets in a source checkout or embedded wheel data."""
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / "skills").is_dir() and (source_root / "catalog").is_dir():
        return source_root
    packaged = Path(__file__).resolve().parent / "data"
    if (packaged / "skills").is_dir() and (packaged / "catalog").is_dir():
        return packaged
    raise FileNotFoundError("AgentForge assets are missing from both the source tree and package data")


def load_manifest(root: Path, scope: str) -> tuple[Path, dict[str, Any]]:
    manifest_path = (Path.home() if scope == "global" else root) / ".agentforge" / "install-manifest.json"
    if manifest_path.exists():
        try:
            data = _load_json_file(manifest_path)
        except (json.JSONDecodeError, OSError, ValueError) as exc:
            raise ValueError(f"Cannot read install manifest: {manifest_path}: {exc}") from exc
    else:
        data = {"version": 1, "installations": []}
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ValueError(f"Unsupported or malformed install manifest: {manifest_path}")
    entries = data.get("installations")
    if not isinstance(entries, list):
        raise ValueError(f"Malformed installations list in manifest: {manifest_path}")
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"Malformed manifest entry at index {index}")
        if entry.get("target") not in TARGETS:
            raise ValueError(f"Unknown target in manifest entry {index}")
        if not isinstance(entry.get("path"), str) or not Path(entry["path"]).is_absolute():
            raise ValueError(f"Invalid absolute path in manifest entry {index}")
        if not isinstance(entry.get("kind"), str) or not isinstance(entry.get("name"), str):
            raise ValueError(f"Invalid kind/name in manifest entry {index}")
        if not isinstance(entry.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            raise ValueError(f"Invalid SHA-256 in manifest entry {index}")
    return manifest_path, data


def _hash_path(path: Path) -> str:
    digest = hashlib.sha256()
    if path.is_file():
        digest.update(path.read_bytes())
    elif path.is_dir():
        for child in sorted(p for p in path.rglob("*") if p.is_file()):
            digest.update(child.relative_to(path).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(child.read_bytes())
            digest.update(b"\0")
    else:
        return "missing"
    return digest.hexdigest()



def _is_within(path: Path, root: Path) -> bool:
    """Return True when path resolves inside root (including root itself)."""
    try:
        path.resolve(strict=False).relative_to(root.resolve(strict=False))
        return True
    except ValueError:
        return False


def _is_managed_location(path: Path, root: Path, scope: str) -> bool:
    """Constrain manifest-driven deletion to AgentForge's known install paths."""
    try:
        relative = path.resolve(strict=False).relative_to(root.resolve(strict=False)).as_posix()
    except ValueError:
        return False
    if scope == "project":
        allowed = (
            ".claude/skills/", ".claude/agents/", ".codex/agents/",
            ".agents/skills/", ".agents/agents/", ".agents/rules/",
            ".gemini/skills/", ".gemini/agents/",
            ".github/skills/", ".github/agents/",
            ".agentforge/rules/", ".agentforge/workflows/",
        )
        exact = {"AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"}
    else:
        allowed = (
            ".claude/skills/", ".claude/agents/", ".agents/skills/",
            ".codex/agents/", ".copilot/skills/", ".copilot/agents/",
            ".gemini/skills/", ".gemini/agents/",
            ".gemini/config/skills/", ".gemini/config/agents/", ".gemini/config/rules/",
            ".gemini/antigravity-cli/skills/",
        )
        exact = set()
    return relative in exact or any(relative.startswith(prefix) for prefix in allowed)


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json_file(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return json.loads(
        text,
        object_pairs_hook=_reject_duplicate_json_keys,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"invalid JSON constant: {value}")),
    )

def validate_repository(root: Path | None = None, strict: bool = False) -> list[str]:
    root = root or data_root()
    errors: list[str] = []
    skills_dir, agents_dir = root / "skills", root / "agents"
    if not skills_dir.is_dir():
        errors.append("Missing skills/ directory")
    if not agents_dir.is_dir():
        errors.append("Missing agents/ directory")

    skill_names: set[str] = set()
    if skills_dir.is_dir():
        for folder in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill_file = folder / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"{folder.relative_to(root)}: missing SKILL.md")
                continue
            try:
                metadata, body = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            except (OSError, UnicodeError) as exc:
                errors.append(f"{skill_file.relative_to(root)}: cannot read file ({exc})")
                continue
            name = metadata.get("name", "")
            description = metadata.get("description", "")
            rel = skill_file.relative_to(root)
            if not name:
                errors.append(f"{rel}: missing frontmatter name")
            if not description:
                errors.append(f"{rel}: missing frontmatter description")
            if name and not SKILL_NAME_RE.fullmatch(name):
                errors.append(f"{rel}: invalid skill name '{name}'")
            if name in RESERVED_SKILL_NAMES:
                errors.append(f"{rel}: reserved word used as skill name")
            if name and name != folder.name:
                errors.append(f"{rel}: name '{name}' does not match directory '{folder.name}'")
            if name in skill_names:
                errors.append(f"Duplicate skill name: {name}")
            skill_names.add(name)
            if len(name) > 64:
                errors.append(f"{rel}: skill name exceeds 64 characters")
            if len(description) > 1024:
                errors.append(f"{rel}: description exceeds 1024 characters")
            if "<" in description or ">" in description:
                errors.append(f"{rel}: description must not contain XML/HTML tags")
            if not body.strip():
                errors.append(f"{rel}: empty skill body")
            skill_files = [p for p in folder.rglob("*") if p.is_file() and p.name.lower() == "skill.md"]
            if len(skill_files) != 1:
                errors.append(f"{folder.relative_to(root)}: expected exactly one SKILL.md, found {len(skill_files)}")
            content = skill_file.read_text(encoding="utf-8")
            if strict:
                if "TODO" in content or "FIXME" in content:
                    errors.append(f"{rel}: contains TODO/FIXME marker")
                if len(content.splitlines()) > 500:
                    errors.append(f"{rel}: exceeds 500 lines; move deep reference material into references/")
                for relative in re.findall(r"\[[^\]]+\]\((?!https?://|mailto:)([^)#]+)(?:#[^)]*)?\)", content):
                    if not (folder / relative).exists():
                        errors.append(f"{rel}: broken local reference link '{relative}'")

    agent_names: set[str] = set()
    if agents_dir.is_dir():
        for agent_file in sorted(agents_dir.glob("*.md")):
            meta, body = parse_frontmatter(agent_file.read_text(encoding="utf-8"))
            name, description = meta.get("name", ""), meta.get("description", "")
            if not name or not description:
                errors.append(f"{agent_file.relative_to(root)}: missing name or description frontmatter")
            if name and name != agent_file.stem:
                errors.append(f"{agent_file.relative_to(root)}: name does not match filename")
            if name in agent_names:
                errors.append(f"Duplicate agent name: {name}")
            agent_names.add(name)
            if not body.strip():
                errors.append(f"{agent_file.relative_to(root)}: empty agent prompt")

    for catalog_name, key, actual in [
        ("skills.json", "skills", skill_names),
        ("agents.json", "agents", agent_names),
    ]:
        catalog_file = root / "catalog" / catalog_name
        if not catalog_file.is_file():
            errors.append(f"Missing catalog/{catalog_name}")
            continue
        try:
            catalog = json.loads(catalog_file.read_text(encoding="utf-8"))
            catalog_names = {item["name"] for item in catalog.get(key, [])}
            if catalog_names != actual:
                errors.append(f"catalog/{catalog_name}: entries do not match filesystem")
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            errors.append(f"Invalid catalog/{catalog_name}: {exc}")

    for required in ["README.md", "LICENSE", "SECURITY.md", "AGENTS.md", "docs/compatibility.md"]:
        if not (root / required).is_file():
            errors.append(f"Missing required project file: {required}")

    # All committed JSON must be valid, duplicate-key-free, and consistently
    # rendered with two-space indentation, UTF-8 characters, and a final newline.
    for json_file in sorted(root.rglob("*.json")):
        if ".git" in json_file.parts or ".venv" in json_file.parts:
            continue
        try:
            raw = json_file.read_text(encoding="utf-8")
            parsed = _load_json_file(json_file)
            canonical = json.dumps(parsed, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
            if raw != canonical:
                errors.append(f"{json_file.relative_to(root)}: JSON is not pretty-printed (use 2 spaces and a trailing newline)")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{json_file.relative_to(root)}: invalid JSON: {exc}")

    try:
        skills_catalog = _load_json_file(root / "catalog" / "skills.json")
        skill_entries = {item["name"]: item for item in skills_catalog["skills"]}
        if set(skill_entries) != skill_names:
            errors.append("catalog/skills.json: entries do not match filesystem")
        for skill_name, entry in skill_entries.items():
            if entry.get("path") != f"skills/{skill_name}/SKILL.md":
                errors.append(f"catalog/skills.json: invalid path for {skill_name}")
            if not isinstance(entry.get("title"), str) or not isinstance(entry.get("tags"), list):
                errors.append(f"catalog/skills.json: malformed entry for {skill_name}")
            skill_file = root / "skills" / skill_name / "SKILL.md"
            if skill_file.is_file():
                metadata, _ = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
                if entry.get("description") != metadata.get("description"):
                    errors.append(f"catalog/skills.json: description mismatch for {skill_name}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"catalog/skills.json: invalid catalog structure: {exc}")

    try:
        agents_catalog = _load_json_file(root / "catalog" / "agents.json")
        agent_entries = {item["name"]: item for item in agents_catalog["agents"]}
        if set(agent_entries) != agent_names:
            errors.append("catalog/agents.json: entries do not match filesystem")
        for agent_name, entry in agent_entries.items():
            if entry.get("path") != f"agents/{agent_name}.md":
                errors.append(f"catalog/agents.json: invalid path for {agent_name}")
            if entry.get("default_mode") not in {"read-only", "read-write"}:
                errors.append(f"catalog/agents.json: invalid default_mode for {agent_name}")
            recommendations = entry.get("recommended_skills", [])
            if not isinstance(recommendations, list) or not set(recommendations).issubset(skill_names):
                errors.append(f"catalog/agents.json: unknown recommended skill for {agent_name}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"catalog/agents.json: invalid catalog structure: {exc}")

    try:
        target_catalog = _load_json_file(root / "adapters" / "targets.json")
        if set(target_catalog.get("targets", {})) != set(TARGETS):
            errors.append("adapters/targets.json: targets do not match implemented adapters")
        for target_id, target in TARGETS.items():
            configured = target_catalog["targets"].get(target_id, {})
            skill_paths = configured.get("skills", {}).get("project", [])
            agent_paths = configured.get("agents", {}).get("project", [])
            if not skill_paths or skill_paths[0] != target.project_skills:
                errors.append(f"adapters/targets.json: project skill path mismatch for {target_id}")
            if target.project_agents and (not agent_paths or agent_paths[0] != target.project_agents):
                errors.append(f"adapters/targets.json: project agent path mismatch for {target_id}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"adapters/targets.json: invalid target registry: {exc}")

    return errors


def _parse_agents(agent_arg: str) -> list[str]:
    if agent_arg.strip().lower() == "all":
        return list(ALL_TARGETS)
    requested = [item.strip().lower() for item in agent_arg.split(",") if item.strip()]
    if not requested:
        raise ValueError("Select at least one target or use --agent all")
    unknown = sorted(set(requested) - set(TARGETS))
    if unknown:
        raise ValueError("Unknown target(s): " + ", ".join(unknown) + ". Valid targets: " + ", ".join(ALL_TARGETS))
    return list(dict.fromkeys(requested))


def _select_skills(root: Path, selected: list[str] | None) -> list[Path]:
    all_skills = sorted(p for p in (root / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not selected:
        return all_skills
    wanted = set(selected)
    unknown = wanted - {p.name for p in all_skills}
    if unknown:
        raise ValueError("Unknown skill(s): " + ", ".join(sorted(unknown)))
    return [p for p in all_skills if p.name in wanted]


def _record(manifest: dict[str, Any], target: str, kind: str, name: str, path: Path) -> None:
    absolute = str(path.resolve())
    manifest["installations"] = [
        item for item in manifest["installations"]
        if not (item.get("target") == target and item.get("kind") == kind and item.get("name") == name and item.get("path") == absolute)
    ]
    manifest["installations"].append({
        "target": target, "kind": kind, "name": name,
        "path": absolute, "sha256": _hash_path(path),
    })


def _save_manifest(path: Path, manifest: dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def _copy_managed(source: Path | None, destination: Path, text: str | None, target: str,
                  kind: str, name: str, manifest: dict[str, Any], force: bool,
                  dry_run: bool, messages: list[str], install_root: Path) -> str:
    """Copy one artifact without claiming or overwriting user-owned content.

    --force refreshes only an unchanged AgentForge-managed artifact. A local
    modification is always preserved and must be resolved manually.
    """
    if not _is_within(destination, install_root):
        raise ValueError(f"Refusing to install outside the selected {install_root} scope: {destination}")

    dest_abs = str(destination.resolve(strict=False))
    existing_records = [item for item in manifest["installations"] if item.get("path") == dest_abs]
    owned = bool(existing_records)

    if destination.exists() and not owned:
        messages.append(f"SKIP unmanaged existing path (left untouched): {destination}")
        return "unmanaged"

    if destination.exists() and owned:
        expected_hashes = {item.get("sha256") for item in existing_records}
        current_hash = _hash_path(destination)
        if current_hash not in expected_hashes:
            messages.append(f"KEEP modified managed path (local edits preserved, even with --force): {destination}")
            return "managed"
        if not force:
            messages.append(f"KEEP managed path (use --force to refresh unchanged content): {destination}")
            return "managed"

    messages.append(f"{'WOULD INSTALL' if dry_run else 'INSTALL'} {kind} '{name}' for {target}: {destination}")
    if dry_run:
        return "planned"

    if destination.is_dir():
        shutil.rmtree(destination)
    elif destination.exists():
        destination.unlink()
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source is not None:
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
    else:
        destination.write_text(text or "", encoding="utf-8")
    _record(manifest, target, kind, name, destination)
    return "written"


def install(root: Path | None = None, agent_arg: str = "all", scope: str = "project",
            skills: list[str] | None = None, components: list[str] | None = None,
            force: bool = False, dry_run: bool = False, destination: Path | None = None) -> list[str]:
    source_root = data_root()
    project_root = (destination or root or Path.cwd()).resolve() if scope == "project" else Path.home()
    if scope not in {"project", "global"}:
        raise ValueError("scope must be project or global")
    targets = _parse_agents(agent_arg)
    components = components or sorted(VALID_COMPONENTS)
    unknown = set(components) - VALID_COMPONENTS
    if unknown:
        raise ValueError("Unknown component(s): " + ", ".join(sorted(unknown)))
    manifest_path, manifest = load_manifest(project_root, scope)
    messages: list[str] = []
    selected_skills = _select_skills(source_root, skills) if "skills" in components else []

    for target_id in targets:
        target = TARGETS[target_id]
        skill_root = target.skill_path(scope, Path.home())
        if scope == "project" and not skill_root.is_absolute():
            skill_root = project_root / skill_root
        for skill_dir in selected_skills:
            dest = skill_root / skill_dir.name
            before = len(manifest["installations"])
            status = _copy_managed(skill_dir, dest, None, target_id, "skill", skill_dir.name,
                                   manifest, force, dry_run, messages, project_root)
            if status == "managed" and not dry_run and len(manifest["installations"]) == before and dest.exists():
                if not any(x.get("target") == target_id and x.get("kind") == "skill" and x.get("name") == skill_dir.name and x.get("path") == str(dest.resolve()) for x in manifest["installations"]):
                    _record(manifest, target_id, "skill", skill_dir.name, dest)

        if "agents" in components:
            agent_root = target.agent_path(scope, Path.home())
            if scope == "project" and agent_root is not None and not agent_root.is_absolute():
                agent_root = project_root / agent_root
            if not target.supports_custom_agents or agent_root is None:
                messages.append(f"INFO {target.display_name}: no custom-agent renderer configured")
            else:
                for agent_source in sorted((source_root / "agents").glob("*.md")):
                    filename, rendered = render_agent(target_id, agent_source)
                    dest = agent_root / filename
                    before = len(manifest["installations"])
                    status = _copy_managed(None, dest, rendered, target_id, "agent", agent_source.stem,
                                           manifest, force, dry_run, messages, project_root)
                    if status == "managed" and not dry_run and len(manifest["installations"]) == before and dest.exists():
                        if not any(x.get("target") == target_id and x.get("kind") == "agent" and x.get("name") == agent_source.stem and x.get("path") == str(dest.resolve()) for x in manifest["installations"]):
                            _record(manifest, target_id, "agent", agent_source.stem, dest)

    if scope == "project" and "rules" in components:
        rule_sources = sorted((source_root / "rules").glob("*.md"))
        for rule_source in rule_sources:
            dest = project_root / ".agentforge" / "rules" / rule_source.name
            status = _copy_managed(rule_source, dest, None, targets[0], "rule", rule_source.stem,
                                   manifest, force, dry_run, messages, project_root)
            if status in {"written", "managed"} and not dry_run and dest.exists():
                for extra_target in targets[1:]:
                    _record(manifest, extra_target, "rule", rule_source.stem, dest)
        antigravity_targets = [t for t in targets if t in {"antigravity", "antigravity-cli"}]
        if antigravity_targets:
            primary = antigravity_targets[0]
            for rule_source in rule_sources:
                dest = project_root / ".agents" / "rules" / rule_source.name
                rendered = render_antigravity_rule(rule_source)
                status = _copy_managed(None, dest, rendered, primary, "antigravity-rule", rule_source.stem,
                                       manifest, force, dry_run, messages, project_root)
                if status in {"written", "managed"} and not dry_run and dest.exists():
                    for extra_target in antigravity_targets[1:]:
                        _record(manifest, extra_target, "antigravity-rule", rule_source.stem, dest)

    if scope == "project" and "workflows" in components:
        for workflow in sorted((source_root / "workflows").glob("*.md")):
            dest = project_root / ".agentforge" / "workflows" / workflow.name
            status = _copy_managed(workflow, dest, None, targets[0], "workflow", workflow.stem,
                                   manifest, force, dry_run, messages, project_root)
            if status in {"written", "managed"} and not dry_run and dest.exists():
                for extra_target in targets[1:]:
                    _record(manifest, extra_target, "workflow", workflow.stem, dest)

    if scope == "project" and ({"rules", "workflows"} & set(components)):
        context_files: set[tuple[str, str, str]] = set()
        for target_id in targets:
            for relative, content in render_contexts(target_id):
                context_files.add((target_id, relative, content))
        for target_id, relative, content in sorted(context_files, key=lambda x: (x[1], x[0])):
            dest = project_root / relative
            before = len(manifest["installations"])
            status = _copy_managed(None, dest, content, target_id, "context", Path(relative).name,
                                   manifest, force, dry_run, messages, project_root)
            if status == "managed" and not dry_run and dest.exists() and len(manifest["installations"]) == before:
                if not any(x.get("target") == target_id and x.get("kind") == "context" and x.get("path") == str(dest.resolve()) for x in manifest["installations"]):
                    _record(manifest, target_id, "context", Path(relative).name, dest)

    _save_manifest(manifest_path, manifest, dry_run)
    if not dry_run:
        messages.append(f"Manifest: {manifest_path}")
    return messages


def uninstall(agent_arg: str = "all", scope: str = "project", skills: list[str] | None = None,
              destination: Path | None = None, dry_run: bool = False) -> list[str]:
    if scope not in {"project", "global"}:
        raise ValueError("scope must be project or global")
    targets = set(_parse_agents(agent_arg))
    root = (destination or Path.cwd()).resolve() if scope == "project" else Path.home()
    manifest_path, manifest = load_manifest(root, scope)
    selected_skills = set(skills or [])
    all_entries = manifest["installations"]
    removing = [item for item in all_entries if item.get("target") in targets and (not selected_skills or (item.get("kind") == "skill" and item.get("name") in selected_skills))]
    keeping = [item for item in all_entries if item not in removing]
    messages: list[str] = []
    preserved_modified: list[dict[str, Any]] = []
    candidate_paths = sorted({item.get("path") for item in removing if item.get("path")}, key=len, reverse=True)
    for raw in candidate_paths:
        path = Path(raw)
        if any(item.get("path") == raw for item in keeping):
            messages.append(f"KEEP shared path (still used by another target): {path}")
            continue
        entries_for_path = [item for item in removing if item.get("path") == raw]
        expected = entries_for_path[0].get("sha256") if entries_for_path else None
        if not _is_managed_location(path, root, scope):
            messages.append(f"SKIP unsafe manifest path (outside AgentForge-managed locations): {path}")
            preserved_modified.extend(entries_for_path)
            continue
        if not path.exists():
            messages.append(f"ALREADY ABSENT: {path}")
            continue
        if expected and _hash_path(path) != expected:
            messages.append(f"KEEP modified path (hash changed): {path}")
            preserved_modified.extend(entries_for_path)
            continue
        messages.append(f"{'WOULD REMOVE' if dry_run else 'REMOVE'}: {path}")
        if not dry_run:
            shutil.rmtree(path) if path.is_dir() else path.unlink()
    if not dry_run:
        manifest["installations"] = keeping + preserved_modified
        _save_manifest(manifest_path, manifest, False)
        messages.append(f"Manifest updated: {manifest_path}")
    return messages


def generate(root: Path | None = None, agent_arg: str = "all", scope: str = "project",
             force: bool = False, dry_run: bool = False) -> list[str]:
    """Generate native specialist profiles and project-level context/rules."""
    return install(root=root, destination=root, agent_arg=agent_arg, scope=scope,
                   components=["agents", "rules"], force=force, dry_run=dry_run)
