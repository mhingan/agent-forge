# Data pipeline delivery workflow

**Purpose:** Deliver an ingestion/transformation pipeline that is correct, governed, observable, restartable, and cost-aware.

## Phase 1 — Source and consumer discovery
Identify source of truth, producer, consumer, data owner, volumes, update frequency, latency/freshness requirement, access class, retention, and deletion behavior.

## Phase 2 — Contract
Define schema, types, nullability, keys, units, timezone, event/processing time, compatibility, and ownership. Agree on how breaking schema changes are announced and rolled out.

## Phase 3 — Ingestion and orchestration
Choose batch, micro-batch, or stream based on actual latency and operational cost. Define pagination, rate limits, checkpointing, watermarking, late/duplicate delivery, ordering, retries, backpressure, and cancellation.

## Phase 4 — Transformation and quality
Keep transformations deterministic and versioned. Define grain, joins, business logic, deduplication, partitions, and incremental semantics. Add schema, uniqueness, integrity, accepted range, freshness, completeness, anomaly, and reconciliation checks.

## Phase 5 — Privacy and access
Apply least privilege. Preserve tenant/data permissions through derived tables, indexes, caches, and exports. Minimize sensitive columns and propagate retention/deletion.

## Phase 6 — Test and backfill
Test malformed, missing, late, duplicate, out-of-order, and partial data. Make backfills idempotent, restartable, checkpointed, and rate-limited. Verify row counts/totals and domain invariants.

## Phase 7 — Operate
Add freshness, completeness, quality, volume, queue age, duration, failure, and cost metrics. Document replay, quarantine, dead-letter, reconciliation, and escalation. Do not backfill production data without approval.

## Handover
Record pipeline owner, data contract, runbook, alert, quality dashboard, replay procedure, known limitations, and downstream consumer impact.
