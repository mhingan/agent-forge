# Pull request review workflow

1. Confirm base/head revisions and intended change.
2. Read the full diff and inspect affected callers, data models, configuration, and tests.
3. Review correctness, security, authorization, compatibility, reliability, performance, and maintainability.
4. Verify whether tests exercise the changed behavior and failure cases.
5. Write actionable findings with severity, file/line, trigger, impact, and remediation.
6. Separate blocking defects from optional improvements.
7. State test coverage, commands run, and residual risks.

Default to read-only review. Do not edit the pull request unless asked.
