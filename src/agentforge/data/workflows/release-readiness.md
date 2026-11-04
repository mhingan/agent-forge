# Release readiness workflow

**Purpose:** Confirm that a specific artifact can be released to a specific environment with understood risk and a recovery path.

## Phase 1 — Identify the release
Record version, commit, artifact digest, target environment/region, release owner, approver, included changes, and exclusions. Verify that the artifact was built from the intended commit.

## Phase 2 — Quality gates
Confirm required tests, type/lint/static checks, dependency/security scans, build/package integrity, and critical user-journey smoke tests. Distinguish passed, skipped, blocked, and not-run checks.

## Phase 3 — Data and compatibility
Review API/schema changes, old/new application compatibility, migrations, backfills, generated clients, feature flags, and client minimum versions. Confirm that data migration and application rollout order are compatible.

## Phase 4 — Operations and security
Verify target configuration, identity, secrets, permissions, network exposure, monitoring, alerts, dashboards, support/runbook, backup/restore, and operational owner. Ensure no secret is embedded in artifacts or logs.

## Phase 5 — Rollout plan
Choose phased, canary, rolling, blue/green, or feature-flagged release as appropriate. Define health gates, success thresholds, monitoring window, abort triggers, rollback/forward-fix, and decision owner.

## Phase 6 — Approval gate
Present the exact environment, artifact, expected side effects, user impact, and recovery strategy. Do not deploy, publish, change traffic, or rotate credentials without explicit approval.

## Phase 7 — Post-release verification
Check process readiness, critical user paths, latency/error/saturation, queue age, data reconciliation, and external integrations. Record outcome, owner, incidents, and follow-up actions.

## Release decision
Return Ready / Ready with conditions / Not ready. Every condition must have an owner and an explicit completion point.
