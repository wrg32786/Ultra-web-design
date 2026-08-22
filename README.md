# Ultra Web Design

A production-grade Agent Skill for researching, positioning, designing, building, auditing, and shipping distinctive business websites.

Ultra Web Design turns product truth, audience context, brand evidence, visual references, implementation constraints, accessibility, performance, and business goals into one coherent website system. It is intentionally broader than a style guide and stricter than a prompt collection.

> **Version:** 1.1.0  
> **Status:** Production  
> **Canonical skill:** [`skills/ultra-web-design/SKILL.md`](skills/ultra-web-design/SKILL.md)

## What it is

Ultra Web Design is a modular operating system for website work. Its governing loop is:

> **Read → Shape → Inspire → Synthesize → Produce → Build → Taste → Resolve → See → Polish**

It covers:

- Business strategy, offer clarity, message hierarchy, proof, objections, and conversion architecture
- Brand authority, visual-world synthesis, composition, typography, color, material, imagery, and iconography
- Landing pages, company sites, SaaS, ecommerce, services, media, communities, portfolios, courses, events, nonprofits, and public-service websites
- Responsive recomposition, interaction states, forms, motion, GSAP, accessibility, performance, SEO, security, privacy, analytics, CMS operations, localization, and RTL
- Existing-site audits and redesigns that preserve routes, forms, analytics, proof, legal language, and working business infrastructure
- Anti-generic release tests that reject interchangeable AI layouts without replacing one rigid house style with another

It is **not** a component library, a theme, a fixed stack, or a demand that every site use the same visual tricks.

## Install

### Agent Skills CLI

```bash
npx skills add https://github.com/wrg32786/Ultra-web-design --skill ultra-web-design
```

### Manual use

Copy this directory into the skill location supported by your agent:

```text
skills/ultra-web-design/
```

The portable unit is the entire folder, including `SKILL.md` and its templates.

### Direct prompt use

Point the agent to the canonical file and give it the project brief:

```text
Use skills/ultra-web-design/SKILL.md as the governing website-design and
implementation skill. Read the project before choosing a direction. Apply the
always-active core, load only the specialist modules the task needs, and verify
the result against the definition of done before shipping.
```

## How to use the skill

1. **Establish product truth.** Complete `PRODUCT.md` or label unknown claims rather than inventing them.
2. **Declare the design read.** Resolve the page kind, audience, decision context, visual language, and likely design-system family.
3. **Set expression dials.** Choose project-specific values for design variance, motion intensity, and visual density.
4. **Research deliberately.** Audit the category rut, use outside-category references, and record what discipline each reference contributes.
5. **Choose one visual world.** Define a signature system and a restraint system. Do not combine unrelated attractive ideas.
6. **Write the contract.** Produce `DESIGN.md`, route briefs, content, motion, and measurement plans before broad implementation.
7. **Build within the real stack.** Reuse existing patterns, native platform features, and installed dependencies before adding code or packages.
8. **Inspect rendered output.** Test mobile, keyboard, reduced motion, zoom, slow networks, content extremes, and actual browser behavior.
9. **Run the release gates.** A site must be truthful, usable, accessible, fast, maintainable, measurable, and recognizably its own.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
├── skills/
│   ├── llms.txt
│   └── ultra-web-design/
│       ├── SKILL.md
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
    └── validate.py
```

`SKILL.md` is the single source of truth. The files in `templates/` are extracted working copies of Section 38, included so a project can start without manually copying fenced examples.

## Source synthesis

The skill is an original synthesis and reconciliation of seven repositories, pinned so future updates can be reviewed rather than silently drifting:

| Source | Primary contribution |
|---|---|
| `pbakaus/impeccable` | Product/design authority, visual-world creation, craft floor, critique, hardening, and responsive adaptation |
| `nextlevelbuilder/ui-ux-pro-max-skill` | Searchable design intelligence, product/style/type/color/UX catalogs, stack guidance, and recommendation provenance |
| `emilkowalski/skills` | Motion purpose, timing, easing, interaction vocabulary, prototyping, and animation critique |
| `greensock/gsap-skills` | Official GSAP implementation, timelines, ScrollTrigger, lifecycle cleanup, framework integration, and performance |
| `VoltAgent/awesome-design-md` | Comparative grammar distilled from many distinct design systems |
| `nexu-io/open-design` | Modular skill architecture, portable design-system packages, artifact workflows, handoff, provenance, and bounded critique |
| `Leonxlnx/taste-skill` | Brief inference, expression dials, anti-habit controls, image-first art direction, redesign preservation, and completeness checks |

Exact commits, license notes, retained knowledge, rejected overfit rules, and conflict resolution live in Sections 40–42 of the canonical skill.

## Design philosophy

The skill does not ban a visual choice merely because an LLM often uses it. Inter, centered heroes, cards, gradients, serif type, dark mode, glass, motion, and bento layouts can all be correct.

A choice fails when it is:

- Unsupported by the product, audience, content, or brand
- Repeated mechanically across the page
- Inaccessible, misleading, slow, or brittle
- Copied too closely from a reference
- Interchangeable with an unrelated business

Distinctiveness is enforced through product truth, category-rut refusal, one-world synthesis, controlled variance, signature and restraint systems, a uniqueness ledger, and release tests—not arbitrary novelty.

## Templates

Start with the smallest set the project actually needs:

- `PRODUCT.md` — business and evidence source of truth
- `SURFACE-BRIEF.md` — route-level job, content, states, context, and analytics
- `DESIGN.md` — executable visual and interaction contract
- `CONTENT-MATRIX.md` — production content and proof ledger
- `MOTION-PLAN.md` — motion purpose, ownership, reduced motion, and validation
- `QA-REPORT.md` — design jury, technical audit, findings, and release status
- `REFERENCE-COMP-BIBLE.md` — image-first direction and extraction contract

Delete unused fields rather than preserving empty process theater.

## Validation

Run the stdlib-only validator:

```bash
python scripts/validate.py
```

It verifies the canonical file, frontmatter, version, complete numbered sections, source snapshots, template inventory, and minimum size needed to catch accidental truncation.

GitHub Actions runs the same check on pushes and pull requests.

## Updating the skill

A source update is accepted only when it changes a website-design decision. Record:

1. The exact upstream commit
2. The applicable license
3. The concrete contribution
4. Conflicts with current doctrine
5. What was integrated, reconciled, or rejected
6. The updated version and changelog entry

Do not paste an upstream skill wholesale. Preserve the authority hierarchy and resolve contradictions in one place.

## License

Apache License 2.0. See [`NOTICE.md`](NOTICE.md) for upstream provenance and third-party license notes.
