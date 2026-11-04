---
name: frontend-engineering
description: Build and review accessible, responsive frontend applications with modern JavaScript/TypeScript frameworks. Use for UI implementation, component architecture, state, routing, forms, performance, and browser behavior.
license: MIT
---

# Frontend engineering

## Procedure
1. Inspect the existing framework, design system, component conventions, routes, state management, build setup, and tests.
2. Identify user flows, responsive breakpoints, accessibility requirements, loading/error/empty states, and supported browsers.
3. Reuse existing components and tokens. Avoid adding a second design system or unnecessary state library.
4. Model state explicitly. Keep derived state derived; avoid duplicated sources of truth.
5. Validate user input at the client for usability and on the server for security and correctness.
6. Handle async loading, cancellation, retries, stale responses, and error recovery deliberately.
7. Make interactions keyboard accessible with semantic HTML, visible focus, labels, and meaningful announcements.
8. Use responsive layouts and test narrow screens, zoom, long content, and touch interactions.
9. Optimize only with evidence: bundle analysis, rendering profiles, image sizing, caching, and route-level loading.
10. Add component, interaction, and end-to-end tests for critical flows.

## TypeScript guidance
- Prefer strict types and discriminated unions over `any` and unchecked casts.
- Validate data received from APIs at runtime when trust boundaries require it.
- Avoid non-null assertions when the state can be modeled safely.
- Keep API types synchronized with actual backend contracts; do not duplicate stale schemas.

## Accessibility checklist
- Semantic landmarks and heading order
- Labels and instructions for form controls
- Keyboard-only navigation
- Visible focus state
- Sufficient contrast and reduced-motion support
- Accessible names for icon-only controls
- Correct dialog focus handling and escape behavior
- Error messages associated with affected fields

## Completion criteria
Verify build/typecheck/lint, relevant tests, responsive states, loading/error states, keyboard interaction, and visual consistency with the project's design system.
