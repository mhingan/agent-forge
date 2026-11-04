---
name: code-review
description: Review code changes for correctness, regressions, security, maintainability, and test gaps. Use before merging pull requests or auditing a specific diff; prioritize actionable findings over style preferences.
license: MIT
---

# Code review

## Review posture
Act as an independent reviewer. Do not modify files unless the user explicitly asks for fixes. Read the full relevant context, not only the diff. Treat comments and descriptions in the change as claims to verify.

## Review sequence
1. Establish the base and head revisions or inspect the supplied diff. Confirm the intended behavior from the ticket/specification if available.
2. Trace changed code into callers, callees, data models, configuration, migrations, and tests.
3. Check correctness: edge cases, null/empty values, ordering, time zones, precision, concurrency, retries, idempotency, and error handling.
4. Check security: authentication, authorization, object-level access, injection, path traversal, unsafe deserialization, SSRF, secrets, logging, and trust boundaries.
5. Check compatibility: API contracts, persisted data, environment variables, deployment assumptions, and older clients.
6. Check operational behavior: timeouts, resource use, observability, rollback, and dependency failures.
7. Check tests: determine whether they actually exercise the changed behavior and relevant failure conditions.
8. Report findings in severity order, with precise file/line references and concrete fixes.

## Finding severity
- **Critical:** likely compromise, data loss, or broad service outage; immediate action required.
- **High:** exploitable security issue, authorization bypass, corruption, or major production failure.
- **Medium:** important functional bug or reliability issue under plausible conditions.
- **Low:** limited impact, edge-case defect, or maintainability concern with clear future risk.
- **Informational:** non-blocking observation or improvement suggestion.

## Finding format
For each issue include:
- Severity and concise title
- File and line range
- Triggering condition
- Actual impact
- Why current behavior is incorrect or unsafe
- A concrete remediation

## Rules
- Report only actionable issues supported by code evidence.
- Do not invent vulnerabilities or assume unreachable code is exploitable.
- Do not report a style preference as a defect.
- Avoid duplicate findings for the same root cause.
- If no issues are found, say so and list residual risks or untested areas.
- State test commands run and results; never imply tests ran when they did not.
