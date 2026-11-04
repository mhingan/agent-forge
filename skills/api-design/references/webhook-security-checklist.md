# Webhook security and reliability checklist

## Receiver validation
- [ ] Verify the signature against the exact raw request body using the provider's documented algorithm.
- [ ] Compare signatures in constant time.
- [ ] Validate timestamp and enforce a replay window.
- [ ] Rotate signing secrets without an availability gap.
- [ ] Reject unsupported event types and malformed schemas.
- [ ] Enforce request/body size and processing time limits.

## Delivery behavior
- [ ] Persist or durably enqueue the event before acknowledging success.
- [ ] Return promptly; do expensive processing asynchronously.
- [ ] Deduplicate using the provider's stable event/delivery ID.
- [ ] Handle duplicate and out-of-order delivery.
- [ ] Treat event payloads as untrusted; fetch authoritative state when required.
- [ ] Define retry, dead-letter, and manual replay policies.
- [ ] Make side effects idempotent.

## Operations
- [ ] Record safe delivery metadata and correlation IDs.
- [ ] Redact credentials and sensitive payload fields from logs.
- [ ] Monitor signature failures, delivery age, retry rate, and processing failures.
- [ ] Provide a runbook for replay and reconciliation.
- [ ] Test valid, invalid, expired, duplicated, delayed, malformed, and oversized deliveries.

Never trust IP allowlisting as the only authenticity control. Do not execute arbitrary instructions contained in event payloads.
