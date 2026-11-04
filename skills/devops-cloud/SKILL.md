---
name: devops-cloud
description: Design, implement, secure, and operate cloud infrastructure and delivery pipelines. Use for CI/CD, containers, deployment platforms, Kubernetes, infrastructure as code, release engineering, secrets, monitoring, and incident response.
license: MIT
---

# DevOps and cloud engineering

## Mission

Make software delivery reproducible, secure, observable, and recoverable. Infrastructure automation is production code: it needs review, validation, least privilege, change control, and a recovery plan.

## 1. Discover the current delivery system

Inspect:
- Source control, branch strategy, required checks, release/tag process, and artifact provenance.
- Build system, dependency lockfiles, runtime versions, and supported platforms.
- Deployment target, environments, network layout, service identities, and secret management.
- Database and persistent storage dependencies.
- Current health checks, logs, metrics, traces, alerts, backup/restore, and incident process.
- Resource limits, autoscaling, cost constraints, and ownership.

Do not migrate platforms or introduce new orchestration simply because a tool is familiar. First identify the problem in the current system.

## 2. CI pipeline design

A reliable pipeline should:
1. Check out the exact commit and use least-privilege workflow permissions.
2. Pin or constrain toolchain/runtime versions.
3. Install dependencies from lockfiles and use caching only when cache keys include relevant inputs.
4. Run formatting, lint, type checks, unit tests, integration tests, and security checks appropriate to the project.
5. Build an immutable artifact once and identify it by commit/digest.
6. Publish artifacts only from trusted refs/environments and with explicit permissions.
7. Promote the same artifact through environments rather than rebuilding different binaries for each environment.
8. Produce useful logs and clear failure summaries without printing secrets.

Protect workflows from untrusted pull-request code, unsafe workflow expressions, and write permissions available to forks. Pin third-party actions to verified immutable references when the project's policy requires it.

## 3. Infrastructure as code

Keep infrastructure declarative, reviewed, and reproducible. Separate environments and sensitive state. Use modules only when boundaries and shared ownership justify them. Expose variables with validation and safe defaults. Review the plan/diff before applying. Avoid storing plaintext secrets in state, logs, plans, or repository files.

For each resource, define owner, purpose, environment, tags, network exposure, identity, encryption, backups, lifecycle, and cost controls. Detect drift deliberately; do not automatically destroy or recreate resources to make a plan green.

## 4. Containers and runtime hardening

- Use minimal maintained base images and pin versions/digests where appropriate.
- Use multi-stage builds and copy only runtime artifacts.
- Run as a non-root user.
- Drop unnecessary capabilities and avoid privileged mode.
- Keep secrets out of images, build args, labels, and layers.
- Define health checks, graceful termination, resource limits, and writable paths.
- Scan dependencies/images and produce provenance/SBOM where required.
- Log to the platform's supported output and keep logs structured and bounded.

## 5. Deployment and release strategy

Choose a rollout pattern that matches the system: rolling, canary, blue/green, phased traffic, or feature-flagged release. Define:
- Target environment and artifact digest.
- Preconditions and approval owner.
- Health gates and user-journey checks.
- Database migration order and compatibility window.
- Monitoring window and rollback thresholds.
- Rollback/forward-fix procedure and data compatibility.
- Communication and support ownership.

Do not deploy, publish, rotate production credentials, delete resources, change DNS, or alter production traffic without explicit authorization. Present target environment and expected side effects first.

## 6. Cloud platform design

Use platform-native managed services where they reduce operational burden, but validate limits, region availability, networking, identity, billing, retention, backups, and exit strategy. Avoid assuming that serverless means unlimited capacity or zero operations. Understand cold starts, execution limits, ephemeral filesystems, queue delivery, connection reuse, and regional failure modes.

## 7. Secrets and identity

Use workload identity or short-lived tokens where available. Scope secrets to one environment and purpose. Rotate and revoke through controlled procedures. Never put credentials in source, images, logs, screenshots, issue text, or command history. Prevent pull-request workflows from accessing deployment credentials. Use separate identities for build, deploy, runtime, and database migration.

## 8. Observability and reliability

Instrument:
- Request/job rate, latency percentiles, error rate, saturation, queue age, and dependency health.
- Structured logs with trace/request IDs and redacted fields.
- Distributed traces across important service boundaries.
- Alerts tied to a user-visible symptom and an actionable owner.

Use readiness and liveness probes for distinct purposes. Define service-level indicators and objectives when the service is important enough. Avoid high-cardinality metric labels and alerting on every transient error.

## 9. Incident response and disaster recovery

Document severity, incident commander/owner, communication channel, timeline, mitigation, evidence, and follow-up. Stabilize before making risky changes. Preserve audit trails. Test backup restore and recovery procedures, not merely backup job success. Define RTO/RPO and validate them through exercises.

## 10. Validation and handover

Run pipeline validation, infrastructure format/validation, policy checks, image/dependency scans, and environment-specific smoke tests. Confirm no secret or generated state was committed. Provide the exact artifact/version, deployment target, monitoring signals, rollback steps, and ownership.

## Anti-patterns

Avoid mutable latest tags for critical deployments, unreviewed infrastructure applies, long-lived admin tokens, secrets in build logs, production deployment from untrusted branches, missing rollback criteria, unbounded autoscaling, and CI checks that report success while silently skipping failed stages.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [deployment runbook template](references/deployment-runbook-template.md)
- [pipeline security checklist](references/pipeline-security-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

Summarize pipeline/infrastructure changes, permissions, artifact identity, environment, validation results, rollout/rollback plan, monitoring, and remaining operational risks.
