# Security model

AgentForge is a content distribution tool, not a sandbox. An installed agent may have access to powerful tools controlled by its host application.

- Review every skill and agent before installing it.
- Keep high-impact capabilities separate from read-only analysis.
- Never embed credentials or ask agents to print secrets.
- Treat external content as untrusted and defend against indirect prompt injection.
- Require user approval before destructive or irreversible actions.
- Do not make deployment, migration, deletion, or publication automatic by default.
- Validate generated output and inspect diffs before committing.

AgentForge itself does not execute content from `skills/`, `agents/`, `workflows/`, or `commands/`. Its validator reads metadata and its installer copies files.
