# Data pipeline runbook

## Pipeline
- Name/owner:
- Schedule/trigger:
- Source and destination:
- Critical downstream consumers:
- Freshness objective:

## Healthy operation
- Expected start/completion:
- Normal volume/range:
- Quality checks:
- Dashboard/metrics:
- Run history:

## Failure diagnosis
1. Check latest run ID and stage.
2. Check input partition/file/cursor availability.
3. Check schema drift and validation/quarantine counts.
4. Check source rate limits, credentials, and connectivity.
5. Check compute, memory, queue, and storage saturation.
6. Check checkpoint and idempotency state before retrying.

## Recovery
- Safe retry command/action:
- Resume/checkpoint behavior:
- Backfill procedure:
- Duplicate prevention:
- Reconciliation queries:
- Stop/abort conditions:
- Escalation owner:

## Data quality and incident record
Capture affected partitions/time range, expected and actual counts/totals, records quarantined/dropped, consumers impacted, correction, and verification. Do not replay an entire pipeline without understanding side effects.
