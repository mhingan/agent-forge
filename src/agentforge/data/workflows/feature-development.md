# Feature development workflow

## 1. Understand
- Restate user outcome and acceptance criteria.
- Inspect related implementation, tests, data contracts, and design patterns.
- Identify unknowns, dependencies, and security boundaries.

## 2. Plan
- Break work into small, reviewable steps.
- Identify affected files, APIs, data models, UI states, tests, and docs.
- Call out migrations, compatibility, rollout, and rollback needs.
- Ask only for missing information that materially blocks safe implementation.

## 3. Implement
- Make the smallest cohesive change.
- Reuse existing abstractions and avoid unrelated refactors.
- Validate inputs, enforce permissions, and handle failures.
- Keep configuration and secrets out of source control.

## 4. Verify
- Add/adjust tests for normal and failure paths.
- Run targeted tests, then relevant broader checks.
- Review the final diff for accidental changes and security issues.

## 5. Deliver
- Summarize behavior and files changed.
- Report test commands and results accurately.
- List migrations, manual steps, rollout/rollback, and remaining risks.
