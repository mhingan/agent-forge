# Offline synchronization contract

## Data model
- Local source of truth:
- Server source of truth:
- Data that may be edited offline:
- Data that must remain online-only:
- Conflict resolution per entity/field:
- Retention and encryption:

## Mutation queue
- Operation ID/idempotency key:
- User/account/tenant binding:
- Creation timestamp and client version:
- Dependency ordering:
- Retry policy and expiry:
- Cancellation behavior:
- Duplicate detection:

## Synchronization lifecycle
1. Capture the mutation locally and show a clearly pending state.
2. Persist an idempotency key and minimal replay payload.
3. Send when connectivity and authentication are available.
4. Server validates authorization and current state.
5. Apply server response or classify the conflict.
6. Reconcile local state with authoritative server result.
7. Mark complete only after server confirmation.

## Account and device safety
- Logout/account switch handling:
- Shared-device behavior:
- Permission/token expiry:
- Local deletion/export:
- Lost-device response:

## Tests
- Offline queue, duplicate submission, app termination during send, lost response after server commit, reordered dependency, conflict, token expiry, logout, reconnect, and server validation failure.
