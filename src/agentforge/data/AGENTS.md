# AgentForge repository instructions

This repository is a vendor-neutral library of AI-agent skills, specialist roles, engineering rules, workflows, and prompt commands. Canonical assets live at the repository root; provider-specific output is rendered by the Python adapter layer.

## Source of truth

- `skills/`: canonical reusable task procedures and linked references.
- `agents/`: provider-neutral specialist role definitions.
- `rules/`: persistent engineering, safety, and domain constraints.
- `workflows/`: multi-step engineering and operations playbooks.
- `commands/`: focused reusable prompt recipes.
- `catalog/`: machine-readable skill and agent indexes.
- `adapters/targets.json`: human/machine-readable target registry.
- `src/agentforge/`: CLI, rendering, validation, and safe installation engine.
- `src/agentforge/data/`: generated package asset mirror; do not edit by hand.

## Engineering rules

1. Read the relevant skill and repository docs before editing a matching area.
2. Preserve the Agent Skills format: one `SKILL.md` per skill directory, valid YAML frontmatter, required `name` and `description`.
3. Use progressive disclosure: main skill is actionable; deeper templates/checklists belong in linked references.
4. Keep role definitions provider-neutral. Put target-specific rendering in adapters.
5. Verify target paths/formats against current official documentation; never infer feature support from filenames.
6. Preserve all user changes and do not overwrite unmanaged files.
7. `--force` must preserve locally modified managed content.
8. Manifest-driven uninstall must be confined to known AgentForge-managed paths under the selected root.
9. Do not add runtime dependencies without a concrete justification.
10. Do not execute scripts embedded in skills during validation or installation.
11. Never include credentials, private data, or proprietary customer content in source/examples/logs.
12. Require explicit approval for destructive, irreversible, production, or externally visible side effects.

## Quality gates

- JSON is strict, pretty-printed (two spaces), UTF-8, and ends with one newline.
- Catalog entries, skill frontmatter, filesystems, and adapter targets agree.
- Skill local reference links resolve.
- Generated outputs are deterministic and valid for the target format.
- Tests cover normal, error, shared path, and safety behavior.
- Embedded package data matches canonical source.

## Validation commands

```bash
python scripts/format_json.py --check
python -m agentforge validate --strict
python scripts/sync_package_data.py --check
python -m unittest discover -s tests -v
```

Do not claim a check passed unless it was actually executed and its result is available. Report changed files, test commands/results, compatibility impact, and residual risks.
