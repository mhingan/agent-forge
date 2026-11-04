---
name: frontend-engineering
description: Build, refactor, or review accessible, responsive web frontends using React, TypeScript, and other modern frameworks. Use for UI architecture, component design, routing, forms, state, API integration, browser behavior, performance, and visual quality.
license: MIT
---

# Frontend engineering

## Mission

Build interfaces that help users complete real tasks reliably. A production frontend must be responsive, accessible, secure at the client boundary, resilient to asynchronous behavior, and consistent with the product's design system—not simply visually attractive in one screenshot.

## 1. Discover the existing product and codebase

Before implementation, inspect:
- Framework, router, build tool, package manager, scripts, versions, and lockfile.
- Design system, tokens, typography, icons, shared components, and page patterns.
- Existing state/data-fetching libraries, API clients, validation, auth flow, and error handling.
- Supported browsers, breakpoints, accessibility targets, and mobile constraints.
- Existing tests, screenshots, lint, typecheck, and build requirements.

Understand the target user's goal and the full flow: entry point, empty state, interaction, success, failure, and recovery. Reuse project components before adding abstractions or dependencies.

## 2. Component and page architecture

Keep components cohesive and named for their responsibility. Separate:
- Page/layout composition.
- Reusable presentation components.
- Domain-specific components.
- Form and interaction state.
- API/data-access functions.
- Pure transformations and validation.

Avoid components with many unrelated boolean props, deeply nested conditional JSX, duplicated data-fetching logic, and global state for local UI concerns. Use composition and explicit state models where they clarify behavior. Do not create a design system inside a project that already has one.

## 3. Visual and interaction quality

Translate design requirements into measurable decisions:
- Content hierarchy and scan order.
- Grid, spacing, alignment, typography, and responsive constraints.
- Interactive states: default, hover, focus, active, disabled, loading, success, and error.
- Long text, empty data, large numbers, localization, and content overflow.
- Touch target size and behavior on narrow screens.
- Reduced motion and visual feedback for state changes.

Use design tokens for colors, spacing, typography, radii, shadows, and layers. Avoid arbitrary one-off values unless the design requires them. Use one icon system and consistent SVG or icon components; do not mix emoji with professional UI iconography when the design calls for icons.

## 4. Responsive behavior

Design mobile and desktop as real supported layouts, not a desktop page squeezed into a small viewport. Test narrow widths, orientation changes, browser zoom, touch input, safe areas, and long content. Use flexible layouts, content-based breakpoints, and responsive image sizing. Avoid fixed widths/heights that clip controls or data. Do not disable browser zoom or basic accessibility features to preserve visual layout.

## 5. Accessibility

Use semantic HTML first. Provide:
- Correct heading hierarchy and landmarks.
- Accessible names and labels for controls, including icon-only buttons.
- Keyboard navigation and visible focus.
- Logical focus order and focus restoration for dialogs/menus.
- Proper field labels, descriptions, and linked validation messages.
- Status announcements for asynchronous updates.
- Sufficient text/control contrast and non-color-only status.
- Meaningful alternative text for informative images and empty alt for decorative images.
- Reduced-motion behavior for non-essential animation.

Test the primary journey with keyboard only and at least one screen-reader-oriented inspection when feasible. Automated checks help but do not prove accessibility.

## 6. State and data fetching

Keep server state, form state, URL state, and ephemeral UI state distinct. Model asynchronous states explicitly:
- Initial/unrequested.
- Loading.
- Loaded with data.
- Empty.
- Failed with recoverable or terminal error.
- Refreshing/stale where appropriate.

Cancel obsolete requests or ignore stale responses. Prevent duplicate submissions and race conditions. Handle optimistic updates only when rollback/reconciliation semantics are clear. Keep URL parameters shareable when they represent meaningful navigation/filter state.

Treat API responses as untrusted runtime data. Validate at boundaries where schema drift or unsafe content matters. Do not expose secrets in frontend environment variables; anything bundled into client code is public.

## 7. Forms and validation

Define required/optional fields, constraints, defaults, normalization, error mapping, and submission states. Use client validation for fast feedback but let the backend remain authoritative. Preserve user input on recoverable errors. Display field-level and form-level errors clearly. Prevent accidental repeated submission and confirm high-impact actions.

## 8. Security and privacy

Avoid unsafe HTML injection. Sanitize content according to the rendering context and use framework-safe escaping. Protect against XSS, open redirects, leaking tokens in URLs, sensitive information in local storage, and overbroad browser permissions. Do not trust hidden fields, disabled controls, or route guards as authorization. The backend must enforce access.

## 9. Performance

Measure before optimizing. Check bundle composition, route-level splitting, unnecessary rendering, image sizes, font loading, network waterfall, cache headers, and large lists. Use virtualization when measured rendering cost warrants it. Avoid speculative memoization and abstractions that make code harder to reason about.

## 10. Testing and verification

Test behavior at appropriate levels:
- Unit: pure transforms, validation, hooks, and state machines.
- Component: rendering, keyboard behavior, forms, and conditional states.
- Integration: API integration, routing, and authentication flows.
- End-to-end: login, critical business journeys, and high-impact mutations.
- Visual: key pages at representative viewport sizes, when screenshot infrastructure exists.

For every UI change verify build, typecheck, lint, affected tests, console errors, loading/error/empty states, keyboard navigation, and responsive layouts. Do not claim visual verification if no browser or screenshot check was performed.

## Deliverables

Provide implementation notes, changed routes/components, states handled, API assumptions, accessibility decisions, and verification results. Include screenshots only when actually captured and useful.

## Anti-patterns

Avoid giant page components, duplicate sources of truth, untyped API data, inaccessible custom controls, unbounded lists, magic breakpoints, disabling zoom, hover-only interactions, and optimistic mutations without recovery logic.

## Completion report

State what changed, which user journey it improves, responsive/accessibility coverage, tests/build checks run, and remaining limitations.
