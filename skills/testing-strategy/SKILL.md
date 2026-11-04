---
name: testing-strategy
description: Design, implement, and improve automated tests across unit, integration, contract, browser, end-to-end, performance, and security layers. Use for new features, bug fixes, regression prevention, CI quality, and flaky-test investigation.
license: MIT
---

# Software testing strategy

## Mission

Create confidence in user-visible behavior and critical invariants with the smallest reliable set of tests. Tests should detect meaningful regressions, be deterministic, explain failures, and run at a cost appropriate to their value.

## 1. Understand risk and expected behavior

Before writing tests:
- Identify user outcomes, business rules, state transitions, security boundaries, external dependencies, and data contracts.
- Read existing tests and project conventions.
- Find the current failure or acceptance criteria.
- Rank risks by likelihood, impact, detectability, and blast radius.
- Identify environments and data requirements.
- Decide which behavior must be tested at unit, integration, contract, browser, or end-to-end level.

Do not add tests merely to raise a line-coverage percentage. Coverage is a navigation aid, not proof of behavior.

## 2. Choose the lowest useful test layer

### Unit tests
Use for pure functions, domain rules, state transitions, validation, transformations, and deterministic edge cases. Keep dependencies isolated. Unit tests should be fast and explain the rule they protect.

### Integration tests
Use when behavior depends on real framework wiring, database constraints, transactions, queues, storage, authentication middleware, or external protocols. Prefer disposable test infrastructure over excessive mocks when the integration itself is the risk.

### Contract tests
Use for API schemas, webhook formats, event payloads, generated clients, and service-to-service compatibility. Validate both consumer expectations and producer output.

### Component and browser tests
Use for forms, navigation, accessibility behavior, loading/error states, keyboard interaction, and visual interaction. Avoid asserting implementation details that users cannot observe.

### End-to-end tests
Reserve for a small number of critical user journeys across real boundaries. Keep fixtures controlled and isolate external services. E2E tests should verify integration, not duplicate every unit assertion.

### Non-functional tests
Use performance, load, resilience, accessibility, and security tests where the product risk or requirement justifies them. Define a safe environment and explicit test envelope.

## 3. Design test cases

For each requirement, cover applicable categories:
- Happy path and expected output.
- Empty, null, missing, malformed, and boundary input.
- Invalid state transition and business-rule violation.
- Unauthenticated and unauthorized access.
- Cross-user/tenant/object access.
- Duplicate request, idempotency, and concurrency.
- Timeout, retry, dependency unavailable, and partial failure.
- Pagination, ordering, precision, timezone, and locale.
- Persistence, migration, and old/new version compatibility.
- Accessibility, responsive behavior, and user recovery.

Use equivalence classes and boundary analysis. Pairwise combinations can control combinatorial growth, but never omit a known high-risk interaction.

## 4. Fixtures and test data

Create minimal, explicit fixtures. Use unique IDs and isolated schemas/databases. Prefer factories/builders when setup has meaningful variation; avoid magic fixture hierarchies. Control clock, randomness, locale, timezone, environment variables, and concurrency where relevant.

Never use real secrets, production credentials, or unnecessary personal/customer data. Clean up resources even after failure. Ensure tests can run independently and in a different order.

## 5. Mocking and external dependencies

Mock at the boundary when the external service is not the subject of the test. Do not mock the function under test or every layer of the system. Ensure mocks reflect real schemas and failure behavior. For critical integrations, add contract/integration tests against a controlled fake or sandbox.

For timeouts and retries, use deterministic clocks or injected policies rather than long sleeps. Avoid tests that rely on network access unless the suite explicitly categorizes them as opt-in integration tests.

## 6. Determinism and flakiness

A flaky test is a defect in the test system until proven otherwise. Investigate:
- Shared mutable data and order dependence.
- Race conditions and arbitrary sleeps.
- Port/filename/time collisions.
- External service instability.
- Uncontrolled clocks, randomness, and timezone.
- Browser animation and asynchronous UI readiness.
- Resource leaks and incomplete cleanup.

Do not hide flakiness by rerunning until green. Record the original failure, root cause, and any quarantine/skip decision with an owner and expiry.

## 7. Regression testing

For a bug fix, reproduce the original defect with a test that fails before the fix. Prefer a focused test at the layer where the invariant was violated. Then add adjacent boundary cases and run broader impacted tests. Do not write a test that merely reproduces the new implementation's internal structure.

## 8. CI strategy

Organize checks by feedback time:
- Fast formatting, lint, type checks, and unit tests on every change.
- Integration/contract checks on relevant changes or every PR when practical.
- Browser/E2E suites on PRs for critical flows, with stable fixtures.
- Expensive load/security/system tests on a controlled schedule or release gate.

Make failures visible. Avoid silently skipping required tests based on missing dependencies. Report which checks are optional and how to run them locally.

## 9. Test quality criteria

A strong test:
- Has a descriptive name tied to behavior.
- Fails for the defect it is meant to catch.
- Uses assertions that identify what went wrong.
- Is deterministic and independently runnable.
- Exercises the intended boundary and realistic data shape.
- Has no unnecessary setup or hidden external dependency.
- Does not leak resources or sensitive information.

## 10. Completion evidence

Report exact commands, runtime/environment, test counts, pass/fail/skip results, and known exclusions. Distinguish tests authored from tests executed. Never claim a suite passed if it was not run.

## Test plan format

For significant work, produce:
- Change and acceptance criteria.
- Risk matrix or prioritized risk list.
- Test layer and scenario.
- Fixture/data strategy.
- Environment and external dependencies.
- Commands and execution order.
- Pass/fail criteria.
- Exclusions and residual risk.

## Anti-patterns

Avoid arbitrary sleeps, giant E2E-only suites, tests coupled to private implementation, snapshots without behavior assertions, shared state, real production data, broad exception assertions, hidden skips, and line coverage as the only quality metric.

## Completion report

List the behavior covered, regression case, test layers, exact execution results, flaky/blocked tests, and remaining risk.
