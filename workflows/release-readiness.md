# Release readiness workflow

## Scope
Confirm release version, target environment, included changes, release owner, and approval path.

## Validation
- Build is reproducible and artifacts are identified.
- Automated tests, static checks, and security scans have reviewed results.
- Database migrations are reviewed for locks, data backfill, compatibility, and rollback/forward-fix.
- Secrets and environment configuration are managed outside source control.
- Monitoring, alerts, dashboards, and support/runbook updates are ready.
- Feature flags, staged rollout, health gates, and rollback criteria are defined.

## Approval
Present the release plan and target. Do not deploy, publish, or modify production without explicit approval.

## After release
Verify health, key user journeys, error rates, latency, and background processing. Record the outcome and any follow-up work.
