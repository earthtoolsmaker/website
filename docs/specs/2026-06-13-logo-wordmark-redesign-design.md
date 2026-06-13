# Logo wordmark redesign

**Date:** 2026-06-13
**Status:** Implemented

## Goal

Replace the EarthToolsMaker text wordmark with a cleaner, more distinctive
treatment. Keep the existing pangolin-and-globe icon; change only the text.

The old logo set the name in a flowing three-color script
(charcoal / coral / magenta), which read as informal and generic. The new
wordmark is a single, deliberate serif in one color.

## Type treatment

Shared across every lockup:

- **Icon:** existing `assets/images/logos/etm-logo.png` (pangolin + globe),
  unchanged.
- **Typeface:** Fraunces (serif), weight 600.
- **Case:** all lowercase.
- **Letter-spacing:** −0.015em.
- **Color:** charcoal `#1f2937` (single unified color).
- **Placement:** the word is pulled in toward the pangolin (−4px) and dropped
  down (+5px) so it nests into the pangolin's body. Vertical centering uses the
  font's constant x-height (NOT each word's own bounding box) so that every
  lockup shares the exact same baseline and pangolin position — essential for
  the header crossfade (below) to not make the word jump.

Two word lockups appear on the site: compact `etm` and full `earthtoolsmaker`.
(During design we also explored pangolin-as-"e" variants — `arthtoolsmaker`
and `tm` — but they are not used.)

## Behavior

The header logo is responsive to page and hover:

- **Home page header:** full `earthtoolsmaker`, static (baked lockup
  `etm-logo-text.png`).
- **Every other page header:** compact `etm` by default, **staggered-fading**
  to the full `earthtoolsmaker` on hover/focus. The pangolin is a *separate
  static layer* that never animates; only the word swaps. The word fade is
  staggered (etm fades out over ~0.18s, then earthtoolsmaker fades in over the
  next ~0.18s) so the two words never overlap — at the midpoint only the
  pangolin shows. The three layers (pangolin + two words) share identical image
  dimensions and stack absolutely; the full-width pangolin layer reserves the
  wide full-word width so the nav never shifts.
- **Footer (all pages):** full `earthtoolsmaker`, static.

The header logo was also reduced in size (max-height 120px → 60px desktop,
scaling down on smaller breakpoints). The leftover `padding-top: 40px` on
`.main-nav` and `.header__cta` — which had vertically centered them against the
old 120px logo — was removed so the grid's `align-items: center` aligns the
nav and Support button with the new, smaller logo.

## Deliverables

Asset files under `assets/images/logos/` (each as SVG + PNG):

| Asset | Purpose |
|---|---|
| `etm-logo-text` | Full `earthtoolsmaker` lockup — home header + footer |
| `logo-pangolin` | Static pangolin layer — non-home header swap |
| `logo-word-etm` | `etm` word layer — non-home header swap |
| `logo-word-full` | `earthtoolsmaker` word layer — non-home header swap |

Each SVG embeds the pangolin as a base64 PNG and carries the Fraunces text as
vector outlines (paths), so it renders without the font installed. Each PNG is
rasterized from its matching SVG (transparent background, 8× device scale). The
three swap layers share ONE canvas (the full-word lockup geometry) so they are
identical-size and stack pixel-perfectly.

Site wiring:

- `config.toml` — `params.logo` = `etm-logo-text.png` (full; footer + home).
- `layouts/partials/header.html` — home → static full lockup; other pages →
  `<span class="logo__swap">` with three layered `<img>`s (pangolin +
  word-etm + word-full). Word layers are `aria-hidden`; the pangolin carries
  the alt text.
- `assets/sass/3-modules/_header.scss` — smaller `max-height`; `.logo__swap`
  static pangolin + absolutely-stacked word layers with staggered opacity on
  `:hover`/`:focus-visible`; removed the stale 40px nav/CTA top padding.

## Production approach

Tooling (verified): headless Chromium (`/snap/bin/chromium`, snap — `$HOME`
paths only), Python with PIL and fontTools. The generator lives in the
gitignored build dir `.superpowers/logobuild/gen_logo.py`:

1. Download the Fraunces variable TTF; pin a static instance at
   `wght=600, opsz=38, SOFT=0, WONK=0` with `fontTools.varLib.instancer`.
2. Outline each lowercase letter (`SVGPathPen`), laying glyphs out by advance
   width + −0.015em tracking; embed the pangolin as a base64 `<image>`; place
   the word with the variant's −4px / +5px offsets; vertical metrics from the
   font's x-height/ascender/descender (constant across words). Fill `#1f2937`.
3. Rasterize the SVG with Chromium at 8× on a transparent background; crop to
   the constant canvas height.

`build_layers()` emits the three swap layers (`logo-pangolin`,
`logo-word-etm`, `logo-word-full`) from one shared canvas — the pangolin
`<image>` alone, and each word's paths alone — so all three rasterize to
identical dimensions and overlay exactly.

## Out of scope

- The icon-only mark (`etm-logo.png`) — unchanged.
- The favicon and other brand assets.
- Dark-mode logo variant (`params.logo_dark` remains unset, as before).

## Verification

- All assets exist and are transparent. The three swap layers are identical
  dimensions (2892×560) with matching baseline (row 396) and word start-x
  (col 505).
- `hugo` builds cleanly. Home header shows full `earthtoolsmaker`; interior
  pages show `etm`. The staggered fade (verified via a replica render) shows
  etm → pangolin-only → earthtoolsmaker with the pangolin solid throughout and
  no word overlap.
- Nav links and Support button align with the new smaller logo (home + interior
  screenshots).
- Footer shows the full wordmark at its 50px max-height.
