# Frontend-specific rules

- Follow the existing framework and design system; do not replace the UI stack to solve a single page.
- Build complete interaction states: initial, loading, loaded, empty, validation error, recoverable failure, terminal failure, submitting, success, and stale/refreshing.
- Use semantic HTML, accessible names, labels, keyboard behavior, focus management, and non-color status cues.
- Do not disable browser zoom or hide focus indicators to preserve a layout.
- Validate external API data at boundaries and handle stale asynchronous responses.
- Do not expose secrets in bundled configuration, URLs, local storage, logs, or analytics.
- Treat hidden buttons and client-side route guards as UX only; enforce authorization on the backend.
- Use design tokens; avoid arbitrary spacing, color, shadow, type, and breakpoint values.
- Test narrow and wide viewports, long content, localization, zoom, keyboard navigation, and failure states.
- Measure before optimizing rendering or adding memoization.
