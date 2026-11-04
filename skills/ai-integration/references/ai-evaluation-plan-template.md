# AI feature evaluation plan

## Feature and version
- Product behavior:
- Model/provider/version:
- Prompt/system instruction version:
- Tool/retriever version:
- Evaluator owner:

## Success definition
- User task success:
- Acceptable error/failure behavior:
- Unacceptable outputs/actions:
- Latency budget:
- Cost/token budget:
- Privacy constraints:

## Evaluation dataset
For each case record user intent, context, source evidence, expected behavior, acceptable variants, unsafe outcomes, and category (normal, edge, adversarial, regression).

## Metrics
| Metric | Definition | Grader/source | Threshold | Guardrail |
|---|---|---|---|---|
| Task success | | | | |
| Factuality/grounding | | | | |
| Citation correctness | | | | |
| Tool selection/arguments | | | | |
| Authorization outcome | | | | |
| Refusal/escalation | | | | |
| Prompt-injection resistance | | | | |
| Latency/cost | | | | |

## Method
- Deterministic checks:
- Human review sample:
- Model-based grader calibration:
- Test environment:
- Sampling/seed:

## Release decision
Compare baseline and candidate. State regressions, confidence, known limitations, rollback criteria, and required human approval.
