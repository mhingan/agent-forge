# Observability and reliability rules

- Instrument critical user journeys, not just internal functions.
- Use structured logs with stable fields and correlation IDs; redact credentials and sensitive payloads.
- Use counters, gauges, and histograms appropriately; avoid unbounded/high-cardinality labels.
- Track rate, errors, latency percentiles, and saturation for important services.
- Propagate trace context across service and asynchronous boundaries.
- Distinguish liveness, readiness, and optional dependency health.
- Alerts must have impact, threshold, owner, runbook, and action; avoid paging on every exception.
- Set bounded timeouts/retries, backpressure, concurrency limits, and idempotency.
- Define SLI/SLO measurement windows and exclusions explicitly.
- A backup is not proven until restore is tested; document RTO/RPO where applicable.
