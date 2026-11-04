---
name: testing-strategy
description: Design and implement reliable automated testing across unit, integration, contract, UI, and end-to-end layers. Use when adding features, fixing bugs, or improving test confidence and CI reliability.
license: MIT
---

# Testing strategy

## Test design
1. Identify critical user outcomes, business invariants, integration boundaries, failure modes, and non-functional requirements.
2. Choose the lowest test level that provides meaningful confidence. Do not force every behavior into end-to-end tests.
3. Cover normal, boundary, invalid, unauthorized, conflict, timeout, retry, and partial-failure behavior where relevant.
4. Make tests deterministic: isolate external services, control time/randomness, use unique test data, and clean up reliably.
5. Assert observable behavior and contracts rather than private implementation details.
6. Include regression tests for defects, preferably reproducing the original failure.
7. Use contract tests for service boundaries and migration tests for data changes.
8. Keep UI/E2E tests focused on high-value user journeys; avoid brittle selectors and arbitrary sleeps.
9. Run the smallest relevant test set first, then broader suites and static checks.
10. Report exact commands, environment assumptions, pass/fail counts, and tests not run.

## Test pyramid guidance
- Unit: fast, isolated domain logic and edge cases.
- Integration: database, framework, queue, and service boundaries.
- Contract: compatibility between producers and consumers.
- End-to-end: a small number of critical user journeys.
- Non-functional: security, load, accessibility, resilience, and recovery where required.

## Anti-patterns
- Tests that pass without exercising the changed code.
- Snapshot-only coverage for behavior that needs assertions.
- Shared mutable fixtures and order-dependent tests.
- Real production credentials or live customer data.
- Arbitrary sleep-based synchronization.
- Catching and ignoring test failures.

## Completion criteria
Tests should fail for the regression they guard against, pass consistently, and clearly explain failures. Do not hide flaky behavior by rerunning until green without reporting it.
