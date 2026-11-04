---
name: architecture
description: Design or review software architecture for new systems, major refactors, service boundaries, data ownership, technology choices, and migration plans. Use this skill when the task involves structural decisions or meaningful long-term technical trade-offs.
license: MIT
---

# Software architecture

## Mission

Produce an architecture that satisfies the actual business and quality requirements with the least complexity that can reasonably meet them. Optimize for understandable ownership, reliable change, security, operability, and reversible decisions—not novelty or diagram count.

## When to activate

Use this skill for:
- New applications, platforms, services, or major capabilities.
- Choosing between a modular monolith, services, serverless functions, queues, or event-driven components.
- Defining domain boundaries, ownership, integration contracts, or data architecture.
- Replacing a framework, database, hosting model, or major infrastructure component.
- Planning a high-risk refactor, migration, scaling change, or reliability improvement.
- Reviewing whether an existing architecture still fits current requirements.

Do not use it for a small isolated code change with no meaningful architectural consequence. In that case, follow local conventions and keep the implementation focused.

## Required inputs

Establish, or explicitly mark as unknown:
- Business outcome, users, primary workflows, and acceptance criteria.
- Functional scope and explicit non-goals.
- Scale assumptions: users, requests, data volume, growth, concurrency, and geographic distribution.
- Quality attributes: availability, latency, throughput, consistency, durability, privacy, accessibility, and recovery objectives.
- Security, regulatory, tenancy, data residency, and audit requirements.
- Team size, skills, ownership boundaries, delivery timeline, budget, and operational maturity.
- Existing systems, integrations, deployment constraints, and migration dependencies.

Never convert an unverified assumption into a stated requirement. Use ranges and scenarios when exact measurements are not available.

## Architecture workflow

### 1. Understand the system before proposing a solution

For an existing repository, inspect entry points, dependency manifests, deployment files, configuration, database schemas, routes, background workers, integrations, tests, and observability. Trace at least one representative request and one important state-changing workflow end to end.

Create a concise current-state map:
- Runtime components and their responsibilities.
- Data stores and the authoritative owner of each important entity.
- Synchronous calls, asynchronous messages, scheduled work, and external dependencies.
- Trust boundaries, identities, secrets, and authorization checks.
- Deployment units, environments, failure domains, and operational owners.

Record what is confirmed from source code separately from what is inferred.

### 2. Model the domain and boundaries

Identify business capabilities, actors, core entities, invariants, lifecycle transitions, and language used by domain experts. Assign each important piece of data one authoritative owner. Define which component may create, mutate, and publish it.

Prefer cohesive modules with explicit interfaces. Keep business rules close to the domain they govern. Avoid splitting modules merely because they are large; split when ownership, change cadence, security boundary, deployment needs, or scaling needs justify it.

### 3. Select the simplest viable topology

Compare realistic choices:
- **Modular monolith:** default starting point for a small or medium product when independent deployment is not yet required.
- **Separate services:** justified by independent ownership, scaling, security isolation, release cadence, or fault-containment requirements.
- **Serverless functions:** useful for event-driven or bursty workloads when cold-start, execution, networking, and platform constraints are understood.
- **Queues and workers:** useful for long-running, retryable, burst-buffered, or decoupled work.
- **Event-driven integration:** useful when multiple consumers need durable facts about state changes; requires ownership, schema evolution, replay, and idempotency discipline.

For every proposed component, state the problem it solves and the operational cost it introduces. Include a simpler alternative and explain why it is insufficient.

### 4. Design data and consistency

Define:
- System of record and ownership for each entity.
- Transaction boundaries and invariants that must hold atomically.
- Strong versus eventual consistency requirements.
- Read models, caching, search indexes, and derived data.
- Retention, deletion, backup, restore, export, and audit requirements.
- Migration and backfill approach, including mixed-version compatibility.

Avoid dual-writing to two authoritative systems without a deliberate consistency protocol. If using asynchronous events, define delivery semantics, idempotency keys, ordering requirements, dead-letter handling, replay, and schema compatibility.

### 5. Design for failure and operations

For each critical dependency, decide timeout, retry, backoff, circuit breaking, concurrency limit, fallback, and user-visible error behavior. Distinguish transient failures from permanent validation or authorization failures. Define health signals, structured logs, metrics, tracing, alert ownership, recovery procedures, and rollback conditions.

Set explicit objectives where relevant: availability target, latency percentile, recovery time objective, recovery point objective, and maximum acceptable data loss. Do not claim high availability without identifying redundant components and failure modes.

### 6. Design security and privacy into boundaries

Map principals, roles, resources, operations, and trust zones. Enforce authorization at the server or service boundary, not only in UI or prompts. Apply least privilege, secret isolation, encryption in transit and at rest, data minimization, auditability, and safe handling of untrusted input. Consider tenant isolation, SSRF, injection, and supply-chain risks.

### 7. Plan incremental delivery

Break the architecture into deployable steps. Identify compatibility windows, feature flags, data migration, dual-read/write risks, observability gates, rollback/forward-fix, and ownership. Prefer reversible decisions and expand/contract migrations. State which decision must be made now and which can be deferred until evidence exists.

## Required deliverables

For material architecture work, provide:
1. Context, requirements, constraints, assumptions, and non-goals.
2. Current-state description, when applicable.
3. Proposed architecture and component responsibilities.
4. Data ownership, important flows, and consistency model.
5. Security boundaries and principal risks.
6. Failure modes, observability, and operations model.
7. Alternatives considered with concrete trade-offs.
8. Incremental implementation and migration plan.
9. Acceptance criteria and open decisions.

Use diagrams only when they clarify a relationship or sequence. A component diagram should label responsibility and protocol; a sequence diagram should show important calls, asynchronous boundaries, and failure responses. Keep diagrams synchronized with the text.

## Decision record standard

Create an Architecture Decision Record for decisions with meaningful future impact. Include:
- Title, date, status, decision owner.
- Context and forces.
- Decision and alternatives rejected.
- Positive and negative consequences.
- Security, reliability, cost, and operational implications.
- Revisit trigger or evidence that would justify changing it.

## Quality gates

Before finalizing, verify that:
- Every component has a clear owner and purpose.
- Data has an authoritative owner and a migration path.
- Interfaces define errors, timeouts, and compatibility.
- Failure and recovery behavior is explicit.
- Security is enforced at actual trust boundaries.
- Operational burden is understood by the team.
- The proposed design is no more complex than the requirements demand.

## Anti-patterns

Do not introduce microservices, Kubernetes, Kafka, Redis, GraphQL, a service mesh, or a new ORM merely because they are popular. Do not equate horizontal scaling with reliability. Do not add caches without invalidation semantics. Do not create an abstraction before there are multiple real use cases. Do not hide unknown requirements behind precise-looking diagrams.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [architecture decision record](references/architecture-decision-record.md)
- [architecture review checklist](references/architecture-review-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

State the chosen design, why it fits, alternatives rejected, files or decisions changed, validation performed, migration implications, and unresolved risks. Clearly distinguish an implemented architecture from a proposal.
