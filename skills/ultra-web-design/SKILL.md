---
name: ultra-web-design
description: >-
  Use this skill to design, redesign, audit, or implement substantial business
  websites, marketing sites, landing pages, ecommerce surfaces, editorial sites,
  and related web experiences. It governs product truth, content architecture,
  visual direction, implementation, responsive behavior, accessibility,
  performance, motion, SEO, and release QA. For tiny fixes, use its minimal path
  and load only the relevant reference module.
license: Apache-2.0
compatibility: >-
  Best in coding agents with repository access, browser rendering, and the ability
  to run the project's existing build, test, accessibility, and performance tools.
metadata:
  version: "2.0.0"
  status: "beta"
  repository: "wrg32786/Ultra-web-design"
  manifest: "MANIFEST.md"
---

# Ultra Web Design

Build business websites that make the product easier to understand, trust, use,
remember, and buy without collapsing into a reusable AI template.

This file is the **runtime authority**. It stays lean so the agent can preserve
context for the actual brief and codebase. `MANIFEST.md` is the complete reference
corpus. When they conflict, this runtime file wins.

## 1. Authority order

Resolve conflicts in this order:

1. Safety, security, data integrity, law, and non-negotiable accessibility.
2. Explicit user requirements and approved business decisions.
3. Verified product truth and real content.
4. Repository instructions, technical constraints, and established patterns.
5. Established brand authority and approved assets.
6. Approved project `DESIGN.md`.
7. Route or surface brief.
8. Universal craft and implementation rules.
9. References, catalogs, and style presets.
10. Model defaults.

A user may override an aesthetic default. They may not silently waive truthful
claims, secure data handling, keyboard access, required labels, or data-loss
protection.

## 2. Start by classifying the task

Read the repository before choosing a path. Inspect `AGENTS.md`, `CLAUDE.md`,
product/design truth, route entry points, tokens, assets, dependencies, tests,
analytics, forms, SEO, deployment, and every caller of shared code you may change.

| Task | Minimum path | Load |
|---|---|---|
| Tiny copy, style, or state fix | Read → Build → See | `modules/01-operating-loop.md` only if needed |
| Local component or route extension | Read → Shape surface → Build → Taste → See | Core + relevant craft module |
| Existing-page refinement | Read → Taste → Resolve → See → Polish | Operating loop + audit module |
| Audit only | Read → Audit | Audit module; do not edit |
| New route in an established brand | Read → Shape → Produce → Build → See | Business, design contract, relevant craft |
| Preserve-mode redesign | Read → preservation inventory → modernize → See | Operating loop + audit + design contract |
| Full visual redesign | Full loop; preserve business infrastructure | All relevant modules |
| Greenfield site | Full loop | All relevant modules |
| Motion enhancement | Static hierarchy → motion plan → Build → See | Motion module |
| Image-first direction work | Shape → Synthesize → reference frames → extract contract → Build | Visual craft + templates |

Do not run a brand workshop for a one-line defect. Do not skip product truth for a
full redesign.

## 3. Load references only when required

Read a module when its condition applies. Do not load the entire corpus by habit.

| Reference | Read when |
|---|---|
| [`modules/00-core.md`](modules/00-core.md) | Authority, truth labels, project artifacts, or package shape needs detail |
| [`modules/01-operating-loop.md`](modules/01-operating-loop.md) | Substantial work, redesigns, direction selection, implementation, or rendered QA |
| [`modules/02-business-content.md`](modules/02-business-content.md) | Positioning, offers, message hierarchy, proof, conversion, navigation, or page grammar |
| [`modules/03-visual-craft.md`](modules/03-visual-craft.md) | Layout, type, color, imagery, icons, components, forms, or state coverage |
| [`modules/04-motion-context-quality.md`](modules/04-motion-context-quality.md) | Motion, responsive adaptation, accessibility, performance, SEO, security, privacy, or analytics |
| [`modules/05-development-operations.md`](modules/05-development-operations.md) | Stack decisions, component libraries, CMS, localization, deployment, or resilience |
| [`modules/06-design-system-contract.md`](modules/06-design-system-contract.md) | Creating or updating `DESIGN.md` and durable design-system rules |
| [`modules/07-audit-release.md`](modules/07-audit-release.md) | Critique, technical audit, anti-generic review, or release readiness |
| [`modules/08-templates.md`](modules/08-templates.md) | A project artifact or reusable template is actually needed |
| [`modules/09-agent-source-analysis.md`](modules/09-agent-source-analysis.md) | Provenance, upstream rationale, source conflicts, or maintenance work |

The standalone files in `templates/` are working copies generated from
`modules/08-templates.md`.

## 4. Always-active rules

### Truth and continuity

- Never invent testimonials, metrics, ratings, customers, awards, prices,
  certifications, capabilities, affiliations, or legal claims.
- Label uncertain inputs as `SUPPLIED`, `ASSUMED`, `ILLUSTRATIVE`, `MISSING`, or
  `PROHIBITED`; do not silently promote them to production truth.
- In a redesign, inventory routes, redirects, navigation labels, forms, field
  names, analytics events, SEO metadata, proof, legal copy, brand assets, and
  accessibility wins before changing them.
- Never make a control appear functional when it is not.

### Minimum implementation

Use the first rung that solves the problem correctly:

1. Does this need to exist?
2. Is the solution already in the codebase?
3. Can semantic HTML, CSS, browser APIs, or platform behavior solve it?
4. Can the language or framework standard library solve it?
5. Can an installed dependency solve it?
6. Can a small local implementation solve it?
7. Only then add a dependency or abstraction.

Do not simplify away trust-boundary validation, error handling that prevents data
loss, security controls, accessibility, or explicit requirements.

### Design quality

- Choose one visual world per surface. Define both a signature system and a
  restraint system.
- References donate discipline, not another brand's combined identity.
- Product evidence outranks fashionable style mappings.
- Aesthetic anti-patterns are contextual review signals, not universal bans.
- A site fails when it is untruthful, unusable, inaccessible, slow, brittle, or
  interchangeable with an unrelated business.
- Motion must explain state, continuity, space, feedback, or a rare brand moment.
  Capability is not justification.
- Responsive work recomposes priority, media, interaction, and layout; it does not
  merely shrink desktop.

### Completion

- Lock the requested routes, files, sections, components, states, and formats.
- No placeholder omissions such as `TODO`, `same as above`, or bare ellipses in
  requested production output.
- Every non-trivial branch, parser, form path, money/security path, or shared state
  transition leaves one small runnable regression check.
- Inspect rendered output, not only source code.

## 5. Full operating loop

Use this loop only for substantial work.

### Read

Understand the business problem, code path, content source, visual authority,
existing system, constraints, and deployment path. Reuse before adding.

### Shape

State the surface job, audience and decision context, primary action, required
proof, non-goals, success measure, and one-line design read. Ask at most three
questions only when answers would materially change the product.

### Inspire

Research the product mechanism and audience first, category conventions second,
and outside-category systems after that. Record what each reference contributes
and what identity must not be copied.

### Synthesize

When direction is not established, produce three materially different candidates,
not color swaps. Pick one using product clarity, audience trust, differentiation,
content fit, scalability, accessibility, performance, and feasibility.

### Produce

Create only the contracts the work needs: normally `PRODUCT.md`, `DESIGN.md`, a
surface brief, real content/proof inventory, tokens, motion plan, and QA report.
Delete unused fields rather than preserving process theater.

### Build

Implement the smallest complete representative slice in the real stack. Include
semantic structure, real content, responsive behavior, interaction states,
failure recovery, analytics, SEO, and legal/operational requirements that belong
to the slice.

### Taste

Judge the artifact against the brief and chosen world. Run the logo-removal,
interchangeability, squint, grayscale, image-off, content-stress, and mobile-authored
tests. Explain corrections as Before → After → Why.

### Resolve

Fix shared causes in priority order: blockers, major defects, minor friction, then
polish. Prefer correcting a token, shared primitive, content structure, or data
boundary over repeated local patches.

### See

Inspect narrow mobile, common mobile, tablet, laptop, wide desktop, keyboard,
coarse pointer, reduced motion, zoom/reflow, slow/offline behavior, failures, and
real browser output. Use automated tools as a floor, not proof.

### Polish

Finish content, links, line breaks, media crops, browser surfaces, metadata,
forms, consent, analytics, monitoring, deployment, rollback, and ownership. Stop
when release requirements pass and further changes are preference churn.

## 6. Required artifacts by scope

| Scope | Minimum durable output |
|---|---|
| Tiny fix | Code diff + one check when logic is non-trivial |
| Route extension | Surface brief + code + checks |
| New route | Surface brief + content/proof inventory + code + checks |
| Substantial redesign | Preservation inventory + product truth + `DESIGN.md` + route briefs + QA report |
| Greenfield site | Product truth + direction decision + `DESIGN.md` + route briefs + content matrix + implementation + QA report |
| Audit only | Evidence-based findings, severities, root causes, corrections, and positive findings |

Templates live in [`templates/`](templates/). Use the smallest set that makes the
work executable.

## 7. Release gates

A release is blocked by any known P0/P1 defect or by failure of an applicable hard
gate:

- Truth and business continuity.
- Working primary actions and recoverable failures.
- Semantic, keyboard-operable, WCAG 2.2 AA-targeted interaction.
- Responsive recomposition and no unintended overflow.
- Performance budget and low-end/mobile viability.
- Accurate SEO, structured data, analytics, consent, and legal behavior.
- Asset, font, code, and brand rights.
- No fake product UI, fake precision, filler content, or unknown proof.
- Requested deliverable count is complete.

Numeric jury scores in the full manifest are **advisory heuristics**, not calibrated
scientific thresholds. Use them to structure critique; use hard defects, evidence,
and explicit owner decisions to determine release.

## 8. Verification

Use the repository's existing checks first. For this skill repository itself run:

```bash
python scripts/build_manifest.py
python scripts/sync_templates.py --check
python scripts/validate.py
skills-ref validate skills/ultra-web-design
```

For a website implementation, run the project's formatter, linter, type checks,
tests, build, accessibility checks, browser tests, and performance tools that are
already installed. Add no duplicate quality stack merely because this skill names
a category of check.

## 9. Response contract

For substantial work, report only material information:

1. Task classification and assumptions.
2. Source-of-truth files read.
3. Chosen path and visual direction when relevant.
4. Locked deliverable count.
5. Changes or artifacts produced.
6. Checks run and exact results.
7. Remaining risks only when real.

Do not narrate every tool call or recite this skill back to the user.

## 10. Provenance and complete reference

The complete synthesis, source-by-source analysis, templates, conflicts, standards,
and historical doctrine live in [`MANIFEST.md`](MANIFEST.md). Exact upstream
snapshots and licenses also live in the repository `NOTICE.md` and the manifest's
provenance sections.
