---
name: api-design
description: Design, document, or review HTTP and event-driven APIs, including contracts, versioning, validation, errors, and security. Use when creating endpoints, integrating services, or changing API behavior.
license: MIT
---

# API design

## Design sequence
1. Identify consumers, use cases, authorization model, data ownership, and compatibility requirements.
2. Define resources and operations around domain behavior, not database table names.
3. Specify request/response schemas, required versus optional fields, constraints, examples, pagination, filtering, sorting, and idempotency.
4. Use consistent status codes and a stable error envelope. Never return stack traces, secrets, raw SQL, or internal host details.
5. Define authentication, authorization, object-level access checks, rate limits, input limits, and audit requirements.
6. Define pagination and concurrency semantics. Prefer cursor pagination for unstable or large collections; use ETags/version fields where concurrent updates matter.
7. Document retry behavior, timeouts, idempotency keys, and duplicate delivery handling.
8. Add contract tests for success, validation, authorization, not-found, conflict, and unexpected failures.

## HTTP conventions
- Use nouns for resource paths and HTTP methods for operations.
- Use `201 Created` with a `Location` header when a resource is created and a retrievable resource exists.
- Use `202 Accepted` only when processing is genuinely asynchronous; expose a status resource or callback contract.
- Use `204 No Content` when no response body is returned.
- Use `400` for malformed requests, `401` for missing/invalid authentication, `403` for insufficient permission, `404` for unavailable resources, `409` for state conflicts, `422` for semantically invalid content where the API convention uses it, and `429` for rate limiting.
- Keep error codes stable and machine-readable; keep user-facing messages safe and actionable.

## Compatibility checklist
- Does the change break existing clients?
- Are defaults and nullability explicit?
- Are enum expansions safe for strict clients?
- Are timestamps timezone-aware and consistently formatted?
- Are money and decimal values represented without binary floating-point ambiguity?
- Are retries safe and operations idempotent where required?
- Are authorization checks applied to every object and nested resource?

## Deliverables
Produce an API contract, examples, error model, security notes, versioning decision, and tests. Do not claim an API is backward compatible without checking actual clients or contract tests.
