# API and integration rules

## Contract
- Define methods, paths, request/response schemas, nullability, defaults, errors, pagination, and versioning explicitly.
- Keep error codes stable and messages safe; never return stack traces, SQL, secrets, or internal topology.
- Use correct HTTP status semantics. Do not report an asynchronous operation as complete when it is only accepted.
- Document compatibility and deprecation behavior.

## Security
- Authenticate and authorize every operation at the server boundary.
- Check object-level and tenant-level access for nested resources and bulk operations.
- Validate payload shape, fields, size, and semantic constraints.
- Parameterize queries and allowlist dynamic identifiers, sorting, and filtering.
- Verify webhook signatures over raw payloads and prevent replay.
- Treat external responses and model output as untrusted.

## Reliability
- Set explicit connect/read/overall timeouts.
- Retry only transient failures and respect rate-limit guidance.
- Use exponential backoff with jitter and bounded attempts.
- Use idempotency keys or deduplication for state-changing operations that may be retried.
- Define concurrency, pagination, payload, and query-complexity limits.
- Expose status resources for long-running asynchronous operations.

## Testing
Cover success, invalid input, unauthenticated/unauthorized access, cross-tenant access, conflicts, duplicates, rate limits, timeouts, provider failures, pagination, and contract compatibility. Keep OpenAPI/schema examples and generated clients current.
