# GitHub Copilot instructions

Follow `AGENTS.md` for repository-wide engineering and safety rules.

## Repository structure
- `skills/` contains canonical Agent Skills.
- `agents/` contains provider-neutral specialist roles.
- `rules/`, `workflows/`, and `commands/` contain reusable policy/playbook/prompt content.
- `src/agentforge/adapters.py` renders native formats.
- `src/agentforge/data/` is generated package data; do not edit it directly.

## Contribution requirements
- Preserve valid Agent Skills frontmatter and directory/name matching.
- Keep skills focused, actionable, and linked to deep reference material.
- Do not assume every host supports identical metadata, tools, or agent capabilities.
- Verify provider-specific behavior against official docs.
- Keep JSON strict, UTF-8, two-space formatted, with a trailing newline.
- Update catalogs, schemas, tests, changelog, and embedded package assets as appropriate.
- Never overwrite unmanaged or locally modified installed files.
- Do not execute skill scripts during validation or installation.

## Validation
Run `python scripts/format_json.py --check`, `python -m agentforge validate --strict`, `python scripts/sync_package_data.py --check`, and `python -m unittest discover -s tests -v`.

Never expose secrets. Ask before destructive, production, or external side-effect operations.
