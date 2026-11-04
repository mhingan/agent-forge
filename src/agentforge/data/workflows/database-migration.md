# Database migration workflow

1. Inspect current schema, migration history, engine/version, data volume, and dependent application versions.
2. State the desired invariant and exact data transformation.
3. Classify operations: additive, backfill, constraint tightening, rename, or destructive removal.
4. Estimate locks, table rewrites, runtime, replication impact, and storage growth.
5. Prefer expand/contract for rolling deployments: add compatible structures, deploy dual-compatible code, backfill, switch reads/writes, validate, remove old structures in a later release.
6. Define batching, checkpoints, idempotency, monitoring, and stop conditions for large backfills.
7. Provide pre-checks, validation queries, backup expectations, rollback or forward-fix, and recovery steps.
8. Test on representative non-production data.
9. Obtain explicit approval before production execution or destructive changes.
10. Verify integrity and application behavior after migration.
