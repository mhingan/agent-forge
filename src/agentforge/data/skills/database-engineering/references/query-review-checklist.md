# SQL and ORM query review

## Correctness
- [ ] Query filters enforce tenant and authorization scope.
- [ ] NULL and missing-value semantics are intentional.
- [ ] Ordering is deterministic, including tie-breakers.
- [ ] Pagination has a stable cursor/key.
- [ ] Timezone, date boundaries, currency, and decimal precision are explicit.
- [ ] Writes are protected by constraints/transactions under concurrency.

## Performance
- [ ] Only required columns are selected.
- [ ] Result size is bounded.
- [ ] N+1 queries and accidental Cartesian products are absent.
- [ ] Query plan was inspected on representative data when performance matters.
- [ ] Index supports actual filtering/join/order pattern and selectivity.
- [ ] Index write/storage cost has been considered.
- [ ] Connection use and transaction duration are bounded.

## Security
- [ ] Values are parameterized.
- [ ] Dynamic identifiers are allowlisted.
- [ ] No raw exception/SQL details are exposed.
- [ ] Sensitive data is not logged unnecessarily.
- [ ] Database role follows least privilege.

## Operations
- [ ] Timeout and cancellation behavior are defined.
- [ ] Lock contention and deadlock behavior are understood.
- [ ] Query is observable without high-cardinality labels.
- [ ] Migration/backfill effects are documented.
