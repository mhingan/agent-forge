# Bug investigation workflow

**Purpose:** Find the root cause of a defect and verify a correction without damaging evidence or production state.

## Phase 1 — Define the symptom
Capture expected behavior, actual behavior, affected users/data, frequency, severity, first occurrence, environment, version, input, and correlation IDs.

## Phase 2 — Preserve evidence
- Read current instructions and inspect the working tree.
- Preserve local/user changes.
- Capture complete stack traces, logs, traces, metrics, and recent deployment/config changes.
- Redact credentials, session cookies, and private payloads.
- Prefer read-only production inspection.

Do not restart services, replay jobs, modify data, disable controls, or roll back production without approval.

## Phase 3 — Reproduce
1. Reproduce using the smallest reliable input and state.
2. Record versions, environment, timezone, locale, configuration names, and feature flags.
3. Compare known-good and failing environments.
4. Reduce unrelated variables without removing the condition that triggers the bug.
5. If local reproduction is impossible, design a safe diagnostic experiment.

## Phase 4 — Build a hypothesis matrix
For every hypothesis, state evidence for/against it, the experiment that distinguishes it, and expected outcome. Test one major variable at a time.

## Phase 5 — Trace the causal path
Inspect input validation, authentication/authorization, business logic/state transitions, persistence, locks/transactions, queues, external services, serialization, and user-visible response. Check duplicate delivery, retries, stale state, and partial failure.

## Phase 6 — Determine root cause and blast radius
Separate:
- Trigger.
- Root cause.
- Contributing factors.
- Detection gap.
- Affected versions/users/records.
- Whether historical data requires reconciliation.

Do not confuse the location of a crash with the cause of the invalid state.

## Phase 7 — Correct and prevent recurrence
Implement the narrowest safe fix. Add a regression test that fails before and passes after the fix. Add observability only when it answers an identified diagnostic question. Keep temporary instrumentation out of the final diff.

## Phase 8 — Verify and communicate
Re-run the original reproduction, adjacent boundary cases, focused tests, and broader relevant checks. Inspect the diff for debug code, disabled validation, temporary credentials, and unrelated changes.

## Required incident note
- Symptom and scope.
- Reproduction.
- Evidence.
- Root cause and confidence.
- Contributing factors.
- Fix and regression coverage.
- Commands/checks and results.
- Data repair/rollout needs.
- Remaining uncertainty.

**Completion rule:** If the cause is not proven, say the investigation is inconclusive and give the next discriminating experiment. Do not present a guess as a fix.
