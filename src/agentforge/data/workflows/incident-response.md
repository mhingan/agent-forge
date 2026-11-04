# Production incident response workflow

**Purpose:** Stabilize user impact, preserve evidence, coordinate responders, and verify recovery. This playbook is for authorized operational responders.

## Phase 1 — Declare and coordinate
Establish incident severity, incident lead, technical owner, communication channel, timeline, and decision authority. Identify affected service, region, users, and business workflows.

## Phase 2 — Assess impact
Use user-visible signals, SLOs, error/latency/saturation metrics, queue age, and recent releases. Separate confirmed facts from hypotheses. Record the first known impact and current blast radius.

## Phase 3 — Stabilize safely
Prefer reversible mitigations that reduce impact. Consider traffic reduction, feature flag disablement, bounded load shedding, or rollback only when authorized and when data compatibility is understood. Avoid speculative changes and destructive actions.

## Phase 4 — Preserve evidence
Capture relevant logs, traces, metrics, deployment/config versions, and correlation IDs. Redact secrets and personal data. Preserve audit history. Do not replay jobs or alter production data before understanding duplication and state.

## Phase 5 — Recover
Apply the approved mitigation/fix. Verify critical user journeys, error rate, latency, dependency health, queue processing, and data integrity. Keep monitoring long enough to establish stable recovery.

## Phase 6 — Communicate
Provide concise updates with time, impact, status, actions, and next update. Do not overstate certainty or claim recovery before it is measured.

## Phase 7 — Learn and prevent recurrence
Write timeline, root cause, trigger, contributing factors, detection gaps, recovery effectiveness, and corrective actions with owners/dates. Focus on system/process improvements, not blame.

## Boundaries
Do not restart, fail over, replay, rollback, deploy, modify access, or repair production data unless the operator is authorized. Escalate when actions exceed the approved scope.
