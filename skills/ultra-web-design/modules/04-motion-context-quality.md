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
