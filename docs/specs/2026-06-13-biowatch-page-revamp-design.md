# Biowatch tool page revamp

**Date:** 2026-06-13
**Branch:** `worktree-biowatch-page-revamp` (off `main`)
**File touched:** `content/tools/biowatch/index.md` (only — reuses existing components, no SCSS/template changes)

## Goal

Apply the same visual language used on the refreshed Animal reID page: turn the
bullet sections into Support-style cards, add a strong closing CTA, and drop the
video. The page is already emoji-free and well structured, so this is a focused pass.

## Decisions

- **Why Biowatch?** → 3 simple `.support__card`s in the base `.support__grid` (fills
  one 3-col row).
- **Key Features** → 6 simple `.support__card`s in the base `.support__grid` (3×2).
  Inline links (Camtrap DP, GBIF, LILA) preserved as real `<a>` tags inside the card
  descriptions.
- **Carousel kept** as the screenshot showcase (no image cards, no new styling).
- **Remove the YouTube video** block from Documentation (keep the manual link +
  "Read the Manual" button).
- **Closing CTA:** one teal `.support__cta-band` (reused from the Support page) with
  two buttons — **Download Biowatch** (primary, jumps to the OS-aware download
  buttons at `#container-button-download-biowatch`) + **Support development** (ghost,
  → `/support/`). Placed at the very end, after About.
- **Light consistency:** a one-line intro above each card section.
- **Emoji:** none (the existing `support-cta` partial's 🌍 is NOT reused; the band is
  written fresh, emoji-free).

## Changes (all in `content/tools/biowatch/index.md`)

### 1. Why Biowatch? → cards

Intro: "Built around three principles:" then a `.support__grid` of 3 `.support__card`:

- **100% offline & private** — Your research data stays on your machine — no cloud
  uploads, no accounts, no tracking. Built for the sensitive location data of
  endangered species.
- **Open source** — Inspect the code, contribute improvements, or adapt it to your
  needs — built transparently by the conservation community, for the conservation
  community.
- **On-device AI** — Run powerful species-identification models directly on your
  computer, with no internet required after setup.

### 2. Key Features → cards

Intro: "Everything from raw captures to published data:" then a `.support__grid` of 6
`.support__card`. Titles / descriptions kept close to the current bullets:

1. **Import from anywhere** — own image folders, a Camtrap DP package, or curated
   public datasets from GBIF and LILA — or the one-click demo dataset. (links kept)
2. **On-device species ID** — local AI models (SpeciesNet, MegaDetector, DeepFaune,
   Manas), with a coverage map to pick the best fit for your region.
3. **Interactive maps** — camera locations as species pie-charts, abundance markers,
   or density heatmaps, filtered to an area you draw.
4. **Activity & trends** — daily-activity clocks, seasonal timelines, and
   per-deployment activity charts.
5. **Media management** — browse, filter, and search thousands of images and videos,
   review AI detections, and correct bounding boxes.
6. **Standards-based export** — publish to GBIF as a Camtrap DP package, or export
   media organized into one folder per species.

### 3. Documentation — remove the video

Delete the `<iframe>` YouTube embed, its `<em>` caption, and the surrounding `<br>`.
Keep the manual paragraph + "Read the Manual" button.

### 4. Closing CTA band

After the About section:

```html
<div class="support__cta-band">
  <div class="support__cta-band-text">
    <h3 class="support__cta-band-title">Ready to try it?</h3>
    <p class="support__cta-band-description">Biowatch is free and open source — and built in the open. Download it for Windows, macOS, or Linux, or help us keep developing it.</p>
  </div>
  <div class="support__cta-band-buttons">
    <a class="link-no-decoration" href="#container-button-download-biowatch"><button class="button">Download Biowatch</button></a>
    <a class="link-no-decoration" href="/support/"><button class="button button--ghost">Support development</button></a>
  </div>
</div>
```

## Out of scope

- No SCSS or template changes (reuses `.support__card`, `.support__grid`,
  `.support__cta-band`, all top-level selectors from the merged reID work / Support
  page).
- No change to the top download buttons, the OS-detection `<script>`, the carousel,
  Installation tabs, or front matter.

## Verification

- `hugo` builds with no errors.
- Why = 3 cards (one row); Key Features = 6 cards (3×2); both stack to 1 col on mobile.
- Card links (Camtrap DP / GBIF / LILA) resolve.
- Video iframe gone; manual button remains.
- Closing band shows both buttons; Download jumps to the top download buttons, Support
  → `/support/`.
- Support page itself unaffected.
