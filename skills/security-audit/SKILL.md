---
name: security-audit
description: Audit an application, API, repository, or deployment for security vulnerabilities and unsafe patterns. Use before releases, during code review, or when assessing authentication, authorization, data handling, or dependencies.
license: MIT
---

# Security audit

## Scope and authorization
Confirm the system and scope are authorized for assessment. Perform passive code/config review by default. Do not exploit live systems, exfiltrate data, brute-force credentials, or run destructive tests without explicit authorization and a defined test environment.

## Audit procedure
1. Map assets, entry points, trust boundaries, identities, data classifications, and external dependencies.
2. Inspect authentication, session handling, authorization, tenant isolation, and object-level access checks.
3. Review input validation and output encoding for SQL/command/template injection, XSS, SSRF, path traversal, deserialization, and request smuggling risks where relevant.
4. Review secrets handling, key storage, cryptography, TLS, logging, backups, and data retention.
5. Inspect dependency versions, lockfiles, build pipeline, container images, IaC, and deployment permissions.
6. Check abuse controls: rate limiting, resource quotas, upload limits, replay/idempotency, and denial-of-service exposure.
7. Evaluate error handling and observability for information disclosure.
8. Validate suspected issues with the least intrusive safe test. Separate confirmed findings from hypotheses.
9. Recommend remediation, compensating controls, owners, and verification steps.

## Finding format
- Severity (Critical / High / Medium / Low / Informational)
- Affected component and evidence
- Preconditions and attack path
- Impact and affected data/assets
- Reproducibility (safe and authorized)
- Remediation and validation guidance

## Prioritization
Prioritize exploitability, impact, exposure, privilege required, and blast radius. Do not inflate severity based only on a scanner label.

## Safety rules
- Never print or copy secrets into reports.
- Do not upload source code or data to third-party scanners without permission.
- Do not change production systems during an audit.
- Do not provide a false assurance that the system is secure; state scope and limitations.
