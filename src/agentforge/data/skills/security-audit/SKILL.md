---
name: security-audit
description: Assess application, API, infrastructure, identity, dependency, and AI-agent security. Use for authorized security reviews, threat modeling, pre-release audits, penetration-test planning, and remediation verification.
license: MIT
---

# Security engineering and security audits

## Mission and authorization

Identify, prioritize, and help remediate security weaknesses using evidence and the least intrusive safe validation. Work only within the explicitly authorized scope. Default to passive source/configuration review. Do not exploit live systems, exfiltrate data, brute-force credentials, persist access, or run destructive tests without explicit authorization and a defined test environment.

## 1. Establish scope and rules of engagement

Record:
- Systems, repositories, environments, domains, APIs, accounts, and time window in scope.
- Systems and data explicitly out of scope.
- Authorization owner and permitted testing methods.
- Production restrictions, rate limits, data handling, and stop conditions.
- Required evidence and disclosure channel.

If authorization or scope is unclear, limit work to local code/configuration review and ask before active testing.

## 2. Build an attack-surface and trust-boundary map

Inventory entry points, identities, roles, resources, integrations, network boundaries, storage, secrets, build systems, and administrative operations. Identify data classes: public, internal, confidential, regulated, and authentication material.

Model trust boundaries between browser/server, service/service, tenant/tenant, user/agent/tool, application/database, and trusted/untrusted content. Include background jobs and administrative paths, not just public HTTP routes.

Use a lightweight threat model:
- Asset and security property.
- Threat actor and capability.
- Entry point and preconditions.
- Attack path and trust-boundary crossing.
- Impact and affected scope.
- Existing controls, evidence, and residual risk.

## 3. Review authentication and session security

Check identity proof, credential storage, token signing/validation, expiry, rotation, revocation, session fixation, refresh behavior, logout, MFA/step-up needs, and secure cookie/storage settings. Verify that authorization uses trusted claims and current account state where necessary.

Do not confuse authentication with authorization. Test direct API access, ID substitution, horizontal/vertical privilege escalation, cross-tenant references, bulk endpoints, nested resources, and background job identity.

## 4. Review input, output, and protocol boundaries

Assess:
- SQL/NoSQL/ORM, command, template, expression, and LDAP injection.
- XSS, unsafe HTML rendering, CSRF, clickjacking, open redirects, and CORS assumptions.
- SSRF, DNS rebinding, URL allowlist bypass, and cloud metadata access.
- Path traversal, unsafe archive extraction, upload/download handling, and filename confusion.
- Deserialization, parser confusion, request smuggling, and malformed content handling.
- Resource exhaustion from unbounded payloads, expensive queries, concurrency, recursion, decompression, or regex behavior.

Validate at trust boundaries. Prefer parameterized APIs, context-aware output encoding, strict schemas, allowlists, bounded resources, and explicit URL/file rules.

## 5. Review data and cryptography

Check data minimization, retention, deletion, backups, exports, encryption in transit and at rest, key lifecycle, password hashing, random token generation, and field-level access. Use vetted cryptographic libraries and well-understood schemes. Do not design custom cryptography.

Review logs, metrics, traces, error messages, analytics, browser storage, and crash dumps for credentials, session tokens, sensitive personal data, and private payloads.

## 6. Review infrastructure and software supply chain

Inspect:
- IAM/service-account permissions and credential exposure.
- Public network surfaces, firewall/security group rules, TLS, and administrative access.
- Container base images, root privileges, capabilities, filesystem permissions, and runtime secrets.
- Dependency versions, lockfiles, transitive packages, package provenance, and abandoned dependencies.
- CI workflow triggers, untrusted pull-request execution, permissions, artifact handling, and release signing/provenance.
- Infrastructure-as-code drift, state files, encryption, and destructive plans.
- Backups, restore tests, incident access, and audit retention.

Do not upload proprietary code or data to third-party scanners without permission.

## 7. Review AI and agent-specific risks

For LLM, RAG, and agent applications, inspect:
- Prompt injection through user input, retrieved content, images, web pages, files, and tool output.
- Confused-deputy behavior where a model can use the caller's tools with broader permissions.
- Tool schemas, input validation, authorization, side-effect controls, and result redaction.
- Data leakage through prompts, context, logs, model providers, or cross-tenant retrieval.
- Unsafe autonomous loops, uncontrolled spend, unbounded tool calls, and destructive actions.
- Trust separation between system/developer policy and untrusted retrieved/user content.
- Evaluation for adversarial instructions, refusal correctness, and policy regression.

The model must not be the only authorization layer. Enforce permissions in deterministic application/tool code and require human confirmation for high-impact actions.

## 8. Validate findings safely

Use static inspection and unit/integration tests first. For active validation, use an approved non-production target and non-destructive test data. Reproduce only enough to confirm the weakness. Stop when evidence is sufficient or when testing could affect availability, confidentiality, or integrity.

Separate confirmed findings from plausible concerns and scanner-only warnings. Record evidence without collecting unnecessary sensitive data.

## 9. Prioritize and report

A finding should include:
- Severity and concise title.
- Affected component and exact source/config reference.
- Preconditions and reproducible attack path.
- Impact on confidentiality, integrity, availability, and scope.
- Evidence and confidence.
- Recommended remediation and safe verification.
- Any temporary compensating control.

Prioritize based on exploitability, exposure, required privilege, impact, blast radius, and environmental controls—not only a scanner score. Avoid duplicate findings for one root cause.

## 10. Remediation and verification

Recommend the smallest fix that closes the trust-boundary failure. Include negative tests proving denied behavior, regression coverage, rollout considerations, and monitoring. Re-test the original condition after the fix. Do not declare a whole system secure because a limited review found no critical issues.

## Quality gates

- Scope and authorization are clear.
- Every finding has code/config evidence or a clearly labeled test result.
- Authorization is checked server-side at the object/action boundary.
- Secrets and sensitive evidence are redacted.
- Severity is justified by scenario and impact.
- Remediation is actionable and verifiable.
- Scope limitations and untested areas are explicit.

## Anti-patterns

Do not perform out-of-scope scans, expose credentials in reports, exploit real users, run destructive tests on production, treat a scanner score as proof, or claim complete security from a partial assessment.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [threat model](references/threat-model.md)
- [security finding template](references/security-finding-template.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

Provide scope, methodology, findings by severity, evidence, remediation, validation status, exclusions, and residual risk. If no findings are confirmed, state what was actually reviewed and what was not.
