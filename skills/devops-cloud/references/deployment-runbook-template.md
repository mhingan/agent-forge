# Deployment runbook

## Release metadata
- Service/application:
- Release/version:
- Artifact digest:
- Target environment/region:
- Change owner and approver:
- Deployment window:
- Change/ticket reference:

## Preconditions
- [ ] Correct artifact and commit verified.
- [ ] Required CI/security checks passed.
- [ ] Configuration and secrets are available in target environment.
- [ ] Database compatibility and migration order reviewed.
- [ ] Dependencies and capacity are healthy.
- [ ] Monitoring, alerting, and on-call owner are ready.
- [ ] Rollback/forward-fix and stop conditions are agreed.

## Deployment steps
| Step | Command/action | Expected result | Stop condition |
|---|---|---|---|
| | | | |

## Health verification
Check readiness, smoke tests, key user journeys, error rate, latency percentiles, saturation, queues, and dependency health. Record expected baseline and abort thresholds.

## Rollback / forward-fix
- Trigger:
- Decision owner:
- Exact recovery action:
- Data compatibility:
- Verification:
- Communication:

## Post-deployment
- [ ] User journey verified.
- [ ] Error/latency/saturation reviewed.
- [ ] Background jobs and queues healthy.
- [ ] No secret/config leak.
- [ ] Release notes and incident/change records updated.
