# CI/CD security checklist

## Workflow trust
- [ ] Workflow permissions are least-privilege.
- [ ] Untrusted pull-request code cannot access deployment credentials.
- [ ] Expressions do not interpolate attacker-controlled data into shell commands.
- [ ] Fork workflows cannot write repository, package, or cloud resources.
- [ ] Third-party actions and dependencies are pinned/verified per policy.

## Secrets and identity
- [ ] Build, publish, deploy, and runtime identities are separate where practical.
- [ ] Short-lived workload identity is preferred over long-lived tokens.
- [ ] Secrets are not printed, cached, uploaded as artifacts, or embedded in images.
- [ ] Environment approvals protect production credentials.
- [ ] Secret rotation and revocation are documented.

## Supply chain
- [ ] Dependencies use lockfiles and reviewable versions.
- [ ] Build artifacts are immutable and traceable to commit.
- [ ] Artifact provenance/signing is considered for release-critical software.
- [ ] Container/image/dependency scans have an owner and severity policy.
- [ ] Generated artifacts are checked for secrets and private data.

## Deployment safety
- [ ] Production environment is protected.
- [ ] Deployment target and artifact digest are explicit.
- [ ] Rollback and migration compatibility are reviewed.
- [ ] Smoke tests and health gates run after deployment.
