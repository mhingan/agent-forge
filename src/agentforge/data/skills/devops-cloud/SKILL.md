---
name: devops-cloud
description: Build and operate deployment pipelines and cloud infrastructure safely. Use for CI/CD, containers, Kubernetes, infrastructure configuration, releases, observability, and incident response.
license: MIT
---

# DevOps and cloud engineering

## Operating principles
- Prefer declarative, reviewed, reproducible infrastructure.
- Separate environments and credentials; use least privilege and short-lived identity where available.
- Make builds reproducible and deployments observable.
- Design health checks, rollback, backups, and recovery before production rollout.

## Workflow
1. Identify platform, environments, deployment model, ownership, service criticality, and change window.
2. Inspect existing CI/CD and infrastructure configuration before proposing new tooling.
3. Build immutable artifacts once and promote the same artifact through environments where practical.
4. Pin or constrain dependencies and base images; scan dependencies and artifacts.
5. Keep secrets in approved secret stores. Never commit them or print them in build logs.
6. Use least-privilege service identities and scoped tokens.
7. Configure readiness/liveness appropriately; do not use liveness checks to test flaky external dependencies.
8. Add resource requests/limits and autoscaling based on measured workloads.
9. Define rollout strategy, health gates, rollback conditions, and post-deploy verification.
10. Emit actionable logs, metrics, traces, and alerts; avoid noisy alerts without an owner/action.

## Kubernetes checklist
- Namespaces and RBAC are scoped.
- Workloads run as non-root where possible.
- Capabilities, filesystem access, and network policies are restricted.
- Secrets are not stored in plain manifests or images.
- Probes, disruption budgets, resource requests/limits, and rollout strategy are deliberate.
- Persistent data has backup and restore procedures.

## Change safety
Never apply infrastructure changes, publish images, rotate production credentials, delete resources, or deploy to production without explicit authorization. Show the plan and affected environment first.

## Deliverables
Provide change summary, pipeline/config updates, security implications, validation commands, rollout plan, rollback plan, and operational follow-up.
