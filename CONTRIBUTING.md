# Contributing

Ultra Web Design accepts corrections, stronger synthesis, verified standards
updates, useful templates, evaluation improvements, and upstream knowledge that
changes real website decisions.

## Good contributions

- Correct an inaccurate or stale implementation rule.
- Resolve a contradiction between runtime and reference modules.
- Reduce active context without removing necessary behavior.
- Add or improve a realistic trigger or output eval.
- Add a missing accessibility, performance, content, business, or operational
  requirement.
- Improve a template so it produces a more executable artifact.
- Integrate a source at an exact commit with clear provenance and license review.
- Replace a rigid aesthetic rule with a better contextual decision rule.

## Not useful

- Large lists of fashionable effects without selection logic.
- A style preset that duplicates an existing preset under another name.
- Inspiration dumps without provenance and extracted design knowledge.
- Framework migrations, dependencies, or scaffolding unrelated to the skill.
- Claims that a technique is “premium” without fit, restraint, and failure modes.
- Benchmark claims without retained run artifacts.
- More always-loaded prose when an on-demand reference solves the problem.

## Change process

1. Edit the smallest authoritative source:
   - runtime behavior: `skills/ultra-web-design/SKILL.md`;
   - detailed doctrine: the relevant ordered module;
   - templates: `modules/08-templates.md`;
   - activation/output behavior: `evals/`.
2. Regenerate the full manifest when modules change:

   ```bash
   python scripts/build_manifest.py
   ```

3. Regenerate templates when module 08 changes:

   ```bash
   python scripts/sync_templates.py
   ```

4. Update `CHANGELOG.md` for user-visible behavior changes.
5. Update snapshots, ingestion reports, and `NOTICE.md` for upstream changes.
6. Run all validation commands.
7. Submit a focused pull request explaining the problem, decision change,
   evidence, and eval impact.

## Pull-request checklist

- [ ] The change has one clear purpose.
- [ ] The runtime remains under 500 lines.
- [ ] No unsupported top-level Agent Skills metadata was added.
- [ ] No conflicting duplicate rule was added.
- [ ] Contextual guidance remains contextual.
- [ ] Provenance and licenses are recorded where applicable.
- [ ] Generated manifest and templates are synchronized.
- [ ] Relevant evals were added, updated, or explicitly shown to remain sufficient.
- [ ] No benchmark or maturity claim exceeds retained evidence.
- [ ] Validation passes with a clean generated diff.
