# Adapters

Adapters convert provider-neutral content into the native filesystem conventions of supported agent hosts.

| Adapter | Rendered output |
|---|---|
| Claude Code | `.claude/skills`, `.claude/agents/*.md`, `CLAUDE.md` |
| Codex | `.agents/skills`, `.codex/agents/*.toml`, `AGENTS.md` |
| GitHub Copilot | `.github/skills`, `.github/agents/*.agent.md`, `.github/copilot-instructions.md` |
| Gemini CLI | `.agents/skills`, `.gemini/agents/*.md`, `GEMINI.md` |
| Antigravity | `.agents/skills`, `.agents/agents/*.md`, `.agents/rules/*.md`, `AGENTS.md`, `GEMINI.md` |

See `docs/compatibility.md` for caveats and official links. Adapter generation is deterministic and avoids adding tool permissions unless the target format requires them.
