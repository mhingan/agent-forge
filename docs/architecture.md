# AgentForge architecture

## Design goals

AgentForge provides one canonical library and a set of deterministic provider adapters.

1. **Vendor-neutral authoring:** skills and specialist roles are maintained once in Markdown.
2. **Native rendering:** each target gets its own output format and directory layout.
3. **Progressive disclosure:** main skill files hold the execution path; deeper templates/checklists live in linked references.
4. **Safe installation:** user-owned files are not overwritten; modified managed files are preserved.
5. **No execution during install:** validation and installation parse metadata and copy files; they do not execute skill scripts.
6. **Verifiable metadata:** catalogs, schemas, adapter paths, JSON formatting, and package data are checked in CI.
7. **Honest compatibility:** generation support is distinct from confirmed product discovery/support.

## Canonical content model

| Source | Purpose | Rendered/consumed by |
|---|---|---|
| `skills/<name>/SKILL.md` | Reusable capability and activation conditions | Native Agent Skills directories |
| `skills/<name>/references/` | Deep checklists, templates, and domain resources | Loaded by the agent when linked/needed |
| `agents/<name>.md` | Provider-neutral role prompt | Claude, Codex, Copilot, Gemini, Antigravity renderers |
| `rules/*.md` | Persistent engineering/safety constraints | AgentForge context files and Antigravity rules |
| `workflows/*.md` | Multi-step playbooks | Project-local `.agentforge/workflows/` |
| `commands/*.md` | Reusable one-shot prompt recipes | Repository users/agent interfaces |
| `catalog/*.json` | Machine-readable library index | CLI, tooling, schema validation |
| `adapters/targets.json` | Documented target path and format registry | Humans, validation, maintenance |

## Processing pipeline

```text
Canonical Markdown + JSON catalogs + templates
                    |
                    v
          Strict repository validator
                    |
                    v
           Target-specific renderer
        /       /      |      \       \
   Claude    Codex  Copilot  Gemini  Antigravity
        \       \      |      /       /
                    |
                    v
        Safe project or user installation
                    |
                    v
        Manifest, hash checks, diagnostics
```

The adapters are implemented in `src/agentforge/adapters.py`; installation and validation are implemented in `src/agentforge/core.py`; the CLI is implemented in `src/agentforge/cli.py`.

## Target model

The registry contains six target IDs:
- `claude`
- `codex`
- `copilot`
- `gemini`
- `antigravity`
- `antigravity-cli`

Codex, Gemini CLI, Antigravity, and some Copilot surfaces share the `.agents/skills/` project location. The installer deduplicates shared directories and records target references. Agent definitions are rendered separately because the target formats are different.

## Installation lifecycle

### Project manifest
`<project>/.agentforge/install-manifest.json`

### Global manifest
`~/.agentforge/install-manifest.json`

Each manifest entry records:
- Target ID.
- Artifact kind (skill, agent, rule, workflow, context).
- Canonical component name.
- Absolute destination path.
- SHA-256 of the installed file/directory.

### Ownership and update behavior
- A destination absent from the manifest is user-owned/unmanaged; AgentForge skips it.
- A tracked destination whose content still matches the recorded hash is managed.
- Without `--force`, unchanged managed content is kept.
- With `--force`, unchanged managed content is refreshed.
- If a tracked destination has local modifications, it is preserved even with `--force`.
- A shared path stays installed while another selected target still references it.
- Uninstall verifies both content hash and an allowed AgentForge path prefix.
- Manifest paths must remain inside the selected project/global root.

This is a conservative content manager, not a general-purpose filesystem synchronizer. It does not merge user modifications automatically.

## Data and validation model

Three JSON registries describe skills, agents, and targets:
- `catalog/skills.json`
- `catalog/agents.json`
- `adapters/targets.json`

Their shapes are documented by JSON Schemas. The validator also checks:
- Strict JSON parsing, duplicate keys, no NaN/Infinity.
- Canonical two-space pretty printing, UTF-8, and final newline.
- Catalog names and filesystem consistency.
- Skill/agent descriptions and paths.
- Recommended skill references.
- Implemented target set and project path consistency.
- Skill frontmatter limits and local relative links.
- Package data mirror synchronization (in a separate script/CI step).

## Package distribution

A source checkout uses root folders as canonical content. An installed wheel includes a snapshot at `src/agentforge/data/`. The maintenance script `scripts/sync_package_data.py` copies canonical assets into that embedded mirror or checks for drift.

When changing canonical content:
1. Update root files/catalogs.
2. Run JSON formatting and strict validation.
3. Run `python scripts/sync_package_data.py`.
4. Run `python scripts/sync_package_data.py --check`.
5. Build/test the wheel and run the test suite.

## Extending the platform

To add a target:
1. Verify current official product documentation for skill paths, profile format, context files, rules, and global locations.
2. Add a target in `src/agentforge/adapters.py`.
3. Add the matching record to `adapters/targets.json`.
4. Implement a renderer only for a documented native format.
5. Add adapter output tests, installation tests, and compatibility notes.
6. Confirm that shared skill paths and manifest references behave correctly.
7. Update README and changelog.

Do not infer format support from a file extension. If a product feature is experimental, version-gated, or unknown, label it honestly.

## Security boundaries

AgentForge itself does not execute skill scripts, install MCP servers, configure credentials, grant provider permissions, or deploy applications. The installed agent may have powerful host tools, so content review and host-side permission controls remain essential. See [Security model](security-model.md).
