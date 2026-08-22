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
