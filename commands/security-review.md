# Perform a scoped security review

## Purpose
Assess source code and configuration for evidence-backed security weaknesses within an authorized scope.

## Procedure
1. Confirm authorized repository/system scope and exclusions.
2. Map entry points, identities, data classes, trust boundaries, and external dependencies.
3. Review authentication, object/tenant authorization, injection, SSRF, XSS/CSRF, file paths, secrets, logging, dependencies, CI/IaC, and AI retrieval/tool paths as relevant.
4. Prefer passive code/config review and safe local tests.
5. For each suspected issue, verify preconditions, data/control flow, existing mitigations, and actual impact.
6. Do not probe live systems or access production data without explicit authorization.
7. Recommend precise remediation and regression verification.

## Finding format
Severity, affected file/component, evidence, preconditions/attack path, impact, confidence, remediation, and retest plan.

## Boundaries
Do not exploit out-of-scope services, exfiltrate data, brute-force, persist access, or run destructive tests. Never include secrets in the report. Do not claim that a partial audit proves the system secure.
