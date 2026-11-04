# Python rules

- Use supported project Python version and existing formatting/lint conventions.
- Add type annotations to public functions and non-trivial interfaces.
- Prefer standard-library functionality or already-installed dependencies over new packages.
- Use context managers for managed resources and explicit timeout values for network operations.
- Avoid mutable default arguments, broad exception swallowing, and unnecessary global state.
- Validate external data at boundaries; do not trust type hints as runtime validation.
- Keep async code free of blocking I/O and use async only when the call chain benefits.
- Use parameterized SQL and avoid logging secrets or sensitive records.
- Add tests for edge cases and failure behavior.
