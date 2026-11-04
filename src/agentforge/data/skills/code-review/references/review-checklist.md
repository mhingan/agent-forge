# Deep review checklist

## Correctness
- Nullability, empty collections, defaults, ordering, and boundary values
- State transitions and invalid transitions
- Concurrent updates, race windows, retries, and duplicate events
- Resource lifecycle and cleanup
- Time zones, locale, decimal precision, and date boundaries

## Security
- Authentication and object-level authorization
- Tenant isolation and privilege escalation
- Injection and output encoding
- File paths, uploads, downloads, and URL fetching
- Secret management and sensitive logging
- Dependency and build provenance

## Operations
- Timeouts, retries, circuit breakers, queue redelivery
- Bounded memory, concurrency, payload size, and rate limits
- Health checks, metrics, logs, traces, and alertability
- Feature flags, rollout, compatibility, rollback

## Tests
- Positive and negative paths
- Regression case
- Integration boundary behavior
- Migration/data compatibility
- Tests assert contract, not just implementation detail
