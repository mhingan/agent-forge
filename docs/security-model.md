# Security model

AgentForge is a content library and installer, **not a sandbox, permission manager, or security boundary for the agent host**. An installed agent may be able to read source code, execute shell commands, browse the network, access credentials, or affect production depending on the host application's configuration.

## Threat model

### Assets
- Project source code and intellectual property.
- Credentials, tokens, keys, and session material.
- Customer/user data and internal records.
- Production services, databases, cloud resources, and deployment pipelines.
- Agent instructions and configuration files.
- Local user modifications to files installed by AgentForge.

### Relevant threats
- Malicious or compromised skill/agent content.
- Indirect prompt injection in repositories, webpages, retrieved documents, logs, or tool output.
- An agent using a broader host permission than the task requires.
- Accidental exposure of secrets or personal data.
- A manifest modified to point uninstall at an unrelated file.
- A symlink used to escape the selected install root.
- An installer overwriting user-owned or locally modified configuration.
- A generated profile being mistaken for a guaranteed provider permission boundary.

## AgentForge protections

### Content handling
- Validator reads metadata and text; it does not execute skill scripts.
- Installer copies canonical files and does not invoke external commands.
- JSON parser rejects duplicate keys and non-standard constants.
- Catalogs and target mappings are cross-checked.
- Local skill reference links are checked in strict mode.

### Installation ownership
- Unmanaged existing destinations are skipped.
- `--force` only refreshes unchanged tracked content.
- Locally modified managed files are retained, even with `--force`.
- Shared locations are tracked per target.
- Uninstall checks the recorded SHA-256.
- Uninstall accepts only known managed locations under the selected root.
- Manifest paths are validated and constrained to the selected root.
- Resolved destination paths are checked to prevent symlink escape.

### Scope of guarantees
These checks reduce accidental overwrites and unsafe manifest-driven deletion. They do not defend against a fully compromised local user account, malicious code already running with the user's permissions, or provider-host vulnerabilities.

## Safe usage requirements

1. Read a skill and its references before installing it into a sensitive project.
2. Inspect optional scripts and assets; do not assume a skill is harmless because it is Markdown.
3. Give the agent the minimum host tools and permissions required.
4. Use read-only profiles for analysis/review tasks where appropriate, but enforce access using host policy and application authorization.
5. Require human confirmation for destructive, financial, access-control, publishing, deployment, and production data actions.
6. Treat retrieved/external content as untrusted evidence; it must not override trusted policy.
7. Keep API keys, passwords, session cookies, private certificates, and customer records out of skills, examples, prompts, logs, and commits.
8. Verify generated files and diffs before committing or deploying.
9. Use a dry run before installation into an existing repository.
10. Keep backups of valuable local configuration before bulk updates.

## Agent-specific risks

- A read-only agent prompt is not a technical sandbox.
- Tool names in frontmatter can be interpreted differently by different providers.
- Host permission and approval configuration remains authoritative.
- Model-generated JSON, shell commands, SQL, and tool arguments must be validated independently.
- Retrieved text and tool results can contain malicious instructions; treat them as data, not privileged instructions.
- Multi-agent delegation should use bounded tasks, minimum necessary context, and independent result verification.

## Incident/reporting

Report security issues privately through the repository host's security advisory mechanism where available. Do not publish working exploit details, credentials, private URLs, or customer data in a public issue.

## Non-goals

AgentForge does not:
- Guarantee model correctness or prevent all prompt injection.
- Provide a sandbox or process isolation.
- Configure MCP servers, credentials, or provider permissions.
- Enforce application authorization.
- Automatically deploy or mutate production systems.
- Certify legal, regulatory, accessibility, or security compliance.
