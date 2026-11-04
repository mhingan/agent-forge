# Product discovery and specification workflow

**Purpose:** Convert an ambiguous request into a validated problem statement and implementation-ready specification.

## Phase 1 — Problem framing
Identify target user, use context, current workflow, pain point, frequency, impact, and workaround. Gather evidence from analytics, support, research, operational data, or stakeholder input. Label assumptions as assumptions.

## Phase 2 — Outcome and measurement
Define the user outcome and business objective. Select a primary success measure and guardrails. Record baseline and target only when sourced or explicitly proposed for approval.

## Phase 3 — Explore options
Compare a small set of plausible solutions, including process changes or a smaller experiment. Compare user value, effort, time to learn, operational cost, risk, reversibility, and dependencies.

## Phase 4 — Specify behavior
Define actors, preconditions, triggers, normal journey, business rules, data ownership, roles/permissions, state transitions, notifications, external side effects, validation errors, empty states, recovery, and cancellation.

## Phase 5 — Quality attributes
Specify relevant security, privacy, performance, availability, accessibility, localization, compatibility, support, observability, retention, export, and deletion needs. Avoid vague adjectives without observable criteria.

## Phase 6 — Acceptance criteria and scope
Write Given/When/Then criteria for normal, invalid, boundary, unauthorized, duplicate, concurrent, and failure cases. Separate must-have, later, optional, and explicit non-goals.

## Phase 7 — Handoff
Provide problem/evidence, goals/non-goals, journeys, functional and non-functional requirements, acceptance criteria, success measures, risks, dependencies, rollout, and open decisions. Link design/architecture/API artifacts instead of duplicating them.

## Readiness gate
A brief is implementation-ready when the critical user journey is complete, criteria are testable, scope is explicit, risks are visible, and open decisions have owners.
