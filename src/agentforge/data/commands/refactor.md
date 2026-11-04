# Refactor a focused area safely

## Purpose
Improve structure or maintainability while preserving externally observable behavior.

## Inputs
- Target module/files.
- Refactoring goal and known pain point.
- Required compatibility constraints.
- Relevant tests or runtime versions.

## Procedure
1. Inspect repository rules, status, diff, callers, dependencies, and tests.
2. Identify the concrete problem (duplication, coupling, unclear ownership, poor testability, complexity, or performance evidence).
3. Define invariants and observable behavior that must remain unchanged.
4. Add characterization/regression tests if existing coverage is insufficient.
5. Propose a small sequence of behavior-preserving steps.
6. Refactor one concern at a time; do not mix unrelated feature work.
7. Preserve API/schema/configuration compatibility unless a breaking change is explicitly requested.
8. Run targeted tests after each meaningful step and relevant broader checks at the end.
9. Inspect the final diff for accidental behavior changes and unnecessary abstractions.

## Required output
- Problem and evidence.
- Invariants to preserve.
- Refactoring plan.
- Files changed and responsibility changes.
- Tests run/results.
- Compatibility/migration impact.
- Remaining technical debt or risk.

## Boundaries
Do not alter production data or deployment. Do not "clean up" user changes. Do not add a dependency or framework merely to make the refactor easier. If a proposed change changes behavior, call it out separately from the refactor.
