---
name: database-engineering
description: Design, query, migrate, and optimize relational databases, especially PostgreSQL. Use for schema design, SQL, indexing, transactions, data integrity, and database performance.
license: MIT
---

# Database engineering

## Procedure
1. Identify the database engine/version, schema, data volume, write/read patterns, transaction boundaries, retention needs, and consistency requirements.
2. Inspect existing migrations and query paths before proposing schema changes.
3. Model entities, ownership, relationships, nullability, uniqueness, and lifecycle explicitly.
4. Enforce invariants in the database where appropriate using foreign keys, unique constraints, check constraints, and not-null constraints.
5. Choose indexes from observed query predicates, joins, sort orders, and cardinality. Consider write amplification and storage overhead.
6. Use parameterized queries and least-privilege database roles. Never concatenate untrusted values into SQL identifiers or expressions.
7. Use transactions for related changes; define isolation and locking expectations for concurrent operations.
8. Design migrations for deployability: expand, backfill, validate, switch reads/writes, then contract in a later release when needed.
9. Check lock behavior, table rewrites, index build strategy, rollback, backups, and recovery before production changes.
10. Measure query plans and representative workloads rather than guessing.

## PostgreSQL guidance
- Inspect `EXPLAIN (ANALYZE, BUFFERS)` on safe representative data when evaluating query plans.
- Use `jsonb` only when flexible document semantics are genuinely needed; keep frequently queried stable attributes relational.
- Prefer `timestamptz` for instants and store/communicate timezone semantics explicitly.
- Avoid relying on implicit casts or locale-dependent formatting.
- Use `ON CONFLICT` for well-defined upsert semantics, not as a substitute for understanding race conditions.

## Migration safety
- Never run destructive DDL, mass updates, or production migrations without explicit approval.
- Provide pre-checks, expected duration/locks, backup expectations, batch strategy, validation query, and rollback/forward-fix plan.
- Do not claim rollback is safe if a migration irreversibly discards information.

## Deliverables
Provide schema rationale, migration steps, indexes with expected query support, data-integrity constraints, test strategy, and operational risks.
