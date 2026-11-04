# RAG quality and security checklist

## Ingestion
- [ ] Every source has an owner, classification, timestamp, and stable provenance.
- [ ] Parsing preserves relevant structure, tables, code, and metadata.
- [ ] Schema and file size are validated.
- [ ] Secrets and prohibited data are filtered or access-controlled.
- [ ] Deletion and permission changes propagate to indexes/caches.

## Retrieval
- [ ] Retrieval applies the caller's authorization and tenant scope before returning context.
- [ ] Chunking and metadata reflect the source and query patterns.
- [ ] Retrieval recall/precision is evaluated separately from generation.
- [ ] Freshness, duplicate, conflicting, and stale documents are handled.
- [ ] Retrieved references can be traced to exact source sections.

## Generation
- [ ] Retrieved text is clearly treated as untrusted evidence.
- [ ] Retrieved instructions cannot override system/developer policy.
- [ ] Answers cite evidence for factual claims.
- [ ] The model abstains or states uncertainty when evidence is missing.
- [ ] Citation links resolve to the correct allowed source.

## Evaluation and operations
- [ ] Cross-tenant leakage cases are tested.
- [ ] Prompt injection and data exfiltration attempts are evaluated.
- [ ] Retrieval quality and answer faithfulness metrics exist.
- [ ] Provider retention and privacy behavior are documented.
- [ ] Token/cost/latency limits and outage fallback are defined.
