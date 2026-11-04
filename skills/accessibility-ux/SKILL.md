---
name: accessibility-ux
description: Design, implement, and audit accessible digital experiences using semantic structure, keyboard interaction, assistive technology, inclusive visual design, and WCAG-aligned practices. Use for UI reviews, design systems, forms, navigation, dialogs, and accessibility remediation.
license: MIT
---

# Accessibility and inclusive UX

## Mission

Enable people with different abilities, devices, input methods, and contexts to perceive, understand, navigate, and operate the product. Accessibility is a design and engineering quality attribute, not a final automated scan.

## 1. Define the target and scope

Identify product type, platform, supported assistive technologies, applicable accessibility standard/legal target, user journey, and existing known barriers. Use WCAG 2.2 AA as a practical web baseline where appropriate, but confirm the applicable requirement rather than assuming a single standard applies everywhere.

Inspect actual rendered UI and interaction. Review both desktop and mobile behavior, including zoom, text scaling, keyboard, touch, and screen-reader output.

## 2. Semantic structure

Use native semantic elements for headings, landmarks, lists, buttons, links, tables, inputs, and dialogs. Preserve logical heading order and meaningful labels. Avoid clickable generic containers when a native button or link is correct.

Accessible names should communicate purpose, not appearance. Icon-only controls need an accessible name. Decorative graphics should be hidden from assistive technology; informative images need concise alternative text describing their purpose in context.

Use ARIA only when native HTML cannot express the required semantics. Incorrect ARIA can make an interface less accessible. Ensure roles, states, properties, and relationships match the actual behavior.

## 3. Keyboard and focus

Verify that all functionality is available without a pointer. Use a logical tab order, visible focus indicator, no keyboard traps, and expected keyboard conventions for menus, dialogs, tabs, and composite widgets. When opening a modal, move focus appropriately, keep it within the modal, support Escape when appropriate, and restore focus to the invoking control after close.

Do not remove outlines without a clear replacement. Avoid keyboard shortcuts that conflict with assistive technology or browser behavior.

## 4. Forms and validation

Every field needs a programmatic label. Explain required format and constraints before or at input. Associate field errors and hints with the field. On submit, identify the first error, summarize errors when helpful, preserve valid user input, and announce asynchronous validation. Do not rely on color, placeholder text, or icon alone to communicate state.

Use appropriate autocomplete tokens, input types, and grouping. Make required/optional status explicit and provide accessible instructions for complex controls.

## 5. Visual design

Check contrast for text, controls, icons, focus indicators, and status. Do not encode meaning only through color. Support text zoom and browser zoom without clipping or requiring horizontal scrolling for ordinary content. Respect reduced-motion preferences and avoid flashing content. Ensure content order remains meaningful when layout changes.

Review long labels, localization, large text, high contrast modes, dark/light appearance, and images with text. Avoid low-contrast disabled controls when users must still understand their state.

## 6. Dynamic content and complex widgets

Use live regions sparingly for important status changes. Announce loading completion, errors, and results without overwhelming the user. Keep focus stable during asynchronous updates. For menus, tabs, comboboxes, and grids, implement expected keyboard interaction rather than layering ARIA roles over arbitrary controls.

Tables should have meaningful headers and captions where appropriate. Complex visualizations need a textual summary or data alternative. Media needs captions/transcripts and keyboard-accessible controls.

## 7. Testing process

Combine:
- Automated checks (axe or equivalent) on representative pages.
- Manual keyboard-only completion of key journeys.
- Screen reader checks with relevant platform/browser combinations.
- Browser zoom and text-size checks.
- Contrast evaluation and reduced-motion testing.
- Real-device/touch testing for mobile interactions.

Automated scans detect only a subset of issues. Record the exact pages, controls, browser, assistive technology, and test coverage. Do not claim full conformance from a single scan.

## 8. Prioritize remediation

Prioritize barriers that prevent task completion, block critical paths, hide important information, cause data loss, or affect many users. Fix root semantics and shared components rather than patching each page. Add regression checks to the design system and test suite.

## Accessibility acceptance checklist

- Every control has an accessible name and correct role/state.
- Keyboard users can reach and operate all functionality.
- Focus is visible, logical, and managed after dialogs/navigation.
- Forms expose labels, instructions, and errors.
- Content remains usable under zoom and text scaling.
- Contrast and non-color cues communicate all important states.
- Dynamic updates are announced appropriately.
- Media and visual data have accessible alternatives.
- Reduced motion and platform settings are respected.
- Manual testing covers key user journeys.

## Deliverables

Report standard/target, scope, barriers found by severity, affected elements, reproduction steps, remediation, automated/manual checks, and remaining limitations.

## Anti-patterns

Avoid positive tabindex ordering, clickable divs without keyboard behavior, placeholder-only labels, color-only indicators, focus removal, excessive live announcements, ARIA used to imitate native controls, and claims of compliance based only on automated scans.

## Completion report

State which barriers were addressed, which journeys/devices/assistive technologies were tested, what was not tested, and whether the result is a partial audit or a formal conformance assessment.
