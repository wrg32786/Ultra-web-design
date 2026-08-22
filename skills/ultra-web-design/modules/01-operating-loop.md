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
