# Ultra Web Design Manifest

> **Revision 1.1.0:** integrates `Leonxlnx/taste-skill` at commit `843c8dd4d18ccff0d5a9cd4b0b71d7dbf7278293`, including contextual anti-tell controls, expression dials, image-first art direction, redesign preservation, bounded presets, and completeness verification.

## 0. Mission

Build business websites that make the product easier to understand, trust, use, remember, and buy—without collapsing into a reusable AI template.

This is not a gallery of styles and not a prompt that says “make it beautiful.” It is an operating system. It governs the full path from business truth to production code:

> **Read → Shape → Inspire → Synthesize → Produce → Build → Taste → Resolve → See → Polish**

A finished site must be all of the following:

- **True:** claims, pricing, proof, testimonials, metrics, logos, certifications, and product capabilities come from supplied or verified evidence.
- **Specific:** the design expresses this product, this audience, this use scene, and this business model. Replacing the logo and copy with an unrelated company must break the concept.
- **Coherent:** one visual world, one message hierarchy, one token system, and one interaction vocabulary govern the site.
- **Useful:** users can find information, compare options, complete actions, recover from errors, and understand what happens next.
- **Accessible:** target WCAG 2.2 AA unless a stricter requirement applies.
- **Responsive:** the experience is recomposed for context rather than merely shrunk.
- **Fast:** it meets the project’s performance budget and targets good Core Web Vitals in field data.
- **Maintainable:** it uses the existing stack and patterns where possible, adds the fewest justified abstractions, and records durable decisions.
- **Measurable:** conversion events and quality signals are defined before launch.
- **Distinctive:** it passes the interchangeability, logo-removal, category-rut, and screenshot-recognition tests in Section 36.

A visually unusual site that is confusing, slow, inaccessible, or dishonest has failed. A usable site that could belong to any company has also failed.

### 0.1 Repository-ingestion scope

The source repositories were ingested at the level that can change website-design decisions: canonical skill and protocol files, design-system schemas, catalog structures and reasoning fields, motion guidance, representative implementation examples, critique and quality contracts, repository architecture, provenance, licenses, and the boundaries between source truth and generated mirrors. Generated copies, lockfiles, binaries, localized duplicates, screenshots, test fixtures, application runtime plumbing, release infrastructure, and unrelated product code were inventoried or classified but are not reproduced as design doctrine. Section 40 records the retained and excluded material repository by repository.

This revision covers seven unique repositories. The added Taste Skill repository was analyzed across its current v2 skill, preserved v1, GPT-oriented variant, image-to-code and image-direction skills, redesign workflow, three named style presets, brand-kit and Stitch contracts, completeness skill, research appendix, examples, packaging, and maintenance scripts. Its strongest ideas were integrated as contextual controls; its duplicated, platform-specific, unsupported, or overly absolute claims were not promoted to universal law.

### 0.2 Uniqueness claim

No finite document can mathematically guarantee that two independently built sites will share no pattern. This manifest enforces operational uniqueness instead: product-specific truth, category-rut refusal, outside-category research, controlled variance, one-world synthesis, signature and restraint systems, a uniqueness ledger, a branded-reference similarity ceiling, and screenshot-recognition release tests. A site fails when its structure and visual language remain interchangeable with an unrelated product.

---

## 1. Normative language

- **MUST / MUST NOT:** release requirement.
- **SHOULD / SHOULD NOT:** default; deviate only with a recorded reason.
- **MAY:** optional when it serves the brief.
- **EARNED:** justified by product truth, audience context, content, or the selected visual world—not by model habit.
- **VISUAL WORLD:** the governing combination of composition, type, color, imagery, materials, geometry, motion, and restraint.
- **SURFACE:** one route, page, flow, or artifact with a specific job.
- **PRODUCT TRUTH:** facts about the offer, audience, mechanism, proof, constraints, and business objective.
- **CRAFT FLOOR:** universal usability and implementation rules that apply unless a stronger product or accessibility constraint supersedes them.
- **DESIGN READ:** one sentence that resolves the page kind, audience, desired language, and likely design-system or aesthetic family before visual generation begins.
- **EXPRESSION DIALS:** the project-specific coordinates for design variance, motion intensity, and visual density. They are constraints, not quality scores.
- **AI TELL:** a recurring model-generated pattern that may reveal habit rather than intent. It is a review heuristic, not automatically a ban.
- **STYLE PRESET:** a bounded, optional visual module with explicit fit, non-fit, dial range, signature, restraint, mobile behavior, and accessibility risks.

---

## 2. How to use this file

### 2.1 Always-active core

For every website task, apply:

1. Sections 3–14: authority, workflow, and phase gates.
2. Sections 15–16: business and page architecture.
3. Sections 17–29: craft and production floors.
4. Sections 35–37: critique, anti-slop, and ship gates.

### 2.2 Load-on-demand modules

Use these modules when the task contains the corresponding condition:

| Condition | Load |
|---|---|
| Existing repository or redesign | Sections 5, 10, 12, 31, 35 |
| New brand or no visual authority | Sections 7–9, 17–21, 34 |
| Established brand | Sections 5.3, 9.5, 34 |
| Landing or conversion page | Sections 15–16, 22–23, 28, 30 |
| Interactive tool or account area | Sections 22–27, 31 |
| Animation, scroll storytelling, SVG, or GSAP | Section 24 |
| Ecommerce or payment | Sections 16.5, 23, 29–30 |
| Editorial, media, or long-form content | Sections 16.6, 17–18, 28, 32 |
| International audience | Sections 25–26, 33 |
| Data visualization | Section 21.4 |
| CMS or frequent publishing | Section 32 |
| Ambiguous brief with materially different visual paths | Section 6.1A |
| Image-led concepting or reference-to-code | Sections 8.6A and 20.8 |
| Named aesthetic/style preset | Sections 8.4B and 34.20 |
| Reusable cross-project block requested | Section 9.6A; create only after reuse is real |
| Pre-launch audit | Sections 35–37 |

### 2.3 Do not turn this into a checklist performance

The user should see decisions and results, not narration of every rule. Internally apply the rules; externally explain only material choices, tradeoffs, assumptions, and unresolved risks.

### 2.4 Bounded iteration

Do not loop forever in pursuit of aesthetic certainty.

- One research and context pass.
- One direction round with three materially different candidates when direction is not already established.
- One chosen direction.
- One batched desktop/mobile visual inspection.
- One batched correction pass.
- One confirmation pass.
- Up to three critique rounds when the artifact is still below the release bar.
- For an image-first branch, one global design-bible pass and one frame pass; regenerate unclear frames directly rather than repeatedly cropping or patching a weak composite.

More passes require new evidence, a changed brief, or a clearly identified defect.

---

## 3. Authority and conflict resolution

Resolve conflicts in this order:

1. **Safety, security, data integrity, law, and non-negotiable accessibility.** These are not aesthetic preferences.
2. **Explicit user requirements and approved business decisions.** The brief wins over model taste.
3. **Verified product truth and real content.** Never distort facts to fit a composition.
4. **Repository instructions, technical constraints, and established implementation patterns.** Read before writing.
5. **Established brand authority.** Approved assets, tokens, product UI, prior campaigns, and existing customer-facing surfaces.
6. **Approved site-level `DESIGN.md`.** Durable visual and interaction decisions.
7. **Surface brief.** Route-specific purpose, hierarchy, content, and exceptions.
8. **Universal craft floor.** Accessibility, state coverage, responsive behavior, performance, and interaction discipline.
9. **Reference systems and searchable catalogs.** Candidate generators, never authorities.
10. **Model defaults.** Last and weakest.

A user may intentionally choose an aesthetic that violates a stylistic default. They may not silently waive truthful claims, secure handling of data, keyboard access, required labels, or other trust-boundary obligations.

Repository anti-pattern lists that describe common AI tells sit below product truth, brand authority, the approved `DESIGN.md`, and the craft floor. Promote one to a project-level prohibition only when it conflicts with the brief, repeats mechanically, causes a measurable defect, or belongs to the documented category rut. A stylistic blacklist is not a substitute for judgment.

---

## 4. Required project artifacts

Create only the artifacts the work needs. A greenfield or substantial redesign normally requires the first four; a small extension may require only a surface brief and implementation diff.

| Artifact | Job | Source of truth |
|---|---|---|
| `PRODUCT.md` | Business, audience, offer, mechanism, proof, constraints, and success metrics | Product truth |
| `DESIGN.md` | Durable visual world, tokens, composition, imagery, components, motion, and restraint | Brand contract |
| `SURFACE-BRIEF.md` | Route-specific job, content hierarchy, CTA, proof, states, and exceptions | Page contract |
| `CONTENT-MATRIX.md` | Actual copy/assets, source, status, owner, and legal/proof status | Content truth |
| `tokens.css` | Compiled semantic token contract | Implementation truth |
| `DECISIONS.md` | Material tradeoffs, assumptions, rejected directions, and reasons | Continuity |
| `QA-REPORT.md` | Findings, severities, evidence, fixes, and release status | Release truth |

### 4.1 Truth labels

Every claim or asset in planning documents MUST carry one of these statuses when its authority is not obvious:

- `VERIFIED` — checked against a primary or supplied source.
- `SUPPLIED` — provided by the owner but not independently verified.
- `ASSUMED` — necessary working assumption; must be visible to the owner.
- `ILLUSTRATIVE` — explicitly non-production example.
- `MISSING` — required input not yet available.
- `PROHIBITED` — cannot be invented or used.

Never convert `ASSUMED` or `ILLUSTRATIVE` into production copy without approval.

### 4.2 Design-system package shape

A portable package SHOULD use:

```text
design-system/
├── manifest.json       # identity, provenance, file paths
├── PRODUCT.md          # optional when product truth lives elsewhere
├── DESIGN.md           # canonical prose contract
├── tokens.css          # canonical semantic tokens
├── USAGE.md            # read order and inheritance guidance
├── components.html     # optional component/state fixture
├── assets/             # approved media
├── fonts/              # licensed, self-hosted fonts when applicable
├── preview/            # reference pages
└── source/             # evidence and provenance
```

Derived files are caches, not competing truth sources. If generated JSON, Tailwind mappings, or component manifests disagree with `DESIGN.md` and `tokens.css`, fix the source and regenerate.

---
