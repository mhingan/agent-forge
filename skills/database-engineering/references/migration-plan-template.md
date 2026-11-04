# Database migration plan

## Metadata
- Migration/change ID:
- Owner/reviewer:
- Database engine/version:
- Target environment:
- Expected table/row volume:
- Maintenance window (if any):

## Change classification
Mark all that apply: additive / constraint tightening / data backfill / rename / type conversion / destructive / index change.

## Preconditions
- [ ] Backup and restore capability verified.
- [ ] Current schema and migration history inspected.
- [ ] Application versions that may run concurrently identified.
- [ ] Lock/table-rewrite/replication impact estimated.
- [ ] Disk and transaction-log capacity checked.
- [ ] Rollback or forward-fix decision documented.

## Deployment sequence
| Phase | Application compatibility | Database action | Validation | Abort condition |
|---|---|---|---|---|
| Expand | | | | |
| Deploy compatible code | | | | |
| Backfill | | | | |
| Switch reads/writes | | | | |
| Contract (later release) | | | | |

## Backfill design
- Checkpoint/resume key:
- Batch size:
- Rate limit:
- Idempotency rule:
- Retry behavior:
- Progress metrics:
- Quarantine/reconciliation behavior:

## Validation queries
Record pre/post counts, null/duplicate checks, referential integrity, value reconciliation, and application-level invariants.

## Risk and recovery
- Lock and outage risk:
- Data-loss risk:
- Rollback limitation:
- Forward-fix plan:
- Restore point:
- Owner/approval:

## Post-migration checks
- [ ] Application behavior verified.
- [ ] Error/latency/lock/replication metrics reviewed.
- [ ] Data reconciliation passed.
- [ ] Old fields/tables retained until rollback no longer needs them.
- [ ] Runbook and migration record updated.
