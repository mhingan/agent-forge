---
name: performance-optimization
description: Measure, diagnose, and improve application, API, database, frontend, build, and infrastructure performance. Use when latency, throughput, memory, CPU, bundle size, startup time, or operating cost is a material concern.
license: MIT
---

# Performance engineering and optimization

## Mission

Improve a measurable user or operational outcome without sacrificing correctness, security, reliability, or maintainability. Performance work begins with a baseline and ends with comparable evidence.

## 1. Define the objective

Translate vague requests such as "make it faster" into a measurable target:
- User experience: page load, interaction latency, route transition, input responsiveness.
- API/service: p50, p95, p99 latency, throughput, error rate, concurrency, queue age.
- Database: query latency, rows scanned, lock wait, cache hit ratio, connection use.
- Runtime: CPU, memory, allocations, garbage collection, startup/cold-start time.
- Delivery: build duration, test duration, bundle size, deployment duration.
- Cost: cost per request/job, idle capacity, storage growth, egress.

Identify the affected user journey and the performance budget. Do not optimize a metric that does not correspond to the problem.

## 2. Establish a valid baseline

Record environment, hardware/runtime, version, configuration, dataset, workload shape, warm/cold state, concurrency, and measurement duration. Use representative data and realistic request patterns. Run enough samples to distinguish signal from noise. Report percentiles and variance rather than relying only on averages.

Separate local microbenchmarks from end-to-end production behavior. Do not compare results measured under materially different conditions.

## 3. Profile before changing code

Find the dominant cost with tools appropriate to the layer:
- CPU profiles, flame graphs, allocation profiles, and event-loop monitoring.
- Distributed traces, dependency timings, network waterfall, and queue metrics.
- Database query plans, lock monitoring, slow-query logs, and buffer statistics.
- Browser performance traces, rendering profiles, layout-shift metrics, and bundle analysis.
- Build profiles and test-suite timing by test group.

Identify whether the bottleneck is CPU, I/O, network, database, lock contention, rendering, memory pressure, cold start, or external dependency. Follow the critical path rather than optimizing the loudest component.

## 4. Form one testable hypothesis

State the measured bottleneck, suspected cause, expected improvement, correctness risk, and how to prove or disprove the hypothesis. Change one major variable at a time. Preserve a rollback point.

## 5. Common optimization areas

### Application and algorithms
Choose data structures and algorithms that fit input size and access patterns. Avoid repeated parsing/serialization, unnecessary copying, repeated expensive computation, unbounded recursion, and accidental quadratic behavior. Batch only when it reduces overhead without increasing latency or memory beyond the budget.

### Database
Inspect query plans and access patterns. Address N+1 queries, poor selectivity, unnecessary columns, missing/incorrect indexes, large sorts, lock contention, connection pool pressure, and inefficient pagination. Account for write amplification and index maintenance.

### Network and APIs
Reduce unnecessary round trips, use appropriate connection reuse, compress large payloads where it helps, set timeouts, and avoid duplicate calls. Use caching only with explicit freshness, invalidation, and privacy semantics. Bound retries and concurrency.

### Frontend
Measure JavaScript execution, rendering, network, font/image loading, and layout stability. Use route-level code splitting, responsive images, caching, list virtualization, and smaller dependency surface when evidence supports them. Avoid speculative memoization and excessive client-side hydration.

### Infrastructure
Right-size resources based on CPU/memory profiles and saturation. Validate autoscaling lag, cold starts, noisy neighbors, network egress, disk I/O, and regional placement. Scale the actual bottleneck; adding replicas does not fix a single hot database row or serialized lock.

## 6. Caching decisions

Before adding a cache, define:
- Cache key and scope, including tenant/user boundaries.
- Source of truth and invalidation trigger.
- TTL, stale-while-revalidate behavior, and acceptable staleness.
- Negative caching, stampede protection, and memory limits.
- Behavior during cache outage or partial inconsistency.
- Whether cached data is sensitive or permission-dependent.

Do not cache authorization decisions or private data across users without a carefully defined isolation key and invalidation model.

## 7. Capacity and load testing

Model arrival rate, concurrency, request mix, burst behavior, queue depth, and downstream capacity. Test expected peak and a controlled overload. Verify backpressure, rate limiting, graceful degradation, and recovery after load. Avoid running load tests against production without explicit authorization and a defined safe envelope.

## 8. Verify the change

Repeat the same baseline workload and environment. Compare the target metric and guardrail metrics. Confirm functional equivalence, data correctness, error rate, resource use, and tail latency. A faster average with worse p99 or higher failure rate is not necessarily an improvement.

Add a benchmark, regression test, or alert if the bottleneck is likely to return.

## Required report

- Goal and performance budget.
- Baseline and environment.
- Profile evidence and identified bottleneck.
- Hypothesis and change.
- Before/after measurements with comparable conditions.
- Correctness/security/reliability checks.
- Trade-offs, residual bottlenecks, and follow-up work.

## Anti-patterns

Do not optimize before measuring, trust one benchmark run, remove validation/security for speed, add speculative caches, overuse memoization, parallelize unbounded work, or claim improvement without comparable evidence.

## Completion report

State the measured result and confidence, tests run, non-performance regressions checked, and remaining constraints.
