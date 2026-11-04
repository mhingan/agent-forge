# AgentForge

**A vendor-neutral toolkit for building, validating, and distributing AI coding-agent skills, specialist agents, rules, and workflows.**

> Write reusable expertise once. Install it into the native layout of the agents you use.

AgentForge is an open-source starter repository and local CLI. The canonical content lives in this repository; adapters materialize it into each tool's supported project or user directory.

## Supported targets

| Target | Skills | Specialist agents | Persistent instructions |
|---|---|---|---|
| Claude Code | `.claude/skills/` | `.claude/agents/*.md` | `CLAUDE.md` |
| OpenAI Codex | `.agents/skills/` | `.codex/agents/*.toml` | `AGENTS.md` |
| GitHub Copilot | `.github/skills/` | `.github/agents/*.agent.md` | `.github/copilot-instructions.md` |
| Gemini CLI | `.agents/skills/` | `.gemini/agents/*.md` | `GEMINI.md` |
| Google Antigravity IDE / CLI | `.agents/skills/` | `.agents/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |

Skills follow the open [Agent Skills](https://agentskills.io/) directory format (`SKILL.md` with YAML frontmatter). Supported locations can vary by product/version; see [compatibility notes](docs/compatibility.md) and official links there. Codex, Gemini CLI, and Antigravity can share `.agents/skills/` at project scope; AgentForge avoids writing duplicate copies to that shared directory.

## Quick start

Requirements: Python 3.10 or newer. The installer uses only the Python standard library.

```bash
# 1. Download or clone this repository
# 2. From the repository root:
python -m agentforge validate
python -m agentforge list

# Install all skills and native agent profiles into the current project
python -m agentforge install --agent all --scope project

# Install only selected skills for Claude Code and Codex
python -m agentforge install --agent claude,codex --skill code-review --skill security-audit

# Show target paths and detected tools
python -m agentforge doctor
```

For a global installation:

```bash
python -m agentforge install --agent all --scope global
```

Global mode installs skills and native specialist-agent profiles. It does not overwrite global instruction files; project rules/workflows are installed in project scope only.

### Optional: install as a CLI

```bash
python -m pip install .
agentforge validate
agentforge install --agent all --scope project
```

## What is included

- **13 portable skills** for architecture, API design, backend/frontend engineering, database work, debugging, code review, security, testing, DevOps, performance, AI integration, and technical writing.
- **10 specialist-agent profiles** with native renderers for Claude Code, Codex, GitHub Copilot, Gemini CLI, and Google Antigravity.
- **Layered rules** for universal engineering practices, security, Git, Python, TypeScript, and APIs.
- **Repeatable workflows** for feature delivery, bug investigation, pull-request review, release readiness, and database migrations.
- **Prompt recipes** for common one-shot tasks.
- **CLI tooling** to list, validate, install, uninstall, generate, and inspect the local setup.
- **CI validation** for Agent Skills metadata, repository structure, package-data synchronization, and Python tests.

## CLI commands

| Command | Purpose |
|---|---|
| `list [skills\|agents\|targets]` | List the repository catalog |
| `validate [--strict]` | Validate skill metadata and project files |
| `install` | Install skills, agent profiles, rules, and workflows |
| `uninstall` | Remove AgentForge-managed files without deleting locally modified installs |
| `generate` | Render native agent profiles and project instruction files |
| `doctor` | Show supported paths, Python version, and detected CLIs |

Run `python -m agentforge --help` or `python -m agentforge install --help` for full options.

### Install options

```bash
python -m agentforge install \
  --agent claude,codex,copilot,gemini,antigravity \
  --scope project \
  --skill backend-engineering \
  --skill testing-strategy

# Preview without writing files
python -m agentforge install --agent all --scope project --dry-run

# Refresh files previously installed and tracked by AgentForge
python -m agentforge install --agent all --scope project --force

# Include/exclude components
python -m agentforge install --agent all --scope project --components skills,agents,rules,workflows
```

`--force` refreshes AgentForge-managed files. An existing destination not recorded as AgentForge-managed is left untouched, even with `--force`.

## Repository layout

```text
skills/           Portable Agent Skills (canonical source)
agents/           Provider-neutral specialist-agent definitions
rules/             Reusable engineering rules
workflows/         Multi-step delivery playbooks
commands/          Reusable prompt recipes
adapters/          Target mapping and output-format documentation
templates/         Starter files for new skills and agents
catalog/           Machine-readable catalog
scripts/           Package-data synchronization and maintenance scripts
src/agentforge/    Python CLI, installation engine, and embedded package assets
tests/             Automated tests
docs/              Compatibility, security, authoring, and architecture docs
```

## Security model

Agent instructions and scripts are executable influence, not harmless documentation. Review all content before installation. AgentForge does not install MCP servers, grant permissions, add API keys, or execute skill scripts. It copies reviewed files only. Never commit secrets, personal tokens, or private project data to this repository. See [SECURITY.md](SECURITY.md).

## Contributing

Add skills under `skills/<name>/SKILL.md`, add specialist definitions under `agents/`, update catalog metadata, and run:

```bash
python -m agentforge validate --strict
python -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md). When changing canonical content (skills, agents, rules, workflows, docs, or catalog files), run `python scripts/sync_package_data.py` before building a wheel; CI checks that the embedded package copy is in sync.

## License

MIT. See [LICENSE](LICENSE).
