---
name: ai-integration
description: Design, implement, evaluate, and secure LLM-powered features, RAG systems, tool-using agents, and model-provider integrations. Use for model APIs, structured outputs, retrieval, prompt injection defenses, orchestration, evaluation, privacy, and cost control.
license: MIT
---

# AI application and agent engineering

## Mission

Build AI features that are useful, bounded, measurable, secure, and operable. Choose the simplest approach that meets the product requirement. A model call is not a substitute for deterministic application logic, and an agent is not automatically better than a workflow.

## 1. Define the product behavior

Clarify:
- User and job-to-be-done.
- Expected output, accepted error rate, and unacceptable failure modes.
- Whether answers must be grounded in supplied data or current sources.
- Latency, availability, cost, throughput, and context-size budgets.
- Data sensitivity, retention, region, and provider constraints.
- Whether the feature can take actions or only provide information.
- Required human review, auditability, and recovery path.

Define success with representative examples and measurable evaluation criteria before choosing a model.

## 2. Choose the right pattern

Prefer, in order, the least complex viable approach:
1. Deterministic code or standard search when the task is fully specified.
2. A single model call for interpretation, transformation, summarization, or generation.
3. Retrieval-augmented generation when answers need private or changing source material.
4. Tool calling when the model must request bounded application capabilities.
5. A multi-step agent/workflow when the task requires conditional planning, iteration, or stateful orchestration that cannot be expressed cleanly as a deterministic pipeline.

Do not use multi-agent orchestration just to parallelize trivial work. Account for the increased latency, cost, coordination failures, and review burden.

## 3. Model/provider abstraction

Inspect provider APIs, supported models, limits, data policies, pricing, tool semantics, structured-output behavior, streaming, and region availability. Isolate provider-specific request/response formats when portability is a real requirement, but do not hide important capability differences behind a lowest-common-denominator interface.

Implement bounded:
- Connect/read timeouts and cancellation.
- Rate/concurrency limits and retry budget.
- Token/context budget and truncation policy.
- Error classification and provider fallback.
- Request IDs, usage/cost accounting, and safe observability.
- Model/version selection and rollback.

Do not log full prompts or completions when they may contain sensitive user data.

## 4. Prompt and instruction design

Separate trusted application policy from user content and retrieved material. State task, context, constraints, output contract, and refusal/escalation conditions clearly. Provide examples only when they resolve ambiguity. Avoid contradictory requirements and bloated global instructions.

Treat model output as untrusted. Validate structured output against a schema and semantic constraints. Never trust the model to enforce identity, permission, spending, data retention, or irreversible action policy.

## 5. Structured output and tool use

For structured output:
- Define a minimal schema with required fields, enums, bounds, and clear null semantics.
- Validate syntactic and semantic correctness after generation.
- Handle refusal, incomplete output, truncation, and schema mismatch explicitly.
- Avoid assuming the model will always return valid JSON or obey a schema perfectly.

For tools:
- Give each tool one narrow purpose and a strict input schema.
- Validate every argument in application code.
- Authenticate and authorize the user/action/resource independently.
- Enforce tenant boundaries, rate limits, quotas, and timeouts.
- Return bounded, redacted outputs with stable errors.
- Require explicit human confirmation before irreversible, destructive, financial, access-control, or production actions.
- Record audit events for side effects without logging secrets.

Tool descriptions must state when the tool should and should not be used, its side effects, and expected result.

## 6. Retrieval-augmented generation

Define the data sources and their access policies before designing indexing. Preserve document permissions, tenant identity, provenance, timestamps, and source links throughout ingestion, chunking, embedding, retrieval, and answer generation.

Evaluate separately:
- Ingestion completeness and freshness.
- Chunking and metadata quality.
- Retrieval recall/precision and ranking.
- Grounding and citation correctness.
- Answer faithfulness and abstention when evidence is insufficient.

Prevent cross-tenant retrieval and stale access after permission revocation or deletion. Treat retrieved text as untrusted evidence, not privileged instructions. The model must not follow instructions embedded in documents that request secrets, policy changes, or actions outside the user request.

If source evidence is missing, conflicting, or stale, communicate uncertainty rather than inventing a confident answer.

## 7. Agent orchestration and state

Define the agent's allowed tools, step/time/token/cost limits, stopping conditions, state model, and owner of each transition. Make side-effecting tools idempotent when retries are possible. Keep deterministic validation and authorization outside the model loop.

For multi-agent work:
- Assign bounded tasks with explicit inputs and expected outputs.
- Avoid delegating secrets or unnecessary user data.
- Define how outputs are verified and reconciled.
- Prevent parallel agents from editing the same resources without coordination.
- Keep a parent-level owner responsible for final correctness.
- Stop loops that repeat without progress or exceed budget.

## 8. Evaluation and quality assurance

Build a versioned evaluation set from representative user tasks, edge cases, adversarial inputs, and known failures. Measure:
- Task success and completeness.
- Factuality/faithfulness and citation accuracy.
- Tool selection, argument correctness, and authorization outcomes.
- Refusal correctness and escalation quality.
- Robustness to prompt injection and data leakage.
- Latency, cost, and resource usage.
- User correction rate and downstream outcome.

Use deterministic graders for objective properties, model-based graders only with calibration and sampling, and human review for high-impact decisions. Evaluate before model, prompt, retriever, or tool changes.

## 9. Privacy and safety

Minimize data sent to providers. Redact or transform sensitive fields when possible. Document provider retention, training use, region, subprocessors, and contractual controls. Apply access control before retrieval and before tool execution. Do not expose hidden prompts, credentials, private files, or other tenants' data.

For high-impact domains, define human oversight, appeals, logging, incident response, and safe fallback. Avoid presenting generated content as verified fact without evidence.

## 10. Operations and cost

Track provider/model, prompt version, input/output tokens, latency, status, retry, cost estimate, and evaluation version using privacy-safe telemetry. Set per-user and per-feature quotas. Monitor timeouts, refusal spikes, schema failures, empty retrieval, tool errors, and unusual cost growth.

Define fallback behavior for provider outage: cached/known data, deterministic path, reduced capability, or clear unavailability. Do not silently fabricate results during outages.

## Deliverables

Provide architecture/pattern choice, model/provider decision, prompt/output schema, tool permission model, retrieval design (if any), evaluation plan, privacy/security review, budget controls, and operational runbook.

## Anti-patterns

Avoid direct model authority over permissions, arbitrary shell/database tools, unrestricted multi-agent loops, trusting retrieved instructions, unvalidated JSON, logging sensitive prompts, using LLMs for simple deterministic transformations, and claims of guaranteed correctness.

## Supporting reference material

Load these resources when the task needs a reusable template or deeper checklist:
- [ai evaluation plan template](references/ai-evaluation-plan-template.md)
- [rag security checklist](references/rag-security-checklist.md)

The procedure and quality gates in this SKILL.md remain the primary workflow.


## Completion report

State the selected pattern, provider assumptions, tools/permissions, evaluation results, privacy safeguards, cost/latency limits, failure behavior, and known limitations.
