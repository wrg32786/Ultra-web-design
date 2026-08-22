# Contributing

Ultra Web Design accepts corrections, stronger synthesis, verified standards updates, useful templates, and upstream knowledge that changes real website decisions.

## Good contributions

- Correct an inaccurate or stale implementation rule
- Resolve a contradiction between modules
- Add a missing accessibility, performance, content, business, or operational requirement
- Improve a template so it produces a more executable artifact
- Integrate a source at an exact commit with clear provenance and license review
- Replace a rigid aesthetic rule with a better contextual decision rule

## Not useful

- Large lists of fashionable visual effects without selection logic
- A new style preset that duplicates an existing preset under a different name
- Generated screenshots or inspiration dumps without provenance and extracted design knowledge
- Framework migrations, dependencies, or scaffolding unrelated to the skill
- Claims that a technique is “premium” without explaining fit, restraint, and failure modes

## Change process

1. Edit the relevant ordered module under `skills/ultra-web-design/modules/`.
2. Update any extracted template affected by the change.
3. Update `CHANGELOG.md` for behavior changes.
4. Update source snapshots, ingestion reports, and `NOTICE.md` when upstream material changes.
5. Run `python scripts/build_skill.py` and `python scripts/validate.py`.
6. Submit a focused pull request explaining the problem, the decision change, and the evidence.

## Pull-request checklist

- [ ] The change has one clear purpose.
- [ ] No conflicting duplicate rule was added.
- [ ] Contextual guidance remains contextual.
- [ ] Provenance and licenses are recorded where applicable.
- [ ] Templates remain synchronized.
- [ ] Validation passes.
