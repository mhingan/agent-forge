---
name: backend-engineering
description: Build, refactor, debug, or review production backend services, APIs, integrations, and background jobs. Use for Python, TypeScript, Java, Go, or other server-side applications involving business logic, persistence, identity, reliability, or external systems.
license: MIT
---

# Backend engineering

## Mission

Deliver backend behavior that is correct, secure, observable, testable, and maintainable. A successful endpoint is not enough: the implementation must preserve business invariants, enforce authorization, handle failure, and remain operable after deployment.

## 1. Repository reconnaissance

Before editing:
1. Read applicable AGENTS.md, README, contribution guidance, and local rules.
2. Inspect language/runtime version, dependency lockfiles, formatter/linter/type checker, test commands, framework, and project structure.
3. Trace the relevant request/job from its entry point through validation, authorization, business logic, persistence, and integrations.
4. Inspect nearby code for naming, dependency injection, transaction, error, logging, and test patterns.
5. Identify public contracts, migrations, feature flags, environment variables, and deployment implications.

Do not introduce a new framework, ORM, queue, or service abstraction without identifying a concrete gap.

## 2. Layering and responsibility

Keep responsibilities clear:
- **Transport:** routing, serialization, request parsing, protocol-specific status mapping.
- **Application/service layer:** use-case orchestration, transaction boundary, authorization coordination, idempotency, and external calls.
- **Domain layer:** business rules, invariants, value objects, state transitions, and domain errors.
- **Infrastructure:** database, queue, file storage, email, model providers, and other I/O adapters.

Use the lightest architecture that makes behavior independently testable. Avoid both huge controllers and unnecessary layers for trivial logic.

## 3. Data contracts and validation

Validate all external inputs at boundaries: HTTP bodies, query parameters, headers, webhooks, queue messages, files, environment configuration, and third-party responses. Distinguish missing, null, empty, invalid, and defaulted values. Normalize only when normalization is part of the contract.

Use explicit request/response models. Do not expose internal ORM entities directly when it would couple persistence to public API. Bound input size, list length, recursion, and processing cost. Reject malformed data with stable, safe errors.

## 4. Identity and authorization

Establish the authenticated principal once through a trusted mechanism, then enforce authorization for the specific action and resource. Check tenant, ownership, role, object-level permission, and sensitive fields. Apply authorization to background jobs and service-to-service operations too. Do not trust IDs, role names, tenant IDs, or user-supplied claims without verification.

Test denial paths, including access to another user's record, cross-tenant reads, bulk operations, and indirect object references.

## 5. Persistence and transactions

- Keep database access explicit and use parameterized queries.
- Define transaction boundaries around invariants, not arbitrary function length.
- Use uniqueness and foreign-key constraints to protect critical invariants at the database boundary.
- Handle concurrent updates with version checks, locks, or atomic database operations.
- Avoid N+1 queries and unbounded reads; paginate and select related data deliberately.
- Use migrations for schema evolution. Consider table locks, backfills, old/new application versions, rollback, and data validation.
- Do not perform network calls while holding a database transaction open unless the design explicitly accounts for lock duration and failure.

Never run destructive DDL or mass data changes without explicit approval.

## 6. External services and asynchronous work

For every remote call define timeout, retryability, retry budget, error mapping, circuit/fallback behavior, and telemetry. Use exponential backoff with jitter for transient errors only. Add idempotency for operations that may be retried. Bound concurrency and payload size.

For background jobs, define:
- Queue semantics and at-least-once/at-most-once expectations.
- Idempotency/deduplication key.
- Retry and dead-letter policy.
- Cancellation, timeout, and poison-message handling.
- Job state and user-visible completion status.
- Correlation IDs and safe logs.

Never report an async operation as completed merely because it was accepted for processing.

## 7. Framework guidance

### Python and FastAPI
- Use Pydantic models for request/response contracts and explicit dependency injection for request-scoped resources.
- Keep routers thin and move use-case behavior into testable services.
- Manage database sessions and transactions explicitly; use one clear owner for commit/rollback.
- Use async only when the full I/O call path is genuinely asynchronous. Do not block the event loop with synchronous network or filesystem calls.
- Prefer lifespan-managed resources over import-time side effects.
- Handle application exceptions centrally while preserving stable public error codes.

### Django
- Use Django's authentication and authorization primitives consistently; custom object permissions must still be enforced on every query/action.
- Use transaction.atomic() for multi-row invariants and select_for_update() only when the locking behavior is justified.
- Avoid N+1 queries with select_related/prefetch_related and paginate large querysets.
- Keep migrations small, explicit, reviewed, and compatible with deployment sequencing.

### TypeScript / Node.js
- Validate request and environment data at runtime; static types do not validate network input.
- Handle promise rejection, cancellation, and timeouts explicitly.
- Avoid unbounded event-loop work and unbounded concurrency.
- Use structured logging and propagate request context through asynchronous boundaries.
- Close database, queue, and server resources predictably.

### Go / Java / other runtimes
Follow native idioms for context cancellation, resource ownership, transactions, error wrapping, and dependency management. Do not transplant patterns from another language if the runtime has a safer standard abstraction.

## 8. Configuration and secrets

Validate required configuration at startup and fail clearly for invalid/missing mandatory settings. Keep secrets outside source control and logs. Use environment-specific config with safe defaults; distinguish public configuration from credentials. Never print complete configuration objects when they may contain secrets.

## 9. Observability and operations

Emit structured logs with request/job correlation IDs, trace key dependencies, record latency/error/throughput metrics, and expose health checks that reflect readiness without failing due to every optional downstream dependency. Avoid high-cardinality labels and sensitive data in telemetry.

Consider graceful shutdown, worker draining, connection pool sizing, rate limits, quotas, backup/restore, and operational runbooks.

## 10. Testing strategy

Use:
- Unit tests for domain logic and deterministic edge cases.
- Integration tests for database, queue, framework, and storage boundaries.
- Contract tests for external interfaces.
- End-to-end tests for critical user journeys only.
- Concurrency and idempotency tests for state-changing flows.

Cover success, validation failure, authorization failure, not found, conflict, duplicate requests, timeout, retry exhaustion, and partial failure.

## Definition of done

- Business behavior and invariants are implemented.
- Authentication and object-level authorization are tested.
- Input and dependency responses are validated.
- Transactions and retry/idempotency behavior are explicit.
- Errors are stable and do not leak sensitive internals.
- Logs/metrics support diagnosis without exposing private data.
- Tests, type checks, linters, and relevant builds pass.
- Configuration, migrations, and rollout concerns are documented.

## Do not

Do not swallow exceptions, return fake success, hardcode credentials, trust UI-only checks, create hidden global mutable state, retry non-idempotent calls blindly, or mark an async job complete when it has merely been queued.

## Completion report

Summarize behavior, interfaces, data changes, authorization, operations and migration impact, tests run with results, and any residual risks.
