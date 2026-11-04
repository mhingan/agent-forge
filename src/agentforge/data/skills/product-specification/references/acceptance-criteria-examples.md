# Acceptance criteria patterns

Use observable outcomes and realistic examples. Avoid criteria that prescribe internals without a business reason.

## Authorization
**Given** a signed-in user who does not own a record  
**When** they request the record by identifier  
**Then** the API denies access without revealing protected fields.

## Duplicate submission
**Given** a user submits a payment/leave/request action and the client retries after a timeout  
**When** the same idempotency key is received again  
**Then** the operation is not applied twice and the original result is returned.

## Asynchronous processing
**Given** a request is accepted for background processing  
**When** the API returns an accepted response  
**Then** the response includes a status identifier and the UI shows a pending state until a terminal status is confirmed.

## Recoverable validation error
**Given** the user submits a form with one invalid field  
**When** validation fails  
**Then** the field error is associated with the control, valid inputs remain populated, and the user can correct and resubmit.

## Partial dependency failure
**Given** an optional external provider is unavailable  
**When** the user requests the core function  
**Then** the system follows the documented fallback and does not report an unavailable side effect as completed.

## Data boundary
**Given** a timestamp or monetary value crosses an API boundary  
**When** it is serialized and read in another timezone/locale  
**Then** the instant/currency/precision remains unambiguous according to the contract.
