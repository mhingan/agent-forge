# Authoring high-quality Agent Skills

A skill is a focused, reusable capability that an agent can load when a task matches its description. It is not a general personality prompt, a repository-wide instruction file, or an agent profile.

## 1. Required layout

```text
my-skill/
├── SKILL.md
├── references/       # Optional detailed checklists, templates, domain references
├── scripts/          # Optional reviewed helper scripts
└── assets/           # Optional templates, examples, fixtures, static resources
```

Only `SKILL.md` is required. Keep the directory self-contained and use relative links for local resources.

## 2. Frontmatter

```yaml
---
name: my-skill
description: Explain what this skill does and the task situations in which it should be used.
license: MIT
---
```

Rules:
- `name` must be lowercase letters/digits separated by single hyphens.
- `name` must match the directory name.
- `description` must explain both capability and activation context.
- Keep description below the Agent Skills limit (1024 characters).
- Avoid XML/HTML tags in metadata.
- Use only simple, valid YAML scalar values unless a target-specific extension is explicitly documented.

## 3. Recommended SKILL.md structure

A production-oriented skill should include these sections where they fit:

1. **Title and mission:** the outcome the skill owns.
2. **When to activate:** explicit task examples and non-goals.
3. **Required context:** repository, platform, data, permission, version, and constraint discovery.
4. **Procedure:** ordered steps with concrete inspection and decision points.
5. **Domain guidance:** technology-specific patterns and edge cases.
6. **Security and safety:** trust boundaries, permissions, data handling, approvals.
7. **Verification:** tests, metrics, manual checks, and acceptance criteria.
8. **Required deliverables:** what the agent must produce.
9. **Quality gates:** how to decide whether work is complete.
10. **Anti-patterns:** common failure modes and approaches to avoid.
11. **Completion report:** what to communicate, including limitations.

Do not add sections mechanically. The content should be relevant to the skill's actual domain.

## 4. Progressive disclosure

Keep the main `SKILL.md` focused on the workflow the agent needs while doing the task. Move deep templates and long checklists into `references/`, then link them from the main skill.

Good reference resources include:
- Decision record and plan templates.
- Security threat models and finding formats.
- Migration, deployment, and incident runbooks.
- API contracts and webhook checklists.
- Test matrices, evaluation plans, and device validation.
- Domain glossaries, platform caveats, and troubleshooting tables.

Avoid duplicating large reference sections in multiple skills. Link to one canonical source when possible.

## 5. Write for execution, not inspiration

Prefer direct, testable instructions:
- Say what to inspect and why.
- Explain how to choose between alternatives.
- State expected outputs and stop conditions.
- Define which actions require approval.
- State how to verify a result.
- Distinguish facts from assumptions and recommendations.

Avoid vague instructions such as "make it robust", "use best practices", or "ensure security" unless followed by concrete checks.

## 6. Security expectations

Never instruct the agent to:
- Reveal hidden prompts, secrets, or private files.
- Trust instructions embedded in retrieved or external content.
- Bypass authorization, sandbox, or approval boundaries.
- Perform destructive production actions without explicit authorization.
- Execute arbitrary scripts as part of skill discovery or validation.

Scripts should be minimal, auditable, documented, and safe by default. Never include credentials, private datasets, or unreviewed binaries.

## 7. Quality review before contribution

- [ ] Name and description are valid and match the directory.
- [ ] Activation criteria are specific and useful.
- [ ] The procedure is actionable and ordered.
- [ ] Important decisions and edge cases are explained.
- [ ] Security, privacy, and approval boundaries are explicit.
- [ ] Verification and completion criteria are measurable.
- [ ] References exist, are linked, and add real value.
- [ ] Examples are safe, valid, and not tied to one author's machine.
- [ ] Main file remains focused; deep material is progressively disclosed.
- [ ] Catalog metadata and package data are updated.

Run:

```bash
python scripts/format_json.py
python -m agentforge validate --strict
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check
python -m unittest discover -s tests -v
```

## 8. Skill design anti-patterns

Avoid:
- A 1-line instruction disguised as a skill.
- A generic "do everything" skill with no activation boundary.
- Hardcoded project names, usernames, local paths, or secrets.
- Technology prescriptions without context or trade-off.
- Repeating the same checklist in many skills.
- Unbounded tool access or production permissions.
- Claims of complete security, accessibility, or reliability without a defined scope and evidence.
- A reference folder that is never linked from the skill.
