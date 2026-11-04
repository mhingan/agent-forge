---
name: code-review
description: Perform read-only, evidence-based reviews of pull requests, diffs, or repository changes for correctness, security, data integrity, compatibility, reliability, and test quality. Use before merging or releasing code.
license: MIT
---

# Code review

## Mission

Find defects that matter before they reach users. A review should be independent, specific, reproducible, and ordered by risk. It is not a style rewrite, a summary of every changed line, or an opportunity to impose personal preferences.

## Review posture

Default to read-only. Do not edit files, commit, push, approve, or merge unless the user explicitly changes the task to request those actions. Treat the PR description and inline comments as claims to verify. Do not assume tests passed just because a badge is green; inspect the relevant checks when available.

## 1. Establish scope

Identify base and head revisions, changed files, intended behavior, supported runtime versions, and acceptance criteria. Inspect repository guidance, surrounding source, callers, data models, configuration, migrations, and tests. Understand the project conventions before judging the change.

If the diff is too large, review by subsystem and state any unreviewed areas.

## 2. Review in risk order

### Correctness and domain behavior
- Does the change implement the requested behavior and preserve established invariants?
- Are null, empty, boundary, invalid, and unusual values handled?
- Are state transitions valid and complete?
- Are timestamps, timezone, currency, decimal precision, locale, and ordering correct?
- Are concurrency, retries, duplicate events, and cancellation handled?
- Are resource lifecycles and cleanup correct?

### Security and privacy
- Is authentication trusted and authorization enforced for the object/action?
- Can another user or tenant access data through IDs, nested routes, bulk operations, or background jobs?
- Are untrusted values safely validated, queried, serialized, and rendered?
- Are secrets, personal data, or internal errors exposed in logs or responses?
- Are file/URL/network operations constrained?
- Do AI/retrieval/tool paths preserve trust boundaries and enforce permissions outside the model?

### Data integrity and persistence
- Are transactions aligned with business invariants?
- Are uniqueness and foreign-key assumptions enforced under concurrency?
- Are migrations compatible with old/new application versions?
- Can backfills resume safely?
- Is data deletion, retention, and rollback behavior correct?

### Reliability and operations
- Are timeouts, bounded retries, rate limits, and dependency failure behavior defined?
- Can repeated requests cause duplicate side effects?
- Are logs/metrics enough to diagnose failure without sensitive data?
- Are configuration defaults safe?
- Is rollout and rollback feasible?

### Compatibility and maintainability
- Are public contracts, generated clients, configuration names, and supported versions preserved?
- Are new abstractions justified and consistent?
- Are dependencies necessary, maintained, and correctly pinned?
- Does the change create hidden coupling or duplicate sources of truth?

### Test effectiveness
- Do tests actually exercise the new or changed behavior?
- Is there a regression case for the motivating defect?
- Are negative, authorization, boundary, and failure paths tested?
- Are tests deterministic and independent?
- Are integration/contract tests needed where mocks hide the real contract?

## 3. Validate findings

For each suspected issue:
1. Locate the exact changed line and relevant caller/callee.
2. Identify a realistic triggering condition.
3. Trace the actual control/data flow.
4. Verify whether an existing guard, constraint, or test prevents the issue.
5. Estimate impact and affected scope.
6. Avoid reporting issues based only on assumptions about framework behavior.

Use safe local tests or static inspection if needed. Do not run destructive operations or access production data. If a finding depends on an unknown deployment setting, state that assumption.

## 4. Severity rubric

- **Critical:** broad compromise, severe data loss, or outage with immediate high impact.
- **High:** authorization bypass, exploitable sensitive-data exposure, corruption, or major failure in a common path.
- **Medium:** meaningful functional/reliability defect under plausible conditions or important security weakness with constraints.
- **Low:** limited-scope defect or maintainability issue that can realistically cause future failure.
- **Informational:** non-blocking observation, missing follow-up, or improvement note; not a defect claim.

Use severity based on exploitability, preconditions, impact, exposure, and blast radius. Do not inflate a finding because a scanner assigns a high score.

## 5. Finding format

For every finding include:
- Severity and concise title.
- Exact file and line range.
- Triggering condition or minimal reproduction.
- Actual behavior and why it is incorrect/unsafe.
- Impact on users, data, security, or operations.
- Recommended correction.
- Confidence and any assumptions.

Do not combine unrelated defects in one finding. Avoid duplicate findings caused by the same root cause.

## 6. Review summary

After findings, provide:
- Scope and revisions reviewed.
- Findings by severity.
- Tests/checks inspected or executed.
- Areas not reviewed.
- Residual risks and recommended follow-up.

If no issues are found, say "No actionable findings identified in the reviewed scope" and still describe what was reviewed and what remains unverified.

## Review quality gates

A finding is ready only when a maintainer can locate it, understand the trigger, assess impact, and act on the recommended fix. Prefer one high-confidence defect over several speculative warnings.

## Anti-patterns

Do not report formatting as a defect unless it causes an actual problem. Do not demand refactors unrelated to the change. Do not claim a security issue without a concrete trust boundary or attack path. Do not state that the whole system is safe after a narrow diff review.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [review checklist](references/review-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

Return findings first, sorted by severity, followed by the review scope, checks performed, and residual risk. Be explicit about tests not run.
