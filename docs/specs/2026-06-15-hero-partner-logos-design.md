# Hero partner logos — design

**Date:** 2026-06-15
**Status:** Approved
**Scope:** Individual project pages (`layouts/projects/single.html`)

## Goal

Show partner/collaborator logos directly on the project hero image so the
collaboration is visible at a glance, without scrolling to the existing
"In partnership with" strip lower on the page.

## Decision summary

- **Placement:** top-right corner of the hero, overlaid on the photo +
  gradient. The title, tagline, and stat band stay where they are
  (bottom-left). Logos and stats never compete for the same space.
- **Treatment:** each partner logo sits in its own **white rounded chip**
  (logo rendered as an `<img>`). A small right-aligned uppercase label
  **"In partnership with"** sits above the chip row.
- **Data source:** the existing `clients:` front matter. No new front-matter
  fields, no content edits.
- **The existing lower partner strip (section 5) stays unchanged.** The hero
  chips are the at-a-glance signal; the lower strip remains the fuller,
  light-background showcase. Intentional, mild repetition.

## Why these choices

- **White chips** guarantee legibility for the heterogeneous logo files
  (transparent PNGs, JPGs with white backgrounds, SVGs, dark-ink marks) on a
  dark photo, without requiring new white/knockout logo variants — which most
  partners don't have.
- **Top-right placement** keeps the existing bottom-left composition
  (kicker → title → tagline → stats) intact, so this is additive rather than a
  re-layout.

## Logo resolution

Reuse the exact logic already in section 5 of `single.html`:

- For each `client`, take `client.logo`, strip the leading `/`.
- Prefer a dark-text variant: `resources.Get (replace path "logo.png" "logo_dark.png")`,
  falling back to `resources.Get path`. (Chips are light, so white-on-transparent
  logos would vanish without the dark variant — same reason the lower strip does this.)
- For non-SVG raster logos wider than a threshold, resize down (the lower strip
  uses `380x`; the hero chips are smaller, so resize to a hero-appropriate width,
  e.g. `200x`, and let CSS cap the rendered height to ~24–28px).
- Pass SVGs through untouched.
- Skip any client whose logo resource can't be resolved (same guard as today).

## Markup

Add a hero logo block inside `.about-hero__overlay` (or as an absolutely
positioned sibling within `.project-hero`), gated on `.Params.clients`:

```
{{ with .Params.clients }}
<div class="project-hero__partners">
  <span class="project-hero__partners-label">In partnership with</span>
  <div class="project-hero__partners-logos">
    {{ range $partner := . }}
      {{/* same logo resolution as section 5 */}}
      {{ with $img }}
      <span class="project-hero__partner-chip" title="{{ $partner.name }}">
        <img src="{{ .RelPermalink }}" alt="{{ $partner.name }}" loading="eager">
      </span>
      {{ end }}
    {{ end }}
  </div>
</div>
{{ end }}
```

Notes:
- The hero is above the fold, so `loading="eager"` (the hero photo itself
  already uses `fetchpriority="high"` / `lazy=false`).
- Chips are not links in the hero (the lower strip keeps the links). Keeps the
  corner uncluttered; the title/CTA are the hero's interactive elements.

## Styling (`assets/sass/4-layouts/_project-single.scss`)

- `.project-hero__partners` — absolutely positioned, `top`/`right` ~20px, on a
  z-index above the overlay gradient. Right-aligned text.
- `.project-hero__partners-label` — small (~10px), uppercase, letter-spaced,
  white at ~80% opacity, right-aligned, small bottom margin.
- `.project-hero__partners-logos` — flex, `gap` ~9px, `flex-wrap: wrap`,
  `justify-content: flex-end`, with a capped `max-width` so chips wrap to a
  second row in the corner instead of crossing into the title.
- `.project-hero__partner-chip` — white background (~94% opacity), rounded
  (~8px), padding ~7px 12px, subtle shadow; `img` inside capped to ~24–28px
  tall, `width: auto`, `display: block`.

### Responsive

- **Desktop / tablet:** top-right as above. 4 partners (wild salmon) wrap to two
  rows — validated in the brainstorm mock.
- **Mobile (`max-width: $mobile`):** there's no room top-right next to the
  larger relative title, so the partner block **reflows into the bottom overlay**
  beneath the stats: static position (not absolute), left-aligned label and
  chips, normal flow at the end of `.about-hero__overlay` content.
  Implementation options (pick during build): a single block whose positioning
  switches at the breakpoint, or duplicate-and-toggle with `display`. Prefer the
  single-block switch if achievable without markup duplication.

## Edge cases

- **No `clients`:** the whole block is gated by `{{ with .Params.clients }}`,
  so nothing renders (current behavior preserved).
- **1 partner (coral, several others):** single chip top-right.
- **4 partners (wild salmon):** chips wrap to two rows in the corner; reflow to
  bottom stack on mobile.
- **Projects without a hero image** (`project-hero--gradient`): the chips render
  the same way over the gradient background — no special handling needed.
- **Logo with only `logo.png` (no dark variant):** uses `logo.png`; white chip
  keeps it legible.

## Files changed

- `layouts/projects/single.html` — add the hero partner block in the hero
  overlay, reusing section 5's logo resolution.
- `assets/sass/4-layouts/_project-single.scss` — new `.project-hero__partners*`
  styles + mobile reflow.
- Section 5 (lower strip), front matter, and content files: **unchanged.**

## Verification

- `hugo` builds clean.
- Spot-check rendered pages across the partner-count spread:
  - 1 partner: `coral_reef_health_monitoring`
  - 2 partners: `biowatch-app` / `elephants_passive_acoustic_monitoring`
  - 4 partners: `wild_salmon_migration_monitoring`
  - no stats vs. with stats; gradient-only hero (no image) if one exists.
- Confirm chips are legible on the photo, wrap correctly at 4 partners, and
  reflow to the bottom on a mobile viewport without overlapping the title.
- Confirm the lower "In partnership with" strip is still present and unchanged.
