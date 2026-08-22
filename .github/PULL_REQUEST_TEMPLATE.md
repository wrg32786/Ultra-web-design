## Problem

<!-- What concrete execution, design, provenance, or maintenance problem does this solve? -->

## Decision change

<!-- State the smallest authoritative rule or implementation change. -->

## Evidence

<!-- Source, standard, failing case, screenshot, benchmark, or reproduction. -->

## Evaluation impact

<!-- Eval added/updated, or why existing cases already cover the change. -->

## Checks

- [ ] `python scripts/build_manifest.py`
- [ ] `python scripts/sync_templates.py --check`
- [ ] `python scripts/validate.py`
- [ ] `skills-ref validate skills/ultra-web-design`
- [ ] Generated diff is clean
- [ ] Changelog updated for user-visible behavior
