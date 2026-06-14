# Homepage Hero Revamp

**Date:** 2026-06-13
**Status:** Approved

## Problem

The homepage hero is pure centered typography on a plain page background: a
93px Newsreader headline with a teal-gradient italic span, a description line,
and two buttons. It's clean but visually flat — it carries no imagery and does
little to convey what EarthToolsMaker actually does. The goal was explicitly
**more visual impact** and a **modernized aesthetic**, not more conversion or
credibility machinery.

## Goal

A warmer, more alive hero — "Living Canvas": the headline sits centered over a
soft flat-vector nature scene (layered hills + drifting wildlife silhouettes) in
the existing ocean palette, in the same visual language as the spaces cards. New
copy and a calmer, solid-color title highlight. Light mode is the design target;
dark mode degrades gracefully.

## Decisions

- **Direction:** A — "Living Canvas". Full-bleed flat-vector scene as a band
  *behind* the centered text (not a side panel). Text stays centered and fully
  legible.
- **Copy:**
  - Headline: `Open tools for the people <span><i>protecting nature</i></span>`
  - Tagline: `We build open source AI that helps conservation scientists monitor
    wildlife, detect threats, and protect ecosystems.`
- **Title highlight color:** solid deep teal (`--secondary-color`, `#006d77`),
  replacing the current teal gradient. Quieter, more editorial.
- **Buttons:** `Get In Touch` (primary → `/contact/`, unchanged) +
  `Our Work` (secondary → `/projects/`, replacing the old `About` → `/about/`).
- **Artwork:** CC0 PhyloPic silhouettes composed into one scene, same flat-vector
  style/palette as the spaces card SVGs. Starting cast: whale, a small bird
  flock, a fish, kelp. Swappable.
- **Motion:** subtle independent drift on the silhouettes via CSS keyframes;
  disabled under `prefers-reduced-motion`.
- **Scope:** light mode only for this design. Dark mode must not look broken, but
  no bespoke dark scene (see Out of scope).

## Design

### Layout & page fit

The hero becomes a full-bleed band. Structure, front to back:

1. **Header/nav** sits over the top of the scene (as it effectively does today).
   The scene's top is veiled so nav links stay legible.
2. **`.hero__inner`** — centered headline, tagline, buttons — z-indexed above the
   scene. Unchanged structure; restyled.
3. **`.hero__scene`** — an inline SVG behind the content.

**Critical transition:** the scene's vertical gradient resolves to
`--background-color` at the bottom, so the hero *dissolves* into the
"Featured Projects" section rather than ending in a hard band edge. This reuses
the veil/fade technique already present in `.hero__image--illustration`
(top veil for nav legibility + bottom fade to page color).

The rest of the homepage (`section-projects` onward), section spacing, the coral
zig-zag divider, and the card grid are **untouched**. The hero is the only thing
that changes; the fade is what makes it hand off cleanly.

### The scene (inline SVG)

The scene is **inline SVG** (not an `<img>`) so individual silhouette groups can
be CSS-animated and gated by `prefers-reduced-motion`. To keep
`section-hero.html` readable, the scene markup lives in a new partial
`hero-scene.html`.

Composition, in the spaces-card visual language:

- **Background gradient** — soft sky → sand → seafoam → page color (top to
  bottom), matching the card `sky`/`water` gradient feel.
- **Layered hills** — 2–3 stacked wave/hill paths (`#bfe0d6`, `#88c8b9`,
  `#4f9e8e`) along the bottom, as in the cards.
- **Silhouette groups** — 4 CC0 PhyloPic silhouettes (whale, bird flock, fish,
  kelp), each in its own `<g class="hero__crit hero__crit--N">`, at staggered
  positions and opacities (foreground solid, mid/background faded ~0.5/0.3),
  fill = a deep teal (`#0c6f78`).

The scene is decorative: `aria-hidden="true"` / `role="presentation"`, no alt
text. The headline carries the accessible meaning.

### Motion

- Per-silhouette `@keyframes` drift (small `translate`, e.g. 8–16px), each group
  with its own duration (~9–15s) and `ease-in-out infinite`, so they move
  independently and slowly.
- Wrapped in `@media (prefers-reduced-motion: reduce)` → `animation: none`.

### Title restyle

- `.hero__title span` changes from `background: var(--text-gradient)` +
  transparent fill to `color: var(--secondary-color)` (solid). Keep the italic.
- The new headline is longer than the old one, so revisit the base size: drop
  from 93px to a size that fits two lines comfortably (≈64–72px desktop), keeping
  the existing responsive step-downs at `$wide`/`$desktop`/`$tablet`/`$mobile`.

### Light / dark behavior

Light mode is fully designed. For dark mode (graceful, not polished):

- The bottom fade already targets `--background-color`, which is dark in dark
  mode — so the hero still dissolves into the page.
- Add a `:root[dark]` / `.dark-mode` override so the scene's light gradient and
  hill fills don't clash on a dark page: reduce the scene to a subtle wash
  (silhouettes at low opacity over the dark page background, light gradient
  suppressed). The title highlight uses `--secondary-color`, which already swaps
  per theme.
- Goal: legible and not-broken in dark, nothing more.

### Responsive

- Reuse the existing hero height step-down on mobile.
- On small screens, the centered text becomes left-aligned (existing `$mobile`
  rule). Reduce/relocate silhouettes on mobile so they don't collide with the
  text — keep only 1–2 background silhouettes near the edges.

## Files touched

- `config.toml` — `[params.hero]`: update `hero_title` and `hero_description`;
  replace the second button (`hero_button_about` → a "Our Work" label pointing at
  `/projects/`). `hero_image` is already unused by the template — remove it as
  part of this change.
- `layouts/partials/section-hero.html` — include the new `hero-scene.html` behind
  `.hero__inner`; point the second button at `/projects/` with the new label.
- `layouts/partials/hero-scene.html` *(new)* — the inline decorative scene SVG
  (gradient + hills + 4 silhouette groups), `aria-hidden`.
- `assets/sass/3-modules/_hero.scss` — add `.hero__scene` (absolute, behind
  content, top veil + bottom fade to `--background-color`); silhouette drift
  keyframes + `prefers-reduced-motion` guard; change `.hero__title span` to solid
  `--secondary-color`; retune title size for the longer headline; dark-mode
  graceful override; mobile silhouette adjustments.
- `docs/specs/spaces-illustration-credits.md` — add CC0 PhyloPic attribution for
  the hero silhouettes (consistent with the existing card credits).

## Out of scope

- A bespoke, polished dark-mode scene (dark only needs to degrade gracefully).
- Any other homepage section (projects, testimonials, blog, tags).
- New conversion or credibility elements (stats, partner logos, product UI) —
  this is a look-and-feel + copy change only.
- Scroll-based parallax (we chose subtle CSS drift, not scroll effects).
