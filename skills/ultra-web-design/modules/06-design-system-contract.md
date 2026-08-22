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
