---
name: data-engineering
description: Design, build, validate, and operate reliable data pipelines, ingestion, transformation, orchestration, analytics models, and data contracts. Use for ETL/ELT, batch/stream processing, warehouse/lakehouse work, data quality, and governed data access.
license: MIT
---

# Data engineering

## Mission

Move and transform data with explicit contracts, lineage, quality checks, security, and recovery. A pipeline is a production system: it needs ownership, idempotency, monitoring, schema evolution, and an understood correction strategy.

## 1. Discover data sources and consumers

Identify:
- Source systems and authoritative owners.
- Data producers, consumers, schemas, formats, delivery modes, and volumes.
- Batch versus streaming latency requirements.
- Data classification, access policy, consent, retention, deletion, and residency.
- Expected freshness, completeness, correctness, and availability.
- Existing warehouse/lakehouse, orchestration, catalog, and governance conventions.

Document source-of-truth and downstream dependencies. Do not create a new copy of data without a clear consumer and ownership model.

## 2. Define data contracts

For each dataset/event specify:
- Schema, field meaning, type, nullability, unit, timezone, and constraints.
- Primary/business keys and deduplication semantics.
- Event time versus ingestion/processing time.
- Producer/consumer ownership and change policy.
- Compatibility and deprecation rules.
- Sensitive fields and access classification.
- Expected volume, freshness, retention, and deletion behavior.

Validate incoming data at ingestion boundaries. Treat schema drift as an explicit event, not a silent cast or dropped field.

## 3. Design ingestion

Choose batch, micro-batch, or streaming based on latency, volume, cost, and operational complexity. Make ingestion restartable and idempotent. Define watermarking, late-arriving data, duplicate delivery, ordering, replay, checkpointing, and backpressure.

For external APIs:
- Use bounded pagination and concurrency.
- Respect rate limits and Retry-After.
- Store cursors/checkpoints safely.
- Handle partial pages, expired tokens, and schema changes.
- Do not acknowledge data loss as successful completion.

For file ingestion:
- Validate size, encoding, format, schema, and archive paths.
- Use atomic staging/finalization where possible.
- Record source checksum, arrival time, and lineage.
- Quarantine invalid inputs with safe diagnostics.

## 4. Transformations and modeling

Separate raw/immutable landing data from cleaned, conformed, and serving models when the architecture requires it. Keep transformations deterministic and versioned. Document business definitions, grain, joins, time semantics, currency, deduplication, and slowly changing dimensions.

Avoid hidden business logic in dashboards. Keep shared metrics in governed models with one definition and clear owner. Choose partitioning and clustering based on observed query patterns and retention.

## 5. Data quality

Define quality checks at appropriate layers:
- Schema and required fields.
- Uniqueness and key integrity.
- Referential integrity.
- Accepted ranges/enums and domain invariants.
- Freshness and completeness.
- Distribution/anomaly checks for important measures.
- Reconciliation between source and target counts/totals.
- Duplicate, late, missing, and out-of-order records.

Distinguish warning from blocking checks. Define whether bad data is quarantined, rejected, or allowed with a quality flag. Never silently drop rows without a recorded reason and reconciliation.

## 6. Orchestration and dependencies

Model pipelines as explicit DAGs with bounded retries, timeout, concurrency, dependencies, and ownership. Make tasks idempotent and safe to rerun. Track run IDs, input partitions, code version, data version, and output location. Handle partial success, cancellation, backfill, and dependency outage.

Avoid a single monolithic pipeline with hidden ordering assumptions. Do not create unnecessary orchestration layers for a simple scheduled query.

## 7. Privacy and governance

Apply least privilege to raw and derived datasets. Mask or tokenize sensitive fields where appropriate. Preserve consent and deletion propagation through downstream copies, caches, exports, and backups according to policy. Audit privileged access. Do not place credentials or private records in sample files, logs, or notebooks committed to source control.

Use a catalog/lineage system where the scale and governance requirements justify it. Document owner, classification, retention, freshness, and downstream consumers.

## 8. Performance and cost

Measure scan volume, compute time, shuffle, memory, storage, egress, concurrency, and query patterns. Use incremental processing when correctness allows. Partition only when pruning benefits outweigh metadata/maintenance overhead. Avoid repeated full refreshes when a well-defined incremental strategy exists.

Optimize for workload cost and freshness together. A faster pipeline that doubles compute cost or corrupts late-arriving data is not a successful optimization.

## 9. Testing and recovery

Test:
- Schema validation and schema evolution.
- Duplicate and out-of-order input.
- Late/missing partitions and retries.
- Partial batch failure and checkpoint restart.
- Backfill and idempotency.
- Data quality rule behavior.
- Reconciliation and deletion propagation.
- Access control and sensitive-data masking.

Maintain a replay/backfill procedure, checkpoint recovery, source reconciliation, and a documented correction strategy. Verify backups/retention where required.

## Deliverables

Provide data flow, contracts, source-of-truth, transformation model, quality gates, orchestration behavior, lineage/ownership, security controls, cost/freshness objectives, and recovery procedure.

## Anti-patterns

Avoid silent data drops, non-idempotent replay, unbounded extraction, undocumented schemas, metrics defined differently across teams, hardcoded credentials, personal data in notebooks, and pipelines with no owner or recovery path.

## Completion report

State datasets and contracts changed, lineage/quality checks added, volume/freshness assumptions, privacy/access controls, test results, and backfill/recovery implications.
