# TypeScript and JavaScript engineering standards

## Type safety
- Follow the repository's TypeScript target, module system, lint, formatter, and framework conventions.
- Prefer strict typing, discriminated unions, explicit domain types, and unknown plus validation over any.
- Avoid unchecked casts, broad non-null assertions, and duplicated type definitions.
- Validate data from APIs, storage, URLs, postMessage, files, and third-party libraries at runtime where it crosses a trust boundary.
- Keep generated API types synchronized with the backend contract.

## Async behavior
- Handle rejected promises, cancellation, timeouts, stale responses, and race conditions explicitly.
- Prevent duplicate submissions and duplicate side effects.
- Bound concurrency and payload size.
- Do not use arbitrary sleeps for synchronization.
- Clean up event listeners, subscriptions, timers, abort controllers, and framework resources.

## State and architecture
- Keep server state, URL state, form state, and ephemeral UI state distinct.
- Avoid multiple sources of truth and derived state duplication.
- Reuse established components and utilities; do not add a framework or state library without a concrete need.
- Keep modules cohesive and avoid hidden circular dependencies.

## Security
- Anything included in a client bundle is public; do not place secrets in frontend environment variables.
- Do not inject untrusted HTML.
- Validate redirects, URLs, file inputs, and browser storage.
- UI visibility is not authorization; the backend must enforce access.
- Avoid placing tokens or sensitive data in URLs, logs, analytics, or local storage without an approved design.

## UI quality
- Prefer semantic HTML and accessible native controls.
- Provide keyboard interaction, visible focus, labels, and meaningful error/status feedback.
- Support responsive layouts, zoom, text scaling, and reduced motion.
- Test loading, empty, error, disabled, and success states.

## Completion
Run build, typecheck, lint, relevant unit/component/browser tests, and report untested browser/platform coverage.
