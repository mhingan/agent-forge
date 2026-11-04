# TypeScript rules

- Enable strict type checking where project constraints allow.
- Prefer explicit domain types, discriminated unions, and `unknown` plus validation over `any`.
- Validate untrusted API, storage, and URL input at runtime when it crosses a trust boundary.
- Avoid unchecked casts and non-null assertions when the state can be modeled safely.
- Keep derived state derived and avoid duplicated sources of truth.
- Handle asynchronous cancellation, stale responses, and errors deliberately.
- Use semantic HTML and accessible interaction patterns in UI code.
- Follow established project lint, format, test, and build conventions.
