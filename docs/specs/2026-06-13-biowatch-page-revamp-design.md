# Biowatch tool page revamp

**Date:** 2026-06-13
**Branch:** `worktree-biowatch-page-revamp` (off `main`)
**Files touched:**
- `content/tools/biowatch/index.md`
- `layouts/tools/single.html` (one guarded block; affects all tool pages but inert unless the flag is set)

## Goal

Apply the visual language used on the refreshed Animal reID page (Support-style
cards, strong CTAs, no emojis), tighten the copy, and improve the section flow. The
page was already emoji-free and well structured, so this is a focused pass — but it
grew over several iterations into a fuller revamp (see Changes).

## Final section order

```
H1 + intro
Image carousel (6 app screenshots, kept as the showcase)
Download buttons (Windows / macOS / Linux — moved here from the top of the page)
"New to Biowatch?" manual CTA card (.about-cta)
## Why Biowatch?      → 3 cards
## Key Features       → 6 cards (3×2)
## About              (moved up, sits with the narrative sections)
## Installation       (OS tabs, each with its own download button)
Closing CTA band (.support__cta-band): Download Biowatch + Support development
```

## Changes

### Content — `content/tools/biowatch/index.md`

1. **Why Biowatch?** → 3 simple `.support__card`s in the base `.support__grid` (one
   row). Intro: "Three things set it apart:".
2. **Key Features** → 6 simple `.support__card`s in the base `.support__grid` (3×2).
   Intro: "Everything from raw captures to published data:". Inline links (Camtrap
   DP, GBIF, LILA) preserved as real `<a>` tags.
3. **Carousel kept** as the screenshot showcase.
4. **Video removed** from the old Documentation section.
5. **Download buttons moved** from above the H1 to just below the carousel. The
   container keeps `id="container-button-download-biowatch"` (the OS-detection
   `<script>` and the closing band's Download button both reference it).
6. **In-tab download buttons:** each Installation tab (Windows/macOS/Linux) now leads
   with its own OS-colored download button; the redundant "download … above" step was
   dropped.
7. **Manual card:** the "Read the Manual" button became a full-width `.about-cta` card
   ("New to Biowatch?", `button--cta`), placed just below the download buttons. The
   `## Documentation` heading was removed (redundant with the card title).
8. **About moved up** to between Key Features and Installation, so the page ends on a
   clean action cluster (Installation → closing CTA).
9. **Closing CTA band:** one `.support__cta-band` (reused from the Support page) with
   **Download Biowatch** (jumps to `#container-button-download-biowatch`) +
   **Support development** (ghost, → `/support/`). Emoji-free (the existing
   `support-cta` partial's 🌍 is NOT reused).
10. **Copy pass:** dropped the intro's duplicated manual sentence; rewrote the About
    paragraphs to be sharper and less redundant ("grew out of a simple conviction…",
    "no cloud, no subscriptions, and no lock-in"); changed the Why intro from "Built
    around three principles:" to "Three things set it apart:".

### Template — `layouts/tools/single.html`

11. **Footer meta-links gated.** The auto-generated `<ul>` of meta links (🛠️ Learn
    more about the project / GitHub / 🚀 All downloads) is now wrapped in
    `{{ if not .Params.hide_meta_links }} … {{ end }}`. `hide_meta_links: true` is set
    in biowatch's front matter only; pyronear/salmonvision (which use the same fields)
    are unaffected.

## Components reused (no SCSS changes)

`.about-cta`, `.support__card`, `.support__grid`, `.support__cta-band` — all top-level
selectors from the merged reID work / Support page. The tool page now depends on
`.support__*` styles from `_support.scss` (intentional cross-file reuse).

## Out of scope

- No SCSS changes.
- No change to the OS-detection `<script>`, the carousel, or the tab shortcode.
- Front-matter unchanged except the new `hide_meta_links: true`.

## Verification

- `hugo` builds with no errors (verified).
- Section order matches the list above (verified in source + rendered HTML).
- Why = 3 cards (one row); Key Features = 6 cards (3×2); both stack to 1 col on mobile.
- Card links (Camtrap DP / GBIF / LILA) resolve; in-tab download buttons render in all
  three tabs.
- Video gone; footer meta-links gone for biowatch; pyronear/salmonvision still show
  theirs.
- Closing band shows both buttons; Download jumps to the relocated download buttons,
  Support → `/support/`.
- Support page itself unaffected by the `.support__grid`/`--two`/band reuse.
