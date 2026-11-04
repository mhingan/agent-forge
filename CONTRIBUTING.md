# Contributing to AgentForge

Contributions should improve the library's usefulness, technical accuracy, safety, clarity, and cross-agent portability. Avoid adding content solely to increase file count; every component should solve a distinct recurring task.

## Repository model

- Root `skills/`, `agents/`, `rules/`, `workflows/`, `commands/`, `docs/`, `catalog/`, and `adapters/` are canonical source.
- `src/agentforge/data/` is an embedded snapshot used by installed wheels.
- Provider-specific behavior belongs in `src/agentforge/adapters.py`, not in the canonical provider-neutral role description.
- Catalog JSON files are human-reviewable, pretty-printed, and schema-backed.

## Add or improve a skill

1. Create `skills/<lowercase-hyphen-name>/SKILL.md`.
2. Add valid YAML frontmatter with `name`, `description`, and optional `license`.
3. Match `name` to the directory and describe both capability and activation context.
4. Keep the main skill focused on a complete, actionable task procedure.
5. Include scope, prerequisites, inspection steps, decision points, verification, deliverables, boundaries, and completion criteria where relevant.
6. Move detailed reusable templates/checklists into `references/` and link them in the skill.
7. Use relative links; do not duplicate long reference content across multiple skills.
8. Add/update `catalog/skills.json` and any applicable JSON Schema.
9. Add tests for new validator or behavior where needed.

## Add or improve a specialist agent

1. Create `agents/<name>.md`.
2. Include `name` and `description` frontmatter.
3. Define a bounded role, responsibilities, working method, inputs/outputs, safety boundaries, and completion standard.
4. Keep tool permissions conservative. A read-only prompt is not a sandbox.
5. Update `catalog/agents.json`, including recommended skills and default mode.
6. Ensure native renderers handle the profile correctly and add adapter tests if formats change.

## Add rules, workflows, or commands

- **Rules:** persistent constraints, concise enough to remain useful as context.
- **Workflows:** ordered playbooks with gates, stop conditions, validation, and handover.
- **Commands:** focused prompts with purpose, inputs, procedure, output, and boundaries.

Keep task-specific depth in skills/references rather than repeating it globally.

## Add or update a target adapter

1. Verify the target's current official documentation.
2. Update `src/agentforge/adapters.py` and `adapters/targets.json`.
3. Update `docs/compatibility.md` and `adapters/README.md`.
4. Add renderer, serialization, and install/uninstall tests.
5. Test shared paths, user/global paths, and existing-file protection.
6. Do not claim compatibility from a filename alone.

## Style and content standards

- Use clear, direct, actionable English in the public library.
- Prefer measurable acceptance criteria over vague adjectives.
- Separate facts, assumptions, recommendations, and examples.
- Use safe placeholders; never include secrets or private/customer data.
- Explain version and platform caveats.
- State when an operation requires explicit human approval.
- Avoid hardcoded project paths, user names, credentials, or environment-specific values.

## JSON and catalog standards

Canonical JSON format:
- Strict JSON only (no comments, trailing commas, NaN, or Infinity).
- Two-space indentation.
- UTF-8, with Unicode characters preserved.
- Exactly one final newline.
- Stable key ordering and clear nested structure.
- Catalog metadata must match the filesystem and source frontmatter.

Run `python scripts/format_json.py` to format and `python scripts/format_json.py --check` to verify.

## Required validation

Before finalizing:

```bash
python scripts/format_json.py
python -m agentforge validate --strict
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check
python -m unittest discover -s tests -v
```

If possible, build and inspect the wheel:

```bash
python -m pip install build
python -m build
```

CI runs the JSON check, embedded package-data check, strict validation, and unit tests on Python 3.10–3.13.

## Pull requests

Include motivation, scope, user impact, target compatibility, data/security implications, tests, and limitations. Update changelog and documentation for user-visible changes. Do not mark tests as passing unless the actual result is available.

## Package data synchronization

After changing canonical files included in the library, run:

```bash
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check
```

Do not hand-edit the embedded mirror. The root files are canonical.
