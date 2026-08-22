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
