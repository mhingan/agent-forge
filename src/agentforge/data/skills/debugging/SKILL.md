---
name: debugging
description: Investigate defects, failed builds, unexpected output, production incidents, and intermittent behavior using reproducible experiments and evidence. Use when symptoms are unclear, cross components, or require root-cause analysis.
license: MIT
---

# Debugging and root-cause analysis

## Mission

Find the smallest evidence-backed explanation for the observed behavior, then implement or recommend a correction that prevents recurrence. Do not treat suppressing an error message as fixing the defect.

## 1. Establish the problem

Capture:
- Expected behavior and the exact observed behavior.
- User/system impact, frequency, severity, and affected environments.
- First known occurrence and recent code, configuration, dependency, data, or infrastructure changes.
- Exact inputs, identifiers, timestamps, request/job IDs, and reproduction sequence.
- Whether the issue is deterministic, intermittent, load-dependent, or environment-specific.

Keep facts, hypotheses, and unknowns separate. Never include credentials, session tokens, or sensitive customer payloads in diagnostic notes.

## 2. Preserve evidence and scope

Before changing anything:
- Inspect repository status and preserve existing user modifications.
- Read the full error/stack trace, not just the last line.
- Capture relevant logs, metrics, traces, deployment versions, and configuration names.
- Compare a working and failing environment when available.
- Determine whether a rollback, restart, replay, data repair, or external action would change evidence.

For production incidents, prefer read-only inspection first. Ask before restarting services, replaying messages, changing production data, disabling controls, or performing a rollback.

## 3. Reproduce the failure

Reduce the issue to the smallest reliable input and execution path. Remove unrelated variables while preserving the failure. Record the runtime version, platform, dependency versions, feature flags, timezone, locale, and relevant state.

If the failure cannot be reproduced locally, create a safe diagnostic experiment that narrows the cause. Do not claim a bug is fixed because it did not happen once after a change.

## 4. Form and test hypotheses

For each hypothesis, state:
- Evidence supporting it.
- Evidence against it.
- A test that would distinguish it from competing causes.
- The expected observation if the hypothesis is true.

Change one major variable at a time. Prefer binary-searching a regression range, isolating a dependency, or adding temporary instrumentation over random edits. Keep diagnostic changes minimal and remove them after use.

## 5. Trace the causal chain

Follow the execution path across layers:
1. Input parsing and validation.
2. Authentication and authorization.
3. Business logic and state transitions.
4. Database/cache/queue reads and writes.
5. Network calls and external services.
6. Serialization, UI rendering, and final response.
7. Retry, timeout, cancellation, and cleanup behavior.

For distributed systems, align clocks and correlation IDs, distinguish event time from processing time, and check duplicate delivery, reordering, retries, and partial failure. For frontend defects, inspect browser console, network requests, viewport, device/browser differences, stale state, and asynchronous races.

## 6. Identify root cause and blast radius

A root cause explains why the incorrect state was produced, not merely where the process crashed. Determine:
- Why existing validation or tests did not catch it.
- Which users, records, environments, or versions are affected.
- Whether data was lost, duplicated, leaked, or left inconsistent.
- Whether the bug is still active or only affects historical data.
- Whether dependent systems or queued jobs need reconciliation.

Distinguish trigger, root cause, contributing factors, and detection gap.

## 7. Fix and prevent recurrence

Prefer the smallest change that restores the intended invariant. Avoid special-casing one example unless the actual contract requires it. Add a regression test that fails before the fix and passes after it. If the cause is missing observability, add a bounded, safe signal. If the defect is data-related, provide a separately reviewed repair plan.

For high-impact changes, define rollout, monitoring, rollback, and recovery conditions before release.

## 8. Verification

Run the narrowest relevant test first, then broader tests and static checks. Reproduce the original case after the fix. Test an adjacent boundary case and the primary failure path. Inspect the final diff for debug code, disabled checks, temporary credentials, and unrelated modifications.

For production incidents, verify the service and data state with read-only checks and confirm impact has stopped. Do not equate a healthy process with corrected business data.

## Diagnostic output format

1. **Symptom:** expected versus actual.
2. **Scope:** affected versions, users, systems, and time window.
3. **Evidence:** logs, trace, source locations, reproduction.
4. **Root cause:** causal chain with confidence.
5. **Contributing factors:** detection and prevention gaps.
6. **Correction:** code/config/data action and risk.
7. **Verification:** exact commands/checks and outcomes.
8. **Recovery:** data reconciliation, rollout, or follow-up needed.

## Anti-patterns

Avoid changing multiple unrelated variables, catching and ignoring exceptions, returning fake success, retrying non-idempotent work, deleting evidence, disabling authorization or validation, and blaming a dependency without a reproducing test.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [incident investigation template](references/incident-investigation-template.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

Report the verified cause, evidence, code/data/config changes, regression coverage, commands run, production actions (if authorized), and residual uncertainty. Explicitly say when the investigation is inconclusive.
