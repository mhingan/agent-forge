# API contract template

## Overview
- **API/service:**
- **Version:**
- **Owner:**
- **Consumers:**
- **Base URL/environment:**
- **Authentication:**
- **Compatibility policy:**

## Operation

- **Method and path:**
- **Purpose:**
- **Side effects:**
- **Authorization rule:**
- **Idempotent:** Yes / No / With key
- **Timeout expectation:**
- **Rate limit:**

### Request

| Field | Type | Required | Nullable | Constraints | Meaning |
|---|---|---:|---:|---|---|
| | | | | | |

Include a valid request example and state any normalization, defaulting, or unknown-field behavior.

### Success response

- **Status:**
- **Headers:**
- **Schema:**

Provide one realistic example with placeholders, not real credentials or personal data.

### Errors

| Status | Stable code | Trigger | Retryable | Client action |
|---|---|---|---:|---|
| 400 | | | No | |
| 401 | | | After re-authentication | |
| 403 | | | No | |
| 404 | | | No | |
| 409 | | | Depends | |
| 429 | | | After Retry-After | |
| 5xx | | | Depends on operation | |

Use a consistent error envelope with request/correlation ID. Do not expose internal exception text.

## Pagination and concurrency

Document page size limits, cursor behavior, stable ordering, ETag/version semantics, stale update handling, and concurrent mutation behavior.

## Retry and idempotency

Document timeouts, retryable status/error categories, backoff, idempotency-key scope, retention period, and replay response.

## Security

List authentication, object-level permission, tenant isolation, field-level restrictions, input size limits, audit events, and sensitive fields.

## Compatibility and rollout

List consumers/versions, additive/breaking impact, deprecation plan, migration, rollout order, monitoring, and rollback.

## Tests and examples

Link OpenAPI/schema, consumer contract tests, authorization tests, and sample requests. Record the exact commands used to validate the contract.
