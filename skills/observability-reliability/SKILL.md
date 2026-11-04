---
name: observability-reliability
description: Design, instrument, and operate observable software systems using structured logs, metrics, traces, service objectives, alerting, and incident practices. Use for production readiness, diagnosing failures, reliability improvements, and SLO design.
license: MIT
---

# Observability and reliability engineering

## Mission

Make system behavior understandable in production and make reliability measurable from the user's perspective. Observability is not the number of dashboards; it is the ability to answer important operational questions with timely, trustworthy, privacy-safe evidence.

## 1. Start from user journeys and failure impact

Identify critical journeys, dependencies, service boundaries, and failure consequences. Define what users notice: failed actions, delayed processing, stale data, incorrect results, degraded performance, or lost availability.

Prioritize instrumentation by risk and operational value. Do not instrument every internal event before identifying the questions operators need to answer.

## 2. Define service-level indicators and objectives

Choose SLIs that reflect user experience:
- Availability/success rate for valid requests.
- Latency percentiles for important actions.
- Freshness or completion time for asynchronous processing.
- Correctness/data-integrity signals where measurable.
- Durability and recovery metrics for persistent workflows.

Define SLO target, measurement window, eligible traffic, exclusions, and owner. Distinguish SLO from SLA and internal alert thresholds. Use error budgets to balance release velocity and reliability work where the organization uses them.

Avoid averages as the only latency signal. Track p50/p95/p99 and segment by route, operation, region, or dependency only where cardinality remains bounded.

## 3. Structured logging

Logs should answer who/what/where/when/why without exposing secrets:
- Timestamp in a consistent timezone-aware format.
- Severity, service, environment, version, and event name.
- Request, trace, job, and correlation IDs.
- Safe actor/resource identifiers where policy permits.
- Outcome, error code, duration, retry count, and dependency name.

Use stable field names and structured JSON rather than free-form strings for production systems. Redact credentials, tokens, passwords, session cookies, full payment details, and unnecessary personal data. Avoid logging whole request/response bodies by default.

## 4. Metrics

Use counters for events, gauges for current values, and histograms for distributions. Important signals commonly include:
- Request/job rate, errors, latency, and saturation.
- Queue depth, oldest message age, retry/dead-letter rate.
- Database connections, lock waits, slow queries, replication lag.
- Resource utilization, restarts, memory pressure, and capacity.
- External dependency latency and error rate.
- Business outcome metrics such as successful completion or reconciliation failures.

Keep labels low-cardinality. Do not use raw user IDs, emails, arbitrary URL paths, or request IDs as metric labels. Define units and aggregation semantics.

## 5. Distributed tracing

Propagate trace context across inbound requests, services, message queues, jobs, and external calls. Create spans for meaningful operations and record safe attributes, status, and timing. Link asynchronous work to originating traces where supported. Avoid making every internal helper a span.

Trace sampling should retain enough representative and error-focused data without excessive cost or sensitive capture.

## 6. Health checks and readiness

Distinguish:
- Liveness: process can continue running; a failed check may justify restart.
- Readiness: instance can safely receive new work.
- Dependency health: status of external components, surfaced separately unless they are essential to readiness.

Avoid cascading restart loops because an optional dependency is temporarily unavailable. Provide startup probes where initialization is slow. Test what happens when a dependency becomes degraded rather than just healthy.

## 7. Alerting and on-call

Alerts should be actionable, tied to a user-visible symptom or imminent failure, have a clear owner, and include runbook links. Use multi-window or burn-rate approaches for important SLOs where practical. Separate paging incidents from ticket-level warnings. Avoid alert storms from one underlying event.

For every alert define trigger, impact, dashboard, runbook, owner, severity, and escalation path. Review noisy and unused alerts regularly.

## 8. Incident response

During an incident:
1. Establish severity, incident owner/commander, communication channel, and timeline.
2. State user impact and known scope.
3. Stabilize and reduce impact before making speculative changes.
4. Preserve evidence and audit trail.
5. Communicate confirmed facts and uncertainty.
6. Verify recovery with user-facing and technical signals.
7. Record timeline, root cause, contributing factors, detection gaps, and corrective actions.

Avoid blame. Distinguish trigger, root cause, and organizational/systemic contributors. Track corrective work to completion.

## 9. Reliability engineering

Review timeouts, retry budgets, exponential backoff with jitter, circuit breakers, bulkheads, rate limits, backpressure, graceful degradation, and idempotency. Consider correlated failures and the retry amplification that can worsen an outage.

Define dependency failure behavior and user-visible fallback. Avoid retrying non-idempotent operations without deduplication. Test queue redelivery and delayed work. Use load shedding before uncontrolled resource exhaustion.

## 10. Capacity and recovery

Estimate peak traffic, burst, growth, queue backlog, storage growth, and recovery load. Set thresholds before saturation. Define backup, restore, failover, and disaster recovery procedures with RTO/RPO. A backup is not proven until a restore has been tested.

## Required deliverables

Provide critical user journeys, SLIs/SLOs, instrumentation design, dashboard/alert list, runbooks, incident ownership, dependency failure model, and recovery strategy.

## Quality gates

Verify log fields are structured and redacted, metrics have bounded cardinality, trace context propagates, alerts are actionable, health checks have correct semantics, and recovery procedures are tested.

## Anti-patterns

Avoid dashboards without questions, logs with secrets, high-cardinality metrics, alerting on every exception, retry storms, liveness checks coupled to every dependency, untested backups, and reliability claims unsupported by measured objectives.

## Completion report

List instrumentation, SLIs/SLOs, dashboards and alerts, test/incident exercises, privacy considerations, and operational gaps.
