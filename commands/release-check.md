# Check release readiness

## Purpose
Determine whether a specific artifact is ready for a specific environment; this command does not deploy or publish.

## Procedure
1. Identify version, commit, artifact digest, environment, owner, and included changes.
2. Review required CI checks, tests, build, dependency/security results, and blocked/skipped gates.
3. Check API/schema compatibility, migration order, backfill, config, and supported client versions.
4. Check secrets, identity permissions, environment protection, observability, alerts, and runbooks.
5. Define rollout, health gates, monitoring window, stop conditions, rollback/forward-fix, and decision owner.
6. Verify required approvals and support readiness.

## Output
Decision: Ready / Ready with conditions / Not ready. Include evidence, missing gates, environment, artifact, migration/operational risk, rollback, and owners for conditions.

## Boundaries
Do not deploy, publish, modify production, rotate credentials, or change traffic. Report only checks with actual evidence.
