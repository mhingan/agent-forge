# Backend production-readiness checklist

## Contract and behavior
- [ ] Public inputs/outputs are explicitly typed and validated.
- [ ] Error codes/status mapping are stable and safe.
- [ ] Business invariants and state transitions are explicit.
- [ ] Authentication and object-level authorization are enforced server-side.
- [ ] Duplicate requests and concurrent updates are handled.

## Persistence
- [ ] Transaction boundary matches the invariant.
- [ ] Database constraints protect critical uniqueness/relationships.
- [ ] Queries are bounded and N+1 patterns reviewed.
- [ ] Migration is compatible with deployment order.
- [ ] Data retention, deletion, and backup implications are understood.

## Dependencies and jobs
- [ ] Every remote call has timeout and bounded retry policy.
- [ ] Retries are safe and idempotent.
- [ ] Background job state distinguishes accepted, running, succeeded, and failed.
- [ ] Dead-letter, cancellation, and replay behavior is defined.
- [ ] Concurrency and resource use are bounded.

## Operations and security
- [ ] Configuration is validated at startup.
- [ ] Secrets are isolated and never logged.
- [ ] Structured logs contain correlation IDs but no sensitive payloads.
- [ ] Metrics expose latency, rate, errors, and saturation.
- [ ] Health checks distinguish readiness from dependency health.
- [ ] Graceful shutdown and worker draining are handled.

## Delivery
- [ ] Unit/integration/contract tests cover high-risk behavior.
- [ ] Type checks, lint, and builds pass.
- [ ] Runbook and rollback/forward-fix exist.
- [ ] API/schema/configuration changes are documented.
