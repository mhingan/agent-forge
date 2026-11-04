# Git and repository collaboration rules

## Before changing files
- Run status and inspect the current branch and diff.
- Identify user changes, generated files, local configuration, and ignored files.
- Read contribution guidelines and repository-specific branch/commit conventions.
- Never discard, reset, checkout over, or rewrite user modifications without explicit approval.

## Changes and commits
- Keep changes focused and logically grouped.
- Do not commit secrets, local databases, credentials, private datasets, build artifacts, or environment files.
- Review the staged diff, not just the working diff.
- Use descriptive imperative commit messages that explain the intent.
- Update tests, documentation, changelog, and generated/package copies when the source change requires it.
- Never claim a commit, push, or PR update succeeded without inspecting the returned result.

## Branch and remote safety
- Do not force-push, rewrite shared history, delete remote branches/tags, or change repository settings without explicit authorization.
- Verify remote, branch, and target before pushing.
- Do not commit directly to a protected/default branch when project policy requires a pull request.
- Avoid embedding tokens in Git URLs or shell history.

## Pull requests
- Describe motivation, scope, compatibility, migration/deployment implications, tests, and risks.
- Keep generated diffs reproducible.
- Review all changed files and check for accidental secrets or unrelated changes.
- Do not approve or merge a PR unless explicitly asked and authorized.
