# Architecture

## Design principles

1. **Canonical source:** skills and agents are authored once in provider-neutral Markdown.
2. **Native output:** adapters render only documented native layouts and formats.
3. **Progressive disclosure:** skills keep concise activation metadata in frontmatter and detailed instructions in the body or referenced files.
4. **Safe installation:** existing unmanaged files are never silently overwritten. Uninstall checks hashes and skips modified files.
5. **No execution:** validate/install operations inspect and copy files; they do not execute skill scripts or shell commands.
6. **Deterministic generation:** same repository version and options produce the same generated files.

## Pipeline

```text
Canonical skills + agent roles + rules + workflows
                         |
                         v
               Validation and catalog
                         |
                         v
                  Adapter renderer
          /              |              \\
       Claude          Codex          Copilot
          \\              |              /
                 Gemini / Antigravity
                         |
                         v
            Native project or user paths
```

## Install manifest

AgentForge stores a manifest in `.agentforge/install-manifest.json` for project installs and `~/.agentforge/install-manifest.json` for global installs. The manifest records target, kind, name, path, and content hash. Shared paths can be referenced by more than one target. Uninstall removes a path only when no remaining target references it and its current hash still matches the recorded hash.

## Extending the adapter layer

Add a target configuration in `src/agentforge/adapters.py`, implement rendering only when its native format is documented, then update compatibility documentation and tests. Unknown or unsupported capabilities should be explicitly reported rather than approximated silently.
