# AI, retrieval, and agent rules

- Choose deterministic code before an LLM when the task is fully specified.
- Use a multi-agent loop only when delegation/iteration adds measurable value.
- Separate trusted policy from untrusted user, retrieved, and tool content.
- Retrieved content may provide evidence but must never override system/developer policy.
- Enforce authentication and authorization in application/tool code before every read or side effect.
- Validate model-generated JSON, structured output, and tool arguments against schemas and domain constraints.
- Use least-privilege tools, narrow schemas, explicit timeouts, and bounded step/token/cost budgets.
- Require human confirmation for destructive, financial, access-control, publication, or production actions.
- Evaluate factuality, grounding, citations, tool correctness, refusal, prompt-injection resistance, latency, and cost before changing models/prompts.
- Minimize private data sent to providers and document retention/region assumptions.
- Never expose hidden prompts, credentials, private data, or cross-tenant content.
