# CLI reference

## `agentforge list`

```bash
agentforge list
agentforge list skills
agentforge list agents
agentforge list targets
```

## `agentforge validate`

```bash
agentforge validate
agentforge validate --strict
```

Checks skill directory naming, required frontmatter, duplicate names, catalog consistency, agent definitions, and required project files. Validation never runs bundled scripts.

## `agentforge install`

```bash
agentforge install --agent all --scope project
agentforge install --agent claude,codex --scope global
agentforge install --agent copilot --skill code-review --skill testing-strategy
agentforge install --agent all --components skills,agents,rules,workflows --dry-run
agentforge install --agent all --force
```

Options:

- `--agent`: comma-separated target IDs or `all`.
- `--scope`: `project` (default) or `global`.
- `--skill`: repeatable skill selector; omitted means all skills.
- `--components`: comma-separated subset of `skills`, `agents`, `rules`, `workflows`.
- `--dry-run`: show planned operations without writing.
- `--force`: refresh only files already tracked by AgentForge; unmanaged existing files remain untouched.

## `agentforge uninstall`

```bash
agentforge uninstall --agent claude --scope project
agentforge uninstall --agent all --scope project --skill code-review
```

Only managed, unmodified paths are removed. If a file has changed since installation, it is retained and reported.

## `agentforge generate`

```bash
agentforge generate --agent all --scope project
agentforge generate --agent codex,gemini --scope global
```

Renders specialist-agent profiles and project instruction files. Global generation is limited to native agent profiles; project context files are not written to global folders.

## `agentforge doctor`

Shows Python version, candidate target directories, and whether common agent executables are on `PATH`.
