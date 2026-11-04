---
name: performance-optimization
description: Find and improve measurable application, API, database, or build performance bottlenecks. Use when latency, throughput, memory, bundle size, or resource consumption is a concern.
license: MIT
---

# Performance optimization

## Method
1. Define the user-visible or operational performance objective and the metric: p50/p95/p99 latency, throughput, memory, CPU, database load, bundle size, or startup time.
2. Establish a reproducible baseline using representative data, traffic, hardware, and environment.
3. Profile before changing code. Locate the dominant cost and distinguish CPU, I/O, lock contention, network, database, and rendering work.
4. Form a specific hypothesis and change one major variable at a time.
5. Re-measure using the same workload and tooling. Include variance and confidence limitations.
6. Check correctness, security, maintainability, and cost impacts of the optimization.
7. Add a regression benchmark or alert when the bottleneck is likely to recur.

## Common areas
- Database: query plans, missing/ineffective indexes, N+1 queries, lock waits, connection pools, pagination.
- Backend: repeated serialization, blocking work in async paths, unbounded concurrency, excessive retries, oversized payloads.
- Frontend: bundle size, code splitting, render churn, layout shifts, image dimensions/formats, cache policy.
- Infrastructure: over/under-provisioning, noisy neighbors, network hops, cold starts, inefficient autoscaling.

## Guardrails
- Do not optimize a microbenchmark at the expense of the real workload.
- Do not remove validation, authorization, logging needed for operations, or correctness checks to improve a benchmark.
- Avoid speculative caching; define invalidation and staleness semantics first.
- Do not claim improvement without comparable measurements.

## Report
State baseline, bottleneck evidence, change, before/after measurement, test coverage, and trade-offs.
