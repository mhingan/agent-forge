---
name: ai-integration
description: Integrate LLMs, model APIs, retrieval systems, and AI agents into applications with reliable evaluation, privacy, and safety controls. Use for chat, RAG, tool calling, orchestration, and model-provider abstractions.
license: MIT
---

# AI integration engineering

## Architecture procedure
1. Define the user task, success criteria, unacceptable outcomes, latency/cost budget, data sensitivity, and human oversight requirements.
2. Identify the simplest suitable pattern: deterministic code, single model call, retrieval-augmented generation, tool use, or multi-agent orchestration. Do not add agents by default.
3. Define the trust boundaries between system instructions, developer instructions, user content, retrieved documents, tool results, and model output.
4. Choose provider interfaces and model capabilities deliberately. Isolate provider-specific request/response formats behind a small adapter where portability is needed.
5. Define timeouts, rate limits, token budgets, retries, fallbacks, cancellation, and idempotency for tools.
6. Validate structured outputs against schemas. Treat model output as untrusted until validated.
7. Apply authorization in application code before every tool/data access; do not rely on the model to enforce permissions.
8. Design prompt-injection defenses for retrieved content and tool results. Clearly mark untrusted text and prevent it from changing policy or permissions.
9. Minimize data sent to providers, redact secrets/PII where practical, and document retention/region settings.
10. Build evaluations using representative cases, adversarial examples, regression sets, and human review for high-impact outcomes.

## RAG checklist
- Source provenance and access controls are preserved through retrieval.
- Chunking and metadata support the actual question types.
- Retrieval quality is measured separately from answer quality.
- Citations resolve to the correct source passages.
- Retrieved content cannot issue privileged instructions.
- Stale, conflicting, or missing evidence is communicated accurately.

## Agent/tool checklist
- Tools have narrow schemas and least privilege.
- Every tool validates caller identity and inputs independently.
- Destructive actions require explicit user confirmation.
- Tool outputs are bounded, redacted, and treated as untrusted data.
- Runaway loops are limited by step/time/cost budgets.
- Audit logs record actions without leaking secrets.

## Evaluation
Measure task success, factuality, citation accuracy, refusal quality, tool-call correctness, latency, cost, and robustness to prompt injection. Evaluate across model versions before switching defaults.

## Guardrails
Do not claim deterministic behavior from a probabilistic model. Do not expose hidden prompts or secrets. Do not give the model direct database or shell access when a narrow application tool can enforce authorization and validation.
