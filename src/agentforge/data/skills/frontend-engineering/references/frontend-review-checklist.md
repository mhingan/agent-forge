# Frontend implementation review

## Product and design
- [ ] User journey and acceptance criteria are understood.
- [ ] Existing design tokens/components are reused.
- [ ] Default, hover, focus, active, disabled, loading, success, and error states exist.
- [ ] Empty and long-content states are designed.
- [ ] Mobile and desktop are treated as separate layout constraints.

## Architecture and state
- [ ] Components have one clear responsibility.
- [ ] Server, form, URL, and ephemeral state are not duplicated.
- [ ] Data fetching handles cancellation and stale responses.
- [ ] API data is validated at trust boundaries.
- [ ] Errors and retries are consistent with backend contracts.

## Accessibility
- [ ] Semantic HTML and heading order.
- [ ] Accessible labels/names and focus state.
- [ ] Keyboard-only interaction works.
- [ ] Dialog/menu focus is managed.
- [ ] Contrast and non-color status cues are adequate.
- [ ] Reduced motion and text scaling are respected.

## Security and performance
- [ ] No unsafe HTML injection or client-side secrets.
- [ ] Authorization is enforced by the server.
- [ ] Large lists and assets are measured/bounded.
- [ ] No speculative memoization or unnecessary framework dependencies.

## Verification
- [ ] Build, typecheck, lint, tests.
- [ ] Loading/error/empty states.
- [ ] Console/network failures.
- [ ] Responsive viewport checks.
- [ ] Keyboard interaction and visual regressions.
