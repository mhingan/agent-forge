---
name: technical-writing
description: Create, audit, and maintain technical documentation, READMEs, API references, runbooks, ADRs, onboarding guides, architecture docs, and release notes. Use when technical information must be accurate, usable, and maintainable.
license: MIT
---

# Technical writing and documentation engineering

## Mission

Make technical knowledge discoverable, trustworthy, task-oriented, and maintainable. Documentation is part of the product and must describe what the software actually does—not what the author hopes it does.

## 1. Identify the reader and task

Before writing, establish:
- Audience and expected technical knowledge.
- What the reader needs to understand or accomplish.
- Whether the document is tutorial, how-to, reference, explanation, policy, or operational runbook.
- Prerequisites, permissions, supported versions, and environment.
- Canonical source of truth and responsible maintainer.
- Whether the document is public, internal, or security-sensitive.

Choose one primary reader goal. Split unrelated goals into separate documents and link them.

## 2. Research and verify

Use source code, schemas, tests, build configuration, CLI help, deployment files, product behavior, and authoritative external references. Inspect current version and date for facts that can change. Verify every command, option, path, API field, permission, default, compatibility claim, and generated output.

For each claim, know whether it is:
- **Verified fact:** directly supported by current implementation or authoritative source.
- **Assumption:** not yet confirmed; label it.
- **Recommendation:** advice rather than existing behavior.
- **Example:** illustrative and not a promise of exact production values.

Never invent commands or say something is supported merely because a file can be generated.

## 3. Choose the right document type

### README
Answer what the project is, why it exists, who should use it, supported capabilities, prerequisites, fastest successful path, common commands, configuration, troubleshooting, contribution, and license. Keep detailed reference material elsewhere.

### Tutorial
Guide a beginner through one complete outcome. Explain prerequisites, each step, expected output, and recovery when a step fails.

### How-to guide
Solve a specific task for a reader who already understands the basics. State assumptions and the safe sequence.

### Reference
Document every supported option, type, default, valid value, error, compatibility note, and example. Keep it systematic and complete.

### Explanation
Clarify why the system is designed a certain way, trade-offs, terminology, and constraints. Link to actionable procedures.

### Runbook
Define trigger, severity, preconditions, diagnostic steps, safe mitigation, escalation, recovery, verification, and post-incident work.

### ADR
Record context, decision, alternatives, consequences, status, and revisit conditions.

## 4. Structure and writing style

Use task-oriented headings, descriptive names, active voice, and direct instructions. Put the most important constraint before optional detail. Keep paragraphs focused. Use tables only when comparing structured attributes; use lists for procedures and code blocks for exact commands/configuration.

Examples should be complete enough to adapt. Use obvious placeholders such as YOUR_API_TOKEN and explain how to obtain/store them. Do not use realistic-looking credentials or private URLs. Mark destructive commands clearly and show dry-run or backup alternatives where appropriate.

## 5. Code and command examples

Verify commands against the actual CLI or current official documentation. State working directory, required environment variables, expected output, and whether a command changes local or remote state. Avoid shell commands that depend on unstated platform assumptions. Prefer copyable commands with explicit quoting and error checks. Never include real secrets, personal paths, internal hostnames, or customer data.

For JSON/YAML/TOML, keep examples valid and pretty-printed. Validate machine-readable examples with a parser. Use consistent indentation, stable key ordering where useful, and a trailing newline.

## 6. Documentation architecture

Keep one canonical location per fact. Avoid duplicating long instructions across README, docs, and agent prompts. Put:
- Quick orientation in README.
- Detailed concepts in docs.
- Exact option/reference details in reference pages.
- Task-specific procedures in skills.
- Persistent constraints in rules.
- Release-specific changes in changelog.

Link related documents rather than copy entire sections. Use relative paths that work in the repository. Keep navigation shallow and check links.

## 7. Maintainability

Add version/date context where facts change quickly. Assign ownership for operational docs. Review docs in the same pull request as behavior changes. Remove obsolete options and migration instructions after the supported window ends. Keep changelog entries user-visible and grouped by added/changed/fixed/deprecated/security.

## 8. Review checklist

- Does the title describe the reader's task?
- Are prerequisites and supported versions explicit?
- Are instructions complete and in the right order?
- Are commands and configuration verified?
- Are warnings and destructive actions clear?
- Are examples valid and safe?
- Are internal/private details removed?
- Are links and anchors valid?
- Does the document distinguish facts from assumptions?
- Can a new reader complete the task without hidden context?

## Deliverables

Provide the updated document, list the source-of-truth files checked, call out unverified claims, and describe any docs that must be updated alongside the change.

## Anti-patterns

Avoid marketing claims without evidence, screenshots with secrets, giant README files, duplicate conflicting instructions, ambiguous pronouns, undocumented defaults, stale setup commands, and examples that only work on the author's machine.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [documentation review checklist](references/documentation-review-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

State audience and goal, files updated, sources checked, commands/examples validated, links reviewed, and known documentation gaps.
