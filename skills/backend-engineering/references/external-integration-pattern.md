# External integration design pattern

For each external system, record:

## Contract
- Provider/API/version and owner.
- Authentication scheme and secret storage.
- Request/response schema and source of truth.
- Rate limits, payload limits, and pagination.
- Provider error codes and status semantics.

## Resilience
- Connect/read/overall timeout.
- Retryable versus permanent errors.
- Backoff strategy, jitter, maximum attempts, and retry budget.
- Idempotency or deduplication strategy.
- Circuit breaker/bulkhead behavior where justified.
- Fallback and user-visible degradation.

## Security
- Outbound destination allowlist where practical.
- TLS and certificate validation.
- Request signing and replay protection where required.
- Sensitive fields sent to the provider and retention implications.
- Safe response parsing and redaction.

## Operations
- Correlation/request IDs.
- Latency/error/rate metrics.
- Provider outage runbook.
- Quota/cost monitoring.
- Reconciliation for operations with uncertain outcome.

## Test matrix
Test success, malformed response, timeout, rate limiting, auth failure, partial response, duplicate request, provider outage, and recovery. Use a sandbox or deterministic fake; never assume an external test call is safe for production data.
