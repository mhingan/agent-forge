# AgentForge

**A vendor-neutral toolkit for building, validating, and distributing AI coding-agent skills, specialist agents, rules, and workflows.**

Write reusable expertise once. Install it into the native layout of the AI coding agents you use.

## Supported targets

| Target | Skills | Specialist agents | Instructions |
|---|---|---|---|
| Claude Code | `.claude/skills/` | `.claude/agents/` | `CLAUDE.md` |
| OpenAI Codex | `.agents/skills/` | `.codex/agents/` | `AGENTS.md` |
| GitHub Copilot | `.github/skills/` | `.github/agents/` | `.github/copilot-instructions.md` |
| Gemini CLI | `.agents/skills/` | `.gemini/agents/` | `GEMINI.md` |
| Google Antigravity | `.agents/skills/` | `.agents/agents/` | `AGENTS.md`, `.agents/rules/` |

Portable skills follow the open [Agent Skills](https://agentskills.io/) format. See [compatibility notes](docs/compatibility.md) for product-specific behavior and limitations.

## Quick start

Requires Python 3.10+. The CLI uses the Python standard library.

```bash
git clone https://github.com/mhingan/agent-forge.git
cd agent-forge

python -m agentforge validate
python -m agentforge list
python -m agentforge install --agent all --scope project
python -m agentforge doctor
```

Install selected skills:

```bash
python -m agentforge install \
  --agent claude,codex \
  --skill code-review \
  --skill security-audit
```

Install globally:

```bash
python -m agentforge install --agent all --scope global
```

## What's included

- **13 portable skills** covering architecture, API design, backend/frontend engineering, databases, debugging, code review, security, testing, DevOps, performance, AI integration, and technical writing.
- **10 specialist-agent profiles** with native renderers for Claude Code, Codex, GitHub Copilot, Gemini CLI, and Antigravity.
- **Reusable rules** for engineering fundamentals, security, Git, Python, TypeScript, and APIs.
- **5 delivery workflows** for feature development, bug investigation, pull-request review, release readiness, and database migrations.
- **Prompt recipes** for common development tasks.
- **Python CLI** for listing, validating, installing, uninstalling, generating, and inspecting configurations.
- **GitHub Actions CI** and automated tests.

## CLI

| Command | Purpose |
|---|---|
| `list` | List skills, agents, or supported targets |
| `validate --strict` | Validate skill metadata and repository consistency |
| `install` | Install selected components for one or more agents |
| `uninstall` | Remove AgentForge-managed files safely |
| `generate` | Render native agent profiles and instruction files |
| `doctor` | Inspect supported paths and detected agent CLIs |

Run `python -m agentforge --help` for all options.

## Repository layout

```text
skills/       Portable Agent Skills (canonical source)
agents/       Provider-neutral specialist-agent definitions
rules/        Reusable engineering rules
workflows/    Multi-step delivery playbooks
commands/     Reusable prompt recipes
adapters/     Native target mappings and compatibility notes
templates/    Starter templates for skills and agents
catalog/      Machine-readable catalogs
scripts/      Package-data synchronization and maintenance
src/          Python CLI and embedded package assets
tests/        Automated tests
docs/         Architecture, security, authoring, and compatibility guides
```

## Security

Agent instructions and scripts influence tool behavior. Review content before installation. AgentForge copies reviewed files; it does not install MCP servers, grant permissions, configure credentials, or execute skill scripts. Never commit secrets or private project data. See [SECURITY.md](SECURITY.md).

## Development

```bash
python -m agentforge validate --strict
python -m unittest discover -s tests -v
python scripts/sync_package_data.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
