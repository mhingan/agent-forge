---
name: technical-writing
description: Create or improve technical documentation, runbooks, ADRs, API guides, onboarding material, and release notes. Use when technical information must be accurate, scannable, and maintainable.
license: MIT
---

# Technical writing

## Workflow
1. Identify audience, task, prerequisite knowledge, document purpose, and maintenance owner.
2. Gather facts from the source of truth: code, configuration, product docs, tests, and confirmed stakeholder input.
3. Separate verified facts from assumptions, recommendations, and examples.
4. Organize around reader tasks and decisions rather than the order information was discovered.
5. Use precise terminology, active voice, descriptive headings, and concrete examples.
6. Explain prerequisites, expected outcomes, failure cases, troubleshooting, and rollback where relevant.
7. Keep examples runnable and safe. Use placeholders for secrets and environment-specific values.
8. Cross-check commands, paths, API fields, and versions against the actual project.
9. Remove duplicated or stale guidance; link to canonical references when possible.
10. Review for accessibility, consistency, and future maintainability.

## Document patterns
- **Runbook:** alert/symptom, impact, checks, safe remediation, escalation, verification, rollback.
- **ADR:** status, context, decision, alternatives, consequences, follow-up.
- **API guide:** use case, auth, request, response, errors, pagination, retry behavior, examples.
- **Onboarding:** prerequisites, setup, first success path, architecture map, tests, common issues.
- **Release notes:** user-visible change, compatibility, migration action, known issues.

## Rules
Do not invent commands, settings, API behavior, or performance claims. Mark placeholders clearly. Never include live credentials, internal personal data, or sensitive operational details without authorization.
