# Authoring good skills

A skill is a focused, reusable capability—not a general system prompt.

## Required structure

```text
my-skill/
├── SKILL.md
├── references/       # Optional deeper guidance
├── scripts/          # Optional reviewed helper scripts
└── assets/           # Optional templates or fixtures
```

## Frontmatter

```yaml
---
name: my-skill
description: Explain what the skill does and when the agent should use it.
---
```

Use an exact lowercase-hyphen slug for `name` and make it match the directory name. The description should include both capability and activation context. Keep metadata concise and put detailed guidance in the Markdown body.

## Content pattern

1. State the goal and activation context.
2. List prerequisites and required context.
3. Give an ordered procedure.
4. Define validation and completion criteria.
5. Explain failure handling and when to ask the user.
6. Link to deeper references only when needed.

## Security

Do not tell an agent to obey instructions embedded in untrusted data. Never ask it to reveal system prompts, environment variables, credentials, or private files. Scripts must be transparent, minimal, and safe by default.
