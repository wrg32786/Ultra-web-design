# Evaluation Protocol

Ultra Web Design is labeled **beta** until the runtime skill demonstrates reliable
activation and measurable output improvement across supported agent clients.
Structural validation is necessary but not sufficient.

## What is measured

1. **Trigger precision** — the skill loads for material website work and stays out
   of unrelated or trivial tasks.
2. **Path selection** — tiny fixes remain tiny; substantial redesigns receive the
   full product, preservation, direction, implementation, and QA workflow.
3. **Output quality** — truth, business continuity, visual distinctiveness,
   accessibility, responsive behavior, implementation integrity, and completion.
4. **Cost** — tokens and elapsed time relative to no skill or the previous version.
5. **Consistency** — the same case should not alternate between materially
   different interpretations without new evidence.

## Files

- `evals/evals.json` — six initial output-quality cases with observable assertions.
- `evals/trigger-queries.json` — ten positive and ten near-miss negative activation
  queries.
- `examples/` at the repository root — three rendered visual fixtures covering
  B2B SaaS, local services, and editorial work.

The fixtures prove repository packaging and visual breadth. They do not replace
with-skill versus baseline evaluation.

## Run output evals

For each case, run from a clean context twice:

1. With `skills/ultra-web-design/SKILL.md` installed.
2. Without the skill, or against the previous tagged runtime.

Store results outside the distributable skill directory:

```text
benchmarks/
└── iteration-N/
    ├── <case-id>/
    │   ├── with-skill/
    │   │   ├── outputs/
    │   │   ├── screenshots/
    │   │   ├── timing.json
    │   │   └── grading.json
    │   └── baseline/
    │       ├── outputs/
    │       ├── screenshots/
    │       ├── timing.json
    │       └── grading.json
    └── benchmark.json
```

Record at minimum:

```json
{
  "total_tokens": 0,
  "duration_ms": 0,
  "client": "client and version",
  "model": "model and version",
  "skill_revision": "git SHA"
}
```

Grade every assertion `PASS` or `FAIL` with concrete file, screenshot, or text
evidence. Use deterministic scripts for mechanical checks and blind review for
visual and holistic comparisons.

## Run trigger evals

Run each query at least three times in every supported client. A positive case
passes when its trigger rate is greater than 0.5. A negative case passes when its
trigger rate is less than 0.5.

Do not optimize only against the full query set. Keep a fixed train/validation
split and select the description by validation performance.

## Promotion to production

Change runtime metadata from `beta` to `production` only when all are true:

- Official `skills-ref` validation passes.
- Structural CI passes with a clean generated diff.
- Trigger precision is at least 90% on a held-out validation set in each supported
  client.
- Every required output assertion passes in at least two independent runs per
  case, or accepted failures are documented with a narrower scope boundary.
- Blind review prefers the skill output over baseline on product fit,
  distinctiveness, usability, accessibility, and implementation quality.
- Median token overhead is recorded and judged proportionate to the quality gain.
- At least three real projects complete the workflow without a packaging or
  context-efficiency blocker.

Do not manufacture benchmark values. An empty results directory is more credible
than unverified performance claims.
