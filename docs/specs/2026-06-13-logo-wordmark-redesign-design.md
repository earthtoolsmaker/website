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

Two lockups are used on the site:

- **etm** — pangolin + `etm` (compact abbreviation). File: `etm-logo-etm.*`.
- **earthtoolsmaker** — pangolin + full `earthtoolsmaker`. File:
  `etm-logo-text.*`.

(During design we also explored pangolin-as-"e" variants — `arthtoolsmaker`
and `tm` — but they are not used on the site.)

## Behavior

The header logo is responsive to page and hover:

- **Home page header:** full `earthtoolsmaker`, static.
- **Every other page header:** compact `etm` by default, **crossfading** to the
  full `earthtoolsmaker` on hover/focus (~0.35s ease). Both images are stacked
  in one CSS grid cell so the cell reserves the wider full-word width and the
  nav never shifts; only opacity animates.
- **Footer (all pages):** full `earthtoolsmaker`, static.

The header logo was also reduced in size (max-height 120px → 60px desktop,
scaling down on smaller breakpoints).

## Deliverables

Two asset pairs under `assets/images/logos/`:

| Lockup | SVG | PNG |
|---|---|---|
| Full `earthtoolsmaker` | `etm-logo-text.svg` | `etm-logo-text.png` |
| Compact `etm` | `etm-logo-etm.svg` | `etm-logo-etm.png` |

Each SVG embeds the pangolin as a base64 PNG and carries the Fraunces text as
vector outlines (paths), so it renders without the font installed. Each PNG is
rasterized from its matching SVG (transparent background, 8× device scale,
cropped to a constant canvas height) so PNG and SVG match and both lockups
share identical vertical geometry.

Site wiring:

- `config.toml` — `params.logo` = `etm-logo-text.png` (full; footer + home +
  hover state), new `params.logo_etm` = `etm-logo-etm.png` (interior default).
- `layouts/partials/header.html` — conditional lockup: home → static full;
  other pages → `etm`/full crossfade `<span class="logo__swap">`.
- `assets/sass/3-modules/_header.scss` — smaller `max-height`; `.logo__swap`
  grid-stack + opacity crossfade on `:hover`/`:focus-visible`.

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
3. Rasterize the SVG with Chromium at 8× on a transparent background; crop the
   left/right transparent columns and to the constant canvas height.

## Out of scope

- The icon-only mark (`etm-logo.png`) — unchanged.
- The favicon and other brand assets.
- Dark-mode logo variant (`params.logo_dark` remains unset, as before).

## Verification

- The two asset pairs exist, transparent, with identical pangolin position and
  text baseline (verified: both PNGs 560px tall, baseline at row 396).
- `hugo` builds cleanly. Home header shows full `earthtoolsmaker`; interior
  pages show `etm`; the swap crossfades to the full word on hover with the
  pangolin static and baselines aligned (verified via a replica render).
- Footer shows the full wordmark at its 50px max-height.
