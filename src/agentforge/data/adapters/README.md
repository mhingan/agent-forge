# Platform adapters

Adapters materialize provider-neutral source content into the paths and formats supported by each agent host. The adapter code is authoritative for what AgentForge generates; the compatibility guide and official product documentation describe what each host recognizes.

## Targets

| ID | Product | Skills | Specialist agents | Additional context/rules |
|---|---|---|---|---|
| `claude` | Claude Code | `.claude/skills/` | `.claude/agents/*.md` | `CLAUDE.md` |
| `codex` | OpenAI Codex | `.agents/skills/` | `.codex/agents/*.toml` | `AGENTS.md` |
| `copilot` | GitHub Copilot | `.github/skills/` | `.github/agents/*.agent.md` | `.github/copilot-instructions.md` |
| `gemini` | Gemini CLI | `.agents/skills/` | `.gemini/agents/*.md` | `GEMINI.md` |
| `antigravity` | Antigravity IDE | `.agents/skills/` | `.agents/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/` |
| `antigravity-cli` | Antigravity CLI | `.agents/skills/` | `.agents/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/` |

Global locations and compatibility caveats are recorded in [docs/compatibility.md](../docs/compatibility.md) and [targets.json](targets.json).

## Adapter responsibilities

- Select project/global destination paths.
- Render canonical role prompts into the target-specific syntax.
- Apply conservative tool metadata for read-only specialist profiles where supported.
- Add target-specific Antigravity rule triggers and glob metadata.
- Generate target-specific project context files.
- Deduplicate shared Agent Skills paths via the install manifest.

## Adding a target

1. Verify official product documentation and date/version.
2. Add the target to `src/agentforge/adapters.py` and `targets.json`.
3. Implement only documented output syntax.
4. Add tests for all profile renderings and installation paths.
5. Document limitations and exact product surface.
6. Verify install, force-refresh, and uninstall safety.

Never claim that a generated file will be discovered by a product unless the behavior is documented and tested.
