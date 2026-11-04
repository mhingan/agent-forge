# Accessibility review workflow

**Purpose:** Evaluate and improve a real user journey for keyboard, assistive technology, visual, and responsive accessibility.

## Phase 1 — Scope
Identify pages/components, critical journeys, applicable standard and target level, browser/platform, assistive technology, input methods, and exclusions. Do not assume an audit target without confirming the product requirement.

## Phase 2 — Inspect semantics
Review landmarks, heading order, native controls, accessible names, labels, descriptions, error associations, alternative text, captions, and data alternatives. Use ARIA only when native semantics are insufficient.

## Phase 3 — Keyboard and focus
Complete the critical journey with keyboard only. Check visible focus, tab order, no traps, dialog/menu focus entry and restoration, Escape/back behavior, and operable composite controls.

## Phase 4 — Visual and responsive
Check contrast, zoom/text scaling, narrow viewports, long content, localization, reduced motion, high-contrast mode, touch target behavior, and non-color status.

## Phase 5 — Dynamic content
Check announcements for loading/results/errors, focus stability, form validation feedback, and complex widgets. Avoid excessive live-region noise.

## Phase 6 — Automated and manual testing
Run an automated accessibility scan, then manually reproduce important findings with keyboard and relevant screen reader. Record exact browser, OS, assistive technology, pages, and controls. Automated tests do not prove conformance.

## Phase 7 — Remediate and retest
Fix shared semantic/component issues at the source. Prioritize task-blocking barriers. Add regression coverage and verify the original user journey again.

## Report
Provide finding, severity, user impact, exact element, reproduction, criterion (if known), remediation, test evidence, coverage limits, and residual barriers.
