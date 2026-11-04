# Pull request review workflow

**Purpose:** Produce an independent, actionable review focused on defects and risk rather than style preferences.

## Phase 1 — Establish scope
Confirm base/head, intent, acceptance criteria, affected packages, supported versions, and repository rules. Read the complete diff and enough surrounding code to understand callers, contracts, migrations, and behavior.

## Phase 2 — Review in risk order
1. Security: authentication, authorization, tenant isolation, injection, SSRF, secrets, sensitive logs, AI/tool boundaries.
2. Data integrity: transactions, uniqueness, concurrency, migration compatibility, backfills, idempotency, retention.
3. Correctness: boundary cases, nullability, defaults, timezone, decimal precision, ordering, pagination, error semantics.
4. Reliability: timeout, retry, cancellation, dependency outage, resource cleanup, queue semantics, rollback.
5. Compatibility: API contracts, generated clients, configuration, runtime versions, deployment.
6. Tests: actual changed behavior, negative cases, regression, deterministic fixtures.
7. Maintainability: unjustified dependencies, hidden coupling, duplicate sources of truth.

## Phase 3 — Verify candidate findings
For each issue, locate the exact changed line, trace the actual path, establish a realistic trigger, verify existing guards, and estimate impact. Distinguish confirmed defects from environment-dependent risks and informational suggestions.

## Severity
- Critical: broad compromise, severe data loss, or major outage.
- High: authorization bypass, exploitable exposure, corruption, or severe common-path failure.
- Medium: important functional/reliability defect under plausible conditions.
- Low: limited-impact defect or specific future risk.
- Informational: non-blocking observation, not a defect.

## Finding format
Severity/title, file/line, triggering condition, actual incorrect behavior, impact, remediation, confidence/assumptions.

## Phase 4 — Report
Present findings first, sorted by severity. Then state revisions reviewed, checks run/inspected, unreviewed areas, and residual risks. If there are no actionable findings, say so and describe the scope reviewed.

## Boundaries
Default to read-only. Do not edit, approve, merge, push, or trigger deployment unless separately requested. Do not claim tests passed unless the results are available.
