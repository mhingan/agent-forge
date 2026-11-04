# Python engineering standards

## Project consistency
- Follow the project's Python version, formatter, linter, type checker, package manager, and test conventions.
- Prefer the standard library or an existing dependency over introducing a new package.
- Keep dependency changes intentional, pinned/locked according to repository policy, and documented.
- Avoid import-time network calls, filesystem mutation, or other application side effects.

## Design and typing
- Use type annotations for public APIs and non-trivial interfaces.
- Prefer explicit domain types, dataclasses, enums, and protocols where they improve clarity.
- Avoid Any, unchecked casts, mutable defaults, broad exception swallowing, and unnecessary global mutable state.
- Keep functions cohesive and make side effects visible.
- Separate transport, application/domain behavior, and infrastructure concerns when the codebase warrants it.

## Runtime and resources
- Use context managers for files, locks, database sessions, and other managed resources.
- Set explicit timeouts for network and subprocess operations.
- Handle cancellation and cleanup correctly.
- In async code, never block the event loop with synchronous I/O or CPU-heavy work.
- Use async only when the actual call chain benefits from it; do not add async ceremonially.
- Bound concurrency, queue size, input size, recursion, and memory use.

## Data and security
- Validate external data at runtime; type hints do not validate API input.
- Use parameterized SQL and safe serialization.
- Keep secrets out of source, tests, exceptions, and logs.
- Avoid logging entire request/response objects when they may contain personal or sensitive values.
- Make timezone and decimal/money semantics explicit.

## Testing
- Use pytest or the repository's established framework.
- Test business behavior, edge cases, invalid input, authorization, and dependency failure.
- Keep tests deterministic and isolated; control time/randomness and clean up resources.
- Do not hide flaky tests by rerunning until green.

## Completion
Run focused tests first, then relevant full tests, type checks, lint, and build. Report exact commands and results.
