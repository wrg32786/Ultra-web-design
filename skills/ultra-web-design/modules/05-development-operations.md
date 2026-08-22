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
