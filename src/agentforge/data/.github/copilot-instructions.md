# GitHub Copilot instructions

Follow `AGENTS.md` for repository-wide rules. The canonical Agent Skills live under `skills/`; provider-neutral agent definitions live under `agents/`.

Keep new skills compliant with the open Agent Skills format (`SKILL.md` plus YAML frontmatter). Do not assume every agent host supports the same advanced metadata. Keep provider-specific rendering in `src/agentforge/`. Validate changes with `python -m agentforge validate --strict` and the unit tests.
