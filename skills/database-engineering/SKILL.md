---
name: database-engineering
description: Design, query, migrate, secure, and optimize relational databases, especially PostgreSQL. Use for schema design, SQL, indexes, transactions, concurrency, data integrity, backup/recovery, and production migrations.
license: MIT
---

# Database engineering

## Mission

Protect data correctness first, then optimize for performance, operability, and cost. Database design is part of the application's domain model and deployment strategy. A migration is a production change with lock, compatibility, and recovery implications.

## 1. Discover the database and workload

Before proposing changes, determine:
- Database engine/version, hosting model, extensions, collation, timezone, and connection architecture.
- Current schema, constraints, indexes, migration history, and ownership of each table.
- Approximate row counts, growth, row width, write/read ratio, concurrency, and retention.
- Query patterns, slow-query evidence, lock waits, connection pool behavior, and replication topology.
- Availability, recovery point/time objectives, backup policy, data residency, and deletion requirements.
- Application versions that may run concurrently during deployment.

Inspect real migrations and query call sites. Do not assume a schema diagram reflects the live database.

## 2. Model data and invariants

For every entity, define identity, lifecycle, ownership, relationships, uniqueness, nullability, and retention. Decide which constraints must be enforced by the database because multiple code paths, jobs, or services can write the same data.

Prefer:
- Primary keys that are stable and never repurposed.
- Foreign keys for referential integrity when the deployment and ownership model permits them.
- Unique constraints for natural invariants such as one active membership per user/team.
- Check constraints for local invariants the database can validate.
- Explicit status/state transition rules rather than loosely related booleans.
- Junction tables for many-to-many relationships with their own lifecycle or metadata.

Avoid storing the same fact in multiple authoritative locations. Derived aggregates and caches must have a documented rebuild or reconciliation strategy. Do not use JSON columns as a substitute for modeling stable, frequently queried fields relationally.

## 3. SQL and query design

- Parameterize all values. Do not concatenate untrusted input into SQL.
- Whitelist dynamic identifiers such as sort columns and directions; values cannot be safely parameterized as identifiers.
- Select only needed columns and rows.
- Use bounded pagination and deterministic ordering. Include a unique tie-breaker in pagination order.
- Prefer cursor/keyset pagination for large or frequently changing datasets.
- Check N+1 patterns, accidental Cartesian products, correlated subqueries, and duplicate joins.
- Understand how NULL, collation, timezone, decimals, and implicit casts affect semantics.
- Use batch operations deliberately; consider memory, lock duration, and transaction log growth.

For PostgreSQL, use EXPLAIN (ANALYZE, BUFFERS) on safe representative data when investigating query plans. Interpret estimates, actual rows, loops, buffer hits/reads, sort methods, and sequential/index scans together. Do not add an index solely because a column appears in a WHERE clause: inspect cardinality, write amplification, index size, and query selectivity.

## 4. Transactions and concurrency

Define the invariant that must be atomic and make the transaction boundary match it. Keep transactions short. Avoid remote calls, long file operations, or user interaction while holding locks.

Choose concurrency control deliberately:
- Optimistic locking/version columns for low-conflict updates.
- Unique constraints and atomic upserts for uniqueness races.
- Row-level locking for short critical sections with clear lock order.
- Advisory locks only when their scope and lifecycle are rigorously defined.
- Serializable isolation only when the invariant requires it and retry behavior is implemented.

Test concurrent requests and duplicate jobs. A read-then-write check in application code is not sufficient to guarantee uniqueness under concurrency.

## 5. Schema and data migrations

Classify every migration as additive, backfill, constraint tightening, rename, type conversion, or destructive removal. Evaluate table locks, index build behavior, table rewrite risk, replication lag, disk space, runtime, and application compatibility.

Prefer expand/contract:
1. Add the new schema in a backward-compatible form.
2. Deploy code that can work with old and new representations.
3. Backfill in bounded, restartable batches with checkpoints and rate controls.
4. Verify counts, constraints, and data equivalence.
5. Switch reads/writes and monitor.
6. Remove the old representation in a later release after rollback is no longer needed.

For backfills, define idempotency, resume marker, batch size, throttling, failure handling, progress logging, and stop condition. Avoid a single huge transaction for very large datasets.

Before destructive changes, require explicit approval and confirm backup/restore capability. A database rollback is not automatically safe after information is discarded or external side effects have occurred.

## 6. PostgreSQL-specific guidance

- Use timestamptz for absolute instants and define how local business dates/time zones are represented.
- Use numeric for exact decimal/money calculations; document currency and rounding rules.
- Understand MVCC, vacuum/autovacuum, long-running transactions, bloat, and lock behavior.
- Size connection pools with total application replicas in mind; each process-local pool contributes to the global connection count.
- Use partial, expression, or multicolumn indexes only when they match measured predicates and ordering.
- Be deliberate about JSONB GIN indexes, generated columns, and expression indexes.
- Use concurrent index creation where operationally appropriate and verify cleanup after failures.
- Use ON CONFLICT only when the upsert's conflict target and update semantics match the business invariant.
- Avoid long-lived idle-in-transaction sessions and unbounded cursors.

## 7. Security and privacy

Use least-privilege database roles. Separate application runtime, migration, read-only reporting, and administrative access where practical. Protect credentials, enforce TLS, restrict network access, and audit privileged actions. Avoid exposing raw SQL errors or connection strings. Apply row-level security only with a verified, tested model for role/session context and connection pooling; do not treat RLS as a substitute for application authorization.

## 8. Backup, restore, and incident readiness

Document backup frequency, retention, encryption, restore location, point-in-time recovery, and ownership. A backup is not verified until a restore test succeeds. Record recovery procedures and acceptable data loss. Monitor storage, connections, replication lag, deadlocks, slow queries, failed jobs, and backup freshness.

## Required deliverables

For material schema/query work, provide:
- Schema or query change and rationale.
- Invariants and constraints.
- Expected query access pattern and index rationale.
- Migration sequence, lock/backfill risk, and deployment compatibility.
- Validation queries and test plan.
- Backup, rollback, or forward-fix considerations.
- Measured performance evidence when optimization is claimed.

## Quality gates

Verify correctness with constraints and tests, inspect query plans for performance work, test representative data volume, consider concurrent access, and confirm the application can run during the planned migration sequence.

## Anti-patterns

Never run production DDL or mass updates without approval. Avoid unbounded selects, N+1 access, arbitrary dynamic SQL, implicit transaction assumptions, long-held locks, duplicated authoritative data, undocumented time-zone rules, and irreversible migrations disguised as reversible deploys.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [migration plan template](references/migration-plan-template.md)
- [query review checklist](references/query-review-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

State schema/query changes, data impact, migration sequence, test/plan validation, measured results, backup/recovery implications, and residual risk.
