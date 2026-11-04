---
name: debugging
description: Investigate defects and unexpected behavior systematically using logs, traces, code, reproduction steps, and tests. Use when a bug is intermittent, unclear, or spans multiple components.
license: MIT
---

# Debugging and root-cause analysis

## Goal
Find the smallest evidence-backed explanation for the observed behavior, then implement or recommend a safe correction.

## Investigation procedure
1. Restate the symptom, expected behavior, actual behavior, impact, and first known occurrence.
2. Separate confirmed facts, hypotheses, and unknowns.
3. Reproduce with the smallest reliable case. Capture environment, input, state, timing, and relevant versions without exposing secrets.
4. Trace the execution path through logs, stack traces, requests, state transitions, and dependencies.
5. Form one testable hypothesis at a time. Prefer experiments that distinguish competing causes.
6. Check recent code/config/dependency/data changes and compare working versus failing environments.
7. Identify the root cause, not only the visible failure point.
8. Implement the narrowest fix that addresses the root cause without masking errors.
9. Add a regression test that fails before the fix and passes after it.
10. Verify related paths and report remaining uncertainty.

## Observability guidance
- Correlate events using request/job IDs and timestamps.
- Redact tokens, passwords, session cookies, personal data, and secrets from logs.
- Distinguish client errors, application defects, infrastructure failures, and dependency failures.
- Check retries and queue redelivery before concluding a request happened only once.

## Output
- Reproduction steps
- Evidence collected
- Root cause and causal chain
- Fix or recommended action
- Regression coverage
- Verification performed
- Residual risks / open questions

## Guardrails
Do not randomly change multiple variables, suppress exceptions, disable security controls, or delete data to make an error disappear. Ask before restarting production services or modifying production data.
