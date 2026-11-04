---
name: architecture
description: Design and evaluate software architecture for new systems, major changes, and technical-debt decisions. Use when choosing boundaries, components, dependencies, deployment topology, or migration strategies.
license: MIT
---

# Architecture design

## Objective
Produce an architecture that satisfies the actual requirements while minimizing unnecessary complexity and preserving operational safety.

## Procedure
1. **Clarify constraints.** Identify user goals, functional requirements, quality attributes, scale, latency, availability, privacy, compliance, team skills, budget, and delivery constraints. Mark unknowns explicitly.
2. **Inspect before proposing.** For an existing system, map the current entry points, modules, data stores, queues, integrations, deployment units, and test boundaries. Do not infer architecture from directory names alone.
3. **Define boundaries.** Identify domain responsibilities, ownership of data, stable interfaces, trust boundaries, and synchronous versus asynchronous interactions.
4. **Compare options.** Present at least one viable simpler alternative when recommending a distributed or framework-heavy design. Evaluate operational complexity, failure modes, cost, reversibility, and team familiarity.
5. **Model failure.** Consider timeouts, retries, idempotency, partial failure, duplicate events, dependency outages, data consistency, and recovery.
6. **Plan migration.** For existing systems, propose incremental steps, compatibility windows, rollback points, observability, and data migration strategy.
7. **Record decisions.** Write an Architecture Decision Record (ADR) for decisions with meaningful long-term impact.

## Required output
- Context and constraints
- Proposed design with component responsibilities
- Data ownership and key flows
- Alternatives considered and trade-offs
- Security and failure analysis
- Deployment and observability implications
- Incremental implementation plan and acceptance criteria

## Guardrails
- Do not introduce microservices, event buses, caches, or abstractions without a demonstrated need.
- Keep secrets out of diagrams, examples, and configuration.
- Distinguish facts observed in the repository from assumptions and recommendations.
- Ask before changing public APIs, persistence contracts, or deployment topology.
