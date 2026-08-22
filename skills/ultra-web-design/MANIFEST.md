---
name: ultra-web-design
version: 1.1.0
status: production
license: Apache-2.0
repository: https://github.com/wrg32786/Ultra-web-design
revision_note: Integrated Leonxlnx/taste-skill at a pinned 2026-08-21 snapshot.
last_verified: 2026-08-21
description: >-
  A modular operating system for researching, positioning, designing, building,
  testing, and shipping distinctive business websites. It converts product truth,
  audience context, brand evidence, visual references, universal craft rules, and
  implementation constraints into a coherent website that is useful, accessible,
  fast, truthful, maintainable, and recognizably its own.
triggers:
  - design a business website
  - redesign a website
  - build a landing page
  - create a marketing site
  - create a product website
  - create a company website
  - create a website design system
  - audit or improve a website
  - translate a brand into code
scope:
  - marketing and conversion sites
  - SaaS and software sites
  - service and professional-business sites
  - ecommerce and product sites
  - editorial, media, newsletter, and community sites
  - portfolios, agencies, courses, events, nonprofits, and public-service sites
  - supporting product surfaces when a business site includes interactive tools
source_snapshots:
  pbakaus/impeccable: e5abceedc44ee6284a5ebb0bd309e30706d2cb8c
  nextlevelbuilder/ui-ux-pro-max-skill: bc826e2267a36d98a2dcf5231e16c30ff546770f
  emilkowalski/skills: d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7
  greensock/gsap-skills: aed9cfd3277740755f6bfc1155c7aa645403b760
  VoltAgent/awesome-design-md: 8147538b4226ae41e2487a9179e3bcc1f68e8554
  nexu-io/open-design: 05f5b33ef59f078df10ac1125986e00e4a796cf3
  Leonxlnx/taste-skill: 843c8dd4d18ccff0d5a9cd4b0b71d7dbf7278293
---

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

# Part I — The Operating Loop

## 5. READ — Understand the real system before designing

### 5.1 Read order

For an existing project, inspect in this order:

1. Repository instructions (`AGENTS.md`, `CLAUDE.md`, contribution rules, package guidance).
2. Product and design truth (`PRODUCT.md`, `DESIGN.md`, brand guidelines, content docs).
3. Route and component entry points.
4. Existing tokens, fonts, assets, icon libraries, component primitives, and layout utilities.
5. Data flow, forms, APIs, CMS, analytics, SEO, auth, and deployment configuration touched by the change.
6. Every caller or consumer of a shared function/component before modifying it.
7. Existing tests and quality checks.

Do not infer an unseen codebase from screenshots or snippets. Do not reimplement a utility that already exists a few files away.

### 5.2 Existing-system inventory

Record:

- framework, renderer, routing model, language, styling approach, and build tool;
- installed UI, motion, icon, form, chart, analytics, and testing dependencies;
- component hierarchy and reusable primitives;
- semantic tokens and hard-coded drift;
- content source and ownership;
- supported browsers, devices, locales, and accessibility target;
- current page types, conversion paths, and tracked events;
- performance baseline and known regressions;
- deployment, preview, and rollback path.

### 5.3 Classify visual authority

Choose exactly one:

1. **Established world:** coherent approved system exists. Preserve and extend it.
2. **Incomplete brand:** recognizable ingredients exist but the system has gaps. Preserve the signals; resolve the gaps.
3. **Redesign:** product truth stays, visual world is intentionally replaced.
4. **No authority:** greenfield. Create a new world.

A local addition to an established surface inherits the surface. It does not trigger a new identity exercise.

### 5.3A Redesign preservation inventory

Before editing an existing site, classify each durable surface as `PRESERVE`, `EVOLVE`, `REPLACE`, or `OWNER APPROVAL REQUIRED`.

Inventory at minimum:

- routes, URL slugs, redirects, anchor IDs, canonical relationships, and ranking pages;
- primary navigation labels, task paths, information architecture, and deep links;
- page titles, descriptions, social cards, structured data, sitemap/indexing behavior, and search intent;
- form field names, order, autocomplete semantics, validation contracts, submission destinations, and CRM mappings;
- analytics event names, selectors, conversion definitions, experiments, and attribution dependencies;
- brand name, logo, wordmark, approved colors, typography, photography, voice, and recognizable interaction patterns;
- legal, consent, privacy, accessibility, security, and regulated-claim copy;
- working keyboard paths, focus treatment, alt text, landmarks, and other existing accessibility wins;
- real content, proof, testimonials, customer permissions, and asset licenses.

Never silently change route slugs, primary navigation labels, form field names/order, analytics contracts, the brand mark, or legal/consent language. A visual redesign may replace the world; it does not get permission to break business continuity.

### 5.4 Root-cause rule

A bug report names a symptom. Trace the full flow and fix the narrowest shared root that resolves all affected callers. One guard in the shared function is smaller and safer than repeated guards in every route.

### 5.5 Development ladder

Stop at the first rung that solves the problem correctly:

1. Does this need to exist?
2. Is the solution already in the codebase?
3. Can semantic HTML, CSS, browser APIs, or platform behavior solve it?
4. Can the language or framework standard library solve it?
5. Can an already-installed dependency solve it?
6. Can a small local implementation solve it?
7. Only then add a dependency or abstraction.

Do not remove validation, error handling, accessibility, security, or data-loss protection in the name of simplicity.

### 5.6 READ gate

Do not proceed until you can state:

- what business/user problem is being solved;
- what route and code path owns it;
- whether the visual world is preserved, completed, or replaced;
- which existing patterns will be reused;
- which constraints are non-negotiable;
- what evidence is missing and which assumptions are being made.

---

## 6. SHAPE — Convert the request into product and surface truth

### 6.1 Ask only decision-changing questions

Ask one compact round of at most three questions when answers would materially alter the site. Do not ask for CSS values, canned style labels, or information already available.

High-value questions usually cover:

- **Outcome:** What must the visitor understand or do?
- **Audience:** Who is deciding, in what context, with what objections?
- **Authority:** What brand, content, proof, assets, or existing product UI must be preserved?

When answers are unavailable, choose reasonable assumptions, label them, and continue.

### 6.1A Declare the design read

Before setting a style, generating a comp, or writing frontend code, state one internal sentence:

> Reading this as: **[page/surface kind]** for **[audience and decision context]**, with a **[visual/interaction language]**, leaning toward **[established system or aesthetic family]**.

The read resolves:

- page kind and dominant surface mode;
- buyer/user context and trust sensitivity;
- named references or visual cues;
- whether brand authority is established, incomplete, replaced, or absent;
- quiet constraints such as public-sector, accessibility-critical, regulated, child-directed, low-literacy, or low-bandwidth use;
- whether the direction should use an official design system, a custom brand system, or a bounded aesthetic preset.

Ask one clarifying question only when two plausible reads would produce materially different products. Otherwise declare the assumption and proceed. Do not ask the user to choose implementation trivia that the existing codebase or this process can resolve.

### 6.2 Product truth model

Capture:

- business model and primary revenue action;
- offer, price, packaging, and eligibility;
- target audience and excluded audience;
- user job, desired outcome, anxieties, and decision criteria;
- unique mechanism: how the product creates the outcome;
- category and direct alternatives, including doing nothing;
- proof: product evidence, case studies, customer quotes, usage, research, credentials;
- risk reversal: trial, guarantee, demo, cancellation, support, transparency;
- primary and secondary CTA;
- operational constraints: legal, privacy, compliance, claims, locale, launch date;
- success metrics and baseline.

### 6.3 Surface mode

Assign one dominant mode per route:

| Mode | Primary job | Typical evidence | Failure mode |
|---|---|---|---|
| **Persuade** | Build understanding, desire, trust, and action | mechanism, proof, comparison, offer | generic marketing sequence |
| **Operate** | Help users complete tasks and make decisions | state, control, feedback, data | decorative friction |
| **Read** | Support comprehension, scanning, and return | hierarchy, navigation, citations, related content | flat walls of text |
| **Experience** | Create immersion, identity, or exploration | art direction, pacing, interaction | spectacle without orientation |

A site may contain all four. A single surface should not behave as all four at once.

### 6.4 Surface brief

Every route gets:

- route name and mode;
- visitor state on arrival;
- one-sentence job;
- primary action and secondary action;
- top five questions the route must answer;
- required content and proof;
- first-viewport contract;
- section or interaction grammar;
- required states;
- SEO/search intent where applicable;
- responsive and input-context notes;
- analytics events;
- explicit non-goals.

### 6.5 First-viewport contract

Above the first meaningful fold, a visitor SHOULD be able to determine:

1. What is this?
2. Is it relevant to me?
3. What outcome or value does it create?
4. Why should I believe or continue?
5. What can I do next?

Not every answer needs a sentence. Product imagery, interface proof, typography, and composition may carry meaning. Ambiguity used as intrigue is allowed only when orientation arrives before abandonment.

### 6.6 Evidence ladder

Rank proof from strongest to weakest:

1. Direct product behavior or live demonstration.
2. Verifiable outcome with context and methodology.
3. Detailed case study.
4. Attributed customer testimony.
5. Recognizable customer/partner relationship with permission.
6. Process transparency, credential, or third-party review.
7. Founder assertion.

Use the strongest evidence available. Never manufacture a higher rung.

### 6.7 SHAPE gate

Proceed only when the product, audience, route job, action, proof, constraints, and success metric are explicit enough to judge design decisions.

---

## 7. INSPIRE — Research without becoming derivative

### 7.1 Reference hierarchy

Research in this order:

1. Product mechanism, real interface, physical product, service process, or customer environment.
2. Audience culture: publications, places, tools, rituals, materials, and visual languages familiar to them.
3. Category conventions and competitors—to understand what to avoid or intentionally retain.
4. Adjacent disciplines and eras outside the category.
5. Curated design systems and searchable catalogs.
6. Current primary standards for accessibility, performance, SEO, and platform behavior.

Competitor screenshots alone produce category-average work. At least half of the inspiration set SHOULD come from outside the direct category.

### 7.2 Category-rut audit

Before generating directions, list:

- the ten most predictable visual and structural choices in the category;
- the default hero composition;
- the default palette and font class;
- the default proof pattern;
- the default card, icon, and motion behavior;
- the predictable “opposite” that designers use when trying to be different.

Avoid both the rut and its obvious costume-opposite unless evidence supports them.

Examples:

- “AI” does not automatically mean indigo gradients, glowing orbs, grids, monospace, or dark mode.
- “Luxury” does not automatically mean black, gold, glass, serif, and slow fades.
- “Developer tool” does not automatically mean terminal chrome, code rain, and mono everywhere.
- “Wellness” does not automatically mean beige, sage, rounded cards, and soft stock photography.

### 7.3 Seven-source exercise

For a new visual world, identify at least seven concrete source systems across at least three families:

- publication, poster, signage, map, manual, ticket, label, or catalog;
- architecture, interior, landscape, exhibition, or retail environment;
- industrial material, machine, instrument, packaging, or physical product;
- interface, dashboard, notation, diagram, measurement system, or operating panel;
- ritual, movement, sport, craft, or audience behavior;
- photographic, cinematic, theatrical, or image-making tradition;
- historical or regional visual language.

Do not use the product’s literal name as the primary metaphor. A product called “Orbit” does not need planets. A product called “Forge” does not need sparks.

### 7.4 Searchable-catalog protocol

When using a design catalog or recommendation engine:

1. Use one dominant intent and two to five meaningful terms.
2. Include the product type, audience/use context, and interaction constraint that matters.
3. Use a whole-system query for a new direction; use one explicit domain for a focused problem.
4. Detect the actual implementation stack; never assume it.
5. Verify the returned domain, category, top result, and fit.
6. Retry once with a narrower query or explicit domain.
7. After one failed retry, label the result low-confidence and do not persist it as authority.
8. Treat product-to-style mappings as hypotheses. Challenge stereotype-prone recommendations.
9. Record provenance and the specific discipline borrowed.

A database row can suggest a palette or font pairing. It cannot decide the site’s thesis.

### 7.5 Reference donation rule

A reference may donate:

- grid courage;
- typographic contrast;
- image crop behavior;
- palette commitment;
- surface hierarchy;
- information density;
- motion timing;
- component geometry;
- structural honesty.

It may not donate the recognizable combination of another brand’s type, color, layout, imagery, trademark, proprietary asset, or signature motif. Borrow discipline, not identity.

### 7.6 Asset provenance

For every external font, photo, video, icon, illustration, texture, model, or code effect, record:

- source URL or repository;
- creator/provider;
- license or permission;
- permitted use and attribution requirement;
- local filename and transformation;
- expiration or campaign limitation if any.

No production asset enters the site with unknown rights.

### 7.7 INSPIRE gate

Proceed only when the research set includes product evidence, audience evidence, category-rut knowledge, outside-category references, and usable provenance.

---

## 8. SYNTHESIZE — Generate and choose a visual world

### 8.1 Direction inputs

Start with four sentences:

1. **Unique mechanism:** what the business does differently.
2. **Audience scene:** where and how the audience experiences the problem.
3. **First-surface proof:** what evidence should appear earliest.
4. **Category rut and refusal:** what the site will not default to.

### 8.1A Set the three expression dials

Record three values from 1–10 in the direction card and `DESIGN.md`:

| Dial | 1 | 5 | 10 |
|---|---|---|---|
| `design_variance` | symmetrical, predictable, institutional | offset, selective asymmetry | highly art-directed, irregular, experimental |
| `motion_intensity` | static except state feedback | fluid transitions and a few authored sequences | cinematic, scroll-linked, physical, or spatial choreography |
| `visual_density` | gallery-airy | balanced daily-use rhythm | cockpit-dense, data-rich, compressed |

Infer them from the design read rather than using one permanent baseline. Useful starting envelopes:

| Context | Variance | Motion | Density |
|---|---:|---:|---:|
| Public service, regulated, accessibility-critical | 2–4 | 1–3 | 4–6 |
| Mainstream SaaS or B2B marketing | 5–7 | 3–6 | 3–5 |
| Editorial or thought leadership | 5–8 | 2–5 | 2–5 |
| Premium consumer or brand campaign | 6–8 | 4–7 | 2–4 |
| Agency, portfolio, cultural, experimental | 8–10 | 6–9 | 2–5 |
| Operations, telemetry, dense product surface | 4–7 | 2–5 | 7–9 |

These are search coordinates, not aesthetic grades. High variance is not better than low variance. High motion is not evidence of craft. A declared dial must be visible in the output: if motion is scoped out, lower `motion_intensity`; if mobile cannot carry the desktop asymmetry, record the mobile recomposition instead of pretending the variance survives unchanged.

### 8.2 Controlled-variance seed

Use variation only as a tie-breaker after product evidence. Store a stable `variance_seed` in `DESIGN.md`.

A tool-free deterministic seed:

```text
seed_input = project_slug + "|" + primary_audience + "|" + surface_mode
seed = sum((position + 1) × Unicode code point) mod 997
```

Use the seed to force exploration across different starting pressures, not to override fit:

| `seed mod 7` | Composition pressure |
|---:|---|
| 0 | Editorial spine and typographic pacing |
| 1 | Cinematic frame and image-led sequence |
| 2 | Field guide, manual, or annotated system |
| 3 | Product laboratory and mechanism proof |
| 4 | Catalog, collection, or storefront rhythm |
| 5 | Manifesto, poster, or monumental statement |
| 6 | Spatial, architectural, or environmental journey |

Then force challengers from different families. Do not produce three versions of the same centered hero.

### 8.3 Three direction cards

When no direction is approved, generate exactly three materially different candidates. Each card contains:

- name and one-sentence thesis;
- product/audience rationale;
- source families and what they donate;
- first viewport;
- page rhythm and composition grammar;
- typography behavior;
- palette and material behavior;
- imagery/illustration behavior;
- signature system;
- signature interaction, if earned;
- restraint system: what is intentionally absent;
- content/proof strategy;
- responsive behavior;
- accessibility and performance risks;
- implementation complexity;
- reason it could win;
- reason it could fail.

A direction is not “dark version,” “light version,” or a color swap. It must change the governing composition and expressive logic.

### 8.4 Signature system and restraint system

Every chosen world MUST define both.

**Signature system:** one or two repeatable, product-specific moves that make the site recognizable. Examples include an evidence-annotation language, a distinctive image crop, a recurring data scale, a bespoke editorial rule, a spatial reveal tied to the product mechanism, or a highly specific type proportion.

**Restraint system:** deliberate limits that keep the signature meaningful. Examples include one accent used only for decisions, no cards above the fold, motion reserved for state transitions, one display face, no decorative icons, or imagery only when it proves the product.

Distinctiveness comes from commitment plus restraint, not maximal decoration.

### 8.4A Concept spine and second-read moment

Choose one product-grounded concept spine when it helps unify the page. Examples:

- **artifact / collectible** — specimens, evidence, provenance, valued objects;
- **journey / waypoint** — progression, orientation, thresholds, milestones;
- **precision instrument** — calibration, controls, measurement, repeatability;
- **living system** — growth, branching, stewardship, feedback;
- **stage / spotlight** — performer, audience, reveal, contrast;
- **archive / dossier** — indexing, annotation, records, authority.

The spine must change composition, imagery, proof, or interaction. Naming a metaphor without structural consequences is decoration.

Add exactly one deliberate **second-read moment**: a detail that rewards attention after the basic scan without obscuring it. It may be an asymmetric bleed, one oversized numeral/punctuation mark with real meaning, a material switch, a narrow editorial side rail, or a macro crop that carries brand color. It must improve scan order, explanation, or recall. Do not distribute novelty evenly across the page.

### 8.4B Bounded style-preset contract

A named aesthetic may accelerate direction only when encoded as a bounded preset. Every preset MUST declare:

- use cases and `not_for` cases;
- compatible dial ranges;
- governing substrate, palette, typography, geometry, imagery, and motion;
- one signature system and one restraint system;
- component behavior and state treatment;
- mobile collapse/recomposition;
- accessibility, performance, and brand-imitation risks;
- which rules are essential and which are merely examples.

Useful preset families mined from the source corpus include:

- **Premium utilitarian minimalism:** warm or neutral monochrome, editorial type contrast, crisp shallow radii, sparse color, low elevation, generous macro-space.
- **Soft structuralism:** quiet nested frames, soft material edges, editorial hierarchy, spring-like feedback, restrained translucent surfaces.
- **Swiss industrial print:** rigid visible grid, macro grotesk type, micro technical labels, paper-like substrate, one hazard accent, square geometry.
- **Tactical telemetry:** dark technical substrate, dense monospace data, strict compartments, restrained phosphor/alert color, analog degradation used sparingly.
- **High-expression editorial/kinetic:** asymmetry, decisive type/image relationships, strong section variation, authored motion, and aggressive mobile simplification.

Use one primary preset. Do not mix incompatible presets into a mood-board collage. A preset never overrides product truth, approved brand assets, accessibility, or the user’s brief, and its source-specific font/library/punctuation bans do not become universal rules.

### 8.5 Evaluation matrix

Score each candidate from 0–10:

| Dimension | Weight |
|---|---:|
| Product clarity and mechanism fit | 25% |
| Audience identification and trust | 20% |
| Differentiation from category rut | 20% |
| Content and proof fit | 15% |
| Multi-route scalability | 10% |
| Accessibility, performance, and feasibility | 10% |

Record the verdict: `WINNER`, `COMPETITIVE`, or `DECLINED`.

Declined directions may donate discipline, such as a stronger grid or better palette commitment. They may not donate motifs that dilute the winner. One visual world owns the page.

### 8.6 Direction proof

Use real content and correct aspect ratios. Prove the direction through either:

- **Comp-led path:** a high-fidelity first viewport plus one dense and one quiet section; the approved comp becomes visual law.
- **Code-led path:** a written contract plus a working vertical slice with real type, media, states, and responsive behavior.

Wireframes are insufficient for judging a type-led or image-led world. High-fidelity decoration is insufficient for judging a weak information architecture.

### 8.6A Image-first direction proof

Use an image-first branch when the largest uncertainty is art direction, visual composition, image treatment, or the relationship between sections—not when the real problem is information architecture or component behavior.

1. Lock a **reference design bible**: palette, typography mood, grid, spacing, radius/elevation, image treatment, icon/illustration grammar, device/browser framing, concept spine, and dials.
2. Generate one readable frame per major section, state, or screen rather than compressing an entire site into one tall, illegible board. A six-section landing page normally receives six horizontal section references when image generation is the chosen proof method.
3. Keep the global design bible stable while varying section composition. Across a long page, use at least three composition anchors unless the selected world intentionally demands repetition.
4. Regenerate a dedicated frame when a section is unclear. Do not crop a tiny region from a composite and treat the distorted crop as law.
5. Require implementation readability: a developer must be able to infer hierarchy, grid, spacing, type scale, image crop, CTA priority, component material, and responsive intent.
6. Extract the written contract before coding. The reference image supplies direction; semantic HTML, real text, responsive behavior, states, accessibility, and performance remain implementation truth.

Image-first proof is optional. It must not become a ritual that adds generation work when a written contract and live vertical slice already resolve the uncertainty.

### 8.7 Similarity guard

Before approval, compare the direction against its references and category peers:

- Does it reproduce another brand’s combined silhouette?
- Does it rely on a single famous site’s exact hero, navigation, type, and motion pattern?
- Would a knowledgeable viewer call it a clone?
- Is the signature system derived from the product, or attached after the fact?

If yes, return to source disciplines and recombine.

### 8.8 SYNTHESIZE gate

Proceed only when one direction is approved, its thesis is explainable in one sentence, its signature and restraint systems are explicit, and its risks are known.

---

## 9. PRODUCE — Turn direction into an executable contract

### 9.1 Write `DESIGN.md` before broad implementation

The contract should be specific enough that a different capable model can continue the work without inventing a new world. It must cover the modules in Section 34.

### 9.1A Write semantic design language, not framework shorthand

For every durable visual rule, provide:

> **Descriptive name + exact value/range + functional role + exception or counterexample.**

Good: “Decision Orange (`#E66A2C`) is reserved for primary actions, active navigation, and verified alert emphasis; decorative icons remain neutral.”

Weak: “Use `orange-500`.”

Good: “Low surface elevation uses a tinted 24px blur at 6% opacity only when overlap communicates hierarchy.”

Weak: “Use `shadow-lg`.”

A generative design tool may consume natural language, while code consumes tokens. The contract must bridge both. Do not embed implementation-framework vocabulary as the only explanation of intent.

### 9.2 Build the content matrix

For every section or component, record:

| Field | Meaning |
|---|---|
| `id` | stable section/component identifier |
| `visitor_question` | question this unit answers |
| `content` | real copy or asset |
| `source` | owner, document, API, or URL |
| `truth_status` | verified/supplied/assumed/illustrative/missing |
| `proof_type` | demo, metric, quote, case study, credential, process |
| `primary_action` | action, if any |
| `seo_intent` | target query or none |
| `state_requirements` | loading, empty, error, edge, populated |
| `owner` | person/system responsible for updates |

Delete sections that answer no visitor question.

### 9.3 Token contract

Use semantic tokens, not component-color trivia.

```css
:root {
  --canvas: ...;
  --surface: ...;
  --surface-raised: ...;
  --text: ...;
  --text-muted: ...;
  --border: ...;
  --accent: ...;
  --accent-contrast: ...;
  --positive: ...;
  --warning: ...;
  --danger: ...;

  --font-display: ...;
  --font-body: ...;
  --font-utility: ...;
  --font-data: ...;

  --step--1: ...;
  --step-0: ...;
  --step-1: ...;
  --step-2: ...;
  --step-3: ...;
  --step-4: ...;

  --space-1: ...;
  --space-2: ...;
  --space-3: ...;
  --space-4: ...;
  --space-5: ...;
  --space-6: ...;

  --radius-control: ...;
  --radius-surface: ...;
  --border-width: ...;
  --shadow-low: ...;
  --shadow-high: ...;

  --duration-fast: ...;
  --duration-default: ...;
  --duration-slow: ...;
  --ease-enter: ...;
  --ease-move: ...;
  --ease-exit: ...;
}
```

Component tokens MAY alias semantic tokens. They must not create a second ungoverned palette.

### 9.4 Component/state fixture

Before multiplying pages, prove:

- primary, secondary, quiet, and destructive actions;
- text links and navigation states;
- inputs, selects, textareas, checks, radios, and errors;
- surfaces, dividers, lists, tables, and media containers;
- loading, empty, error, populated, and edge states;
- focus, hover, active, disabled, pending, selected, and visited states where relevant;
- long content, missing media, and translated content.

### 9.5 Inheritance

Use this order:

```text
PRODUCT.md
  └── DESIGN.md
       └── SURFACE-BRIEF.md
            └── component/state implementation
```

A surface may override the site system only when its job requires it. Record the exception and preserve shared semantics.

### 9.6 Implementation plan

Plan the smallest coherent slice:

1. foundation and tokens;
2. global shell and navigation;
3. one representative route or vertical slice;
4. shared components only after repetition is real;
5. remaining routes;
6. content/asset integration;
7. state and edge coverage;
8. analytics, SEO, legal, and launch controls;
9. audits and regression checks.

### 9.6A Reusable block contract

Do not create a block library for one site. Create or extend one only when the same semantic block is reused across routes/projects or when its state/accessibility/motion logic must be fixed once.

A reusable block record should include:

```yaml
name: evidence-led-hero
category: hero
dial_compatibility:
  variance: [5, 9]
  motion: [1, 7]
  density: [2, 5]
when_to_use: "One clear claim with one strong proof asset."
not_for: "Multi-step product UI or an editorial article opening."
stack: [semantic-html, css-grid]
```

And these body sections:

1. visual sketch and content relationship;
2. props/content API and required truth statuses;
3. minimum working implementation in the real stack;
4. narrow-screen recomposition and long-content behavior;
5. interaction states and keyboard semantics;
6. motion bands and reduced-motion substitution;
7. theme/material notes;
8. accessibility and performance risks;
9. anti-patterns and misuse cases;
10. source/provenance and one runnable check.

Do not add speculative variants “for later.” The block is complete when one real use proves it and one repeated use confirms the abstraction.

### 9.7 PRODUCE gate

Do not scale implementation until the content, tokens, representative components, and first route prove the direction in real code or a law-level comp.

## 10. BUILD — Implement the smallest complete system

### 10.1 Build order

Before implementation, lock the deliverable count: routes, files, sections, components, states, and requested formats. The final check compares shipped items against this count.

Production output MUST NOT replace requested work with placeholder comments such as `TODO`, `implement here`, `same as above`, `rest follows this pattern`, or a bare ellipsis. A deliberate backlog marker is allowed only when the user requested a scaffold or the unimplemented scope is explicitly excluded.

1. Preserve existing repository conventions and working behavior.
2. Establish semantic HTML and content order.
3. Bind tokens and fonts.
4. Build the smallest representative page slice.
5. Add interaction with native platform features first.
6. Add states and failure handling as part of the component, not later.
7. Recompose for narrow, medium, wide, coarse-pointer, and keyboard contexts.
8. Add motion only after the static hierarchy works.
9. Instrument meaningful events.
10. Run the project’s checks before adding polish.

### 10.2 Native-first implementation

Prefer:

- links for navigation and buttons for actions;
- `<details>/<summary>` for simple disclosure;
- native form types, validation attributes, `autocomplete`, and `inputmode`;
- CSS Grid/Flexbox, container queries, `clamp()`, logical properties, and media queries;
- browser image selection with `srcset`, `sizes`, and `<picture>`;
- `Intl` for dates, numbers, currency, relative time, and plural rules;
- native dialog only when a dialog is actually required and its focus behavior is understood;
- View Transitions or CSS transitions for simple state continuity;
- progressive enhancement when core content can work without JavaScript.

Do not add a carousel, modal, date picker, animation library, validation framework, or state layer because it is familiar. Add it because the requirement exceeds the native solution.

### 10.3 Component rule

Create a reusable component when at least one is true:

- the pattern repeats with the same semantics;
- state logic is non-trivial and must be fixed once;
- accessibility behavior is easy to get wrong in multiple places;
- the design system explicitly defines it as a primitive.

Do not create an interface for one implementation, a factory for one component, or a generic configuration object for values that never vary.

### 10.4 Content and layout order

DOM order follows meaning and keyboard reading order. CSS may create visual tension, but it must not invert the narrative or focus sequence. Never rely on absolute positioning to repair weak structure.

### 10.5 Browser surfaces

Theme the browser-owned details that expose assembly-line work:

- text selection;
- caret;
- focus ring;
- link underline thickness and offset;
- visited links when relevant;
- scrollbars when custom treatment remains usable;
- form autofill;
- placeholder text;
- tabular numerals;
- media controls when custom controls are justified.

### 10.6 Build truthfully

- No fake API data that can be mistaken for production.
- No invented customers, ratings, reviews, awards, security badges, or partner logos.
- No hidden pricing invented for composition.
- No links that look active but do nothing.
- No “coming soon” behavior unless explicitly part of the product.
- Label demonstrations and sample data.

### 10.7 Minimal runnable check

Every non-trivial branch, parser, form path, money/security path, or shared state transition leaves one small runnable check behind. Use the project’s existing test system. For a tiny standalone prototype, a focused assertion or smoke test is enough.

### 10.8 BUILD gate

The representative route must work with real content, keyboard input, narrow screens, slow data, and at least one failure state before the rest of the site is multiplied.

---

## 11. TASTE — Judge the work as a designed whole

Taste is not personal preference. It is the disciplined comparison of the artifact against the brief, chosen visual world, and human perception.

### 11.1 First-pass questions

- Is there one obvious entry point?
- Does the first viewport communicate product, audience, value, proof, and action?
- Can the eye reconstruct the page hierarchy in a three-second scan?
- Is the signature system visible without overpowering the product?
- Does the page alternate tension and rest, density and breathing room?
- Does each section earn its place?
- Are the strongest claims supported by the strongest evidence?
- Does the site look authored at mobile width, or merely collapsed?
- Does motion clarify state and space, or advertise the animation system?
- Is the product recognizable with the logo removed?

### 11.2 Interchangeability test

Temporarily replace the brand name, logo, and primary accent with an unrelated company from the same category.

- If the page still feels plausible, the concept is too generic.
- If only the copy makes it specific, the visual world is underdeveloped.
- If only a decorative motif makes it specific, the concept is attached rather than structural.

Fix the product mechanism, evidence display, composition, and signature system—not just the decoration.

### 11.3 Squint and grayscale tests

- Squint: hierarchy and section rhythm should remain legible.
- Grayscale: emphasis should survive without color.
- Blur thumbnail: the silhouette should not match the category’s default template.
- Text-only: the message should remain coherent without images.
- Image-off: layout must not collapse and essential meaning must remain.

### 11.4 Before / after / why review

For every proposed design correction, state:

- **Before:** the current observable issue.
- **After:** the specific change.
- **Why:** the effect on comprehension, trust, conversion, accessibility, or system coherence.

Do not use “looks cleaner” as a reason.

### 11.4A AI-tell audit

Review recurring model habits as evidence, not superstition. Ask whether each occurrence is required by content, brand, or function.

Common tells worth challenging include:

- version/beta labels, section-number eyebrows, pseudo-technical metadata, or locale/weather strips added only to make a page feel designed;
- decorative colored status dots with no semantic state;
- performative labels such as “quietly trusted,” “from the field,” or faux archival captions without real provenance;
- fake product screenshots made from meaningless rectangles, fake terminals, fake sync timestamps, or fabricated precision;
- an eyebrow above every heading, a divider around every row, a pill around every label, or a card around every idea;
- repeated centered heroes, split text/image sections, bento grids, marquees, and fade-up reveals regardless of content;
- multiple CTA labels that all describe the same intent;
- a punctuation, font, icon, or palette ban applied because a source skill declared it rather than because the project needs it.

Classify findings as:

- `ABSOLUTE`: truth, accessibility, security, broken behavior, unknown rights;
- `PROJECT BAN`: documented in `DESIGN.md` because it violates this brand/world;
- `MECHANICAL TELL`: repeated by habit and should be reduced or varied;
- `ALLOWED`: intentional, useful, and compatible with the brief.

The audit must explain the harm. “Looks AI-generated” is a symptom; identify the repetition, meaninglessness, mismatch, or quality defect beneath it.

### 11.5 TASTE gate

The page should be understandable, recognizable, and coherent before technical audit. Do not polish a concept that still fails the brief.

---

## 12. RESOLVE — Fix causes, not isolated symptoms

### 12.1 Priority

Fix in this order:

1. P0 blockers: data loss, broken actions, security, inaccessible task completion.
2. P1 major: WCAG AA failures, misleading content, severe responsive or performance problems.
3. P2 minor: friction with a workaround, local inconsistency, small content defects.
4. P3 polish: visual refinement with no material user impact.

### 12.2 Systemic fixes

Prefer:

- correcting a token over patching fifteen components;
- fixing a shared primitive over adding route-specific workarounds;
- correcting content structure over positioning hacks;
- fixing data/error handling at the shared boundary;
- deleting an unneeded pattern over styling it harder;
- removing an effect over optimizing an effect that contributes nothing.

### 12.3 Preserve the chosen world

Corrections must not slowly average the site back into category convention. When accessibility, performance, or responsive constraints require a change, preserve the design thesis through other vectors.

### 12.3A Redesign modernization order

For a preserve-mode redesign, apply the lowest-risk levers first and stop when the brief is satisfied:

1. typography and content hierarchy;
2. spacing, rhythm, alignment, and width;
3. semantic palette/token recalibration while preserving owned brand color;
4. states, interaction feedback, focus, and motion appropriate to the existing world;
5. hero and key-section recomposition;
6. full block replacement only where the existing structure cannot be repaired.

Targeted evolution often creates most of the visible lift with less SEO, analytics, content, and implementation risk than a wholesale rebuild. Overhaul mode may replace the visual language, but it still obeys the preservation inventory in Section 5.3A.

### 12.4 One regression check

After each non-trivial systemic fix, run the smallest check that would fail if the defect returns. Do not build an entire new test architecture for one correction.

### 12.5 RESOLVE gate

No known P0 or P1 issue remains. Any accepted P2 risk is recorded with owner and rationale.

---

## 13. SEE — Inspect the rendered experience in context

### 13.1 Batched visual QA

Inspect one batch across:

- narrow mobile around 320–390 CSS px;
- common mobile around 390–430 px;
- tablet/medium layout;
- laptop width;
- wide desktop/4K constraint behavior;
- coarse and fine pointer behavior;
- light/dark/high-contrast contexts where supported;
- reduced-motion preference;
- zoom and text scaling.

Fix findings together, then run one confirmation batch.

### 13.2 Real-context checks

Emulation is insufficient for:

- touch latency and hit areas;
- mobile keyboard and viewport behavior;
- safe areas and browser chrome;
- real CPU/GPU constraints;
- font rendering;
- screen-reader interaction;
- network variability.

Test at least one real iOS device and one real Android device when the audience materially uses mobile. Include a lower-powered device for media- or motion-heavy sites.

### 13.3 Network and data checks

Test:

- offline and timeout;
- slow connection;
- blocked third-party scripts;
- image failure;
- API 400, 401, 403, 404, 429, and 500 paths when applicable;
- empty data;
- extreme data volume;
- duplicate submit and race conditions.

### 13.4 Accessibility observation

Use automated tools as a floor, then manually test:

- keyboard-only path;
- visible and unobscured focus;
- skip links and landmarks;
- screen-reader labels, order, live announcements, and errors;
- 200% zoom and reflow;
- reduced motion;
- forced colors/high contrast where relevant;
- drag alternatives and touch targets.

### 13.5 Performance observation

Use lab tools during development and field/RUM data after launch. A lab score is not field experience. Identify the actual LCP element, long interactions, layout shifts, third-party costs, and low-end device behavior.

### 13.6 SEE gate

The site must survive the contexts users actually have, not only the designer’s browser at the designer’s viewport.

---

## 14. POLISH — Finish the product, not just the screenshot

### 14.1 Final visual pass

Check:

- optical alignment, not only mathematical alignment;
- line breaks and widows at all breakpoints;
- consistent icon stroke and baseline;
- image crop and focal point;
- rhythm between related and unrelated groups;
- border, radius, and elevation logic;
- text selection, caret, focus, underlines, and scrollbars;
- animation interruption and exit timing;
- accent scarcity;
- no accidental default browser or framework styling.

### 14.2 Final content pass

- Replace all filler and illustrative copy.
- Verify names, dates, prices, claims, links, legal notices, and contact details.
- Confirm CTA verbs describe the actual next step.
- Remove duplicate statements.
- Confirm alt text and captions.
- Confirm page title, description, social image, canonical, and structured data.
- Confirm 404, empty search, and unavailable-product language.

### 14.3 Final operational pass

- analytics events fire once and carry no unnecessary personal data;
- forms reach the correct destination and have spam/retry handling;
- consent and privacy behavior match the actual integrations;
- redirects, sitemap, robots, canonical, and indexing rules are correct;
- preview, deployment, rollback, and ownership are documented;
- monitoring covers availability, errors, and Core Web Vitals where justified;
- assets and licenses are preserved.

### 14.4 Finish rule

Stop when every release requirement is met and further changes are preference churn. A finished site is not one with the most effects; it is one whose decisions are coherent and whose remaining imperfections do not harm the user or business.

---

# Part II — Business and Content Architecture

## 15. Business strategy and message architecture

### 15.1 The website’s business job

Choose one primary business objective per surface:

- generate qualified leads;
- start trial or account creation;
- complete a purchase or booking;
- request a demo or consultation;
- explain a complex product;
- establish trust and legitimacy;
- grow an audience or subscription;
- recruit talent or partners;
- support current customers;
- direct visitors to a physical location or event.

Secondary objectives may exist, but they must not compete visually with the primary action.

### 15.2 Visitor-decision model

Organize content around the visitor’s questions, not a template’s section names:

1. **Orientation:** What is this and who is it for?
2. **Relevance:** Does it solve my situation?
3. **Mechanism:** How does it work or create the outcome?
4. **Evidence:** Why should I believe it?
5. **Experience:** What will using, buying, or working with it feel like?
6. **Difference:** Why this instead of alternatives or doing nothing?
7. **Risk:** What are the limits, costs, obligations, and protections?
8. **Action:** What happens next?

A page may answer these in any order appropriate to visitor awareness. Do not force every site into Hero → Features → Pricing → FAQ → CTA.

### 15.3 Claim architecture

Every important claim SHOULD follow:

> **Claim → Mechanism → Proof → Implication**

Example structure, not production copy:

- Claim: the product reduces manual reconciliation.
- Mechanism: it matches records using a defined workflow.
- Proof: a live product demo or measured case study.
- Implication: the operator can close the process sooner.

A claim without mechanism feels inflated. A mechanism without implication feels technical. Proof without context can mislead.

### 15.4 Audience specificity

Describe the audience through decisions and constraints, not demographics alone:

- what triggers their visit;
- what they already know;
- what language they use;
- who approves the purchase;
- what risk they fear;
- what alternative they compare;
- what evidence they trust;
- what device and environment they use;
- what accessibility, language, or connectivity constraints apply.

### 15.5 Awareness and intent

Match the page to visitor state:

| State | Need | Page behavior |
|---|---|---|
| Problem unaware | recognition and education | show the situation without over-selling |
| Problem aware | framing and consequences | clarify why current workarounds fail |
| Solution aware | mechanism and difference | demonstrate how this approach works |
| Product aware | proof, risk, and fit | compare, answer objections, show real usage |
| Most aware | transaction clarity | price, availability, action, and next step |

Do not open a high-intent pricing visitor with a long philosophical manifesto. Do not ask a low-awareness visitor to “Start now” before they understand the category.

### 15.6 Offer and CTA hierarchy

- One primary CTA per surface.
- A secondary CTA is allowed when it serves a different readiness level, such as “View demo” beside “Start trial.”
- CTA copy names the next step: `Book a 20-minute review`, `See the product`, `Start the free workspace`, `Get the estimate`.
- Do not use `Learn more` when a more specific verb exists.
- State what follows after high-friction actions.
- Place the CTA where the visitor has enough evidence to act; repeat it after major proof or objection resolution, not mechanically every section.

### 15.7 Proof without fake social proof

When logos, testimonials, metrics, or case studies are unavailable, use:

- a product walkthrough;
- process transparency;
- sample output clearly labeled;
- founder or team credentials;
- methodology and limitations;
- public documentation or source code;
- transparent pricing and terms;
- a low-risk trial or consultation.

Never fill a design hole with invented trust.

### 15.8 Objection matrix

For each primary audience, record:

| Objection | Type | Evidence/answer | Best surface |
|---|---|---|---|
| “Will this work for my case?” | fit | use case, constraints, example | use-case page |
| “Is it worth the cost?” | value | comparison, outcome, pricing context | pricing/ROI section |
| “Can I trust it?” | risk | security, team, process, proof | trust page/FAQ |
| “Is migration difficult?” | effort | timeline, support, compatibility | implementation section |
| “What if it fails?” | risk reversal | trial, cancel, support, guarantee | offer/FAQ |

### 15.9 Success metrics

Define one primary and a small set of diagnostic metrics:

- primary conversion rate or completion rate;
- qualified lead rate, not only form starts;
- CTA exposure and click-through;
- content engagement where it predicts intent;
- error/abandonment by step;
- page performance and accessibility regressions;
- organic search impressions/clicks when SEO matters;
- revenue or pipeline attribution where data quality permits.

Do not optimize a page toward a proxy that harms qualified outcomes.

---

## 16. Site and page grammars

A grammar is a set of relationships, not a fixed order. Select one dominant page grammar and one supporting grammar.

### 16.1 Core functional units

- **Orientation:** identity, offer, audience, navigation.
- **Resonance:** recognizable problem, context, aspiration.
- **Mechanism:** process, architecture, product demo, or unique method.
- **Evidence:** result, case study, quote, credential, comparison, sample.
- **Experience:** interface, service journey, product detail, environment.
- **Objection:** risk, limitation, FAQ, compatibility, policy.
- **Transaction:** price, plan, booking, purchase, signup.
- **Continuation:** related content, next route, support, footer.

Every unit must answer a visitor question or support an action.

### 16.2 Composition grammars

| Grammar | Best for | Structural behavior | Common risk |
|---|---|---|---|
| Editorial spine | thought leadership, services, complex products | strong type hierarchy, paced evidence, asymmetric columns | style without product proof |
| Product theater | SaaS, hardware, tools | product demo owns the page; copy annotates behavior | fake UI and excessive animation |
| Field guide/manual | technical, operational, educational | numbered or annotated procedures, diagrams, evidence | turning everything into documentation |
| Catalog/collection | ecommerce, portfolios, media | repeatable items with strong filtering and image rules | interchangeable card grid |
| Manifesto/poster | launches, cultural brands, events | monumental statements, sparse proof, bold rhythm | ambiguity and inaccessible type |
| Dossier/case file | B2B, security, research | sourced claims, metadata, comparison, evidence | density without hierarchy |
| Spatial journey | hospitality, real estate, experience brands | full-bleed environments, route-like pacing | media weight and orientation loss |
| Product laboratory | technical or scientific products | mechanism, test, data, interactive demonstration | decorative pseudo-science |
| Command console | operational products | state, controls, live data, utility | dashboard cosplay on marketing pages |
| Journal/story | founder brands, media, community | chronology, voice, artifacts, human detail | weak transaction path |

### 16.3 Hero alternatives

Use the hero form that best resolves orientation:

- product-first live or recorded demo;
- proof-first result or case study;
- problem-first recognizable scene;
- mechanism-first diagram or physical process;
- editorial headline with supporting evidence;
- split narrative with product and audience context;
- catalog opening with a featured item;
- service promise with concrete scope and next step;
- spatial/cinematic opening for experience mode.

Avoid the default centered headline, vague subhead, two pills, and floating dashboard mockup unless the brief genuinely earns it.

### 16.4 SaaS and software sites

Prioritize:

- real product behavior rather than decorative dashboards;
- role/use-case specificity;
- integrations and constraints;
- onboarding effort and time-to-value;
- security, data handling, and support where relevant;
- transparent plan differences;
- a credible path from marketing claim to product screen.

Common rut: indigo gradient, floating glass panels, generic bento features, invented 10× claims, and identical icon cards.

### 16.5 Ecommerce and product sites

Prioritize:

- product identity and image consistency;
- price, availability, variants, delivery, returns, and total cost;
- material, dimensions, compatibility, and care;
- comparison and selection support;
- trustworthy reviews only;
- cart and checkout clarity;
- stock, failure, and delayed-shipping states;
- product structured data only when accurate and visible.

Do not hide critical purchase information behind decorative interaction.

### 16.6 Editorial, media, newsletter, and community sites

Prioritize:

- reading hierarchy and line length;
- recency, authorship, sourcing, taxonomy, and related content;
- subscription value and frequency;
- archive/search/filter behavior;
- share and citation behavior;
- ad/sponsor distinction;
- accessible media and transcripts;
- route-level identity without destroying publication consistency.

Common rut: generic cards for every story, same visual weight for all content, and subscription prompts that interrupt reading before value is established.

### 16.7 Service and professional-business sites

Prioritize:

- exact scope, geography, availability, and client fit;
- process and what the engagement requires from the client;
- team credibility and named expertise;
- work samples or case studies;
- pricing model or expectation when possible;
- a low-friction qualified inquiry path;
- phone, hours, address, and location details for local businesses.

Common rut: stock-photo hero, vague “solutions,” icon grid, and an unqualified contact form.

### 16.8 Portfolio and agency sites

Prioritize:

- work before self-description;
- role and contribution clarity;
- outcome, constraints, and process for each case;
- visual variety within a coherent shell;
- contact availability and engagement fit;
- fast media and accessible case-study navigation.

Common rut: motion-heavy intro that delays the work, giant manifesto copy, and projects with no explanation of contribution.

### 16.9 Course, event, membership, and community sites

Prioritize:

- transformation and who it is for;
- curriculum/program/schedule;
- instructor or host credibility;
- format, dates, time commitment, access period, and prerequisites;
- community behavior and moderation expectations;
- price, refund, cancellation, and support;
- proof of outcomes without cherry-picked ambiguity.

### 16.10 Nonprofit and public-service sites

Prioritize:

- mission translated into specific action;
- beneficiary and program evidence;
- financial and governance transparency;
- donation use, recurring options, and receipts;
- accessible language and low-bandwidth behavior;
- multilingual and assistive-technology needs;
- crisis or essential information without visual obstruction.

### 16.11 Navigation

- Navigation labels use audience language, not internal organization terms.
- Keep the primary set small enough to scan.
- Current location is clear.
- Mobile navigation is not a compressed desktop mega-menu.
- Do not hide the primary action inside the menu when it must remain visible.
- Use breadcrumbs for deep information hierarchies, not shallow landing pages.
- Search is present when content scale and visitor behavior justify it.

### 16.12 Footer

The footer is a continuation surface, not a graveyard. Include only relevant:

- key navigation and audience paths;
- contact/location/support;
- legal/privacy/accessibility;
- social channels the business actually maintains;
- newsletter or CTA with distinct value;
- copyright and ownership;
- locale/currency controls;
- status/security links for technical products.

---

# Part III — Visual and Interaction Craft

## 17. Layout and composition

### 17.1 One dominant entry point

Every visual region has one primary. Long pages may establish a new primary at an intentional pacing reset, but two simultaneous co-primaries create noise.

Use at least two hierarchy vectors for the dominant element:

- scale;
- weight;
- spacing;
- tracking;
- alignment or grid break.

Hierarchy is relative. To promote one element, demote others.

### 17.2 Semantic role and visual role

An `<h1>` may be visually quieter than a nearby statement, and body copy may act as display type, when:

- DOM and reading order preserve meaning;
- proximity makes relationships clear;
- only one visual primary exists;
- a quick scan still reveals primary, support, and incidental information.

Visual inversion is allowed. Structural confusion is not.

### 17.3 Grid

Define:

- content maximums and full-bleed exceptions;
- primary columns and gutters;
- baseline/rhythm unit;
- alignment anchors;
- narrow-screen collapse/recomposition;
- intentional break rules.

Use grid breaks to signal importance, not because every section needs novelty.

### 17.4 Spacing as information

- Tight spacing groups related items.
- More space above a heading separates it from the previous idea.
- Less space below a heading binds it to its content.
- Isolated elements read as important even at small sizes.
- Uniform section spacing destroys pacing.

Alternate density deliberately. One tight evidence block beside one generous statement often feels more authored than uniform cards.

### 17.5 Cards

A card is earned when it groups content that behaves as one object, has a boundary, or needs independent interaction. It is not the default page container.

MUST NOT:

- nest cards;
- place every icon, heading, and paragraph in identical rounded rectangles;
- combine a border and broad shadow without a deliberate elevation system;
- use a colored side stripe as generic emphasis;
- turn plain lists or sections into cards solely to “add depth.”

### 17.6 First viewport

The first viewport should feel like the beginning of a system, not a detachable poster. It must establish:

- page identity and navigation;
- dominant message;
- evidence or product signal;
- action;
- the governing composition and material behavior.

### 17.7 Scroll pacing

Treat the page as a sequence:

- open with orientation;
- vary density and scale;
- use transitions between ideas, not identical entrance animations;
- place proof near the claim it supports;
- place transaction after sufficient confidence;
- end with a real next step.

### 17.8 Width and measure

- Body text generally reads well around 45–75 characters; sustained editorial copy often works near 60–75ch.
- Do not stretch text to fill 4K screens.
- Let media or spatial composition use wide canvases while copy remains constrained.
- Use `min-width: 0` on flex/grid children where content can overflow.

### 17.9 Optical correction

Mathematical centering is a starting point. Correct for:

- type cap height and punctuation;
- asymmetric logos and icons;
- image subject weight;
- rounded geometry;
- perceived rather than measured whitespace.

### 17.10 Composition repetition budget

Coherence requires repetition; authored work requires controlled variation.

Defaults for a marketing page with eight or more major sections:

- use at least four meaningful layout families unless the chosen world is intentionally systematic;
- do not repeat the same major layout family in adjacent sections without a semantic reason;
- cap a simple left/right zig-zag sequence at two consecutive uses;
- use no more than one decorative marquee per page unless continuous ticker behavior is the product function;
- ration decorative eyebrows to roughly one per three major sections; functional labels and navigation are exempt;
- a bento grid has exactly the number of cells required by its content—no blank or filler tile to complete geometry;
- repeated proof, pricing, or catalog units may share a system, but their internal hierarchy must reflect their actual content rather than identical placeholder anatomy;
- hero compositions should not repeat mechanically across adjacent routes in the same site.

These are review budgets, not automated absolutes. Break them when repetition is the meaning—such as a product catalog, comparison table, timeline, or editorial index—and record that reason.

---

## 18. Typography

### 18.1 Select type by job and culture

Choose fonts based on:

- audience and use scene;
- visual-world thesis;
- content density and reading length;
- required language/script coverage;
- available weights, styles, numerals, and OpenType features;
- license and hosting rights;
- rendering and file cost;
- fallback compatibility.

Do not default to Inter/system sans, a generic geometric sans, or a fashionable serif without evidence. System fonts are valid when speed, platform familiarity, or utilitarian neutrality is the intention—not when font research was skipped.

### 18.2 Type roles

A site normally needs no more than:

- **display:** identity and major entry points;
- **body:** sustained reading;
- **utility:** navigation, controls, metadata;
- **data/code:** measurements, tables, code, or technical notation when needed.

One family may fill multiple roles. Do not add a monospace merely to look technical.

### 18.3 Hierarchy behavior

- One dominant entry point per region.
- Adjacent levels differ through at least two vectors or one strong jump.
- Weight should jump when it carries hierarchy; a regular→medium→semibold→bold ladder often looks default.
- No more than three obvious levels above the fold unless the content truly demands more.
- Scale is not the only hierarchy tool.

### 18.4 Practical floors

Defaults, not rigid constants:

- mobile body text: 16 CSS px or larger;
- small secondary text: use sparingly and maintain contrast/readability;
- body line-height: roughly 1.45–1.7 depending on face and measure;
- display line-height: often 0.9–1.15 depending on face and size;
- tracking on large display text: avoid tighter than about `-0.04em`; many faces prefer `-0.02em` to `-0.03em`;
- all-caps labels: add positive tracking, often at least `0.06em`, and keep them short;
- use tabular numerals for aligned data;
- balance short headings intentionally; do not force balanced wrapping on long body text.

Test the actual font and copy. Numeric defaults do not replace optical judgment.

### 18.5 Responsive type

Use fluid sizing when it improves continuity:

```css
.hero-title {
  font-size: clamp(2.5rem, 7vw, 6rem);
}
```

But set content-driven breakpoints when line breaks or hierarchy fail. Do not let a fluid formula produce unreadably large or tiny type.

### 18.6 Font loading

- Self-host when licensing and operations support it.
- Subset only when language coverage is known.
- Load only used weights/styles.
- Use `font-display` appropriate to the experience.
- Preload only the critical face actually needed above the fold.
- Match fallback metrics with `size-adjust`, ascent/descent overrides, or a compatible fallback when layout shift matters.
- Do not hide the entire page waiting for decorative fonts.

### 18.7 Content stress test

Test:

- one-character and 100-character headings;
- German-length expansion;
- CJK and Arabic/Hebrew where relevant;
- URLs, long tokens, and unbroken strings;
- 200% zoom and user text enlargement;
- missing optional labels;
- numerals and currency extremes.

### 18.8 Typographic anti-patterns

- gradient text as generic emphasis;
- all headings bold and every label uppercase;
- same size/weight/spacing for multiple levels;
- display font used for long body copy without legibility evidence;
- faux bold/italic;
- licensed font referenced but not shipped;
- `letter-spacing` copied from another face;
- system display face on an otherwise ownable brand world without intent.

### 18.9 Typographic mechanical quality

- Prefer same-family emphasis—weight, width, optical size, style, case, or spacing—before adding another face.
- When italic display words include descenders such as `g`, `j`, `p`, `q`, or `y`, reserve enough line-height and bottom space to avoid clipping.
- Use one dominant copy register per surface. Technical notation, editorial prose, and punchy marketing copy may coexist only through an explicit voice hierarchy.
- A hero headline normally resolves in one or two lines on desktop, with concise support and visible primary action; treat this as a composition target, not permission to distort truthful copy.
- Long CTA labels should not wrap on desktop. Shorten the action or give the control sufficient width.
- Avoid using all-caps micro-labels, numbering, punctuation, or monospace as a universal “designed” accent.

---

## 19. Color and material

### 19.1 Derive color from the world

Use product materials, audience environment, approved brand assets, photography, and use context. Do not choose light or dark mode by category habit.

Ask:

- Where is the site used and under what ambient light?
- Does color identify actions, categories, data, or atmosphere?
- Which color is owned by the brand, and which colors are functional?
- How will photography and product UI interact with the palette?

### 19.2 Semantic palette

At minimum define:

- canvas/background;
- one or more surfaces;
- primary and secondary text;
- border/divider;
- accent and accent-contrast;
- positive, warning, danger, and information states;
- focus indicator;
- selection/caret;
- link and visited link where relevant.

Tint neutrals toward the world. Pure neutral gray/black can feel detached from a strongly colored surface.

### 19.3 Accent scarcity

Accent color indicates priority. When everything is accented, nothing is.

As a default:

- reserve the strongest accent for one or two visible decisions per screen;
- use tonal variants or structure for secondary emphasis;
- do not repeat accent on every icon, border, heading, and badge;
- do not use color as the only state signal.

### 19.4 Contrast

Target WCAG 2.2 AA:

- normal text at least 4.5:1;
- large text at least 3:1;
- meaningful non-text UI and focus indicators at least 3:1 where the criterion applies;
- placeholder and secondary text remain readable;
- text over images has a tested treatment, not a hopeful overlay.

On colored surfaces, derive muted text from the foreground or surface hue rather than dropping in generic gray.

### 19.5 Gradients, transparency, and texture

They are allowed when they belong to the selected world and remain performant and accessible.

- Avoid generic purple→blue “trust” gradients.
- Avoid gradient text as default emphasis.
- Avoid glass/blur as decoration.
- Give reduced-transparency users a more opaque alternative where appropriate.
- Texture must come from the subject’s material world, not arbitrary grain, grids, or stripes.
- A broad zero-offset colored glow is not depth.

### 19.6 Dark mode

Dark mode is not a recolor switch. Define:

- elevation behavior;
- image treatment;
- text and muted-text contrast;
- focus and link states;
- color-state recalibration;
- native controls and browser surfaces;
- shadows versus borders.

Offer it when the use scene, brand, or product supports it. Do not add a theme toggle merely as a design feature.

### 19.7 Forced colors and color vision

- Test Windows forced-colors/high-contrast behavior when audience requirements justify it.
- Keep borders, focus, selected state, and icons legible without custom colors.
- Use labels, patterns, position, or icons in addition to color for status and charts.

### 19.8 Palette coherence and category-rut rotation

- Use one neutral temperature/family unless the contrast between warm and cool surfaces is a documented part of the world.
- Use one dominant accent family; semantic status colors remain functional, not competing brand accents.
- Lock the page’s substrate family. A mid-page light/dark inversion is allowed only as one deliberate transition with a reason and accessible continuity.
- Audit category palette ruts. “Premium consumer” should not reflexively mean cream paper, brass/clay/oxblood accents, and espresso text any more than “AI” should mean violet-blue neon.
- Generate alternative palette families from product materials, customer environment, photography, and cultural references—not from a memory of what the previous generated project used.
- A category-default palette may be correct when it is owned by the brand or materially grounded. Document the evidence instead of banning the color family by hex code.

---

## 20. Imagery, art direction, and media

### 20.1 Every image needs a job

An image may:

- prove the product;
- show the customer context;
- explain a mechanism;
- establish atmosphere;
- demonstrate scale or material;
- identify a person, place, or item;
- carry narrative transition.

Delete images whose only job is “make the section less empty.”

### 20.2 Art-direction contract

For each image family define:

- subject and behavior;
- camera distance and angle;
- lighting and contrast;
- background/environment;
- crop and focal-point rules;
- color treatment;
- texture and grain policy;
- caption/credit behavior;
- mobile and wide-screen variants;
- relationship to type and negative space.

Consistency of behavior matters more than using the same filter.

### 20.3 Product imagery and screenshots

- Use real UI or clearly labeled prototypes.
- Show a meaningful state, not a decorative dashboard collage.
- Preserve legibility; do not shrink a full app until text becomes noise.
- Crop to the behavior being explained.
- Annotate only what the copy needs.
- Keep browser/device chrome consistent with the visual world.
- Do not fake customer data or capabilities.

### 20.4 Photography

- Prefer product- or audience-specific photography over generic stock.
- Obtain releases and usage rights.
- Avoid visual stereotypes.
- Preserve skin tone and subject dignity.
- Art-direct negative space for responsive type placement.
- Do not use a geometric circle/polygon as a cheap mask for an organic subject; use a real alpha matte or a clean crop.

### 20.5 Generated imagery

Generated media MAY be used when rights, disclosure, and brand context allow it.

- Establish a repeatable prompt/style bible.
- Lock character, product, material, lens, light, and palette behavior.
- Check anatomy, text, logos, product accuracy, cultural representation, and artifacts.
- Do not imply a generated person is a real customer, employee, or witness.
- Preserve generation provenance and final edits.

### 20.6 Responsive media

Use:

- explicit width/height or `aspect-ratio` to prevent layout shift;
- `srcset` and `sizes` for resolution selection;
- `<picture>` for different crops/compositions;
- modern formats with supported fallbacks;
- lazy loading below the fold;
- eager/high-priority loading only for the true LCP image;
- poster images and captions/transcripts for video;
- reduced-data alternatives when valuable and supportable.

### 20.7 Video and 3D

Use video, WebGL, or 3D only when the medium communicates something static media cannot.

- Provide controls, captions, and pause behavior.
- Avoid autoplay audio.
- Do not block orientation or primary action behind a loading scene.
- Provide a static fallback.
- Profile low-end devices.
- Pause work offscreen and on hidden tabs.
- Preserve reduced-motion and reduced-data paths.

### 20.8 Reference-image-to-code workflow

When visual reference images are part of the process:

1. **Generate at useful granularity.** Prefer a dedicated horizontal frame for each section or a dedicated screen/state frame. Do not force a full site into one tiny composite.
2. **Lock a design bible.** Record palette, typography mood, grid, spacing, component geometry, image treatment, concept spine, framing, and dials before producing multiple frames.
3. **Preserve system, vary composition.** A section set should feel like one product world without cloning one anchor repeatedly.
4. **Regenerate, do not crop weak evidence.** If a detail is unreadable, create a fresh dedicated view using the same bible instead of enlarging distorted pixels.
5. **Extract a build contract.** For each frame, document hierarchy, layout tracks, spacing, type scale, content, media crop, CTA, components, states, and responsive transformation.
6. **Translate rather than trace.** Production text remains text; controls remain semantic controls; repeated content becomes structured data; media receives responsive sources and alt behavior.
7. **Reconcile impossible imagery.** Image models may invent fonts, copy, interactions, or geometry that cannot survive real content. The written contract and live implementation correct these inventions while preserving the governing composition.
8. **Validate both directions.** Compare implementation to the reference for visual intent, then compare it to product truth, accessibility, performance, and responsive requirements. The reference is not allowed to overrule the product.

---

## 21. Icons, illustration, diagrams, and data

### 21.1 Icons

- Use a real, consistent icon system or authored SVG.
- Match stroke, optical size, corner, cap, and fill behavior.
- Use `currentColor` when appropriate.
- Label unfamiliar icons.
- Hide purely decorative icons from assistive technology.
- Do not use emoji or random Unicode glyphs as feature icons.
- Do not place a rounded-square icon tile above every heading.
- Do not add icons that repeat the adjacent word without adding recognition.

### 21.2 Illustration

Illustration must have a defined visual grammar and production quality. Use:

- crisp geometric/vector systems;
- diagrams and linework;
- authored scenes with consistent perspective/material;
- shader or procedural effects when technically and conceptually earned.

Avoid sketchy pseudo-handmade SVG scenes, arbitrary doodles, and turbulence grain when they are merely a shortcut to “personality.”

### 21.3 Diagrams

A diagram should reduce complexity.

- one question per diagram;
- clear start and reading direction;
- labels close to objects;
- consistent notation;
- accessible text equivalent;
- responsive simplification;
- no decorative arrows or nodes with no semantic role.

### 21.4 Data visualization

Choose the chart by the question:

| Question | Preferred forms |
|---|---|
| Compare categories | bar, dot plot, table |
| Show change over time | line, area with restraint |
| Show part-to-whole | stacked bar; pie only for very few clear parts |
| Show distribution | histogram, box plot, strip plot |
| Show relationship | scatter, connected scatter |
| Show rank | sorted bar, bump chart when time matters |
| Show process/funnel | staged counts with denominators |
| Show geography | map only when location is the question |

Rules:

- state source, date range, units, denominator, and uncertainty;
- use accessible colors and direct labels where possible;
- provide a table or textual equivalent;
- do not truncate axes deceptively;
- use animation to preserve object continuity, not to dramatize numbers;
- no 3D charts;
- avoid decorative sparklines/progress rings standing in for actual information.

---

## 22. Components and interaction

### 22.1 Interaction contract

Every interactive element defines:

- semantic element and accessible name;
- default, hover, focus, active/pressed, disabled, pending, success, and error behavior as applicable;
- keyboard behavior;
- touch behavior;
- loading and duplicate-action protection;
- analytics event if meaningful;
- failure and recovery path.

### 22.2 Links and buttons

- Links navigate; buttons act.
- Button text names the action.
- External links are identified when opening a new context matters.
- Underlines or another persistent cue distinguish inline links; color alone is weak.
- Press feedback should be immediate, typically 50–160ms, and may move/scale by a very small amount.
- Disabled controls must remain understandable; prefer explaining why an action is unavailable.
- Pending actions prevent duplicate submission without erasing context.

### 22.3 Hover and pointer behavior

- Hover may enhance but never unlock required functionality.
- Use `(hover: hover)` and pointer queries for context.
- Do not animate standalone images on hover; give the actionable container feedback.
- Keep hover effects fast and restrained because they repeat frequently.
- Coarse-pointer targets SHOULD usually be at least 44×44 CSS px even though WCAG 2.2 AA’s minimum target criterion is 24×24 CSS px with exceptions.

### 22.4 Disclosure, tabs, and accordions

- Use disclosure for optional detail, not to hide primary content.
- Use tabs for peer views whose labels remain visible and whose state is preserved.
- Use accordions when vertical scanning is better than simultaneous comparison.
- Implement keyboard and ARIA patterns correctly.
- Deep-link or persist state when users must return to a specific panel.
- Avoid placing all page content in closed accordions on mobile.

### 22.5 Dialogs and overlays

Use a modal/dialog only when the task requires interruption, protected focus, confirmation, or a contained short flow.

MUST:

- move focus inside on open;
- trap focus only while active;
- restore focus to the logical trigger;
- support Escape unless that would cause data loss without warning;
- label the dialog and explain destructive consequences;
- avoid nested dialogs;
- remain usable with zoom and mobile keyboards.

Prefer inline expansion, a dedicated page, or a non-modal panel when interruption is not necessary.

### 22.6 Tooltips

- Tooltips supplement; they do not contain essential instructions.
- Work on hover and keyboard focus.
- Remain visible while hovered/focused when needed.
- Do not cover the trigger or essential adjacent content.
- Use concise text.
- Mobile requires a different disclosure path.

### 22.7 Toasts and transient feedback

Use toasts for non-blocking, transient confirmation, especially asynchronous completion. Do not use them for:

- critical failures requiring action;
- field validation;
- destructive confirmation;
- information users must retain.

Use a stable screen location, `role="status"` for non-urgent updates, pause auto-dismiss on hover/focus, and avoid stacking noise.

### 22.8 Browser history and state

- Back/forward should behave predictably.
- Filter, search, pagination, and meaningful panel state SHOULD be URL-addressable when users share or revisit them.
- Do not trap users in custom scroll/navigation systems.
- Preserve scroll and focus intentionally after updates.

---

## 23. Forms, feedback, and state coverage

### 23.1 Five required data states

Every surface that fetches, transforms, or accepts data MUST render:

1. **Loading** — scoped to what is loading, with timeout behavior.
2. **Empty** — explanation and next action.
3. **Error** — what happened, why if known, and recovery.
4. **Populated** — normal state.
5. **Edge** — extreme length/volume, missing optional data, RTL, partial network, unusual values.

The most common AI-generated UI defect is designing only the populated state.

### 23.2 Form-specific states

Also cover:

- untouched;
- focused;
- dirty valid;
- dirty invalid;
- submitted pending;
- server rejected;
- submitted success;
- disabled/read-only when applicable.

### 23.3 Labels and instructions

- Every input has a persistent programmatic label.
- Placeholder text is an example or hint, not the label.
- Required/optional expectations are clear.
- Format and constraints appear before error.
- Use native input type, `autocomplete`, `inputmode`, and constraints.
- Do not block paste or password managers.
- Accessible authentication must not require memory puzzles or transcription without alternatives.

### 23.4 Validation timing

- Validate on blur by default.
- After a field has been blurred once, live correction may remove the error as soon as it becomes valid.
- Validate on submit and move focus to the error summary or first invalid field.
- Do not punish the first keystroke.
- Preserve input on every recoverable failure.
- Server-side validation is mandatory at trust boundaries.

### 23.5 Error composition

Every error answers:

1. What happened?
2. Why, if knowable?
3. What can the user do?

Severity matches scope:

- field-level;
- form-level summary plus field markers;
- section-level retry;
- page-level recovery;
- app-level persistent loss-of-function notice.

“Something went wrong” is insufficient when more information is available.

### 23.6 Loading thresholds

Use expected duration to choose feedback:

| Duration | Feedback |
|---|---|
| 0–300ms | usually none |
| 300ms–2s | subtle spinner or matched skeleton |
| 2–10s | labeled spinner or matched skeleton |
| 10–30s | progress when measurable, plus cancel |
| 15s | “taking longer than expected” notice |
| 30–60s | explicit cancel/recovery |
| 60s+ | stop indefinite animation; show retry/cancel/continue |

Skeletons mirror the expected layout. Do not use shimmer forever.

### 23.7 Empty states

Differentiate:

- first-use empty: value + first action;
- no-results empty: echo query and suggest alternatives;
- cleared/complete empty: acknowledge completion and next step;
- permission empty: explain access state;
- error: never masquerade as empty.

### 23.8 Retry and concurrency

- First user retry may be immediate.
- Subsequent automatic retries use capped backoff where appropriate.
- Stop after a small number of failures and offer support/error ID.
- Disable or idempotently handle duplicate submit.
- Cancel stale requests.
- Roll back failed optimistic updates.
- Explain conflicts instead of silently overwriting.

### 23.9 Live announcements and focus

- Non-urgent completion: existing `role="status"` live region; no focus move.
- Inline submit error: announce and focus the first invalid field or summary.
- Critical dialog: `alertdialog` when appropriate; move focus.
- Loading begins: polite announcement; do not focus the spinner.
- User-triggered loaded content may receive focus when it replaces the task context.
- Live region containers should exist before text is injected.

---

## 24. Motion and animation

### 24.1 Motion must earn its place

Before animating, answer:

1. Should this move at all?
2. What user or narrative purpose does movement serve?
3. How frequent is the action?
4. What spatial/state logic should remain continuous?
5. What is the reduced-motion substitute?
6. Can CSS or a native platform feature do it?

Valid purposes include:

- spatial continuity;
- state confirmation;
- explaining a relationship that is inherently temporal/spatial;
- feedback;
- preserving object continuity through layout change;
- avoiding a jarring context switch;
- a rare, brand-defining authored moment in an experience surface.

Invalid purposes include “premium,” “make it interesting,” “show we used GSAP,” or filling dead space.

### 24.2 Frequency gate

| Frequency | Default |
|---|---|
| Keyboard-driven or 100+ times/day | instant; no delaying animation |
| Tens of times/day | remove or reduce to near-instant feedback |
| Occasional | standard transition |
| Rare/first-time | a small amount of delight may be earned |

Keyboard actions must update state immediately. A non-blocking visual confirmation may occur after the state change, but the user must never wait for choreography.

### 24.3 Duration guidance

| Interaction | Typical range |
|---|---:|
| press/toggle/hover | 50–160ms |
| tooltip/popover | 125–200ms |
| dropdown/disclosure | 150–250ms |
| modal/sheet | 200–500ms |
| cross-screen/container morph | 300–500ms, occasionally longer when staged |

Most non-navigation UI transitions SHOULD stay under 300ms and MUST justify exceeding 500ms. Frequent interactions should stay near or below 200ms. Mobile movement often needs shorter duration because travel distances are smaller.

### 24.4 Easing

- Entering UI: strong ease-out.
- Moving/morphing an object already on screen: ease-in-out or a well-tuned spring.
- Color/hover: standard ease.
- Constant motion: linear.
- Exit: faster than entry.
- Avoid ease-in for UI entry.
- Avoid bounce/elastic as a default.

Useful starting curves:

```css
--ease-enter: cubic-bezier(0.23, 1, 0.32, 1);
--ease-move: cubic-bezier(0.77, 0, 0.175, 1);
--ease-standard-m3: cubic-bezier(0.2, 0, 0, 1);
```

Tune to the object, distance, and platform. Do not label the older Material 2 curve as Material 3.

### 24.5 Curve versus spring

- Opacity and color between known values: curve.
- Position, scale, rotation, gesture follow-through, interruption: spring may feel more physical.
- Use modest damping; uncontrolled bounce makes tools feel slow.
- Spring defaults vary radically across libraries. Choose parameters intentionally.

### 24.6 Static hierarchy first

The default, pre-animation state must already be legible. Do not hide every section and reveal it on scroll. One authored moment is usually stronger than identical fade-up entrances on every block.

Avoid entrances from `scale(0)`. A small scale such as ~0.95 plus opacity can work when scale is semantically appropriate.

### 24.7 Technology ladder

1. No animation.
2. CSS transition/keyframes.
3. View Transitions or Web Animations API/native framework capability.
4. Existing installed motion library.
5. GSAP when the requirement needs sequencing, runtime control, scroll linkage, SVG, layout continuity, gestures, or complex interruption.
6. WebGL/shader/custom renderer only when the medium is central and fallbacks exist.

### 24.8 GSAP use

Use GSAP for:

- timelines and coordinated sequences;
- pause/reverse/seek/runtime control;
- scroll-linked or pinned narratives;
- dynamic values;
- SVG drawing/morphing;
- Flip-style layout continuity;
- draggable/observer interactions;
- complex interruption.

Implementation rules:

- register plugins once;
- use `x`, `y`, `scale`, `rotation`, and `autoAlpha` rather than layout properties where possible;
- use timelines and labels, not chains of arbitrary delays;
- scope selectors;
- in React use `useGSAP` or `gsap.context()` and revert on cleanup;
- clean up on unmount/re-render in every framework;
- use `gsap.matchMedia()` for responsive and reduced-motion variants;
- call `ScrollTrigger.refresh()` after meaningful layout changes;
- do not create a trigger for every decorative element;
- avoid broad `will-change`; apply it only where profiling justifies it;
- keep interactions interruptible;
- lazy-load heavy motion code when it is not needed for first paint.

### 24.9 Scroll motion

Scroll is user-controlled. Do not seize it.

- Prefer scrubbed continuity over autoplay sequences that fight the user.
- Pin only when the content relationship genuinely benefits.
- Ensure pinned content has a clear beginning/end and does not trap keyboard or touch users.
- Preserve reading order and provide a static/reduced-motion presentation.
- Avoid excessive scroll-trigger counts.
- Do not animate critical text into unreadable states.
- Scroll progress should remain meaningful when the viewport or content height changes.

### 24.10 View transitions

Use for context continuity when supported, with a no-animation fallback. Skip or simplify under reduced motion. Preserve focus, reading position, live-region behavior, and interaction state; visual continuity is not worth accessibility confusion.

### 24.11 Reduced motion

Every translation, scale, rotation, parallax, or vestibular motion MUST respond to `prefers-reduced-motion: reduce`.

- Remove axis motion or substitute a short opacity/color transition.
- Preserve the state change and information hierarchy.
- Do not apply a global `0.01ms` kill that destroys useful feedback.
- Do not assume View Transitions handles the preference automatically.
- Motion cannot be the only signal.

### 24.12 Ambient and repeated motion

- Loop only when the content is genuinely continuous.
- Provide pause/stop for motion continuing beyond five seconds where WCAG requires it.
- Stop skeleton shimmer when content arrives.
- Reward/confetti animations are one-shot.
- Cancel ambient motion on route change or when hidden.
- Avoid rapid flashing; never exceed applicable WCAG flash thresholds.

### 24.13 Motion plan

For every non-trivial animation, record:

| Field | Required answer |
|---|---|
| Trigger | user action, state, scroll, load |
| Purpose | continuity, feedback, explanation, identity |
| Frequency | high/medium/rare |
| Properties | transform, opacity, clip, SVG, etc. |
| Duration/ease | values and rationale |
| Interruption | how it cancels/reverses |
| Reduced motion | substitute |
| Performance risk | paint/layout/GPU/asset cost |
| Ownership | component/module |

### 24.14 Motion credibility and engine ownership

- Each animated element is owned by one engine. Do not let CSS, Motion, GSAP, and a custom `requestAnimationFrame` loop compete over the same transform or opacity.
- Continuous pointer/scroll values must not flow through React/Vue component state on every frame. Use motion values, scoped GSAP state, CSS scroll-driven animation where supported, or an equivalent render-loop-safe primitive.
- Avoid raw global scroll listeners for animation. Prefer `IntersectionObserver` for visibility, the installed motion library for simple reveals, and ScrollTrigger only for genuine pin/scrub/sequencing.
- For a pinned stack or horizontal pan, verify start at the intended viewport boundary, actual pinning, dynamic end distance, refresh after layout changes, cleanup, reduced-motion fallback, and correct mobile behavior.
- “Motion claimed” must equal motion shipped. If the chosen dial says 7 but scope only supports hover feedback, lower the dial and ship a coherent static system instead of half-working choreography.
- Treat one marquee, one signature scroll sequence, or one ambient loop as a scarce identity resource. Repetition turns authored motion into filler.

## 25. Responsive and contextual adaptation

### 25.1 Recompose, do not shrink

Adaptation changes information priority, layout, interaction, and media behavior for the context. It is not a uniform scale operation.

For each target context, identify:

- viewport and orientation;
- pointer, hover, keyboard, voice, or assistive input;
- network and device capability;
- ambient use scene;
- task duration and attention;
- platform expectations;
- content priority.

### 25.2 Mobile-first foundation

Start with the narrow, content-constrained experience and layer complexity with `min-width` or container queries. This does not mean the desktop design is an enlarged mobile stack; desktop should use its space intelligently.

### 25.3 Content-driven breakpoints

- Stretch the composition until content, hierarchy, or interaction breaks.
- Add a breakpoint there.
- Prefer a few meaningful breakpoints to device-name proliferation.
- Use container queries for reusable modules whose context matters more than viewport.
- Use `clamp()` for values that can fluidly interpolate.

### 25.4 Context transformations

Desktop → mobile may require:

- multi-column to intentional single-column sequence;
- simultaneous comparison to progressive disclosure;
- wide navigation to concise navigation with primary CTA retained;
- hover detail to visible or tap disclosure;
- side panel to inline or bottom sheet;
- wide table to prioritized columns, horizontal region, or card-like rows when semantics survive;
- wide image to a different crop, not merely smaller pixels;
- decorative motion removed or shortened;
- controls moved into thumb reach.

Mobile → desktop may require:

- persistent navigation and context;
- simultaneous panels;
- keyboard shortcuts and multi-select where appropriate;
- richer comparison and data density;
- hover enhancement without hover dependency;
- max-widths to prevent empty 4K stretching.

### 25.5 Input capability queries

```css
@media (pointer: coarse) {
  /* larger targets and spacing */
}

@media (hover: hover) and (pointer: fine) {
  /* optional hover enhancement */
}
```

Screen size does not identify input method. A laptop may have touch; a tablet may have a keyboard.

### 25.6 Safe areas and dynamic viewport

- Use `viewport-fit=cover` only when handling safe-area insets.
- Respect `env(safe-area-inset-*)` for edge-to-edge mobile surfaces.
- Prefer dynamic viewport units such as `dvh` where supported and appropriate.
- Test mobile keyboard resize and fixed/sticky controls.
- Keep focused inputs and submit actions visible.

### 25.7 Core functionality

Do not hide core functionality on mobile. Recompose it. If a feature truly does not belong in the context, explain or route to an appropriate alternative rather than silently removing it.

### 25.8 Responsive content

- Keep meaning and information architecture consistent.
- Shorten copy only when it removes redundancy, not essential detail.
- Do not ship two conflicting content sources for mobile/desktop.
- Avoid `display:none` as a substitute for content strategy; hidden media still may download unless managed correctly.

### 25.9 Responsive testing matrix

Test:

- 320px narrow screen;
- common phone widths;
- portrait and landscape;
- tablet medium layouts;
- laptop and large desktop;
- 200% zoom and text enlargement;
- long translations and RTL;
- coarse and fine pointers;
- mobile Safari and Chromium-based mobile browser behavior;
- real device performance.

---

## 26. Accessibility

### 26.1 Target

Target WCAG 2.2 AA for public business websites unless the governing policy requires more. Treat accessibility as a design and engineering constraint from the first brief, not a final automated scan.

### 26.2 Structure and semantics

- One descriptive page title and primary page heading.
- Logical heading outline without selecting levels for visual size.
- Landmarks: header/banner, navigation, main, complementary, footer/contentinfo as applicable.
- Skip link to main content for repeated navigation.
- Lists, tables, figures, quotes, addresses, time, and controls use semantic elements.
- DOM and reading order follow meaning.
- Use ARIA to supplement native semantics, not replace them.

### 26.3 Keyboard

- Every action is keyboard-operable.
- Tab order is logical and follows visual/context order.
- Focus is visible, sufficiently contrasted, and not obscured by sticky headers, dialogs, or overlays.
- No keyboard trap except a correctly managed active modal.
- Custom widgets implement expected keys.
- Escape closes dismissible overlays.
- Focus returns or advances to a logical destination after actions.

### 26.4 Pointer and touch

- WCAG 2.2 AA minimum target size is 24×24 CSS px with defined exceptions.
- Use roughly 44×44 CSS px as the default usability target for isolated touch controls.
- Provide spacing between small controls.
- Drag interactions have a non-drag alternative.
- Pointer down does not irreversibly commit a destructive action; allow cancellation.
- Do not require path-based or multipoint gestures without alternatives.

### 26.5 Text, zoom, and reflow

- Text can resize to 200% without loss.
- Content reflows without two-dimensional scrolling at narrow equivalent widths except where the content genuinely requires it, such as a data table or map.
- Do not disable browser zoom.
- Avoid fixed-height text containers.
- Preserve content at 400% zoom where the applicable criterion requires reflow.

### 26.6 Color and contrast

- Normal text: at least 4.5:1.
- Large text: at least 3:1.
- Meaningful non-text UI and focus boundaries meet applicable 3:1 requirements.
- Color is not the only state or data signal.
- Links are identifiable within surrounding text.
- Test high contrast/forced colors when relevant.

### 26.7 Images and media

- Informative images have concise meaningful alt text.
- Decorative images use empty alt or CSS and are hidden from assistive technology.
- Complex diagrams have adjacent explanation or long description.
- Video includes captions; audio-only content includes transcript.
- Audio does not autoplay unexpectedly.
- Media controls are keyboard and screen-reader accessible.
- Generated images are described based on their function, not their generation method, while disclosure follows policy/context.

### 26.8 Forms

- Persistent labels and instructions.
- Programmatic association of errors and hints.
- Required state conveyed beyond color.
- Error summary when multiple fields fail.
- Input is preserved.
- `autocomplete` supports user agents and assistive tools.
- Authentication does not depend solely on memorization, puzzles, or blocked password managers.
- Repeated information is auto-populated or selectable when appropriate.

### 26.9 Dynamic content

- Use live regions deliberately.
- Announce status without stealing focus for non-urgent changes.
- Move focus when a user-triggered context replacement requires it.
- Loading, errors, completion, and count changes are understandable without animation.
- Avoid excessive announcements.

### 26.10 Motion and flashing

- Honor reduced motion.
- Provide pause/stop/hide for moving or updating content where required.
- Avoid flashing above WCAG thresholds.
- Do not use motion as the sole instruction or state cue.
- Keep auto-advancing content under user control.

### 26.11 Language and direction

- Set document language.
- Mark meaningful language changes.
- Support `dir="rtl"` and logical CSS properties.
- Mirror directional icons only when meaning should reverse.
- Keep embedded LTR data, code, phone numbers, and email addresses stable inside RTL content.

### 26.12 Accessibility testing

Automated:

- semantic/ARIA checks;
- contrast;
- missing labels/alt;
- obvious focus and landmark defects.

Manual:

- keyboard-only task completion;
- screen-reader smoke test on critical routes;
- zoom/reflow;
- focus visibility and restoration;
- reduced motion;
- high contrast/forced colors;
- touch target and drag alternatives;
- error recovery.

Automated “zero violations” is not proof of accessibility.

---

## 27. Performance and resilience

### 27.1 Performance is design

Performance affects comprehension, trust, conversion, accessibility, and brand perception. Establish a budget before selecting heavy media, fonts, third-party scripts, or motion.

### 27.2 Core Web Vitals targets

Target “good” field performance at the 75th percentile, segmented by mobile and desktop:

- **LCP:** ≤ 2.5 seconds.
- **INP:** ≤ 200 milliseconds.
- **CLS:** ≤ 0.1.

Use lab testing to diagnose before release and real-user monitoring after release when traffic and infrastructure justify it. Lab tests cannot fully measure field interaction experience.

### 27.3 Performance budget

Set route-specific budgets for:

- initial HTML/CSS/JS;
- critical fonts;
- first-viewport images/video;
- third-party scripts;
- long tasks and hydration;
- number of network requests;
- animation/renderer cost;
- LCP, INP, CLS, and supporting metrics;
- low-end mobile behavior.

Do not copy a universal kilobyte number without considering the stack and audience. The budget must be strict enough to force tradeoffs.

### 27.4 LCP

- Identify the actual LCP element.
- Make critical text and media discoverable in initial HTML.
- Do not lazy-load the LCP image.
- Prioritize only the true critical asset.
- Compress and size media appropriately.
- Reduce server and render-blocking delay.
- Avoid client-only rendering for critical marketing content when server/static rendering is available.
- Do not place a heavy intro or animation before meaningful content.

### 27.5 INP

- Keep interaction handlers small.
- Avoid unnecessary hydration and rerenders.
- Break long work into smaller tasks.
- Defer non-critical scripts.
- Use optimistic visual response where safe.
- Virtualize genuinely large lists.
- Debounce/throttle only where semantics permit; do not add latency to every action.
- Profile third-party widgets.
- Avoid layout measurement/write loops.

### 27.6 CLS

- Reserve media and embed dimensions.
- Match font fallbacks and control font swaps.
- Do not inject banners above existing content without reserved space.
- Stabilize async components.
- Use transforms for movement rather than layout jumps.
- Keep cookie/consent UI from unexpectedly shifting the whole page.

### 27.7 Images and video

- Generate responsive sizes.
- Use appropriate modern formats and quality.
- Lazy-load below-fold media.
- Provide poster/fallback.
- Avoid loading desktop video on mobile when a static crop is sufficient.
- Pause offscreen playback.
- Do not preload everything.

### 27.8 Fonts

- Minimize families, weights, and scripts.
- Subset responsibly.
- Preload only critical files.
- Use performant fallback and `font-display` behavior.
- Avoid icon fonts for small icon sets.

### 27.9 CSS and animation

- Prefer transform and opacity for movement.
- Avoid animating width, height, top, left, expensive blur/filter, or huge shadows without profiling.
- Do not apply `will-change` globally or leave it permanently on many elements.
- Reduce active scroll triggers.
- Suspend work offscreen or in hidden tabs.

### 27.10 JavaScript and dependencies

- Ship no JS for static behavior that HTML/CSS already provides.
- Tree-shake and route-split.
- Lazy-load heavy interactive modules.
- Avoid overlapping UI/motion libraries.
- Inspect installed dependencies before adding one.
- Measure the cost of analytics, chat, A/B testing, ads, maps, and embeds.
- Use facades or click-to-load for heavy third-party experiences when appropriate.

### 27.11 Resilience

- Core content survives a blocked third-party script.
- Forms display delivery failure and retry.
- Images and fonts have fallbacks.
- Important contact/purchase information is not dependent on a single widget.
- Timeouts and aborts prevent infinite pending state.
- Partial component failure does not blank the whole page.

### 27.12 Monitoring

Where justified, collect:

- field Web Vitals;
- route and device segmentation;
- JavaScript errors;
- failed network actions;
- form delivery failures;
- uptime;
- deployment version;
- business conversion context.

Do not collect more personal data than the operational question requires.

---

## 28. SEO and discoverability

### 28.1 Search intent and information architecture

- Map one primary intent to each indexable route.
- Avoid multiple thin pages competing for the same intent.
- Use audience language in titles, headings, links, and navigation.
- Create routes because users need them, not only to target keywords.
- Keep important content crawlable in HTML.
- Use internal links that describe the destination.

### 28.2 Page metadata

Every indexable page needs:

- unique, accurate title;
- useful meta description;
- canonical URL;
- correct robots directive;
- social title, description, and image;
- language/locale metadata;
- favicon/app icons and theme color where appropriate.

Do not promise a search snippet Google may rewrite. Metadata is a precise summary, not ad copy disconnected from the page.

### 28.3 Technical SEO

- valid status codes;
- useful 404 and redirect behavior;
- XML sitemap for indexable canonical routes;
- robots.txt that does not accidentally block needed assets/pages;
- noindex for private, duplicate, preview, internal-search, or low-value routes when appropriate;
- stable canonical URL rules;
- pagination/faceted-navigation strategy;
- HTTPS;
- responsive, fast pages;
- international `hreflang` only when localized equivalents are maintained correctly.

### 28.4 Structured data

Use JSON-LD or another supported format only when the data accurately represents visible page content and the page meets the specific feature guidelines.

- Choose the most specific applicable type.
- Include required properties accurately.
- Do not mark up hidden, fake, irrelevant, or misleading content.
- Do not invent ratings, reviews, prices, availability, events, or organization relationships.
- Keep time-sensitive data current.
- Test with the applicable rich-result and schema validators.
- Treat rich-result eligibility as possible, never guaranteed.

### 28.5 Content quality

- Answer the visitor’s actual question.
- Demonstrate experience and specificity.
- Cite or explain evidence where claims matter.
- Keep authorship and update dates honest.
- Avoid generated filler, doorway pages, and duplicated location/service pages with no local value.
- Make sponsorship and affiliate relationships clear.

### 28.6 Social and share behavior

- Social image matches the route, not only the homepage.
- Share title/description remain truthful out of context.
- Images have safe text areas and correct aspect ratio.
- Deep links resolve to meaningful states.

### 28.7 Search accessibility

Good semantics, descriptive headings, link purpose, captions, transcripts, and fast rendering benefit both people and discovery. Do not trade accessibility for search tricks.

---

## 29. Security, privacy, legal, and trust

### 29.1 Security floor

For any site accepting data:

- validate and sanitize on the server;
- encode output and prevent injection/XSS;
- protect state-changing requests against CSRF where applicable;
- use secure, `HttpOnly`, appropriate `SameSite` cookies;
- never expose secrets in client code;
- enforce authorization on the server, not through hidden UI;
- rate-limit and protect public forms/endpoints;
- validate uploads by type, size, content, storage path, and access;
- use HTTPS and appropriate security headers;
- keep dependencies and platform patched;
- handle auth/session errors without leaking sensitive detail.

### 29.2 Payment and sensitive data

- Use established payment providers and hosted/tokenized flows when possible.
- Do not store card data unless the organization is intentionally equipped for the compliance burden.
- Minimize collection of health, financial, identity, and children’s data.
- Explain why sensitive data is needed and how it is handled.
- Mask sensitive values in UI and logs.

### 29.3 Privacy

- Inventory every first- and third-party data flow.
- Collect only what is required.
- Document purpose, retention, access, deletion, and processors.
- Obtain consent where applicable; do not deploy a generic banner disconnected from actual behavior.
- Honor consent before loading gated trackers where required.
- Provide accessible privacy controls.
- Avoid dark patterns that coerce consent.
- Do not put personal data into analytics event names, URLs, or client logs.

### 29.4 Legal and claims

- Display terms, privacy, refund/cancellation, shipping, accessibility, licensing, and other policies when applicable.
- Regulated claims require qualified review.
- Disclosures are proximate and readable, not hidden in tiny gray text.
- Sponsored/affiliate content is identified.
- Copyright, trademarks, font licenses, image rights, releases, and open-source notices are preserved.
- Do not imply endorsement or affiliation without permission.

This manifest is not legal advice. Route jurisdiction-specific obligations to qualified counsel.

### 29.5 Trust design

Trust comes from:

- precise language;
- visible limits and conditions;
- real people and ownership;
- working contact/support paths;
- transparent price and process;
- secure behavior;
- honest errors;
- accessible interaction;
- proof close to claims;
- consistent visual and operational quality.

Security-badge theater and generic lock icons do not create trust.

---

## 30. Analytics and experimentation

### 30.1 Measurement plan

Before implementation, define:

- business question;
- primary event and success condition;
- event owner;
- trigger and deduplication behavior;
- properties required for analysis;
- privacy classification;
- validation method;
- reporting destination;
- decision the data can change.

Do not track events with no expected decision.

### 30.2 Event principles

- Name events by meaningful action, not UI color or DOM selector.
- Fire once per completed action where appropriate.
- Distinguish impression, intent, start, success, and failure.
- Include route/version/experiment context without personal data.
- Validate in preview and production.
- Track form errors and delivery success, not only button clicks.

### 30.3 Funnel integrity

A conversion funnel may include:

- qualified page view;
- CTA exposure;
- CTA activation;
- form or signup start;
- validation/error;
- successful completion;
- downstream qualification/revenue.

A click is not a conversion when the next step fails.

### 30.4 Experimentation

Run an experiment only when:

- the decision is meaningful;
- traffic and duration can support interpretation;
- the primary metric and guardrails are predeclared;
- variants are technically and semantically valid;
- accessibility and performance are equalized;
- stopping and rollout rules exist.

Do not A/B test a broken baseline. Do not test multiple unrelated ideas in one variant and call the result causal.

### 30.5 Qualitative evidence

Use support tickets, sales calls, search queries, recordings with proper consent, usability tests, and direct interviews to understand why. Quantitative data shows where; it often does not explain why.

---

# Part IV — Development Architecture and Operations

## 31. Stack and implementation architecture

### 31.1 Detect, do not assume

Identify the actual stack before recommending code. Record:

Before importing any third-party package, inspect the actual dependency manifest and version. Reuse an installed dependency when it fits; otherwise provide the required install/update step and assess bundle, licensing, maintenance, and overlap. Never write code against an assumed version.


- static/SSR/SPA rendering;
- routing;
- styling and tokens;
- component library;
- data fetching and forms;
- CMS and content format;
- animation and icon libraries;
- testing and deployment.

### 31.2 Default architecture for business sites

When greenfield and requirements do not demand an app runtime, prefer the least complex architecture that provides:

- server-rendered or statically generated indexable content;
- progressive enhancement;
- route-level code splitting;
- straightforward content ownership;
- accessible semantic HTML;
- minimal client JavaScript;
- reliable forms and analytics;
- preview and rollback.

A full client SPA is not the default for a brochure/marketing site.

### 31.3 Vanilla HTML/CSS/JS or static generators

Use when:

- content and interactions are modest;
- deployment simplicity matters;
- performance is critical;
- the team can maintain it.

Keep scripts modular, use semantic markup, and avoid inventing a component framework inside plain JavaScript.

### 31.4 React/Next-style stacks

- Prefer server components/rendering for static marketing content where supported.
- Add client boundaries only for actual interaction.
- Avoid hydrating decorative sections.
- Use framework image/font/metadata capabilities correctly.
- Keep shared layout and route metadata centralized.
- Scope animation and clean up effects.
- Avoid state libraries for local UI state.
- Preserve accessible HTML beneath component abstractions.

### 31.5 Vue/Nuxt, Svelte/SvelteKit, and similar stacks

- Use native framework lifecycle and SSR/static capabilities.
- Keep browser-only code out of server execution.
- Scope and dispose animation/listener resources.
- Prefer framework conventions over cross-framework abstractions.
- Keep content pages server/static where practical.

### 31.6 Astro/content-first stacks

- Use islands only where interaction exists.
- Keep content HTML-first.
- Choose the smallest client framework per island or none.
- Avoid turning every section into an island.
- Centralize tokens and global shell.

### 31.7 Tailwind and utility CSS

- Bind utilities to a semantic token system.
- Avoid raw color/value drift in markup.
- Extract repeated semantic components when repetition is real, not preemptively.
- Do not let default indigo, radius, shadow, and spacing become the brand.
- Review generated class complexity and responsive behavior.

### 31.8 Component libraries

Choose based on required primitives, accessibility quality, styling control, installed dependencies, and bundle cost.

- Reuse an installed library before adding another.
- Do not add overlapping primitive systems.
- Preserve library accessibility behavior while restyling.
- Avoid fighting a library whose structural assumptions contradict the visual world; use lower-level primitives or native elements instead.

### 31.8A Official design-system routing

When the brief, existing product, or governing organization names a real system, use its official package and current primary documentation rather than recreating its look from memory. Examples include Material, Fluent, Carbon, Polaris, Atlassian Design System, Primer, GOV.UK Frontend, USWDS, Bootstrap, Radix, and shadcn/ui.

Rules:

- a design system is an implementation and behavior contract, not a vibe word;
- use one primary component/primitive system per project unless an explicit migration boundary exists;
- preserve the official system’s accessibility and interaction behavior while applying approved brand tokens;
- aesthetic labels such as bento, glassmorphism, editorial, brutalism, dark tech, or kinetic type are not packages—implement them with the existing stack and describe them honestly;
- web recreations of proprietary platform materials, including Apple-style “liquid glass,” are approximations unless an official web package exists;
- check package status, version, deprecation, browser support, and license at implementation time.

### 31.9 Motion libraries

- Use CSS/native for isolated transitions.
- Use an installed motion library before adding GSAP for a simple fade.
- Use GSAP for the specific capabilities in Section 24.8.
- Do not ship multiple motion runtimes for adjacent effects.

### 31.10 Browser support

- Define a support matrix from audience analytics and business risk.
- Use feature detection and progressive enhancement.
- Provide fallbacks for unsupported View Transitions, container queries, or advanced media/effects when the support matrix requires it.
- Do not use browser sniffing when capability detection works.

### 31.11 Error boundaries and failure isolation

- A failed widget should not blank the full page.
- Wrap risky third-party or client-only modules at the appropriate boundary.
- Preserve primary content and action.
- Log actionable context without sensitive data.
- Show recovery or fallback.

### 31.12 Source control and deployment

- Small, coherent diffs.
- No generated/provider duplicates edited by hand when a canonical source exists.
- Preview every material design change.
- Run formatting, lint, type, tests, build, and artifact checks used by the repository.
- Define rollback.
- Do not deploy unreviewed illustrative content.

---

## 32. CMS and content operations

### 32.1 Add a CMS only when operations require it

Use a CMS when non-developers need regular publishing, structured content is reused, approval/workflow matters, or localization/preview requires it. Do not add one for a rarely changed five-page site without an owner need.

### 32.2 Content model

Model meaning, not the current visual arrangement.

Prefer fields such as:

- title, summary, body, author, date, taxonomy;
- claim, proof, source, disclaimer;
- product variant, price, availability;
- case-study challenge, work, result, context;
- CTA label, destination, audience;
- media with alt, caption, credit, focal point.

Avoid `leftColumnText`, `blueCard3`, or an unrestricted page-builder blob unless the business explicitly needs free composition and can govern it.

### 32.3 Editorial governance

Define:

- owner and approver;
- draft/review/publish/archive states;
- scheduled publishing and timezone;
- content freshness rules;
- source and claim verification;
- image rights and credits;
- legal review triggers;
- preview and rollback;
- broken-link and stale-content checks.

### 32.4 Design constraints for editors

Give editors purposeful options rather than unlimited styling:

- a small set of content modules;
- semantic emphasis, not arbitrary font/color controls;
- validated media ratios;
- character guidance without destructive hard caps;
- preview at representative breakpoints;
- accessible heading and link behavior;
- warnings for missing alt, source, or required disclosure.

### 32.5 Empty and partial CMS data

The frontend MUST survive:

- missing optional media;
- draft/unpublished relationships;
- long titles;
- empty collections;
- stale references;
- unrecognized embeds;
- localization fallback;
- API outage or rate limit.

---

## 33. Internationalization, localization, and bidirectionality

### 33.1 Plan before translation

Record:

- supported locales and fallback;
- translation owner/workflow;
- date, time, number, currency, address, phone, and name behavior;
- plural and grammatical variants;
- RTL requirement;
- localized assets and legal content;
- localized SEO and URLs;
- content expansion budget.

### 33.2 Implementation

- UTF-8 everywhere.
- Use `Intl` or established locale tooling.
- Do not concatenate grammar from fragments.
- Use message keys with context.
- Use logical CSS properties.
- Avoid fixed widths around text.
- Keep language switch state and destination clear.
- Preserve user locale choice appropriately.
- Use `hreflang` only for maintained equivalents.

### 33.3 Text expansion

Design for 30–40% expansion where relevant, but test real target languages. German is not the only long language, and CJK/Arabic introduce different rhythm, line breaking, and font needs.

### 33.4 RTL

- Apply `dir` at the document or component boundary.
- Mirror spatial direction when meaning reverses.
- Do not mirror brand marks, media playback, charts, clocks, or code blindly.
- Test mixed-direction content.
- Keep focus order and DOM order meaningful.
- Provide fonts with complete script coverage and matching tone.

### 33.5 Localization is more than text

Adapt:

- imagery and cultural references;
- social proof and payment methods;
- units and pricing;
- legal terms;
- reading density;
- local search/location information;
- support and business hours.

Do not treat one English composition as universally neutral.

# Part V — Design-System Contract

## 34. The modular `DESIGN.md` schema

`DESIGN.md` is the durable brand and interface contract. It is not a mood-board caption, a list of adjectives, or a dump of universal UX rules. It records decisions that should remain stable across routes and implementations.

A new system SHOULD cover every module below. Established systems may use different headings, but the substance must exist.

### 34.1 Identity and thesis

Record:

- system name and version;
- one-sentence visual thesis;
- product mechanism and audience relationship;
- dominant site mode(s);
- use scene and ambient context;
- `variance_seed` for controlled exploration;
- `design_variance`, `motion_intensity`, and `visual_density`;
- the one-line design read and why the dial coordinates fit;
- what makes the world recognizable without a logo.

Weak: “Modern, clean, premium, friendly.”

Strong: “A field manual for independent operators: annotated evidence, compact utility type, warm paper-like surfaces, and one signal orange reserved for decisions.”

### 34.2 Principles and anti-principles

Use behavioral statements:

- “Evidence sits next to the claim it supports.”
- “One monumental statement per viewport; the rest recedes.”
- “Product screens are cropped to behavior, never shrunk into wallpaper.”
- “Motion confirms continuity; it does not decorate reading.”

Also record explicit refusals:

- no generic AI indigo;
- no identical feature-card grid;
- no decorative icons;
- no unverified metrics;
- no dark mode by category habit.

### 34.3 Visual authority and provenance

State:

- authority classification: established, incomplete, redesign, or greenfield;
- approved brand assets and sources;
- reference systems and the discipline each donates;
- trademarks or proprietary patterns that must not be imitated;
- asset/font licenses and attribution;
- source-of-truth precedence.

### 34.4 Visual world

Define:

- composition grammar;
- dominant material/environment metaphor, if any;
- signature system;
- restraint system;
- page pacing;
- relationship of image, type, and product proof;
- optional concept spine and its structural consequences;
- the one second-read moment and what it contributes;
- any bounded style preset, including fit, non-fit, signature, restraint, and mobile behavior;
- how the world changes across Persuade, Operate, Read, and Experience surfaces without fragmenting.

### 34.5 Color contract

Include:

- semantic token table;
- light/dark or single-theme rationale;
- accent-use rules;
- state colors;
- text-on-color rules;
- image/color relationship;
- gradients/transparency/texture policy;
- contrast and forced-colors notes;
- browser-surface colors.

Do not list hex codes without roles and usage.

### 34.6 Typography contract

Include:

- display, body, utility, and data roles;
- exact family/source/license/fallback;
- available weights/styles;
- scale behavior and fluid limits;
- line-height, tracking, measure, and capitalization rules;
- hierarchy vectors;
- numerals, code, quotes, labels, and links;
- language/script coverage;
- loading strategy;
- forbidden substitutions.

### 34.7 Grid, spacing, and composition

Include:

- maximum content widths;
- column/gutter logic;
- spacing scale and grouping behavior;
- section pacing;
- full-bleed and alignment-break rules;
- card/surface policy;
- first-viewport composition;
- narrow/medium/wide transformations;
- container-query behavior where relevant.

### 34.8 Imagery and media

Include:

- photo/product/illustration hierarchy;
- subject, camera, light, crop, treatment, and caption behavior;
- screenshot and demo rules;
- generated-media rules;
- video/3D policy;
- mobile art direction;
- alt text and credit policy;
- asset rights/provenance;
- performance formats and loading.

### 34.9 Iconography, illustration, and data

Include:

- chosen icon library or authored system;
- stroke/fill/optical-size rules;
- when icons are allowed;
- illustration grammar;
- diagram notation;
- chart palette and labeling;
- accessible alternatives;
- prohibited decorative uses.

### 34.10 Components and geometry

Define:

- controls and surface primitives;
- border/radius/elevation logic;
- density and hit areas;
- button/link hierarchy;
- form controls;
- navigation;
- cards, lists, tables, quotes, media, and callouts;
- selection, focus, visited, disabled, pending, and error states;
- when a modal, tooltip, toast, or disclosure is permitted.

A component section should describe behavior and relationships, not only visual values.

### 34.11 Motion personality

Define:

- motion purpose and budget;
- frequency policy;
- durations/eases/springs;
- one signature motion moment, if any;
- CSS/native/GSAP selection rules;
- scroll behavior;
- interruption and cleanup;
- reduced-motion substitutions;
- ambient-loop limits;
- performance constraints.

### 34.12 Content and voice

Define:

- audience vocabulary;
- voice attributes with examples and counterexamples;
- headline behavior;
- CTA verbs;
- proof/citation language;
- error and empty-state voice;
- capitalization, punctuation, numerals, dates, and units;
- terms to avoid;
- punctuation and micro-label policy based on the brand voice rather than a universal source blacklist;
- CTA-intent vocabulary so the same action keeps one label across navigation, hero, body, and footer;
- sponsor/affiliate/disclosure behavior.

### 34.13 Responsive and contextual behavior

Define:

- mobile-first priorities;
- content-driven breakpoints;
- grid transformations;
- navigation transformations;
- media art direction;
- coarse/fine pointer behavior;
- landscape/tablet behavior;
- safe areas and mobile keyboard;
- wide-screen maximums;
- print behavior if required.

### 34.14 Accessibility contract

Define:

- conformance target;
- contrast rules;
- focus appearance;
- target-size default;
- heading/landmark expectations;
- keyboard patterns;
- media requirements;
- motion and flash limits;
- live-region/focus behavior;
- zoom/reflow;
- RTL/language support;
- testing requirements.

### 34.15 State and resilience contract

Define:

- loading, empty, error, populated, and edge state appearance;
- form states;
- retry/backoff behavior;
- timeout thresholds;
- offline/partial failure;
- permission/read-only state;
- long content and large data behavior;
- optimistic update and rollback.

### 34.16 Performance contract

Define:

- route budgets;
- critical media/font policy;
- Core Web Vitals targets;
- client-JS rules;
- third-party policy;
- animation/rendering constraints;
- field monitoring;
- fallback and low-end-device behavior.

### 34.17 Do / do not

Make the final list concrete and auditable. Avoid vague statements such as “keep it modern.”

Examples:

**Do**

- place product evidence beside the claim;
- use one orange decision signal;
- crop screens to the exact workflow step;
- vary section density;
- use strong type contrast and quiet utility text.

**Do not**

- use orange on decorative icons;
- place every feature in a rounded card;
- animate all sections on scroll;
- use generic stock teamwork photos;
- invent performance metrics.

### 34.18 Agent usage guide

End `DESIGN.md` with:

- read order;
- what is mandatory versus optional;
- how route overrides work;
- how to choose components/assets;
- how to handle missing content;
- how to verify compliance;
- what requires owner approval.

### 34.19 AI-tell registry

Maintain a small, project-specific registry rather than copying an infinite blacklist:

| Pattern | Evidence observed | Status | Why | Exception |
|---|---|---|---|---|
| Centered hero + two CTAs + floating mockup | Category/reference audit | MONITOR | Category default | Allowed for manifesto launch |
| Section-number eyebrows | Existing prototype | PROJECT BAN | Decorative pseudo-structure | Allowed for real sequence/manual |
| Product screenshot | Supplied real asset | ALLOWED | Proof | — |

Statuses: `ABSOLUTE`, `PROJECT BAN`, `MONITOR`, `ALLOWED`.

The registry makes anti-slop decisions durable without turning one repository’s production anecdotes into universal aesthetics.

### 34.20 Style-preset module

When a named style is approved, append a module with:

- preset name and one-sentence atmosphere;
- `when_to_use` and `not_for`;
- dial envelope;
- substrate and palette roles;
- typography and hierarchy behavior;
- grid, geometry, material, icon, imagery, and motion;
- signature and restraint systems;
- state behavior;
- mobile/RTL/high-contrast/reduced-motion transformations;
- implementation risks and prohibited combinations.

A preset is subordinate to the shared semantic tokens and component behavior. It may change expression; it does not fork the product into a second design system.

---

# Part VI — Critique, Audit, and Release Control

## 35. Critique and technical audit

Design critique and technical audit are different. Run both.

### 35.1 Design jury

Review the rendered artifact through six independent lenses:

| Role | Question | Weight |
|---|---|---:|
| **Brief / Product** | Does it solve the stated audience and business job truthfully? | 25% |
| **Designer** | Is composition, hierarchy, pacing, and craft coherent? | 15% |
| **Brand / Distinctiveness** | Does it express the chosen world and avoid category interchangeability? | 20% |
| **Copy / Content** | Is language clear, specific, credible, and action-oriented? | 10% |
| **Accessibility / Usability** | Can people perceive, navigate, understand, and recover? | 15% |
| **Engineering / Performance** | Is it responsive, resilient, fast, and maintainable? | 15% |

Score each 0–10 and provide:

- strongest success;
- up to three must-fix findings;
- evidence/location;
- exact correction;
- risk if unchanged.

Composite:

```text
brief × .25
+ designer × .15
+ brand × .20
+ copy × .10
+ accessibility × .15
+ engineering × .15
```

Release threshold: composite ≥ 8.2, with Brief, Accessibility, and Engineering each ≥ 8.0 and no P0/P1 defect.

Run at most three rounds. If the score fails because the brief or direction is wrong, return to Shape/Synthesize; do not keep polishing symptoms.

### 35.2 Technical audit dimensions

Score each 0–4:

1. Accessibility.
2. Performance.
3. Responsive/context adaptation.
4. Theming/tokens/design-system integrity.
5. Implementation integrity and truth.
6. SEO, analytics, security, and launch operations.

Total: 24.

| Score | Rating |
|---:|---|
| 22–24 | excellent; minor polish |
| 18–21 | good; address weak dimensions |
| 14–17 | acceptable; significant work remains |
| 8–13 | poor; major remediation |
| 0–7 | critical; fundamental failure |

### 35.3 Severity

- **P0 Blocking:** task failure, data loss, security exposure, dangerous deception, or inaccessible critical path.
- **P1 Major:** WCAG AA failure, severe performance/responsive defect, misleading claim, broken conversion, or systemic design drift.
- **P2 Minor:** meaningful friction with a workaround or local inconsistency.
- **P3 Polish:** low-impact refinement.

Everything cannot be P0. Too many P3 findings create noise.

### 35.4 Finding format

For each finding:

```text
[P?] Title
Location:
Dimension:
Evidence:
User/business impact:
Standard or contract:
Root cause:
Correction:
Smallest regression check:
```

### 35.5 Systemic pattern review

After individual findings, identify repeated causes:

- hard-coded colors instead of tokens;
- small targets throughout;
- card reflex across sections;
- missing states in every data component;
- client-only critical content;
- accent overuse;
- inconsistent proof language;
- duplicate analytics events;
- unscoped animation resources.

Fix patterns at the shared root.

### 35.6 Positive findings

Record what works and should be preserved. Critique that only tears down makes later rounds less coherent.

### 35.7 Bounded visual inspection

- Inspect desktop and mobile in one batch.
- Gather all visible findings.
- Fix as a batch.
- Confirm once.
- Re-open the direction only for a material thesis failure.

---

## 36. Anti-generic and anti-slop enforcement

### 36.1 Absolute failures

These fail the release gate unless explicitly labeled as a non-production placeholder where appropriate:

- invented testimonials, metrics, reviews, logos, customers, awards, certifications, prices, availability, or affiliations;
- filler copy (`lorem ipsum`, “Feature one,” “Sample content”);
- controls or links that appear functional but do nothing;
- missing accessible names, labels, focus, or critical keyboard paths;
- only-populated-state UI;
- content hidden solely to make the layout fit;
- unknown asset rights;
- client-only validation at a trust boundary;
- secrets in client code;
- a design that directly impersonates another brand;
- nested cards used as page structure;
- infinite loading/spinner with no timeout or recovery.

### 36.2 Unearned defaults

These are not universal bans. They are rejected when chosen by reflex rather than evidence:

- centered hero with vague headline, two buttons, and floating mockup;
- purple/blue/indigo AI gradient;
- default Tailwind indigo accents such as `#6366f1`, `#4f46e5`, `#8b5cf6`, `#7c3aed`, or `#a855f7`;
- identical icon-heading-text card grids;
- bento layout for every section;
- glassmorphism and blur;
- gradient text;
- giant type with no supporting hierarchy;
- dark mode by category;
- monospace as technical costume;
- rounded pills everywhere;
- hard offset shadows outside a real neobrutalist world;
- decorative blobs, waves, grids, grain, and orbital lines;
- section numbers that convey no sequence;
- eyebrow/kicker above every heading;
- marquee text, parallax, scroll pinning, and 3D for spectacle;
- hero metric template;
- decorative progress rings and sparklines;
- generic stock teamwork imagery;
- rounded-square icon tiles;
- repeated fade-up on every section;
- arbitrary device mockups;
- logo strip with no real relationship or permission;
- “Get started” used when a specific action exists.
- fake beta/version stamps, build numbers, sync timestamps, coordinates, weather, or archival labels added as visual seasoning;
- decorative status dots, crosshairs, hairlines, and technical labels without semantic work;
- fake product UI assembled from meaningless divs instead of a real screenshot, real demo, or clearly labeled concept;
- poetic craft labels and faux provenance captions with no real source;
- identical CTA intent expressed through several competing labels;
- wrapped desktop CTA labels caused by arbitrary narrow controls;
- empty bento cells and filler tiles created to satisfy a grid;
- unmotivated mid-page theme inversion;
- long quote blocks used where a scannable proof excerpt is required.

### 36.3 Mechanical lint candidates

Automated checks MAY flag:

- known default-indigo values used as solid accents;
- excessive raw colors outside token definitions;
- accent token visibly repeated across most elements;
- `transition: all`;
- transform motion without reduced-motion handling;
- missing width/height or aspect ratio on media;
- missing alt/label/heading/landmark basics;
- empty `href`, click handlers on non-interactive elements, and fake buttons;
- hard-coded colors that bypass the token system;
- animation/layout properties known to trigger expensive work;
- missing loading/empty/error branches;
- duplicate IDs;
- horizontal overflow;
- third-party scripts loaded before consent when consent is required;
- structured data inconsistent with visible content.
- section-layout family repetition beyond the project budget;
- more than one decorative marquee or signature scroll sequence without an explicit exception;
- duplicate CTA intents with inconsistent labels;
- desktop CTA text wrapping;
- empty bento/grid cells;
- fake precision or fake metadata not marked as illustrative;
- animation dial/plan claiming behavior that the implementation does not contain.

Every automated finding must be verified in context. Do not turn heuristics into false certainty.

### 36.4 Soul test

The site should contain at least one detail that could only come from someone who understands the product:

- a product-specific shortcut hint;
- a status vocabulary used by actual operators;
- a real sample output;
- an evidence annotation;
- a material/interaction derived from the mechanism;
- a comparison that reflects the buyer’s real decision;
- a microcopy line grounded in the workflow.

If a screenshot cannot be associated with the product without its logo, the site still looks like a template.

### 36.5 Uniqueness ledger

Record these before build and verify after:

| Axis | Chosen behavior | Category default refused |
|---|---|---|
| Composition | | |
| Typography | | |
| Color/material | | |
| Imagery | | |
| Evidence display | | |
| Component geometry | | |
| Motion | | |
| Voice | | |
| First viewport | | |
| Signature system | | |
| Restraint system | | |

At least four axes MUST materially differ from the category default, and the differences must remain compatible with product clarity.

### 36.6 Similarity ceiling

A site may reference many systems but should not inherit more than two conspicuous signature traits from any single branded source. If type, palette, hero, navigation, image treatment, and motion all point to the same reference, it is a clone even if the logo changed.

### 36.7 Heuristic false-positive guard

Do not mechanically fail a site because it contains an em dash, Inter, Lucide, a centered hero, a serif dashboard label, a warm beige palette, a light-only theme, a scroll cue, or another item that a source skill bans. Fail it when the choice is unearned, repeated, inaccessible, misleading, off-brand, technically harmful, or indistinguishable from the category default.

Conversely, do not excuse a repeated tell merely because each occurrence can be defended in isolation. Judge the cumulative page signature.

---

## 37. Definition of done

A site is done only when all applicable gates pass.

### 37.1 Product and business

- [ ] Primary audience, business objective, offer, mechanism, proof, CTA, objections, and metric are explicit.
- [ ] Every major claim has a truth status and source.
- [ ] No fake proof or misleading omission.
- [ ] No fake product UI, fake precision, decorative version/status metadata, or faux provenance presented as real.
- [ ] Visitor questions are answered in an intentional sequence.
- [ ] A one-line design read and the three expression dials are recorded and visible in the result.
- [ ] Primary and secondary actions are clear and do not compete.
- [ ] Pricing, terms, availability, geography, and next steps are accurate where applicable.

### 37.2 Visual world

- [ ] Visual authority classification is recorded.
- [ ] One visual direction is approved.
- [ ] Signature and restraint systems are explicit.
- [ ] Layout repetition stays within the documented budget; bento/grid structures contain no filler cells.
- [ ] Any concept spine, second-read moment, or style preset has a functional reason and does not fragment the system.
- [ ] The design differs materially from category rut on at least four axes.
- [ ] It passes logo-removal and interchangeability tests.
- [ ] References donate discipline without brand imitation.
- [ ] Type, color, imagery, geometry, and motion are coherent.
- [ ] No unearned AI-default motif remains.

### 37.3 Content

- [ ] Real production copy and assets replace placeholders.
- [ ] Content is specific, concise, and useful.
- [ ] Proof appears near claims.
- [ ] CTA copy describes the next step.
- [ ] Errors, empty states, and help use product language.
- [ ] Alt, captions, credits, disclosures, and sponsorship labels are complete.
- [ ] Content owner and update process are known.

### 37.4 Interaction and states

- [ ] Links and buttons use correct semantics.
- [ ] Keyboard, touch, hover, focus, active, disabled, pending, success, and error behavior are defined.
- [ ] Loading, empty, error, populated, and edge states exist.
- [ ] Forms preserve input, validate accessibly, prevent duplicate submission, and recover from server failure.
- [ ] Dialogs, disclosures, tabs, tooltips, and toasts follow expected behavior.
- [ ] Browser history and deep links behave predictably.

### 37.5 Responsive and localization

- [ ] Narrow, medium, wide, landscape, coarse-pointer, fine-pointer, and keyboard contexts are handled.
- [ ] Layout is recomposed, not simply shrunk.
- [ ] No unintended horizontal scroll.
- [ ] Text expansion, long tokens, CJK, RTL, and mixed direction are tested when applicable.
- [ ] Mobile keyboard and safe-area behavior are usable.
- [ ] Core functionality remains available on mobile.

### 37.6 Accessibility

- [ ] WCAG 2.2 AA target is met for applicable criteria.
- [ ] Semantics, landmarks, headings, labels, and alt text are correct.
- [ ] Critical paths work keyboard-only.
- [ ] Focus is visible, logical, and unobscured.
- [ ] Contrast and non-color cues pass.
- [ ] Target sizes and drag alternatives pass.
- [ ] Zoom/reflow and text enlargement work.
- [ ] Reduced motion and media controls work.
- [ ] Dynamic changes and errors are announced appropriately.
- [ ] Automated and manual testing are complete.

### 37.7 Performance

- [ ] Performance budget exists and is met or deviations are approved.
- [ ] LCP element is optimized and not lazy-loaded.
- [ ] INP risks and long tasks are addressed.
- [ ] Media/asynchronous space is reserved to prevent CLS.
- [ ] Fonts and third-party scripts are minimized.
- [ ] Motion is profiled and cleaned up.
- [ ] Declared motion intensity matches motion actually shipped, and one engine owns each animated property.
- [ ] Slow/offline/blocked-third-party behavior is resilient.
- [ ] Field monitoring is configured when justified.

### 37.8 SEO and discoverability

- [ ] Titles, descriptions, canonicals, robots, social metadata, and status codes are correct.
- [ ] Sitemap and internal links are correct where applicable.
- [ ] Indexable content is crawlable.
- [ ] Structured data is accurate, visible, specific, and validated.
- [ ] 404, redirects, pagination/facets, and international routes are governed.

### 37.9 Security, privacy, and legal

- [ ] Server-side validation and authorization exist at trust boundaries.
- [ ] Secrets and sensitive data are protected.
- [ ] Public forms have abuse handling.
- [ ] Data collection and third parties are inventoried.
- [ ] Consent/privacy behavior matches actual integrations.
- [ ] Required terms, refund, shipping, accessibility, sponsorship, and other policies are present.
- [ ] Asset, font, code, and brand licenses are preserved.
- [ ] Regulated or consequential claims have appropriate review.

### 37.10 Analytics and operations

- [ ] Meaningful events are defined, deduplicated, and validated.
- [ ] No unnecessary personal data is collected.
- [ ] Form delivery and conversion success are monitored.
- [ ] CMS/editorial ownership and freshness rules exist.
- [ ] Preview, deployment, rollback, and incident ownership are documented.
- [ ] Requested routes, files, sections, components, states, and formats match the locked deliverable count; no placeholder omissions remain.
- [ ] No P0/P1 finding remains.
- [ ] Design-jury and technical-audit thresholds pass.

---

# Part VII — Copy-Ready Templates

## 38. Templates

Use these templates as starting contracts. Delete unused fields rather than leaving empty theater.

### 38.1 `PRODUCT.md`

```markdown
# Product Truth

## Identity
- Product/company:
- Category:
- Business model:
- Primary revenue action:
- Truth owner:
- Last verified:

## Audience
- Primary audience:
- Excluded audience:
- Trigger/context:
- Current workaround:
- Decision maker:
- Main objections:
- Trusted evidence:
- Device/use environment:
- Locale/accessibility constraints:

## Offer
- What is offered:
- Price/packaging:
- Eligibility/geography:
- Primary CTA:
- Secondary CTA:
- What happens next:

## Unique Mechanism
- Problem:
- Mechanism:
- Outcome:
- Why alternatives fail:
- Important limitations:

## Proof
| Claim | Evidence | Source | Status | Context/limits |
|---|---|---|---|---|

## Risk and Trust
- Trial/guarantee/cancellation:
- Security/privacy:
- Support:
- Legal/compliance review:

## Success
- Primary metric:
- Baseline:
- Guardrails:
- Analytics owner:

## Constraints and Non-goals
- Technical:
- Brand:
- Content:
- Timeline:
- Explicit non-goals:
```

### 38.2 Direction card

```markdown
# Direction: [Name]

## Thesis
[One sentence]

## Why it fits
- Product mechanism:
- Audience scene:
- First proof:
- Category rut refused:

## Source systems
| Source | Family | Discipline donated | Identity not copied |
|---|---|---|---|

## First viewport
- Composition:
- Dominant message:
- Evidence:
- CTA:
- Media:

## System
- Composition grammar:
- Typography:
- Color/material:
- Imagery:
- Component geometry:
- Signature system:
- Signature interaction:
- Restraint system:

## Responsive behavior
- Narrow:
- Medium:
- Wide:
- Reduced motion:

## Risk
- Accessibility:
- Performance:
- Content dependency:
- Implementation complexity:

## Verdict
- Product clarity /10:
- Audience fit /10:
- Differentiation /10:
- Content fit /10:
- Scalability /10:
- Feasibility /10:
- Status: WINNER / COMPETITIVE / DECLINED
```

### 38.3 `SURFACE-BRIEF.md`

```markdown
# Surface Brief: [Route]

- Mode: Persuade / Operate / Read / Experience
- Visitor state:
- One-sentence job:
- Primary action:
- Secondary action:
- Search intent:
- Success event:

## Questions to answer
1.
2.
3.
4.
5.

## Required content and proof
| Visitor question | Content | Proof | Source/status | Action |
|---|---|---|---|---|

## First viewport contract
- What is this:
- For whom:
- Value/outcome:
- Proof signal:
- Next action:

## Composition grammar
- Dominant grammar:
- Supporting grammar:
- Section rhythm:
- Signature expression:
- Route-specific override:

## States
- Loading:
- Empty:
- Error:
- Populated:
- Edge:

## Context
- Narrow/mobile:
- Tablet/medium:
- Wide:
- Coarse pointer:
- Keyboard:
- Reduced motion:
- Locale/RTL:

## Analytics
| Event | Trigger | Success | Properties | Privacy |
|---|---|---|---|---|

## Non-goals
-
```

### 38.4 `DESIGN.md`

```markdown
# [System Name] Design Contract

> Version:
> Visual authority: established / incomplete / redesign / greenfield
> Variance seed:
> Source of truth:

## Visual Thesis
[One sentence that links product, audience, and visual behavior]

## Principles
1.
2.
3.
4.

## Refusals
-
-
-

## Visual World
- Composition grammar:
- Materials/environment:
- Page pacing:
- Signature system:
- Restraint system:
- Behavior across Persuade / Operate / Read / Experience:

## Provenance
| Reference/asset | Source | License/permission | Discipline donated | Restrictions |
|---|---|---|---|---|

## Color
| Token | Value | Role | Allowed uses | Contrast notes |
|---|---|---|---|---|

## Typography
| Role | Family/source | Weights | Scale/measure | Rules |
|---|---|---|---|---|

## Grid, Spacing, and Composition
- Max widths:
- Columns/gutters:
- Spacing rhythm:
- Full-bleed rules:
- Grid-break rules:
- Card/surface policy:
- First viewport:

## Imagery and Media
- Photography:
- Product screens:
- Illustration/diagram:
- Generated media:
- Crop/art direction:
- Captions/credits/alt:
- Responsive/performance:

## Iconography and Data
- Icon system:
- Stroke/fill:
- Diagram notation:
- Chart rules:
- Prohibited uses:

## Components and Geometry
- Buttons/links:
- Navigation:
- Forms:
- Surfaces/elevation:
- Lists/tables/cards:
- Dialogs/disclosure/toasts:
- Browser surfaces:

## Motion
- Purpose/budget:
- Durations/easing/springs:
- Signature moment:
- Scroll behavior:
- CSS/native/GSAP rule:
- Reduced motion:
- Cleanup/performance:

## Content and Voice
- Audience language:
- Voice:
- Headline behavior:
- CTA verbs:
- Proof language:
- Error/empty voice:
- Terms to avoid:

## Responsive and International
- Narrow:
- Medium:
- Wide:
- Pointer/hover:
- Safe areas/keyboard:
- Text expansion:
- RTL:

## Accessibility
- Target:
- Contrast:
- Focus:
- Target size:
- Keyboard:
- Media:
- Motion:
- Zoom/reflow:
- Testing:

## States and Resilience
- Loading:
- Empty:
- Error:
- Populated:
- Edge:
- Retry/offline:
- Permissions:

## Performance
- Route budgets:
- Critical media/fonts:
- JS/third-party rules:
- Core Web Vitals:
- Monitoring:

## Do / Do Not
### Do
-
### Do not
-

## Agent Usage
1. Read PRODUCT.md.
2. Read this entire contract.
3. Read the route SURFACE-BRIEF.md.
4. Reuse existing tokens/components.
5. Label missing truth; do not invent it.
6. Verify against the release gates.
```

### 38.5 `manifest.json`

```json
{
  "schemaVersion": "ultra-web-design-system/v1",
  "id": "project-slug",
  "name": "Project Name",
  "category": "Business category",
  "description": "One-sentence catalog description.",
  "source": {
    "type": "project",
    "origin": "Owner-approved design synthesis",
    "verifiedAt": "YYYY-MM-DD"
  },
  "files": {
    "product": "PRODUCT.md",
    "design": "DESIGN.md",
    "tokens": "tokens.css",
    "usage": "USAGE.md"
  }
}
```

### 38.6 `tokens.css`

```css
:root {
  color-scheme: light;

  --canvas: #fff;
  --surface: #fff;
  --surface-raised: #fff;
  --text: #111;
  --text-muted: #555;
  --border: #ddd;
  --accent: #000;
  --accent-contrast: #fff;
  --positive: #087a46;
  --warning: #8a5a00;
  --danger: #b42318;
  --focus: #005fcc;

  --font-display: "Approved Display", sans-serif;
  --font-body: "Approved Body", sans-serif;
  --font-utility: var(--font-body);
  --font-data: ui-monospace, monospace;

  --step--1: clamp(.78rem, .75rem + .12vw, .86rem);
  --step-0: clamp(1rem, .96rem + .18vw, 1.125rem);
  --step-1: clamp(1.25rem, 1.13rem + .55vw, 1.6rem);
  --step-2: clamp(1.6rem, 1.35rem + 1.1vw, 2.3rem);
  --step-3: clamp(2.1rem, 1.65rem + 2vw, 3.4rem);
  --step-4: clamp(2.8rem, 1.95rem + 3.7vw, 5.5rem);

  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-5: 1.5rem;
  --space-6: 2.25rem;
  --space-7: 3.5rem;
  --space-8: 5.5rem;

  --radius-control: .5rem;
  --radius-surface: .875rem;
  --border-width: 1px;
  --shadow-low: 0 .25rem 1rem rgb(0 0 0 / .08);
  --shadow-high: 0 1rem 3rem rgb(0 0 0 / .14);

  --duration-fast: 120ms;
  --duration-default: 180ms;
  --duration-slow: 360ms;
  --ease-enter: cubic-bezier(.23, 1, .32, 1);
  --ease-move: cubic-bezier(.77, 0, .175, 1);
  --ease-exit: cubic-bezier(.4, 0, 1, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-default: 80ms;
    --duration-slow: 120ms;
  }
}
```

The values above are placeholders for a project contract, not a house style. Replace them from the approved world and verify contrast.

### 38.7 `CONTENT-MATRIX.md`

```markdown
# Content Matrix

| ID | Route/section | Visitor question | Production content | Asset | Proof/source | Truth status | Owner | CTA | SEO intent | Legal/accessibility notes |
|---|---|---|---|---|---|---|---|---|---|---|
```

### 38.8 `MOTION-PLAN.md`

```markdown
# Motion Plan

## Motion thesis
- Purpose:
- Frequency policy:
- Signature moment:
- Explicit refusals:

## Tokens
| Token | Value | Use |
|---|---:|---|

## Inventory
| Component/scene | Trigger | Purpose | Frequency | Properties | Duration/ease | Interruption | Reduced-motion substitute | Tech | Risk |
|---|---|---|---|---|---|---|---|---|---|

## GSAP ownership
- Registered plugins:
- Timeline owners:
- ScrollTrigger owners:
- Framework cleanup:
- Responsive matchMedia:

## Validation
- [ ] State is immediate before animation.
- [ ] Keyboard actions are not delayed.
- [ ] Reduced motion is implemented.
- [ ] No layout-thrashing animation.
- [ ] Offscreen/route cleanup works.
- [ ] No loop exceeds policy.
```

### 38.9 `DECISIONS.md`

```markdown
# Decision Log

## [YYYY-MM-DD] [Decision]
- Context:
- Options considered:
- Decision:
- Why:
- Evidence:
- Tradeoff:
- Revisit when:
- Owner:
```

### 38.10 `QA-REPORT.md`

```markdown
# QA Report

- Build/version:
- Routes:
- Browsers/devices:
- Reviewer:
- Date:

## Release summary
- Design jury composite:
- Technical audit score:
- P0:
- P1:
- P2 accepted:
- Release status: BLOCKED / CONDITIONAL / PASS

## Jury
| Lens | Score /10 | Strongest success | Must-fix |
|---|---:|---|---|

## Technical audit
| Dimension | Score /4 | Key evidence |
|---|---:|---|

## Findings
### [P?] Title
- Location:
- Evidence:
- Impact:
- Root cause:
- Correction:
- Regression check:
- Status:

## Context matrix
| Context | Result | Notes |
|---|---|---|
| 320px mobile | | |
| common mobile | | |
| tablet | | |
| laptop | | |
| wide desktop | | |
| keyboard | | |
| screen reader | | |
| reduced motion | | |
| zoom/reflow | | |
| slow/offline | | |
| long/RTL content | | |

## Positive findings
-

## Accepted risks
| Risk | Rationale | Owner | Review date |
|---|---|---|---|
```

### 38.11 `REFERENCE-COMP-BIBLE.md`

```markdown
# Reference Comp Bible

- Project:
- Design read:
- design_variance:
- motion_intensity:
- visual_density:
- Concept spine:
- Signature system:
- Restraint system:
- Second-read moment:

## Global visual system
- Canvas/surfaces:
- Palette roles:
- Typography mood and hierarchy:
- Grid/gutters/max width:
- Spacing rhythm:
- Geometry/elevation:
- Imagery treatment:
- Icon/illustration grammar:
- Browser/device framing:
- Mobile transformation:

## Frame inventory
| Frame | Surface/section job | Required content | Composition anchor | Media/background mode | CTA | States | Output status |
|---|---|---|---|---|---|---|---|

## Extraction contract
For each approved frame, record exact hierarchy, layout tracks, spacing, type behavior, media crop, component/state behavior, responsive transformation, and any impossible generated detail that implementation must correct.
```

### 38.12 Reusable block record

```markdown
---
name: [block-name]
category: [hero / proof / feature / pricing / cta / navigation / footer / transition]
dial_compatibility:
  variance: [min, max]
  motion: [min, max]
  density: [min, max]
when_to_use: "..."
not_for: "..."
stack: ["..."]
---

# [Block Name]

## Content relationship
## Visual sketch
## Props/content API
## Minimum working implementation
## States and semantics
## Mobile/RTL behavior
## Motion bands and reduced motion
## Theme/material notes
## Accessibility and performance risks
## Anti-patterns
## Provenance
## Runnable check
```

# Part VIII — Agent Router and Source Analysis

## 39. Agent execution router

### 39.1 Classify task size

| Task | Required path |
|---|---|
| Tiny copy/style/state fix in an established system | Read → Build → See |
| Local component or route extension | Read → Shape surface → Build → Taste → See |
| Existing-page refinement | Read → Taste → Resolve → See → Polish |
| Technical audit only | Read → Audit; do not edit |
| Hardening | Read → Harden → See |
| Responsive adaptation | Read → Shape target context → Adapt → See |
| New route in established brand | Read → Shape → Produce surface brief → Build → Taste → See |
| Greenfield site | Full loop |
| Visual redesign | Full loop; preserve product truth, replace world |
| Image-first visual exploration | Read → Shape → Synthesize → reference-comp bible → frames → extract contract → Build → See |
| Preserve-mode redesign | Read → preservation inventory → audit → low-risk modernization → See |
| Motion enhancement | Read → static hierarchy check → Motion plan → Build → See |

Do not run a full identity workshop for a one-line defect. Do not skip product truth for a full redesign.

### 39.2 Core modules

- **`shape`** — create or repair product/surface truth. No visual styling by habit.
- **`inspire`** — research product, audience, category, outside references, catalogs, and standards.
- **`synthesize`** — generate three materially different directions and select one.
- **`produce`** — create `DESIGN.md`, tokens, content matrix, surface brief, and representative proof.
- **`build`** — implement the minimum complete system in the existing stack.
- **`taste`** — critique against brief and visual world.
- **`resolve`** — fix prioritized root causes.
- **`see`** — render and inspect contexts, states, accessibility, and performance.
- **`polish`** — finish content, browser surfaces, metadata, operations, and release details.

### 39.3 Specialist modules

- **`audit`** — technical report only; no fixes.
- **`harden`** — extreme content, networks, permissions, errors, concurrency, localization, and data volume.
- **`adapt`** — recompose for another viewport, input method, platform, use scene, print, or email.
- **`animate`** — motion decision, plan, implementation, reduced-motion path, and cleanup.
- **`typeset`** — type roles, hierarchy, scale, measure, loading, and stress testing.
- **`colorize`** — semantic palette, contrast, material, states, and image interaction.
- **`layout`** — grid, rhythm, composition, section pacing, and responsive transformation.
- **`clarify`** — remove ambiguity in navigation, copy, hierarchy, states, and action.
- **`distill`** — delete non-essential content, components, effects, and choices.
- **`bolder`** — increase commitment through one or two governing axes, not more decoration.
- **`quieter`** — reduce competition while preserving the chosen world.
- **`onboard`** — first-use orientation, setup, empty states, progress, and recovery.
- **`optimize`** — performance, delivery, render, asset, and third-party cost.
- **`overdrive`** — experience-mode expansion only after usability/performance floors pass.
- **`art-direct`** — lock a reference-comp bible, generate readable section/screen frames, extract implementation rules, and prevent cross-frame drift.
- **`preset`** — apply one bounded style module with explicit fit/non-fit, dials, signature, restraint, and context fallbacks.

### 39.4 Specialist guardrails

- `bolder` must not turn every element loud.
- `quieter` must not erase the brand into neutral SaaS minimalism.
- `distill` must not remove essential proof, labels, accessibility, or recovery.
- `animate` must begin with the frequency and purpose gate.
- `overdrive` is prohibited on a broken, inaccessible, or slow baseline.
- `audit` reports verified findings and positive evidence; it does not silently edit.
- `adapt` preserves information architecture and core functionality.
- `optimize` measures before and after.
- `art-direct` regenerates unclear frames rather than cropping distorted composites and never treats generated text/UI as implementation truth.
- `preset` cannot override approved brand, product truth, accessibility, or the existing system without an explicit redesign decision.

### 39.5 Agent response contract

For substantial work, output or update:

1. classification, design read, and assumptions;
2. source-of-truth files read;
3. chosen path/modules and expression dials when visual direction is in scope;
4. locked deliverable count;
5. artifact or code changes;
6. checks performed and results;
7. remaining risks, only if real.

Do not narrate low-level tool use. Do not ask for information already supplied. When a missing answer does not block progress, choose and label a reasonable default.

---

## 40. Repository-by-repository ingestion report

This section records what was mined, what was retained, what was rejected, and how conflicts were resolved. “Ingested” means canonical design knowledge, schemas, datasets, examples, workflows, and provenance were analyzed semantically. Generated mirrors, binaries, screenshots, translations, dependency locks, and application plumbing were inventoried but were not copied as doctrine.

### 40.1 `pbakaus/impeccable`

**Pinned snapshot:** `e5abceedc44ee6284a5ebb0bd309e30706d2cb8c`
**License:** Apache-2.0
**Canonical knowledge root:** `skill/`, especially `SKILL.src.md` and `skill/reference/`

#### Repository role

Impeccable is the strongest source for the end-to-end design reasoning loop: product truth, durable design truth, surface-local strategy, visual-authority classification, direction generation, craft floor, refinement modes, and bounded visual QA.

#### Canonical architecture mined

- `PRODUCT.md` as product truth.
- `DESIGN.md` as durable visual truth.
- Surface briefs for route-specific strategy.
- Four modes: Persuade, Operate, Read, Experience.
- Visual authority: established, incomplete, redesign, no authority.
- Refinement preserves; redesign replaces.
- One round of high-value clarification, not endless intake.
- Whole-surface direction generation through 5–7 materially different structures, three candidates, and one lock.
- Visual-world method: unique mechanism, audience cultural home, first-surface proof, category rut/opposite, seven concrete sources across multiple material families, deterministic lead/challenger selection, one-world ownership.
- Comp-led versus code-led proof.
- Bounded desktop/mobile QA.
- Command families for build, evaluate, refine, enhance, fix, and iterate.
- Craft floor covering contrast, type, spacing, states, browser surfaces, copy, responsive behavior, and shipping completeness.
- Hardening against long/short text, i18n, failures, permissions, large data, concurrency, and networks.
- Adaptation as context redesign rather than scaling.
- Separate technical audit from design critique.

#### Strongest contributions retained

- “The brief wins” as the core aesthetic authority rule.
- Product/design/surface truth hierarchy.
- Visual-world engine and challenger logic.
- Signature through system discipline, not decoration.
- One visual world per surface.
- Craft-floor checks and refusal of reflex patterns.
- Browser surfaces as a low-cost signal of authored implementation.
- Rooted hardening and context adaptation.
- Bounded visual review and explicit release audits.

#### Limitations resolved

- Some rules are deliberately opinionated and model-specific. This manifest treats most aesthetic refusals as defaults that the brief can earn back.
- Fixed breakpoint examples were converted into content-driven breakpoint guidance.
- A 44px touch recommendation was reconciled with WCAG 2.2’s 24px AA minimum and its exceptions.
- Provider-specific tags and generated distribution copies were not carried forward.
- The command surface was condensed into one modular router rather than copied verbatim.

#### Excluded as non-doctrine

- provider packaging and generated copies;
- installer/hook mechanics;
- duplicated distribution files;
- native-specific branches outside web scope, except transferable contextual principles.

### 40.2 `nextlevelbuilder/ui-ux-pro-max-skill`

**Pinned snapshot:** `bc826e2267a36d98a2dcf5231e16c30ff546770f`
**License:** MIT
**Canonical knowledge root:** `src/ui-ux-pro-max/`; `.claude` and CLI assets are mirrored distributions

#### Repository role

UI/UX Pro Max is the strongest source for structured retrieval: broad searchable catalogs, stack-aware implementation guidance, domain targeting, provenance, recommendation validation, master/page override behavior, and a priority order that places accessibility and interaction before decoration.

#### Catalog inventory at the pinned snapshot

- 88 styles total: 79 searchable, 50 active, 29 supplemental, 9 deprecated.
- 192 product categories.
- 192 palettes.
- 192 reasoning profiles.
- 74 curated font pairings.
- 1,934 Google Fonts records.
- 105 curated icons plus 1,512 upstream Phosphor icons.
- 119 UX guidelines.
- 17 motion presets.
- 25 chart types.
- 22 implementation stacks.
- 1,260 stack-specific guidelines.

The repository uses hybrid BM25/regex retrieval, domain auto-detection, validation, provenance metadata, and no external Python search dependencies.

#### Strongest contributions retained

- Query the smallest relevant domain instead of loading everything.
- Use two to five terms with one dominant intent.
- Detect stack; never assume.
- Verify domain/category/top result/fit.
- Retry once, then label fallback confidence.
- Never persist unmatched or unverified recommendations.
- Whole-system master plus page-specific override.
- Priority order: accessibility, touch/interaction, performance, style fit, layout/responsive, type/color, animation, forms/feedback, navigation, data.
- Search semantic outcome before stack implementation.
- Broad accessibility, performance, form, chart, and responsive reference coverage.
- Explicit provenance and promotion rules for fonts/data.

#### Limitations resolved

- Product-to-style and product-to-color rows can encode category stereotypes. This manifest uses them as candidate generators and requires a category-rut challenge before adoption.
- A catalog cannot create a product-specific visual thesis. Product/audience evidence outranks retrieved recommendations.
- Large raw tables were not embedded because they would make a single skill less usable and would become stale. Their schemas, querying discipline, confidence rules, and coverage are retained.
- Stack guidance is selected only after inspecting the real codebase.

#### Excluded as non-doctrine

- generated/mirrored skill copies;
- raw catalog rows that duplicate the retrieval system;
- CLI packaging and distribution implementation;
- deprecated style records as recommendations.

### 40.3 `emilkowalski/skills`

**Pinned snapshot:** `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7`
**License:** MIT
**Canonical knowledge root:** `skills/`

#### Repository role

Emil Kowalski’s skill set supplies the clearest motion decision discipline and design-engineering review style. It emphasizes trained taste, invisible details, purpose before animation, frequency-based restraint, interruption, perceived performance, and concrete Before/After/Why critique.

#### Skill inventory mined

- design engineering;
- web animation;
- animation recipes and vocabulary;
- animation opportunity discovery;
- animation improvement and review;
- prototype workflow;
- UI library selection;
- toast/feedback guidance;
- Expo/native animation;
- Apple design and Swift guidance.

#### Strongest contributions retained

- Taste is trained through study, reverse engineering, and comparison.
- Invisible details compound.
- Before / After / Why review language.
- Motion decision: should it animate, purpose, easing, duration.
- Frequency gate: common and keyboard-driven actions should be instant.
- Valid motion purposes: spatial consistency, state, explanation, feedback, and continuity.
- Enter with ease-out; move/morph with ease-in-out; hover/color with ease; constant motion linear.
- Most UI motion under roughly 300ms; explanatory/rare transitions may run longer.
- Springs for gestures and interruption; restrained bounce.
- Press feedback, sensible transform origins, no `transition: all`, no scale-from-zero default.
- Prototype a focused interactive slice before constructing a system.
- Choose UI libraries by actual primitive need, accessibility, style control, existing dependencies, and cost.
- Toasts are for transient non-blocking feedback, not critical action-required errors.

#### Limitations resolved

- Native Expo/Swift/Apple modules were not treated as web implementation instructions. Their perceptual and platform-adaptation principles informed the cross-platform handoff only.
- “Never animate keyboard actions” was interpreted as never delay the state/action; a subtle non-blocking confirmation may follow when useful.
- Numeric recipes are starting points, not identity.
- Motion advice is subordinate to reduced-motion, accessibility, and product frequency.

#### Excluded as non-doctrine

- platform-specific code unrelated to web;
- duplicated examples where the governing principle was already captured;
- product/library recommendations that may change over time.

### 40.4 `greensock/gsap-skills`

**Pinned snapshot:** `aed9cfd3277740755f6bfc1155c7aa645403b760`
**License:** MIT
**Canonical knowledge root:** official skill folders and framework examples

#### Repository role

GSAP Skills is the implementation authority for when and how to use GSAP: core tweens, timelines, ScrollTrigger, plugins, utilities, React/framework lifecycle, performance, and cleanup.

#### Official skill inventory mined

- GSAP core;
- timelines;
- ScrollTrigger;
- plugins;
- utilities;
- React;
- performance;
- frameworks;
- representative vanilla, React, Vue, and Nuxt examples.

#### Strongest contributions retained

- CSS for simple isolated transitions; GSAP for sequencing, runtime control, complex easing, scroll, dynamic values, SVG, and coordinated interruption.
- Respect the project’s chosen library.
- Register plugins once.
- Prefer transform aliases and `autoAlpha`.
- Use timelines, labels, and position parameters instead of chained timeouts/delays.
- Use `matchMedia` for responsive/reduced-motion behavior.
- Scope and clean up with `useGSAP`, `gsap.context`, or framework lifecycle equivalents.
- Refresh ScrollTrigger after layout changes.
- Avoid excessive triggers and broad `will-change`.
- Use plugins by interaction need: Flip, SplitText, Draggable/Observer, MorphSVG/DrawSVG, ScrollSmoother only when justified.

#### Limitations resolved

- Capability is not justification. Emil/OpenDesign frequency and purpose gates run before GSAP selection.
- Plugin availability does not mean every plugin belongs in the bundle.
- ScrollTrigger patterns must preserve keyboard access, reading order, reduced motion, and static fallback.
- API examples were not copied wholesale; the durable selection, lifecycle, and performance contracts were retained.

#### Excluded as non-doctrine

- exhaustive API reference that is better read from current official docs;
- repetitive framework boilerplate;
- example aesthetics.

### 40.5 `VoltAgent/awesome-design-md`

**Pinned snapshot:** `8147538b4226ae41e2487a9179e3bcc1f68e8554`
**License:** MIT, with source-brand rights remaining with their owners
**Canonical knowledge root:** `design-md/*/DESIGN.md`

#### Repository role

Awesome DESIGN.md is the comparative design-system corpus. It demonstrates that one reusable document grammar can encode radically different visual families—editorial, automotive, retail, fintech, developer tools, AI, productivity, and period web—without requiring one universal house style.

#### Inventory mined

At the pinned commit, repository search found 74 distinct `DESIGN.md` files, while the README still stated 73. The corpus spans systems referencing, among others:

- Apple, Tesla, Nike, BMW, Ferrari, Bugatti, Lamborghini, PlayStation;
- WIRED, The Verge, Spotify, Pinterest;
- Stripe, Mastercard, Wise, Coinbase, Binance, Revolut;
- Figma, Framer, Webflow, Clay, Miro;
- Linear, Vercel, Cursor, Warp, Raycast, Superhuman;
- Anthropic/Claude, Runway, Mistral, Cohere, x.ai, ElevenLabs;
- Shopify, Airbnb, Starbucks;
- Nintendo 2001 and Dell 1996 period systems.

#### Reusable schema mined

- visual atmosphere;
- semantic color roles;
- typography hierarchy;
- component styling and states;
- layout principles;
- depth/elevation;
- do/do-not;
- responsive behavior;
- agent usage guidance;
- often imagery, motion, iconography, tokens, density, and accessibility.

#### Comparative findings retained

- Distinctiveness usually comes from a few controlled systems: photography behavior, type proportions, surface contrast, image/space relationship, component geometry, and signature form.
- A signature system must be paired with a restraint system.
- The same schema can represent radical subtraction, dense editorial composition, monumental sports typography, playful creative tools, cinematic austerity, or retro platform chrome.
- References should donate system discipline, not a brand costume.
- Brand-referencing design systems are inspirations, not official assets or permission to impersonate.

#### Limitations resolved

- The corpus is reverse-engineered and brand-referencing. It cannot be used as a source of proprietary assets, fonts, trademarks, or exact brand identity.
- Individual files vary in depth and factual authority.
- This manifest retains the cross-system schema and comparative lessons rather than merging branded values into a universal style.
- The README/file-count discrepancy is recorded rather than silently normalized.

#### Excluded as non-doctrine

- brand-specific token values and recognizable compositions;
- proprietary font/asset assumptions;
- repeated schema wording after the invariant fields were identified.

### 40.6 `nexu-io/open-design`

**Pinned snapshot:** `05f5b33ef59f078df10ac1125986e00e4a796cf3`
**License:** Apache-2.0 for the project; bundled third-party skills/templates retain their own licenses
**Canonical knowledge roots:** `skills/`, `design-templates/`, `design-systems/`, `craft/`, and the associated protocol/documentation

#### Repository role

Open Design contributes the most complete orchestration model: local-first projects, composable functional skills, rendering templates, design-system packages, universal craft references, previewable artifacts, critique rounds, provenance, handoff, and memory. It also demonstrates what should remain separate: application/runtime plumbing versus design methodology.

#### Product and workflow mined

- Core loop: discover brief → lock direction → stream artifact → critique → deliver.
- Extended workflow: brief → plugin → direction → design system → artifact → handoff → memory.
- Four composable planes:
  1. plugins/runnable workflows;
  2. functional skills/agent behavior;
  3. design templates/rendering blueprints;
  4. design systems/brand contract.
- Real files and live preview rather than image-only mockups.
- Normal versus live/refreshable artifact distinction.
- Skill protocol compatible with `SKILL.md`, with optional metadata for mode, surface, scenario, design-system context, craft references, and critique policy.
- Separate registries for functional skills and design templates.
- User-managed sources shadow bundled sources without deleting them.
- Active design context composition order: usage guidance, full `DESIGN.md`, import guidance, `tokens.css`, component manifest, rich-file index, craft references, then task skill.

#### Design-system package mined

At the pinned snapshot, the bundled catalog documented 151 packages with a minimum shape:

- `manifest.json` for stable metadata and provenance;
- `DESIGN.md` for canonical agent prose;
- `tokens.css` for canonical semantic tokens;
- optional `USAGE.md`, components, derived tokens, Tailwind mapping, assets, fonts, previews, and source evidence.

The package quality rules avoid a rigid nine-heading template while requiring substantive coverage and synchronization between prose and tokens.

#### Universal craft layer mined

Open Design explicitly separates brand-specific `DESIGN.md` from brand-agnostic craft. The craft set includes:

- accessibility baseline;
- animation discipline;
- anti-AI-slop;
- color;
- form validation;
- laws of UX;
- RTL/bidirectionality;
- state coverage;
- typography and hierarchy variants.

This separation is foundational to the architecture in Sections 3–4 and 34.

#### Critique system mined

The Design Jury/Critique Theater uses independent lenses for layout, brief, brand, accessibility, and copy; structured rounds; thresholds; transcripts; interruption; degraded states; and a bounded fallback. This manifest preserves independent lenses and bounded rounds, but adds product strategy and engineering/performance as explicit release lenses.

#### Strongest contributions retained

- Brief → direction → design system → artifact → critique → handoff → memory.
- Separation of task workflow, brand contract, and universal craft.
- Portable design-system package with provenance and rich resources.
- Skill/template distinction and modular metadata.
- Real artifact files, preview, and export/handoff.
- Critique as a structured, replayable, bounded process.
- State coverage, anti-slop, typography hierarchy, animation discipline, accessibility, and RTL craft.
- 80% proven behavior plus a small number of product-specific memorable choices.

#### Limitations resolved

- Open Design is also a large desktop/web/daemon application. Electron shells, runtime adapters, storage, release channels, updater logic, tests, and UI implementation are not website-design doctrine.
- Some anti-slop lints are intentionally blunt. This manifest distinguishes absolute trust failures from aesthetic defaults the brief may earn.
- The bundled catalog contains upstream material, including UI/UX Pro Max and Awesome DESIGN.md; duplicated knowledge was deduplicated at its strongest source.
- Product/plugin counts can change quickly; exact snapshot claims are provenance, not timeless design rules.
- The Critique Theater’s v1 weighting is product-specific; this manifest uses a separate release-weight model with hard gates.

#### Excluded as non-doctrine

- Electron and daemon implementation;
- agent runtime adapters and provider integrations;
- release/update/packaging infrastructure;
- application-specific data paths and operational contracts;
- localized README copies;
- screenshots and generated catalog previews;
- duplicated vendored source already analyzed upstream.

---

### 40.7 `Leonxlnx/taste-skill`

**Pinned snapshot:** `843c8dd4d18ccff0d5a9cd4b0b71d7dbf7278293`  
**License:** MIT  
**Canonical knowledge root:** `skills/taste-skill/SKILL.md` (v2 experimental); supporting skills under `skills/`

#### Repository role

Taste Skill is a compact anti-default frontend and art-direction suite. Its strongest contribution is a mechanical decision layer that sits between the brief and implementation: read the room, declare the direction, calibrate expression, ration recurring AI tells, use image references at readable granularity, protect redesign continuity, and verify that every promised deliverable actually shipped.

The repository contains thirteen registered skills:

- current `taste-skill` v2 and preserved `taste-skill-v1`;
- `gpt-taste`;
- `image-to-code-skill`;
- `imagegen-frontend-web` and `imagegen-frontend-mobile`;
- `brandkit`;
- `redesign-skill`;
- `soft-skill`, `minimalist-skill`, and `brutalist-skill`;
- `stitch-skill`;
- `output-skill`.

It also contains a small research appendix on output truncation, three visual example images, README/sponsor assets, and repository-maintenance scripts.

#### Strongest contributions retained

- **Design Read:** one-line inference of page kind, audience, vibe, and system before code.
- **Three dials:** design variance, motion intensity, and visual density as project-specific coordinates.
- **Brief-to-system routing:** distinguish official systems from aesthetic trends; use primary packages/docs when a real system is named.
- **Expression accountability:** declared dials must be visible in the output.
- **Composition budgets:** exact bento occupancy, section-family variation, marquee scarcity, eyebrow rationing, hero/nav discipline, and duplicate CTA-intent detection.
- **AI-tell registry:** production-observed tells are useful review evidence when classified contextually.
- **Image-first branch:** one readable reference frame per section/state, stable design bible, regenerate details rather than crop, extract contract before code.
- **Brand-world logic:** category, audience, function, emotional promise, cultural position, core metaphor, logo methods, and application proof.
- **Redesign preservation:** audit brand/IA/content/SEO/analytics/accessibility before editing; never silently change routes, navigation, forms, brand marks, or legal copy.
- **Modernization order:** typography and rhythm before risky structural replacement.
- **Motion credibility:** one owner per animated property, no frame-by-frame component state, reduced motion, canonical pin/scrub checks, and “motion claimed = motion shown.”
- **Bounded style modules:** utilitarian minimalism, soft structuralism, industrial print, tactical telemetry, and high-expression editorial treated as presets rather than universal taste.
- **Semantic DESIGN.md language:** descriptive names, exact values, functional roles, explicit bans, and tool-readable contracts.
- **Completeness gate:** scope count, no placeholder omissions, and final cross-check against requested deliverables.

#### Conflicts and overfit rules reconciled

The repository intentionally uses hard bans to correct recurring model behavior. Several are too broad for a universal business-site manifest and were converted into contextual heuristics:

- no universal ban on em dashes, Inter, Lucide, centered heroes, warm beige/brass palettes, serifs in software, light-only sites, hand-authored SVG, or section numbering;
- no mandatory dual-mode design for every consumer page;
- no requirement that every website contain generated imagery or that every image-first project always use a fixed frame count;
- no mandatory AIDA sequence, persistent animation, magnetic buttons, GSAP, Motion, Three.js, simulated randomization, or maximum-variance baseline;
- no rule that a static page is inherently incomplete;
- no source-specific exact font, radius, padding, line-count, or package preference promoted above brand/content fit;
- no platform-specific Stitch/mobile image-generation behavior promoted into web implementation law.

The current v2 correctly marks its rules as contextual, but individual subsections still contain absolute language. This manifest follows the top-level contextual instruction and the authority hierarchy in Section 3.

#### Research appendix assessment

The appendix contains useful operational suggestions—modular skills, explicit structure, evidence blocks, chunked execution, deliverable counts, and verification loops. It also contains precise causal, platform, seasonal, cost, context-window, and performance claims without sufficient durable citations or with conclusions broader than the named studies support. Those claims were not used as doctrine. The manifest retains only controls that stand on their own as sound engineering practice.

#### Excluded as non-doctrine

- preserved v1 material duplicated or superseded by v2;
- sponsor/README asset processing scripts and install-registry convenience;
- image binaries and promotional assets;
- mobile-only device-frame and screen-count rules outside transferable consistency principles;
- fixed image-output counts when image generation is not the chosen workflow;
- unverified research percentages, seasonal claims, provider-economics claims, and hidden middleware assertions;
- instructions to reveal private chain-of-thought;
- package-specific code snippets already covered more authoritatively by official documentation and the GSAP/Emil sources.

---

## 41. Cross-source synthesis and conflict resolution

### 41.1 Contribution matrix

| Capability | Primary source | Supporting sources | Manifest location |
|---|---|---|---|
| Product/design/surface truth | Impeccable | Open Design | 3–6, 34 |
| Visual-world generation | Impeccable | Awesome DESIGN.md | 7–9, 36 |
| Retrieval and stack-aware recommendations | UI/UX Pro Max | Open Design | 7.4, 31 |
| Comparative design-system grammar | Awesome DESIGN.md | Open Design | 34, 40.5 |
| Skill/package orchestration | Open Design | Impeccable | 2, 4, 39 |
| Motion decision and taste | Emil Kowalski | Open Design craft | 11, 24 |
| Brief inference and expression calibration | Taste Skill | Impeccable | 6.1A, 8.1A |
| Image-first art direction and reference-to-code | Taste Skill | Impeccable comp-led path | 8.6A, 20.8 |
| Redesign preservation and modernization order | Taste Skill | Impeccable | 5.3A, 12.3A |
| GSAP implementation | GSAP Skills | Emil Kowalski | 24.8–24.9 |
| Anti-generic enforcement | Impeccable, Open Design | Awesome DESIGN.md | 36 |
| Mechanical AI-tell/repetition controls | Taste Skill | Impeccable, Open Design | 17.10, 36 |
| Bounded style presets and semantic tool contracts | Taste Skill | Awesome DESIGN.md, Open Design | 8.4B, 34.20 |
| State hardening | Open Design craft, Impeccable | UI/UX Pro Max | 23, 27, 35 |
| Accessibility | UI/UX Pro Max, Open Design | Impeccable, W3C | 26, 37 |
| Responsive adaptation | Impeccable | UI/UX Pro Max | 25 |
| Technical audit | Impeccable | Open Design jury | 35 |
| Business conversion/message architecture | New synthesis | All | 15–16 |
| SEO/structured data | Primary standards/new synthesis | UI/UX Pro Max | 28 |
| Security/privacy/legal | New synthesis | Impeccable hardening | 29 |
| Analytics/experiments | New synthesis | — | 30 |
| CMS/content operations | New synthesis | Open Design packaging | 32 |

### 41.2 Resolved tensions

#### Taste doctrine versus catalog recommendation

Catalogs generate candidates. Product truth and the selected visual thesis decide. A high-scoring catalog row that produces category cliché is rejected.

#### Motion capability versus motion restraint

The motion purpose/frequency gate runs before technology selection. GSAP is chosen only after motion earns its place and simpler tools fail the requirement.

#### Brand reference versus brand imitation

Reference systems donate one discipline at a time. No site inherits another brand’s combined type, palette, composition, imagery, and motion signature.

#### Brief wins versus universal rules

The brief may override aesthetic defaults. It does not silently override truth, security, data integrity, or critical accessibility.

#### 24px versus 44px targets

WCAG 2.2 AA defines a 24×24 CSS px minimum with exceptions. This manifest uses that as the compliance floor and roughly 44×44 as the default touch usability target.

#### Fixed breakpoints versus content-driven adaptation

Example breakpoint values are useful starting observations. The final breakpoint is placed where content, hierarchy, or interaction breaks.

#### Reduced motion versus disabling all feedback

Reduced motion removes or substitutes vestibular movement while preserving state, hierarchy, and feedback. A universal `0.01ms` kill is not the default.

#### Aesthetic score versus release gate

Aesthetic judgment informs the design. Brief fit, accessibility, engineering, truth, and critical defects determine whether it may ship.

#### Hard anti-tell bans versus contextual taste

Taste Skill’s production blacklist is treated as an empirical heuristic set. Absolute bans remain absolute only for truth, rights, accessibility, security, or broken behavior. Punctuation, fonts, icon libraries, palette families, section labels, hero alignment, and theme count are judged against the brief and cumulative page signature.

#### Image-first generation versus code-first proof

Image-first work is a branch, not a mandatory step. Use it when art direction is the unresolved variable. Use a code-first vertical slice when behavior, content fit, responsiveness, or implementation feasibility is the unresolved variable. Both paths must produce the same durable `DESIGN.md` contract.

#### Preset speed versus system coherence

A style preset accelerates choices but cannot create a second design system. Its expressive values compile into shared semantic tokens, components, states, and contextual fallbacks.

#### Completeness pressure versus bounded scope

Deliver every requested item fully, but do not manufacture speculative files, variants, or abstractions. Scope-lock first; completeness applies to the agreed scope.

### 41.3 Gaps filled beyond the repositories

The source repositories are strongest in visual systems, interaction craft, motion, and agent workflows. A complete business-website skill also needs:

- business objective and buyer decision architecture;
- claim/proof governance;
- conversion and offer logic;
- SEO and structured data;
- security, privacy, and legal review boundaries;
- analytics and experiment integrity;
- CMS/editorial operations;
- deployment, monitoring, rollback, and ownership.

Those modules were added from first principles and current primary web standards rather than inferred from visual-design catalogs.

### 41.4 Deduplication policy

When the same doctrine appears in multiple repositories:

1. retain the clearest canonical source;
2. merge genuinely complementary details;
3. preserve conflicts and resolve them explicitly;
4. exclude generated mirrors and vendored duplicates;
5. avoid embedding large volatile datasets when a query protocol is more usable;
6. retain provenance and exact commit snapshots.

This is why the manifest is a synthesis rather than a concatenation.

---

## 42. Source provenance and licenses

### 42.1 Repository sources

| Repository | Snapshot | License | Source |
|---|---|---|---|
| pbakaus/impeccable | `e5abceedc44ee6284a5ebb0bd309e30706d2cb8c` | Apache-2.0 | https://github.com/pbakaus/impeccable |
| nextlevelbuilder/ui-ux-pro-max-skill | `bc826e2267a36d98a2dcf5231e16c30ff546770f` | MIT | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| emilkowalski/skills | `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7` | MIT | https://github.com/emilkowalski/skills |
| greensock/gsap-skills | `aed9cfd3277740755f6bfc1155c7aa645403b760` | MIT | https://github.com/greensock/gsap-skills |
| VoltAgent/awesome-design-md | `8147538b4226ae41e2487a9179e3bcc1f68e8554` | MIT | https://github.com/VoltAgent/awesome-design-md |
| nexu-io/open-design | `05f5b33ef59f078df10ac1125986e00e4a796cf3` | Apache-2.0; bundled third-party notices apply | https://github.com/nexu-io/open-design |
| Leonxlnx/taste-skill | `843c8dd4d18ccff0d5a9cd4b0b71d7dbf7278293` | MIT | https://github.com/Leonxlnx/taste-skill |

This document is an original synthesis and paraphrase, not a verbatim aggregation. If downstream work copies upstream code, templates, or substantial source text, preserve the applicable copyright and license notices.

Brand names in source corpora identify references. They do not imply sponsorship, affiliation, or permission to reproduce proprietary brand assets.

### 42.2 Primary standards consulted

Current as of 2026-08-21:

- WCAG 2.2, W3C Recommendation: https://www.w3.org/TR/WCAG22/
- WAI summary of WCAG 2.2 additions: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Core Web Vitals overview and thresholds: https://web.dev/articles/vitals
- Core Web Vitals threshold methodology: https://web.dev/articles/defining-core-web-vitals-thresholds
- Google Search structured-data guidelines: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- MDN `prefers-reduced-motion`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion
- MDN View Transition API: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API

Primary standards override stale catalog advice on compliance and platform behavior.

---

## 43. Final operating directive

When asked to design or build a site:

1. Read the real product and codebase.
2. Establish product truth and the surface job.
3. Classify visual authority.
4. Research the product, audience, category rut, and outside visual systems.
5. Declare the design read and calibrate variance, motion, and density.
6. Create or inherit one coherent visual world.
7. Define its signature, restraint, optional concept spine, and one second-read moment.
8. Use image-first proof only when art direction is the unresolved variable; extract a written contract before code.
9. Turn the direction into a durable design contract and semantic tokens.
10. Build the smallest complete representative slice with real content and states.
11. Add motion only when purpose and frequency justify it, and make the declared intensity truthful.
12. Recompose for context; do not merely shrink.
13. Audit truth, accessibility, performance, responsive behavior, SEO, security, operations, repetition, and AI tells.
14. Fix shared root causes.
15. Verify the locked deliverable count and ship only when the artifact is recognizable, useful, accessible, fast, truthful, maintainable, and measurable.

The goal is not to make every site loud or strange. The goal is to make every site inevitable for its product—and impossible to confuse with a generic template.
