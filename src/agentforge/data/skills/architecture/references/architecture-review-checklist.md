# Architecture review checklist

Use as a challenge list, not a mandatory design pattern catalogue. Mark each item Yes / No / Not applicable and explain meaningful No answers.

## Product and requirements
- [ ] User outcomes and critical workflows are explicit.
- [ ] Functional scope and non-goals are clear.
- [ ] Scale, latency, availability, privacy, and compliance constraints have sources.
- [ ] Unknowns and assumptions are visible.
- [ ] The design solves a real requirement rather than introducing technology for its own sake.

## Boundaries and ownership
- [ ] Every component has one clear responsibility and owner.
- [ ] Every important data entity has an authoritative owner.
- [ ] Trust boundaries and identities are mapped.
- [ ] Interfaces have schemas, versioning, and error semantics.
- [ ] Dependencies and deployment units are justified.

## State and consistency
- [ ] Transaction boundaries protect domain invariants.
- [ ] Concurrent updates and duplicate delivery are handled.
- [ ] Cache freshness and invalidation are defined.
- [ ] Event ordering, replay, and schema evolution are addressed.
- [ ] Data migration and retention/deletion are planned.

## Reliability and operations
- [ ] Timeouts, retries, idempotency, and backpressure are deliberate.
- [ ] Partial failure and dependency outage behavior is clear.
- [ ] Logging, metrics, tracing, and alert ownership are planned.
- [ ] Backup, restore, rollback, and disaster recovery are understood.
- [ ] Resource/cost expectations are measurable.

## Security and privacy
- [ ] Authentication and authorization are enforced at the actual boundary.
- [ ] Tenant and object isolation are tested.
- [ ] Secrets and sensitive data have explicit handling.
- [ ] Untrusted input and external instructions are bounded.
- [ ] Administrative/destructive paths require appropriate approval.

## Delivery
- [ ] A simpler alternative was considered.
- [ ] The design can be delivered incrementally.
- [ ] Compatibility and mixed-version deployment are covered.
- [ ] Acceptance criteria and open decisions have owners.
- [ ] The architecture can be observed and operated by the responsible team.
