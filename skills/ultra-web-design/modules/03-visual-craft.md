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
