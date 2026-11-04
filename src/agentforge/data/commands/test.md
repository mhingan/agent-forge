# Build and execute a focused test plan

## Purpose
Choose the smallest reliable set of tests that gives confidence in the changed behavior.

## Procedure
1. Read the acceptance criteria and identify user outcomes, invariants, boundaries, and risks.
2. Inspect the existing test stack, commands, fixtures, and CI gates.
3. Choose the lowest useful layer: unit, integration, contract, component/browser, E2E, performance, or security.
4. Cover success, missing/null/invalid/boundary values, authorization, conflicts, duplicates, timeout, dependency failure, and recovery where relevant.
5. Make tests deterministic: isolate external systems, control clock/randomness, use unique data, and guarantee cleanup.
6. Add a regression test that demonstrates the original bug when fixing a defect.
7. Run focused tests first, then relevant broader tests and static/build checks.
8. Investigate failures; do not rerun until green without documenting the initial failure.
9. Report exact commands and distinguish passed, failed, skipped, blocked, and not-run checks.

## Test plan output
| Requirement/risk | Layer | Scenario | Expected result | Fixture/environment |
|---|---|---|---|---|
| | | | | |

Also list commands, results, exclusions, flaky tests, and residual risks.

## Boundaries
Never use production credentials/customer data. Do not silently skip failed tests or change production state for a test. Do not use line coverage as the sole measure of quality.
