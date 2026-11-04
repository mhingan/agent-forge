# AgentForge

**A vendor-neutral toolkit for AI coding-agent skills, specialist agents, engineering rules, delivery workflows, and reusable prompt commands.**

Write reusable engineering knowledge once. Validate it, version it, and install it into the native project layout of the AI coding agents you use.

AgentForge is both a curated content library and a lightweight Python CLI. The repository is the canonical source of truth; provider adapters render the same specialist roles into the file formats understood by each target.

## What you get

| Library | Included | What it is for |
|---|---:|---|
| Skills | 18 | Detailed task playbooks with activation criteria, procedures, quality gates, and optional reference material |
| Specialist agents | 16 | Bounded roles with delegation guidance, deliverables, and safety boundaries |
| Engineering rules | 12 | Persistent constraints for universal engineering, languages, security, APIs, frontend, mobile, AI, data, and operations |
| Workflows | 9 | Repeatable end-to-end delivery, incident, migration, discovery, review, and release processes |
| Prompt commands | 7 | Focused reusable prompts for planning, explanation, refactoring, review, testing, security, and releases |
| Reference resources | 26+ | ADRs, contract templates, migration plans, runbooks, checklists, evaluation plans, and test matrices |

The library is intentionally vendor-neutral. Skills follow the open [Agent Skills](https://agentskills.io/) directory format. Adapter outputs are target-specific; the same Markdown agent definition is not blindly copied into every provider's native format.

## Supported targets

| Target ID | Product | Project skills | Specialist-agent format |
|---|---|---|---|
| `claude` | Claude Code | `.claude/skills/` | `.claude/agents/*.md` |
| `codex` | OpenAI Codex | `.agents/skills/` | `.codex/agents/*.toml` |
| `copilot` | GitHub Copilot | `.github/skills/` | `.github/agents/*.agent.md` |
| `gemini` | Gemini CLI | `.agents/skills/` | `.gemini/agents/*.md` |
| `antigravity` | Google Antigravity IDE | `.agents/skills/` | `.agents/agents/*.md` and `.agents/rules/` |
| `antigravity-cli` | Google Antigravity CLI | `.agents/skills/` | `.agents/agents/*.md` and `.agents/rules/` |

Global paths, context files, aliases, and product-version caveats are documented in [Compatibility](docs/compatibility.md). Product support evolves independently of this repository; consult official documentation before relying on a specific feature.

## Quick start

Requirements: Python 3.10 or newer. The runtime CLI uses the Python standard library.

### 1. Clone the repository

```bash
git clone https://github.com/mhingan/agent-forge.git
cd agent-forge
```

### 2. Validate and inspect the library

```bash
python -m agentforge validate --strict
python -m agentforge list skills
python -m agentforge list agents
python -m agentforge list targets
```

### 3. Preview an installation

```bash
python -m agentforge install --agent all --scope project --dry-run
```

### 4. Install into the current project

```bash
python -m agentforge install --agent all --scope project
```

This installs skills, specialist profiles, rules, and workflows where supported. It generates project context files for the selected targets and writes an installation manifest under `.agentforge/`.

### Install a focused selection

```bash
python -m agentforge install \
  --agent claude,codex \
  --scope project \
  --skill backend-engineering \
  --skill database-engineering \
  --skill testing-strategy
```

You can install several targets at once. Where products share a skill directory (for example, `.agents/skills/`), AgentForge stores one copy and records each target reference.

### Install globally

```bash
python -m agentforge install --agent claude,codex --scope global
```

Global installs use each target's documented user-level directories for skills and specialist profiles. Project context files, rules, and workflows are not written globally. Global instruction files are deliberately not overwritten.

### Install from PyPI

Install the published package:

```bash
python -m pip install agentforge-toolkit
```

Then use the CLI:

```bash
agentforge --version
agentforge validate --strict
agentforge install --agent all --scope project
```

### Install from source (development)

```bash
git clone https://github.com/mhingan/agent-forge.git
cd agent-forge
python -m pip install -e .
```

See [PyPI publishing](docs/publishing.md) for maintainer release instructions.

## Forge Runtime integration

AgentForge provides the specialist roles and reusable skills used by [Forge Runtime](https://github.com/mhingan/forge-runtime). The `forge-runner` profile coordinates end-to-end delivery and uses the local Forge MCP Gateway when it is available. Install the runtime separately with `python -m pip install forge-agent-runtime`, then run `forge setup --ide copilot` to register the local gateway and Copilot agent profile. Secrets belong in the operating-system credential vault, not in chat or repository files.

## The library

### Skills

Skills are focused procedures, not broad role prompts. Every skill explains when to activate, what context to inspect, how to work, how to validate, what to deliver, and what not to do. Detailed templates and checklists are linked as progressive-disclosure references.

| Skill | Main use |
|---|---|
| `accessibility-ux` | Inclusive interaction, semantics, keyboard, assistive technology, WCAG-aligned review |
| `ai-integration` | LLM features, RAG, tool calling, agent orchestration, evaluation, privacy |
| `api-design` | HTTP/RPC/webhook contracts, schemas, versioning, authorization, retries |
| `architecture` | System boundaries, trade-offs, data ownership, ADRs, migration design |
| `backend-engineering` | Production APIs, service layers, persistence, integrations, background jobs |
| `code-review` | Read-only, evidence-based pull-request and diff review |
| `data-engineering` | Ingestion, transformation, orchestration, data quality, governance |
| `database-engineering` | SQL, PostgreSQL, schema, indexes, transactions, migrations, recovery |
| `debugging` | Reproduction, root-cause analysis, incident evidence, regression prevention |
| `devops-cloud` | CI/CD, infrastructure, containers, deployment, secrets, operations |
| `frontend-engineering` | Responsive UI, TypeScript, state, forms, accessibility, browser behavior |
| `mobile-engineering` | Flutter/React Native/native apps, lifecycle, offline, permissions, releases |
| `observability-reliability` | Logs, metrics, traces, SLI/SLO, alerts, incident response |
| `performance-optimization` | Measurement, profiling, latency, throughput, capacity, cost |
| `product-specification` | Discovery, user journeys, acceptance criteria, MVP and scope definition |
| `security-audit` | Authorized application, API, infrastructure, dependency, and AI security review |
| `technical-writing` | README, API references, runbooks, ADRs, onboarding, release notes |
| `testing-strategy` | Unit, integration, contract, browser, E2E, resilience, and regression testing |

### Specialist agents

The provider-neutral role definitions live in `agents/`. Each includes a mission, responsibilities, workflow, required output, boundaries, and completion standard.

- **Architecture and product:** `architect`, `product-manager`
- **Application engineering:** `backend-engineer`, `frontend-engineer`, `mobile-engineer`
- **Data and platform:** `data-engineer`, `database-engineer`, `devops-engineer`, `reliability-engineer`
- **Quality and safety:** `test-engineer`, `code-reviewer`, `bug-investigator`, `security-auditor`, `accessibility-specialist`
- **Communication and delivery coordination:** `documentation-engineer`, `forge-runner`

See [catalog/agents.json](catalog/agents.json) for recommended skills and agent modes. Agent profiles do not grant host permissions; actual tool access is controlled by the provider and invoking session.

## CLI reference

| Command | Purpose |
|---|---|
| `list [skills\|agents\|targets]` | Browse the library |
| `validate [--strict]` | Validate skill metadata, catalogs, JSON formatting, target mappings, and local skill links |
| `install` | Install selected skills, agents, rules, and workflows |
| `uninstall` | Remove unmodified AgentForge-managed files for selected targets |
| `generate` | Render native specialist profiles and project rule/context files |
| `doctor` | Inspect supported locations and detect common agent executables |

Run `python -m agentforge --help` for the full syntax.

### Useful commands

```bash
# List all skills
python -m agentforge list skills

# Install just the skills you need for Copilot
python -m agentforge install --agent copilot --skill frontend-engineering --skill accessibility-ux

# Install agent profiles and rules without skills
python -m agentforge install --agent all --components agents,rules

# Refresh unchanged AgentForge-managed artifacts
python -m agentforge install --agent all --force

# Generate agent profiles and rules only
python -m agentforge generate --agent claude,codex

# Preview and then uninstall one target
python -m agentforge uninstall --agent claude --dry-run
python -m agentforge uninstall --agent claude

# Diagnose the environment
python -m agentforge doctor
```

### Installation safety

- Existing unmanaged files are never overwritten.
- `--force` refreshes only an unchanged file/directory already tracked by AgentForge.
- Locally modified managed content is preserved, even when `--force` is supplied.
- Uninstall checks the recorded SHA-256 and leaves modified files in place.
- Uninstall rejects manifest paths outside known AgentForge-managed locations.
- Shared skill paths remain while another selected target still references them.
- Installation and validation do not execute scripts embedded in skills.

Read [Installation and lifecycle](docs/installation.md) before using global installation or uninstalling an existing setup.

## Repository structure

```text
skills/                 Canonical Agent Skills and progressive-disclosure references
agents/                 Provider-neutral specialist-agent roles
rules/                  Persistent engineering and safety standards
workflows/              Multi-step delivery and operational playbooks
commands/               Reusable prompt recipes
adapters/               Target registry, JSON Schema, compatibility metadata
catalog/                Machine-readable skills and agents catalogs + schemas
templates/              Starter templates for new library components
scripts/                JSON formatter and package-data synchronizer
src/agentforge/          Python CLI, renderer, validation and install engine
src/agentforge/data/     Embedded mirror used by installed wheels
tests/                   Automated validation, renderer, and installation tests
docs/                    Architecture, compatibility, authoring, security, operations
.github/workflows/       Continuous integration
```

## Quality model

AgentForge aims for production-oriented starting points, not one-size-fits-all mandates. The library emphasizes:
- Explicit activation conditions and scope.
- Step-by-step procedures and decision points.
- Security, privacy, authorization, and trust boundaries.
- Failure behavior, retries, concurrency, and recovery.
- Test strategy and measurable completion criteria.
- Reusable reference templates for deeper tasks.
- Provider-specific rendering and honest compatibility caveats.

A project should usually add or remove a small number of technology-, domain-, or policy-specific details rather than rewrite the core procedures. Review the installed instructions against the actual codebase and your organization's standards.

## Development and validation

```bash
# Format every JSON file in the repository
python scripts/format_json.py

# Verify formatting without changing files
python scripts/format_json.py --check

# Keep wheel-embedded assets identical to canonical files
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check

# Run strict validation and the test suite
python -m agentforge validate --strict
python -m unittest discover -s tests -v

# Build a wheel (optional)
python -m pip install build
python -m build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [quality standards](docs/quality-standards.md).

## Security

Agent instructions and tool descriptions can influence systems with access to source code, terminals, browsers, credentials, and production services. Review content before installation. AgentForge copies reviewed files; it does not install MCP servers, grant provider permissions, configure credentials, execute skill scripts, or deploy applications.

Never commit secrets, private customer data, or personal tokens. See [SECURITY.md](SECURITY.md) and [the security model](docs/security-model.md).

## License

MIT. See [LICENSE](LICENSE).
