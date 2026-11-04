---
name: product-specification
description: Turn ambiguous product ideas into clear product requirements, user stories, acceptance criteria, scope boundaries, and delivery plans. Use for feature discovery, MVP definition, stakeholder alignment, backlog refinement, and product change proposals.
license: MIT
---

# Product discovery and specification

## Mission

Translate a problem into a testable product outcome before implementation begins. A good specification explains why the work matters, who it serves, what success looks like, and what the system must and must not do.

## 1. Frame the problem

Start with the user/problem, not a proposed feature. Record:
- Target user/persona and context of use.
- Current pain point, frequency, severity, and workaround.
- Evidence: interviews, support tickets, analytics, operational data, or validated stakeholder input.
- Business objective and user outcome.
- Constraints, dependencies, risks, and non-goals.

Separate observed evidence from stakeholder assumptions. Do not invent metrics or claim demand without evidence.

## 2. Define outcomes and success measures

State the desired outcome in terms of user or business behavior. Select metrics with:
- Baseline and target, when known.
- Measurement source and event definition.
- Time window and segmentation.
- Guardrails such as error rate, support load, latency, accessibility, or abuse.

Avoid vanity metrics and success criteria that reward clicks without verifying user value. Include qualitative evidence when quantitative measurement is unavailable.

## 3. Explore solution options

Generate a small number of plausible solutions, including a simpler non-feature option when appropriate. Compare user value, implementation effort, operational cost, risk, reversibility, dependencies, and time to learn. Identify assumptions that can be tested with a prototype, experiment, or limited release.

Do not prematurely lock the team into a specific UI or technical architecture before the user need is understood.

## 4. Define functional requirements

For each user journey specify:
- Actor and preconditions.
- Trigger and normal flow.
- Data required and ownership.
- Business rules and state transitions.
- Success response and confirmation.
- Validation errors and recovery.
- Permission/role requirements.
- Notifications, audit events, and external side effects.
- Empty, loading, unavailable, and cancellation states.

Use requirement IDs when scope is large. Each requirement should be specific enough to test and trace to an acceptance criterion.

## 5. Define non-functional requirements

Address relevant qualities:
- Performance and latency.
- Availability and recovery.
- Security and privacy.
- Accessibility and localization.
- Scalability and resource constraints.
- Compatibility and supported platforms.
- Observability and support.
- Data retention, export, and deletion.
- Compliance and audit requirements.

Use numeric targets only when there is a source or stakeholder agreement. Mark proposed targets as proposals until accepted.

## 6. Write acceptance criteria

Use clear Given/When/Then statements or equivalent examples. Cover the happy path plus failure, boundary, authorization, concurrency, and recovery cases. Avoid vague terms such as "fast", "easy", "intuitive", or "secure" without measurable or observable meaning.

Acceptance criteria must be externally observable. They should not prescribe internal implementation unless there is a real constraint.

## 7. Set scope and MVP boundaries

Separate:
- Required for the first useful release.
- Important but deferrable.
- Optional enhancement.
- Explicitly out of scope.

An MVP should validate a critical assumption with a complete, safe user journey. It should not be a broken skeleton that omits security, data integrity, accessibility, or basic observability.

Document dependencies and what must be true before each phase can ship.

## 8. Risk and edge-case analysis

Consider abuse, permissions, duplicate actions, invalid state transitions, partial failure, external dependency outages, migration, concurrency, account switching, time zones, localization, and data lifecycle. Identify reversible versus irreversible decisions and assign risk owners.

For experiments, define hypothesis, variant, population, assignment, exposure event, primary metric, guardrails, sample-size considerations, duration, and decision rule.

## 9. Implementation-ready handoff

A useful product brief includes:
1. Problem and user outcome.
2. Target users and journeys.
3. Evidence and assumptions.
4. Goals and non-goals.
5. Functional requirements.
6. Acceptance criteria.
7. Non-functional requirements.
8. Data, roles, and permission behavior.
9. Edge cases and risks.
10. Success measures.
11. Scope, dependencies, rollout, and open decisions.

Link designs, architecture decisions, analytics definitions, and API contracts where they exist. Do not duplicate all technical implementation detail in the product spec.

## 10. Change control

When requirements change, identify affected acceptance criteria, tests, API/data contracts, UX, documentation, estimates, and release plan. Keep a decision log for changes that affect scope or user promises.

## Quality gates

A specification is ready when the problem is understood, outcomes are measurable or explicitly qualitative, the critical journey is end-to-end, acceptance criteria are testable, non-goals are clear, risks are visible, and unresolved decisions have owners.

## Anti-patterns

Avoid solution-first requirements, untestable adjectives, hidden assumptions, scope creep, user stories without acceptance criteria, MVPs that omit safety, invented metrics, and stakeholder sign-off without clarity on unresolved risks.

## Completion report

Summarize the problem, intended outcomes, key requirements, acceptance criteria, out-of-scope items, risks, dependencies, and decisions still needed.
