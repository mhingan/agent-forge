# Feature development workflow

**Purpose:** Deliver a user-visible capability from a clear requirement through implementation, verification, and handover.

## Phase 0 — Safety and repository orientation
1. Read AGENTS.md, contribution guidance, relevant rules, and the matching skill.
2. Inspect branch, status, diff, package scripts, runtime versions, and working-tree changes.
3. Identify the target repository/project and confirm the task scope.
4. Do not overwrite user changes, expose secrets, or run production actions.
5. If the requested change is external, destructive, or irreversible, identify the approval gate before acting.

**Gate:** The working tree and task boundary are understood.

## Phase 1 — Discover
1. Restate the user outcome and observable acceptance criteria.
2. Inspect the actual current implementation, architecture, API contracts, database schema, UI patterns, and tests.
3. Identify actors, roles, data, state transitions, dependencies, and failure cases.
4. Separate confirmed facts, assumptions, open questions, and non-goals.
5. Identify compatibility, migration, privacy, accessibility, and operational implications.

**Gate:** There is a clear behavior to implement and no critical ambiguity hidden in assumptions.

## Phase 2 — Plan
Produce a concise implementation plan:
- Affected modules/files and why.
- Data/API/UI contracts that change.
- Authorization and trust-boundary changes.
- Tests at the lowest useful layers.
- Documentation/changelog and package data that must be updated.
- Rollout, migration, feature flag, and rollback/forward-fix if needed.

Prefer an incremental, reversible plan. Do not introduce dependencies or infrastructure unless necessary.

**Gate:** Each step has an outcome and a verification method.

## Phase 3 — Implement
1. Make the smallest cohesive change that satisfies the requirement.
2. Follow established conventions and keep responsibilities clear.
3. Validate external input and enforce authorization server-side.
4. Handle errors, retries, cancellation, duplicates, concurrency, and empty states explicitly.
5. Keep secrets and private data out of source, logs, docs, and generated artifacts.
6. Update related schemas, generated clients, migrations, fixtures, tests, and docs together.
7. Avoid unrelated refactoring.

## Phase 4 — Verify
Run in this order:
1. Targeted unit tests for changed logic.
2. Integration/contract tests for changed boundaries.
3. Type check, lint, formatting, and static analysis.
4. Build/package checks.
5. Broader relevant regression tests.
6. Manual/browser/device verification for user-facing behavior when available.

Inspect logs and test output. Do not hide failures or claim a check ran when it did not. If a check is blocked, state the exact blocker.

## Phase 5 — Review
Inspect the final diff for:
- Accidental/unrelated changes.
- Secrets, credentials, private URLs, and user data.
- Authorization gaps and unsafe input handling.
- Incorrect status/error behavior.
- Data loss, duplicate side effects, and race conditions.
- Broken links, outdated docs, and missing package-data copies.
- Tests that assert implementation detail rather than behavior.

## Phase 6 — Deliver
Report:
- User-visible behavior implemented.
- Files/modules/contracts changed.
- Migration/configuration/manual steps.
- Tests and exact results.
- Compatibility and rollout implications.
- Limitations, assumptions, and remaining risks.

## Stop conditions
Stop and ask for approval before production deployment, irreversible data changes, external publication, credential rotation, destructive infrastructure changes, or scope expansion with material side effects.
