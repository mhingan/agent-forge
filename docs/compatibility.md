# Agent compatibility

AgentForge uses the open Agent Skills folder format as its portable content layer. The host-specific paths and agent-definition formats are adapters, not claims that every product implements every feature identically.

## Current target mapping

The following mappings are based on official product documentation checked on 2026-11-04. Product paths and feature support can change; consult the linked references before relying on global discovery in a specific build.

| Product | Project skills | Global skills | Custom specialist agents | Persistent instructions |
|---|---|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `.claude/agents/*.md` with YAML frontmatter | `CLAUDE.md` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` | `.codex/agents/*.toml` | `AGENTS.md` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` | `.github/agents/*.agent.md` | `.github/copilot-instructions.md` |
| Gemini CLI | `.agents/skills/` alias (also `.gemini/skills/`) | `~/.agents/skills/` alias (also `~/.gemini/skills/`) | `.gemini/agents/*.md` | `GEMINI.md` |
| Antigravity IDE | `.agents/skills/` | `~/.gemini/config/skills/` | `.agents/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |
| Antigravity CLI | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` | `.agents/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |

**Shared paths:** `.agents/skills/` is intentionally used by Codex, Gemini CLI, and Antigravity. When installing several of those targets, AgentForge writes a single copy per skill. Uninstalling one target will not remove a shared skill while another selected target still references the same path in the install manifest.

## Important limitations

- Skills are portable at the instruction/resource level; activation behavior, consent prompts, supported frontmatter extensions, and tool access remain host-specific.
- The repository does not install MCP servers, configure credentials, or grant tools/permissions.
- Codex agent files use Codex's TOML custom-agent format. They are not interchangeable with Claude or Gemini Markdown agent profiles.
- Codex custom-agent definitions do not grant or narrow sandbox/approval permissions. Effective permissions are inherited from the invoking Codex session/configuration; keep security boundaries in the host configuration, not in an agent profile.
- Copilot custom agents use `.agent.md` files. Tool names and supported frontmatter can vary by Copilot surface and version; AgentForge avoids hardcoding a tool allowlist.
- Antigravity custom agents use their own Markdown frontmatter format and live in `.agents/agents/`; AgentForge renders this native adapter separately from the Gemini CLI format. Antigravity rule files in `.agents/rules/` require a valid `trigger`, which AgentForge adds during rendering.
- Antigravity IDE's legacy workflow format was scheduled to stop working on 2026-10-19. AgentForge stores reusable workflows as portable Markdown playbooks and skills instead of generating deprecated Antigravity workflow files.
- Copilot's Codex integration and some harness-specific capabilities may be experimental or gated by product settings.

## Official references

- [Agent Skills specification and ecosystem](https://agentskills.io/)
- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude Code skills and subagents](https://code.claude.com/docs/en/skills) and [subagents](https://code.claude.com/docs/en/sub-agents)
- [VS Code Agent Skills and supported locations](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Codex skills](https://developers.openai.com/codex/skills) and [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) and [custom agents](https://docs.github.com/en/copilot/how-tos/copilot-in-the-ide/use-copilot-agents/use-custom-agents)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) and [subagents](https://geminicli.com/docs/core/subagents/)
- [Antigravity skills](https://antigravity.google/docs/ide/skills), [custom subagents](https://antigravity.google/docs/subagents), and [rules](https://antigravity.google/docs/rules/)
- [Antigravity workflows and migration notice](https://antigravity.google/docs/ide/workflows/)

## Update policy

Before changing a target mapping, verify the target's official documentation. Add a dated note to this file and a focused test for any new adapter behavior. Avoid relying on third-party compatibility tables when official documentation is available.
