# Logo wordmark redesign

**Date:** 2026-06-13
**Status:** Approved design, pending implementation

## Goal

Replace the EarthToolsMaker text wordmark with a cleaner, more distinctive
treatment. Keep the existing pangolin-and-globe icon; change only the text.

The current logo sets the name in a flowing three-color script
(charcoal / coral / magenta), which reads as informal and generic. The new
wordmark is a single, deliberate serif in one color.

## The new wordmark

Shared type treatment for both variants:

- **Icon:** existing `assets/images/logos/etm-logo.png` (pangolin + globe),
  unchanged.
- **Typeface:** Fraunces (serif), weight 600.
- **Case:** all lowercase.
- **Letter-spacing:** −0.015em.
- **Color:** charcoal `#1f2937` (single unified color).

Two variants are produced:

**Variant B — pangolin-as-"e" (no "e" letter)** — the default site logo.
- **Word:** `arthtoolsmaker` set immediately after the icon, so the pangolin
  stands in for the first "e" — reading `(e)arthtoolsmaker`.
- **Spacing:** word offset **−5px horizontally** (pulled toward the icon) and
  **+5px vertically** (dropped down) so it nests into the pangolin's body.
  Offsets are at the mockup reference size (icon height 58px, font-size 38px)
  and scale proportionally with the rendered size.
- Decided in the visual brainstorm
  (`.superpowers/brainstorm/.../pangolin-e-v7.html`, option "down 5px").

**Variant A — icon + full word (with "e" letter)**.
- **Word:** full `earthtoolsmaker`, fully legible, set after the pangolin used
  as a standalone icon.
- **Spacing:** standard gap (~12px at reference size), vertically centered. No
  horizontal pull-in or vertical drop.

## What changes in the site

The horizontal lockup lives in one file:

- `assets/images/logos/etm-logo-text.png` (currently 1041×276, RGBA).

It is referenced via `params.logo = "/images/logos/etm-logo-text.png"` in
`config.toml` and rendered in two places:

- Site header — `layouts/partials/header.html` (`logo__image`)
- Footer — `layouts/partials/footer-widgets/widget-info.html`

Replacing that single asset updates both. The icon-only `etm-logo.png` is not
touched. No template or config changes are required if the new file keeps the
same path and a compatible aspect ratio.

## Deliverables

Four asset files — both variants, each in SVG and PNG:

| Variant | SVG | PNG |
|---|---|---|
| B · pangolin-as-"e" (default site logo) | `etm-logo-text.svg` | `etm-logo-text.png` |
| A · icon + full word | `etm-logo-text-full.svg` | `etm-logo-text-full.png` |

All under `assets/images/logos/`. `etm-logo-text.png` is the drop-in
replacement the site already loads via `params.logo`. Variant A is an
additional asset; the site can switch to it later by pointing `params.logo` at
`etm-logo-text-full.png`.

Each SVG embeds the pangolin as a base64 PNG and carries the Fraunces text as
vector **outlines (paths)**, so it renders identically without the font
installed. Each PNG is **rasterized from its matching SVG** (transparent
background, high resolution, auto-cropped) so PNG and SVG are guaranteed to
match.

## Production approach

Available tooling (verified): headless Chromium (`/snap/bin/chromium`, snap —
needs `$HOME`-rooted paths), Python with PIL 10.2 and fontTools 4.46. No
Inkscape, so SVG text is outlined with fontTools rather than an export flag.

Pipeline (per variant):

1. **Font:** download the Fraunces variable TTF from Google Fonts, then pin it
   to a static instance at `wght=600` (and `opsz`/`SOFT`/`WONK` at sensible
   fixed values) with `fontTools.varLib.instancer`. Work directly from this
   TTF in Python — no system install needed, since the SVG carries outlines.
2. **SVG:** for each lowercase letter, pull its glyph outline from the
   instanced font with `fontTools` (`SVGPathPen`), laying glyphs out left to
   right by advance width plus the −0.015em letter-spacing. Embed the pangolin
   as a base64 PNG `<image>`. Apply the variant's icon/word offsets. Fill the
   text paths with `#1f2937`. Write `etm-logo-text.svg` / `-full.svg`.
3. **PNG:** rasterize each SVG with headless Chromium (`--screenshot`,
   transparent background, `--force-device-scale-factor` ≈ 3 for crispness),
   then auto-crop to the non-transparent bounds with PIL. Because the PNG comes
   from the SVG, the two always match.

## Out of scope

- The icon-only mark (`etm-logo.png`) — unchanged.
- The favicon and any other brand assets.
- Switching the site default to variant A — both variants are produced, but
  `params.logo` stays pointed at variant B (`etm-logo-text.png`).

## Verification

- All four assets exist under `assets/images/logos/` with transparent
  backgrounds; PNGs auto-cropped, SVGs open and render standalone.
- Variant B matches the approved mockup (pangolin-as-"e", lowercase Fraunces
  600, charcoal, −5px / +5px offsets); variant A shows the full legible
  `earthtoolsmaker` with a visible "e".
- For each variant, the SVG and its rasterized PNG look identical.
- `hugo` builds cleanly; header and footer show the new variant-B logo at a
  sensible size (no layout overflow). Confirm against a static build, not the
  live `hugo server` (which can serve stale pages).
