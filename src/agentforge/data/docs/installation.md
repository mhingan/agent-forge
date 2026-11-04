# Installation, updates, and removal

This guide explains how AgentForge changes a target project or user environment.

## Installation scopes

### Project scope

Project scope is the default. It writes skills, specialist agents, and supported context/rule files beneath the project or repository root.

```bash
python -m agentforge install --agent all --scope project --dry-run
python -m agentforge install --agent all --scope project
```

Use project scope when the skills and profiles should travel with the repository and be reviewed through source control.

### Global scope

Global scope installs skills and native specialist-agent profiles to the user-level directories defined by each target adapter.

```bash
python -m agentforge install --agent claude,codex --scope global --dry-run
python -m agentforge install --agent claude,codex --scope global
```

Global mode does not write project rules/workflows or replace global instruction files. Global target paths differ; see [compatibility](compatibility.md).

## Select components

```bash
python -m agentforge install \
  --agent claude,codex \
  --components skills,agents \
  --skill backend-engineering \
  --skill testing-strategy
```

Available components: `skills`, `agents`, `rules`, and `workflows`. Skills can be selected with repeatable `--skill` options; omitting them selects all skills when the skills component is enabled.

## Preview and force

Always use `--dry-run` for an unfamiliar target or an existing project with custom agent files.

```bash
python -m agentforge install --agent all --dry-run
```

`--force` refreshes only files/directories already recorded in the AgentForge manifest and whose current SHA-256 still matches the recorded content. Locally modified content is preserved even with `--force`. Unmanaged files are never overwritten.

If a local modification is preserved, review the diff and decide manually whether to keep or replace it. Do not delete the manifest to bypass protection.

## Manifest

Project manifest:
`<project>/.agentforge/install-manifest.json`

Global manifest:
`~/.agentforge/install-manifest.json`

The manifest records target, component kind, name, absolute path, and SHA-256. Shared paths may have multiple target references. The manifest is validated before use; uninstall also restricts removal to known AgentForge-managed locations within the chosen root.

Do not edit the manifest by hand unless you understand the ownership and hash model. Treat it as local installation metadata, not as a source catalog.

## Updates

1. Pull the latest AgentForge version.
2. Review changelog and skill/agent changes.
3. Validate the library.
4. Preview the update.
5. Run install with `--force` to refresh unchanged managed artifacts.
6. Review preserved local modifications and merge manually.

```bash
git pull
python -m agentforge validate --strict
python -m agentforge install --agent all --scope project --dry-run
python -m agentforge install --agent all --scope project --force
```

## Generate only agents and rules

```bash
python -m agentforge generate --agent claude,codex
```

Generation does not install skills or workflow playbooks.

## Uninstall

Preview first:

```bash
python -m agentforge uninstall --agent claude --scope project --dry-run
python -m agentforge uninstall --agent claude --scope project
```

To remove only one selected skill for one target, use `--skill`:

```bash
python -m agentforge uninstall --agent claude --skill code-review --scope project
```

Uninstall removes only unchanged artifacts that the manifest identifies as AgentForge-managed and whose paths are in the target's allowed installation locations. Modified files and shared paths still referenced by another target are retained.

## Recovery and troubleshooting

- If a path is reported as unmanaged, inspect it before moving or renaming it; AgentForge deliberately does not overwrite it.
- If a path is reported as modified, inspect the local diff and merge your custom edits with the new version.
- If the manifest is malformed, back it up and inspect it before repairing; do not delete it without understanding which files it tracks.
- If an uninstall path is rejected, inspect symlinks and manifest paths. AgentForge will not delete arbitrary paths from a manifest.
- If a target fails to discover a generated file, confirm the current product version and consult the vendor's official docs. A generated file alone does not guarantee feature support.
