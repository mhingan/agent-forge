# Database migration workflow

**Purpose:** Plan schema and data changes that preserve integrity across application versions and can be safely operated in production.

## Phase 1 — Discover
Inspect engine/version, schema, migrations, query call sites, row counts, data size, write/read patterns, indexes, constraints, connection pools, replication, and deployment sequencing. Identify source of truth and invariants.

## Phase 2 — Classify risk
Classify each operation as additive, backfill, constraint tightening, rename, type conversion, index change, or destructive. Estimate table locks, table rewrites, replication lag, transaction-log growth, disk space, runtime, and rollback feasibility.

## Phase 3 — Design expand/contract
Prefer:
1. Add new schema compatibly.
2. Deploy code that supports old and new shape.
3. Backfill in bounded, restartable batches.
4. Reconcile and validate.
5. Switch reads/writes.
6. Retain old shape through rollback window.
7. Remove old shape in a later release.

Do not assume the application and migration run in a single atomic deployment.

## Phase 4 — Backfill design
Specify checkpoint key, batch size, throttling, transaction size, idempotency, retry, pause/resume, poison-record handling, progress metrics, and stop conditions. Ensure a restart cannot duplicate side effects or lose rows.

## Phase 5 — Validation
Define pre/post counts and sums, null/duplicate checks, foreign-key integrity, accepted-value ranges, application-level invariants, and query plans. Use representative non-production data.

## Phase 6 — Approval and execution
Before production, confirm authorization, backup/restore capability, maintenance window, lock budget, monitoring, operator, rollback/forward-fix, and communication. Never run destructive DDL or mass updates without explicit approval.

## Phase 7 — Verify and close
Verify application compatibility, data reconciliation, lock/replication/latency/error metrics, and backup status. Record actual duration, unexpected behavior, and cleanup deferred to later releases.

## Required migration plan
Use the reusable template at `skills/database-engineering/references/migration-plan-template.md` in the AgentForge source repository, or open the equivalent reference installed with the database-engineering skill. State clearly when a rollback is not possible because data was discarded.
