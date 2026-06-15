# Pyronear hero video — design

**Date:** 2026-06-15
**Status:** Approved

## Goal

Give the Pyronear tool page the same looping background-video hero that the
SalmonVision tool page has. The clip should read as a drone shot drifting over a
forest canopy and loop seamlessly behind an overlaid headline.

## Background

SalmonVision (`content/tools/salmonvision/index.md`) opens with a `.tool-hero`
block: a muted, autoplaying, looping `<video>` filling a 16/7 rounded panel, with
a gradient overlay carrying a title and tagline. The supporting CSS
(`.tool-hero`, `.tool-hero__video`, `.tool-hero__overlay`, `.tool-hero__title`,
`.tool-hero__tagline` in `assets/sass/3-modules/_tools.scss`) is already generic
— not SalmonVision-specific — so no CSS work is needed to reuse it.

Pyronear (`content/tools/pyronear/index.md`) currently opens with a plain
`# Open, Real-Time Wildfire Detection` H1.

## Design

### 1. Asset
- Source a CC0 / royalty-free aerial-over-forest clip (Coverr / Pixabay are CC0;
  Pexels license permits free use). Prefer footage that already loops cleanly or
  can be trimmed to a clean loop.
- Optimize with `ffmpeg` to match the SalmonVision hero profile: H.264 mp4,
  ~1080p, **audio stripped**, short (~10–20s), small file (SalmonVision's hero is
  ~843 KB — aim for the same ballpark).
- Save to `static/videos/pyronear-hero.mp4`.

**Fallback:** if no strong CC0 clip is found, stop and ask the user (do not
auto-fall-back to extracting Pyronear's YouTube footage).

### 2. Markup
In `content/tools/pyronear/index.md`, replace the
`# Open, Real-Time Wildfire Detection` H1 with the SalmonVision `.tool-hero`
block, adapted:

```html
<div class="tool-hero">
  <video class="tool-hero__video" autoplay muted loop playsinline preload="auto" aria-label="Aerial drone footage drifting over a forest canopy">
    <source src="/videos/pyronear-hero.mp4" type="video/mp4">
  </video>
  <div class="tool-hero__overlay">
    <h1 class="tool-hero__title">Open, Real-Time Wildfire Detection</h1>
    <p class="tool-hero__tagline">Watching the forest for the first signs of smoke — so fire departments get the alert within minutes.</p>
  </div>
</div>
```

The rest of the page (intro paragraph, demos, carousels, etc.) is unchanged.

### 3. CSS
None. `.tool-hero` and friends are already shared/generic.

## Out of scope
- No changes to the SalmonVision page.
- No changes to the shared `.tool-hero` CSS.
- No new shortcode — the hero is inline HTML, matching SalmonVision.

## Verification
- `hugo` builds with no errors; `static/videos/pyronear-hero.mp4` is emitted to
  `public/videos/`.
- The Pyronear tool page renders the looping video hero with the overlaid title
  and tagline, visually consistent with SalmonVision.
- Hero file size is in the same ballpark as `salmonvision-hero.mp4`.
