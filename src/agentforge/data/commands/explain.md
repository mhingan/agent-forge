# Explain a codebase, module, or execution path

## Purpose
Produce an evidence-based explanation that helps a developer understand actual behavior without modifying files.

## Inputs
- Target: file/module/service/feature/request path.
- Desired depth: overview / implementation / runtime / security / operations.
- Question or task context.
- Optional constraints: audience, framework, version, specific files.

## Procedure
1. Read repository guidance and inspect the target source, configuration, tests, and relevant callers.
2. Identify entry points and trace the real execution path.
3. Explain responsibilities and boundaries: transport, domain/application logic, persistence, external dependencies, UI, jobs.
4. Describe the data flow, state changes, contracts, validation, authorization, and failure behavior.
5. Link claims to exact file paths and symbol names.
6. Separate confirmed implementation facts from assumptions, gaps, and recommendations.
7. Avoid copying large source sections. Summarize behavior and quote only the minimum useful fragment.

## Output
1. **What it does** — one-paragraph summary.
2. **Where it lives** — key files and responsibilities.
3. **How it works** — ordered execution/data flow.
4. **Important contracts/state** — input/output, persistence, permissions, and side effects.
5. **Failure behavior** — errors, retries, timeouts, and recovery.
6. **Tests and evidence** — relevant test files and what they verify.
7. **Limitations/open questions** — behavior not established by source.

## Boundaries
Do not edit code, invent runtime behavior, assume an endpoint works because a route exists, or expose secrets/private data. State when you have not run the application.
