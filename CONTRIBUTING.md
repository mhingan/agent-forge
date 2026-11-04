# Contributing

Contributions should improve reuse, safety, clarity, and cross-agent portability.

## Add a skill

1. Create `skills/<lowercase-hyphen-name>/SKILL.md`.
2. Include YAML frontmatter with required `name` and `description` fields.
3. Keep the skill focused on one capability and explain when it should activate.
4. Use progressive disclosure: keep the main file actionable and place long references/examples in sibling files.
5. Avoid vendor-specific commands unless they are clearly labeled as optional platform notes.
6. Do not include secrets, proprietary data, unreviewed binaries, or scripts that access credentials.
7. Add the skill to `catalog/skills.json`.
8. Run validation and tests.

## Add an agent

Create `agents/<name>.md` with YAML frontmatter containing `name` and `description`. The body is the provider-neutral role prompt. Update `catalog/agents.json` if you add/remove an agent. Keep default agent capabilities conservative; do not silently grant destructive or unrestricted tool permissions.

## Style

- Use direct, imperative instructions.
- Prefer concrete steps, checklists, and acceptance criteria.
- State assumptions and ask for missing critical requirements rather than inventing them.
- Separate requirements, recommendations, and optional practices.
- Explain irreversible or high-impact actions and require explicit approval.

## Validation

```bash
python -m agentforge validate --strict
python -m unittest discover -s tests -v
```

## Pull requests

Include the motivation, scope, compatibility impact, and validation output. Update the changelog for user-visible changes.

## Package data

The root folders are canonical in a source checkout. Before building a wheel after changing skills, agents, rules, workflows, documentation, or catalogs, run:

```bash
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check
```

The CLI reads canonical root assets in a checkout and the embedded `src/agentforge/data/` copy when installed as a package.
