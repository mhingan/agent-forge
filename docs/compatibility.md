# Agent compatibility

AgentForge uses the open [Agent Skills](https://agentskills.io/) directory format as its portable skill layer. Each skill is a directory containing a `SKILL.md` file with YAML frontmatter and may include additional references, scripts, or assets.

Platform adapters render specialist agents, rules, and context files using native target conventions. A shared source of knowledge does **not** mean that every host supports the same frontmatter, tool names, discovery rules, permission model, or lifecycle.

## Support matrix

The following mappings were checked against official product documentation on 2026-11-04. Paths and behavior can change; consult the links before relying on a feature in a particular product build.

| Target | Project skills | Global skills | Specialist agents | Persistent context/rules |
|---|---|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `.claude/agents/*.md`; global `~/.claude/agents/*.md` | `CLAUDE.md`; global user instructions supported by Claude Code |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` | `.codex/agents/*.toml`; global `~/.codex/agents/*.toml` | `AGENTS.md`; global Codex instructions |
| GitHub Copilot | `.github/skills/` (Copilot also recognizes `.claude/skills/` and `.agents/skills/` in supported surfaces) | `~/.copilot/skills/` | `.github/agents/*.agent.md`; Copilot CLI user-level `~/.copilot/agents/*.agent.md` | `.github/copilot-instructions.md`; optional path-scoped instructions |
| Gemini CLI | `.gemini/skills/` or interoperable `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` | `.gemini/agents/*.md`; global `~/.gemini/agents/*.md` | `GEMINI.md` and imported context files |
| Antigravity IDE | `.agents/skills/` | `~/.gemini/config/skills/` | `.agents/agents/*.md`; global `~/.gemini/config/agents/*.md` | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |
| Antigravity CLI | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` (CLI-specific discovery can vary) | `.agents/agents/*.md`; global config path is version-dependent | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` |

The exact paths selected by AgentForge are defined in [adapters/targets.json](../adapters/targets.json) and implemented in [src/agentforge/adapters.py](../src/agentforge/adapters.py). The Python implementation is the source of truth for generated destinations; official product documentation is the source of truth for what each host will actually discover and execute.

## Shared skill directories

Codex, Gemini CLI, and Antigravity use the interoperable `.agents/skills/` path in project scope. Some Copilot surfaces can discover it as well. AgentForge writes one skill directory at a shared location instead of duplicating identical copies for each selected target.

The installation manifest records which targets reference each path. Removing one target does not remove a shared skill while another selected target still refers to it.

## Format differences

### Skills
The skill body is shared, but metadata support, activation behavior, resource loading, and tool availability are host-specific. Keep the required Agent Skills fields portable:
- `name`: lowercase hyphenated identifier matching the directory.
- `description`: what the skill does and when to use it.

Do not rely on provider-specific metadata extensions unless the adapter deliberately adds them.

### Specialist agents
Agent role definitions under `agents/` are canonical Markdown with `name` and `description` frontmatter. Adapters render them into provider-native files:
- Claude Code: Markdown subagent definitions.
- Codex: TOML custom-agent definitions.
- Copilot: `.agent.md` profiles.
- Gemini CLI: Markdown subagent definitions.
- Antigravity: Markdown custom subagent definitions.

A generated file does not grant permissions by itself. Effective tools, sandboxing, approval, and network access remain governed by the host application's configuration and invoking session.

### Rules and context
AgentForge installs portable rules under `.agentforge/rules/` for use by context files and workflows. For Antigravity, rules are additionally rendered under `.agents/rules/` with required trigger metadata. Project instruction files are provider-specific and may overlap (for example, Codex and Antigravity both use `AGENTS.md`). AgentForge avoids overwriting existing unmanaged files.

### Workflows
Workflows in `workflows/` are portable Markdown playbooks. They are not automatically converted into every provider's native workflow format. In particular, AgentForge does not generate deprecated legacy Antigravity workflow files; use its supported skills/rules/subagent features for new configurations.

## Product-specific caveats

- **Claude Code:** agent tool allowlists and model settings can vary by version. AgentForge's read-only profiles use a conservative file/search tool set where the native format supports it.
- **Codex:** custom agents are configured using TOML. Agent definitions do not independently grant or restrict the session's sandbox or approval policy.
- **GitHub Copilot:** custom agent and skill support differs between Copilot CLI, IDE, code review, and cloud agent. Tool names/frontmatter are surface- and version-dependent; validate generated profiles in the target client.
- **Gemini CLI:** skill discovery supports its own `.gemini/skills/` directory and interoperable `.agents/skills/` locations in documented versions. Subagent frontmatter and available tools are version-sensitive.
- **Antigravity:** rule triggers and subagent frontmatter are product-specific. Rule files require valid trigger metadata; AgentForge adds this at render time. Do not assume Antigravity IDE and CLI have identical global discovery paths.
- **Global context:** global instruction-file locations are not uniformly generated by AgentForge. It installs global skills and agent profiles; project context, rules, and workflows are project-scoped.

## Shared limitations

- Agent Skills portability applies to instructions and resource layout, not identical model behavior.
- Provider-specific tool names, approval systems, model settings, permission boundaries, and context-loading behavior remain native.
- AgentForge does not install MCP servers, configure API credentials, change provider permissions, or grant shell/network access.
- A profile marked read-only is a design intention and conservative configuration hint, not a security boundary. Enforce permissions in the host.
- Copilot's skill/agent capabilities can be previewed or gated by product settings and plan/surface.
- Legacy Antigravity workflow support was scheduled for retirement on 2026-10-19; AgentForge keeps its own workflows as portable Markdown instead of generating that legacy format.

## Official references

- [Agent Skills specification and ecosystem](https://agentskills.io/)
- [Claude Code skills](https://code.claude.com/docs/en/skills) and [subagents](https://code.claude.com/docs/en/sub-agents)
- [OpenAI Codex skills](https://developers.openai.com/codex/skills) and [Codex subagents](https://developers.openai.com/codex/subagents)
- [GitHub Copilot custom agents](https://docs.github.com/en/copilot/concepts/customizations/custom-agents)
- [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) and [subagents](https://geminicli.com/docs/core/subagents/)
- [Antigravity skills](https://antigravity.google/docs/skills), [subagents](https://antigravity.google/docs/subagents), and [rules](https://antigravity.google/docs/rules/)

## Maintenance policy

Before changing a target path or renderer:
1. Verify the behavior in current official documentation.
2. Update the target registry and this compatibility guide.
3. Add or update adapter tests.
4. Test generated files in the actual host where available.
5. Record limitations and the date checked.

Never claim support solely because a file can be generated.
