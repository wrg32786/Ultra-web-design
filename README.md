# Ultra Web Design

A spec-valid Agent Skill for researching, positioning, designing, building,
auditing, and shipping distinctive business websites.

> **Runtime version:** 2.0.0  
> **Status:** Beta — architecture and structural validation complete; behavioral
> benchmarks are required before promotion to production  
> **Active skill:** [`skills/ultra-web-design/SKILL.md`](skills/ultra-web-design/SKILL.md)  
> **Complete corpus:** [`skills/ultra-web-design/MANIFEST.md`](skills/ultra-web-design/MANIFEST.md)

Ultra Web Design turns product truth, audience context, brand evidence, visual
references, implementation constraints, accessibility, performance, and business
goals into one coherent website system. It is broader than a style guide and more
operational than a prompt collection.

## The v2 architecture

Version 2 separates the two jobs the original repository tried to make one file do:

1. **`SKILL.md` is the lean runtime router.** It contains the authority hierarchy,
   task-size classifier, always-active safeguards, module-loading rules, operating
   loop, and release gates. It remains below the Agent Skills progressive-
   disclosure target so the agent retains context for the actual brief and codebase.
2. **`MANIFEST.md` is the complete reference corpus.** It preserves the full
   source synthesis, detailed doctrine, templates, audit system, standards, and
   provenance without loading all 200 KB on every activation.

The runtime file is authoritative during execution. The manifest is the detailed
reference loaded only when the task requires it.

## What it covers

- Business strategy, offer clarity, message hierarchy, proof, objections, and
  conversion architecture.
- Brand authority, visual-world synthesis, composition, typography, color,
  material, imagery, iconography, and data display.
- Landing pages, company sites, SaaS, ecommerce, services, media, communities,
  portfolios, courses, events, nonprofits, and public-service websites.
- Responsive recomposition, interaction states, forms, motion, GSAP,
  accessibility, performance, SEO, security, privacy, analytics, CMS operations,
  localization, and RTL.
- Existing-site audits and redesigns that preserve routes, forms, analytics,
  proof, legal language, and working business infrastructure.
- Anti-generic release review without imposing one rigid house style.

It is **not** a component library, a theme, a fixed stack, or a requirement that
every site use the same visual tricks.

## Install

### Agent Skills CLI

```bash
npx skills add https://github.com/wrg32786/Ultra-web-design --skill ultra-web-design
```

### Manual installation

Copy the complete skill directory into the skill location supported by the agent:

```text
skills/ultra-web-design/
```

The portable unit includes the runtime `SKILL.md`, modules, templates, complete
manifest, and evaluation definitions.

### Direct use

```text
Use skills/ultra-web-design/SKILL.md for this website task. Classify the task
before loading references, read the real repository and product truth, use only
the modules the task requires, and verify rendered output before shipping.
```

## Operating principle

The governing loop for substantial website work is:

> **Read → Shape → Inspire → Synthesize → Produce → Build → Taste → Resolve → See → Polish**

Tiny changes take a shorter path. A one-line state defect should not trigger a
full identity exercise. A full redesign should not skip product truth,
preservation inventory, or rendered QA.

## Core safeguards

- The brief and verified product truth outrank model taste.
- Safety, security, data integrity, law, and accessibility are not aesthetic
  preferences.
- Existing working routes, forms, analytics, SEO, proof, legal copy, and brand
  assets are preserved unless an approved decision changes them.
- No testimonials, metrics, customers, prices, ratings, awards, capabilities, or
  affiliations are invented to complete a composition.
- Native platform behavior, standard libraries, existing project patterns, and
  installed dependencies are preferred before new abstractions or packages.
- Distinctiveness comes from product-specific truth, one coherent visual world,
  signature and restraint systems, and category-rut refusal—not novelty for its
  own sake.
- Numeric jury scores are advisory review structure until behavioral calibration
  exists. Hard defects and evidence determine release.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
├── examples/
│   ├── precision-saas/
│   ├── local-service/
│   └── editorial/
├── skills/
│   ├── llms.txt
│   └── ultra-web-design/
│       ├── SKILL.md               # lean runtime authority
│       ├── MANIFEST.md            # generated complete corpus
│       ├── MANIFEST.header.md
│       ├── EVALUATION.md
│       ├── evals/
│       │   ├── evals.json
│       │   └── trigger-queries.json
│       ├── modules/
│       │   ├── 00-core.md
│       │   └── 01…09 ordered modules
│       └── templates/
│           ├── PRODUCT.md
│           ├── DIRECTION-CARD.md
│           ├── SURFACE-BRIEF.md
│           ├── DESIGN.md
│           ├── CONTENT-MATRIX.md
│           ├── MOTION-PLAN.md
│           ├── DECISIONS.md
│           ├── QA-REPORT.md
│           ├── REFERENCE-COMP-BIBLE.md
│           ├── BLOCK-RECORD.md
│           ├── manifest.json
│           └── tokens.css
└── scripts/
    ├── build_manifest.py
    ├── sync_templates.py
    └── validate.py
```

## Source-of-truth rules

- `SKILL.md` is the runtime execution authority and is edited directly.
- `modules/` is the editable source for the complete reference corpus.
- `MANIFEST.md` is generated by `scripts/build_manifest.py`; do not hand-edit it.
- `modules/08-templates.md` is the template source of truth.
- `templates/` is generated by `scripts/sync_templates.py`; do not allow it to
  drift from module 08.
- `NOTICE.md` and the manifest provenance sections retain exact upstream snapshots
  and license notes.

## Templates

Use the smallest set the project needs:

- `PRODUCT.md` — business and evidence source of truth.
- `SURFACE-BRIEF.md` — route-level job, content, states, context, and analytics.
- `DESIGN.md` — executable visual and interaction contract.
- `CONTENT-MATRIX.md` — production content and proof ledger.
- `MOTION-PLAN.md` — motion purpose, ownership, reduced motion, and validation.
- `QA-REPORT.md` — design critique, technical audit, findings, and release status.
- `REFERENCE-COMP-BIBLE.md` — image-first direction and extraction contract.

Delete unused fields instead of preserving empty process theater.

## Validation

Run the repository checks:

```bash
python scripts/build_manifest.py
python scripts/sync_templates.py --check
python scripts/validate.py
skills-ref validate skills/ultra-web-design
```

The checks verify:

- Official Agent Skills frontmatter constraints.
- Runtime progressive-disclosure size and module routing.
- Exact manifest generation from the ordered modules.
- Complete numbered corpus and pinned source provenance.
- Exact template synchronization.
- Output and trigger eval definitions.
- Three responsive visual fixtures with rendered desktop/mobile evidence.
- Removal of deprecated monolithic-skill build paths.

GitHub Actions performs the same checks and fails when generated files differ from
the committed tree. CI does not repair or push repository state.

## Evaluation

Structural validity does not prove that a skill improves output. The repository
therefore includes:

- Six realistic output-quality cases covering a tiny fix, route extension,
  preserve-mode redesign, greenfield SaaS, editorial work, and audit-only work.
- Twenty trigger queries split between material website tasks and near-miss
  negatives.
- A documented with-skill versus baseline protocol, assertion grading, timing and
  token recording, blind visual comparison, and production-promotion criteria.

See [`EVALUATION.md`](skills/ultra-web-design/EVALUATION.md).

No benchmark number is claimed until the corresponding run artifacts exist.

## Visual fixtures

The repository includes three dependency-free responsive HTML fixtures plus a
reviewed desktop/mobile evidence contact sheet:

- **Precision SaaS** — product mechanism as proof, annotated operational detail,
  and no invented social proof.
- **Local service** — a field-guide world shaped by geography, site assessment,
  and service decisions rather than SaaS conventions.
- **Editorial** — reading-first hierarchy, issue archive, sponsor disclosure, and
  membership after value.

They demonstrate visual breadth, not conversion performance or customer work. See
[`examples/README.md`](examples/README.md).

## Source synthesis

The complete manifest reconciles seven repositories at exact snapshots:

| Source | Primary contribution |
|---|---|
| `pbakaus/impeccable` | Product/design authority, visual-world creation, craft floor, critique, hardening, responsive adaptation |
| `nextlevelbuilder/ui-ux-pro-max-skill` | Searchable design intelligence, catalogs, stack guidance, recommendation provenance |
| `emilkowalski/skills` | Motion purpose, timing, easing, interaction vocabulary, prototyping, animation critique |
| `greensock/gsap-skills` | Official GSAP implementation, timelines, ScrollTrigger, lifecycle cleanup, framework integration |
| `VoltAgent/awesome-design-md` | Comparative grammar distilled from distinct design systems |
| `nexu-io/open-design` | Modular skill architecture, portable design-system packages, artifacts, handoff, provenance, bounded critique |
| `Leonxlnx/taste-skill` | Brief inference, expression dials, anti-habit controls, image-first art direction, redesign preservation, completeness |

Exact commits, license notes, retained knowledge, rejected overfit rules, and
conflict resolution live in `NOTICE.md` and Sections 40–42 of the manifest.

## Updating the corpus

A source update is accepted only when it changes a website-design or implementation
decision. Record:

1. Exact upstream commit.
2. Applicable license.
3. Canonical files inspected.
4. Concrete contribution.
5. Conflict with current doctrine.
6. Material integrated, reconciled, or rejected.
7. Updated runtime behavior, version, and changelog when applicable.

Do not paste an upstream skill wholesale. Preserve the authority hierarchy and
resolve contradictions once.

## Status policy

The runtime remains `beta` until the criteria in `EVALUATION.md` pass across the
supported clients and at least three real projects. This is deliberate: the
repository applies the same evidence standard to its own maturity claims that it
requires for website claims.

## License

Apache License 2.0. See [`NOTICE.md`](NOTICE.md) for upstream provenance and
third-party license notes.
