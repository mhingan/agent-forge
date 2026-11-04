# Data engineering and governance rules

- Every dataset and pipeline must have a producer, consumer, owner, source of truth, schema, and retention policy.
- Define event time, ingestion time, timezone, keys, units, nullability, and schema compatibility.
- Make ingestion and transformations idempotent, restartable, and replayable.
- Handle duplicate, late, missing, malformed, and out-of-order records explicitly.
- Never silently drop rows; quarantine/reject/warn behavior must be observable and reconcilable.
- Preserve tenant access, privacy classification, consent, retention, and deletion semantics through downstream copies.
- Use checkpoints and bounded backfills; validate counts, totals, and domain invariants.
- Monitor freshness, completeness, schema drift, quality failures, queue age, and cost.
- Do not replay or backfill production data without an approved plan and duplicate-effect protection.
- Keep credentials and private records out of notebooks, sample data, source control, and logs.
