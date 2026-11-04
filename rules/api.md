# API and integration rules

- Define request/response schemas and error behavior explicitly.
- Enforce authentication and authorization server-side on every protected resource.
- Set timeouts for remote calls and retry only transient, safe-to-retry operations.
- Use idempotency keys or equivalent protection for retried state-changing operations.
- Bound payload sizes, pagination, concurrency, and rate of expensive operations.
- Do not leak stack traces, SQL, secrets, internal hostnames, or sensitive details in responses.
- Version breaking contract changes and add contract tests where practical.
- Treat model output, webhooks, and external service responses as untrusted input.
