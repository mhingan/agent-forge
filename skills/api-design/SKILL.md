---
name: api-design
description: Design, document, implement, or review HTTP, RPC, webhook, and event-driven API contracts. Use this skill for endpoint design, integrations, schema changes, versioning, pagination, authorization, and API reliability.
license: MIT
---

# API design and contract engineering

## Mission

Create interfaces that are predictable for consumers, safe under failure, enforce authorization consistently, and can evolve without surprising existing clients. An API is a contract, not simply a route that returns JSON.

## When to activate

Use for new endpoints, API redesigns, external integrations, webhook receivers, event schemas, breaking or additive contract changes, public API reviews, and client/server compatibility work. Do not use for a purely internal function that has no independent contract.

## 1. Discover consumers and context

Before designing, identify:
- Consumer types: browser, mobile app, partner, internal service, batch process, or agent/tool.
- Authentication mechanism, identity source, authorization model, and tenant boundary.
- Expected call frequency, payload size, latency, availability, and rate requirements.
- Data ownership, consistency expectations, and source of truth.
- Compatibility needs, supported client versions, deprecation process, and rollout constraints.
- Whether the operation is synchronous, asynchronous, idempotent, or irreversible.

Inspect existing routes, schemas, naming conventions, error shapes, generated clients, OpenAPI specs, and tests. Reuse established conventions unless there is a documented reason to change them.

## 2. Model resources and operations

Design resource names around domain concepts rather than table names. Use plural nouns for collections and stable identifiers for individual resources. Keep nested paths shallow; use nested paths only when the parent-child relationship is part of the public contract.

For each operation, specify:
- Method and path.
- Purpose and side effects.
- Authentication and object-level authorization.
- Required, optional, nullable, immutable, and server-generated fields.
- Validation constraints and normalization rules.
- Response schema and status codes.
- Error cases and stable error codes.
- Pagination, filtering, sorting, concurrency, and idempotency semantics.
- Whether the operation is safe to retry.

Prefer GET for safe retrieval, POST for creation or commands, PUT for full replacement, PATCH for partial modification, and DELETE for deletion. Do not use a method merely because a framework makes it convenient; define its semantics clearly.

## 3. HTTP status and response conventions

Use status codes consistently:
- **200 OK:** successful request with a response body.
- **201 Created:** resource created; return a stable identifier and Location when appropriate.
- **202 Accepted:** work accepted but not completed. Provide a job/status resource, correlation ID, expected polling behavior, or callback contract.
- **204 No Content:** completed successfully with no response body.
- **400 Bad Request:** malformed syntax or invalid request structure.
- **401 Unauthorized:** missing or invalid authentication.
- **403 Forbidden:** authenticated principal lacks permission; use 404 instead only when the security policy deliberately conceals resource existence.
- **404 Not Found:** resource or route does not exist or is intentionally concealed.
- **409 Conflict:** operation conflicts with current state or uniqueness constraints.
- **412 Precondition Failed:** conditional request precondition failed.
- **422 Unprocessable Content:** syntactically valid content fails semantic validation, when this convention is adopted consistently.
- **429 Too Many Requests:** rate limit exceeded; include Retry-After when meaningful.
- **5xx:** server-side failure; never use these to report ordinary validation failures.

Use one documented error envelope. Include a stable machine-readable code, safe human-readable message, optional field errors, and request/correlation ID. Do not return stack traces, database errors, SQL, secrets, tokens, or internal topology.

## 4. Define schemas precisely

Specify field type, meaning, constraints, defaults, nullability, example, and mutability. Distinguish omitted from explicit null. Use timezone-aware timestamps with a consistent format. Represent money and exact decimal quantities without binary floating-point ambiguity. Define units, enum evolution rules, maximum lengths, collection bounds, and unknown-field behavior.

Validate untrusted requests at the boundary and validate external responses before using them. Server-side validation is authoritative; client-side validation is only a usability aid.

## 5. Authentication and authorization

Authentication identifies the caller. Authorization determines what that caller may do to a specific object in a specific context.

For each operation, verify:
- Principal identity and session/token validity.
- Required role, permission, ownership, and tenant membership.
- Resource-level access, including nested resources and bulk operations.
- Field-level access for sensitive or privileged attributes.
- Whether the action requires re-authentication, step-up authentication, or an audit event.

Never trust a resource ID supplied by a client as proof of ownership. Apply authorization in the service/data-access path, not merely by hiding buttons in the UI. Test cross-tenant and cross-user access explicitly.

## 6. Idempotency, concurrency, and retries

For state-changing operations that clients may retry, define idempotency behavior. Use a caller-scoped idempotency key, request fingerprint, bounded retention period, and deterministic replay response. Reject reuse of a key with a materially different request.

For concurrent updates, choose an explicit model:
- Optimistic concurrency with version/ETag and If-Match.
- Database locking for critical short transactions.
- Domain command serialization where ordering is essential.

Set timeouts for all network calls. Retry only transient failures and respect Retry-After. Use exponential backoff with jitter and bounded attempts. Never retry non-idempotent actions without a protocol that prevents duplicate effects.

## 7. Pagination, filtering, and rate limits

Define maximum page size, stable ordering, cursor encoding, behavior when underlying data changes, and whether total counts are exact or approximate. Cursor pagination is generally safer than offset pagination for large or frequently changing collections.

Whitelist sortable/filterable fields; do not pass arbitrary client strings into SQL or query expressions. Bound query complexity, payload size, upload size, batch size, concurrency, and execution time. Document rate-limit scope and response behavior.

## 8. Asynchronous work and webhooks

For accepted background work, expose a job resource with states such as queued, running, succeeded, failed, and canceled. Define progress semantics, retention, cancellation, retry, and terminal error behavior.

Webhook receivers should:
- Verify signatures over the raw request body, with timestamp/replay protection.
- Validate event type and schema.
- Persist or enqueue before acknowledging.
- Handle duplicate and out-of-order delivery.
- Return promptly and process expensive work asynchronously.
- Expose delivery IDs and safe diagnostics without leaking secrets.

## 9. Versioning and change management

Prefer additive compatible changes. Treat field removal, type changes, semantic changes, stricter validation, enum contraction, and changed defaults as potentially breaking. Define deprecation communication, sunset dates, client telemetry, migration examples, and removal criteria. Update OpenAPI, generated clients, mocks, fixtures, and consumer contract tests together.

## 10. Required tests

Cover:
- Successful path and response schema.
- Missing/invalid fields and boundary values.
- Unauthenticated, unauthorized, cross-tenant, and field-level access.
- Not found, conflict, stale precondition, and duplicate request.
- Rate limit, timeout, dependency failure, and retry behavior.
- Pagination stability and filtering allowlists.
- Contract compatibility for supported clients.
- Webhook signature failure, replay, duplicate, and ordering where applicable.

## Deliverables

Produce an API contract with examples, error model, auth matrix, idempotency/retry behavior, compatibility decision, operational limits, and contract tests. If changing an existing API, include a before/after compatibility assessment and a rollout plan.

## Anti-patterns

Avoid generic success responses for every outcome, ambiguous boolean flags, undocumented nulls, unbounded collection endpoints, leaking internal exception text, client-only authorization, arbitrary SQL sorting, and accepted-job responses without a way to inspect completion.

## Completion report

List operations and schemas changed, compatibility impact, authorization behavior, error/retry model, tests executed, generated artifacts updated, and any assumptions or migration steps.
