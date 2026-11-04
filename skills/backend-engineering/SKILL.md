---
name: backend-engineering
description: Build, refactor, or review production backend services, especially Python APIs and service layers. Use for FastAPI, Django, Flask, service integration, background jobs, and backend reliability work.
license: MIT
---

# Backend engineering

## Working principles
- Inspect the existing framework, package versions, conventions, and tests before editing.
- Keep transport, business logic, persistence, and integration concerns separated at the level justified by the project.
- Prefer explicit types, validated boundaries, predictable errors, and dependency injection over hidden global state.
- Avoid adding dependencies when the standard library or an existing package is sufficient.

## Implementation workflow
1. Trace the request from route/controller through service/domain logic to persistence and external dependencies.
2. Identify authorization and tenant boundaries before implementing data access.
3. Define typed input/output schemas and validate external data at boundaries.
4. Keep business rules out of route handlers and ORM model hooks when they need independent testing.
5. Use transactions for multi-step state changes. Make background tasks idempotent and observable.
6. Set explicit timeouts for network calls. Retry only transient failures and only when the operation is safe to retry.
7. Avoid blocking I/O in async event loops. Do not add `async` to functions that perform only synchronous work without a reason.
8. Add structured logs with correlation/request identifiers. Do not log credentials, access tokens, full sensitive payloads, or personal data unnecessarily.
9. Add unit and integration tests, including authorization and failure scenarios.
10. Run formatting, static analysis, and relevant tests; summarize what ran and what did not.

## Python / FastAPI guidance
- Use Pydantic models for request and response contracts.
- Use dependency injection for database sessions and request-scoped services.
- Keep routers thin; service functions own application behavior.
- Manage database sessions and transactions explicitly.
- Do not expose ORM objects directly when response contracts should be stable.
- Use lifespan hooks for application resources; avoid ad hoc startup side effects in imports.

## Django guidance
- Use Django's authentication and permission mechanisms consistently.
- Use `transaction.atomic()` for multi-row business changes.
- Select/prefetch related data deliberately to avoid query explosions.
- Keep migrations small, reversible where possible, and reviewed for table locks and data volume.

## Completion criteria
A backend change is complete only when behavior is implemented, authorization is verified, errors are handled, tests cover critical paths, configuration is documented, and operational risks are called out.
