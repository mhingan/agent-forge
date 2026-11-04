# Review the current changes

## Purpose
Perform a read-only, evidence-based review of the current diff or pull request.

## Procedure
1. Confirm repository instructions, base/head revisions, target behavior, and current status.
2. Read the entire diff and relevant surrounding code, callers, schemas, migrations, config, and tests.
3. Review correctness, security, data integrity, authorization, compatibility, reliability, performance, and test effectiveness.
4. Reproduce or verify candidate findings safely. Check whether existing guards/constraints prevent the scenario.
5. Report only actionable findings supported by evidence.
6. Sort by severity and distinguish confirmed defects from assumptions or suggestions.

## Finding format
- Severity and title.
- File and line range.
- Trigger/precondition or minimal reproduction.
- Actual behavior and why it is wrong/unsafe.
- User/data/security/operational impact.
- Concrete remediation.
- Confidence and assumptions.

## Severity
Critical = broad compromise/data loss/outage; High = authorization bypass/exploitable exposure/corruption/major common-path failure; Medium = significant plausible defect; Low = limited but actionable risk; Informational = non-blocking observation.

## Final report
Findings first, followed by scope/revisions, checks inspected/run, areas not reviewed, and residual risks. If there are no actionable findings, say so and state the review scope.

## Boundaries
Do not edit, commit, approve, merge, or deploy. Do not report style preferences as defects. Do not imply tests passed if you only inspected the test files.
