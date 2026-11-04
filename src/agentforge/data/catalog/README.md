# Catalogs and schemas

Catalogs are machine-readable indexes of canonical content. They are not the source of the full skill or agent body; the Markdown files remain authoritative for instructions.

## Files

| File | Purpose |
|---|---|
| `skills.json` | Index of each skill's name, title, canonical path, description, and tags |
| `agents.json` | Index of specialist roles, paths, descriptions, recommended skills, default mode, and tags |
| `schemas/skills.schema.json` | JSON Schema for the skills catalog |
| `schemas/agents.schema.json` | JSON Schema for the agent catalog |
| `../adapters/targets.json` | Native target formats and installation paths |
| `../adapters/targets.schema.json` | JSON Schema for the target registry |

## Data rules

- Names are stable lowercase hyphenated IDs.
- Paths are repository-relative and point to canonical source.
- Skill descriptions must match `SKILL.md` frontmatter.
- Agent paths must match the source filename.
- Recommended skills must exist in `skills.json`.
- Default agent mode is either `read-only` or `read-write`; it is guidance, not a host permission grant.
- Tags are short discovery terms, not execution instructions.

## Formatting

All JSON uses strict syntax, two-space indentation, UTF-8 Unicode characters, stable field order, and a trailing newline. Do not hand-minify catalog files.

```bash
python scripts/format_json.py
python scripts/format_json.py --check
python -m agentforge validate --strict
```

The validator checks formatting and core cross-references. The schemas provide a machine-readable contract for external tooling and future integrations.
