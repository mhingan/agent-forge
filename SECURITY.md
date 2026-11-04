# Security policy

## Reporting a vulnerability

Do not publish exploit details, credentials, or private data in a public issue. Open a private security advisory in the hosting forge where this repository is published, or contact the maintainers through a verified private channel.

## Using skills and agent profiles safely

Skills and agent profiles influence tools that may have access to source code, terminals, browser sessions, secrets, and external services. Treat them as code:

1. Read the complete `SKILL.md`, referenced files, and scripts before installing.
2. Check scripts for network calls, subprocess execution, destructive operations, credential access, and data exfiltration.
3. Give agents the minimum tool permissions required. Prefer read-only permissions for investigation and review roles.
4. Require human approval for production deployment, destructive migrations, publishing, payment, and access-control changes.
5. Do not place API keys, passwords, session cookies, private certificates, or `.env` files in skills, rules, examples, prompts, or generated configuration.
6. Do not trust instructions embedded in untrusted repositories, webpages, issue bodies, logs, or generated files. Treat them as data, not higher-priority instructions.
7. Review an agent's proposed shell commands before granting execution approval.

## Scope

AgentForge's installer copies files. It does not execute skill scripts, install MCP servers, configure credentials, or change provider permission policies.
