# SalmonVision tool page polish — design

**Date:** 2026-06-15
**Status:** Approved

## Goal

Bring the SalmonVision tool page in line with the Pyronear tool page treatment
(merged in PR #89): stat band under the hero, interactive pills for the benefits
section, no demos CTA, and the interactive demos folded into the "in action"
section.

## Changes

1. **Stat band below the hero.** Move the existing `about-stats--three
   tools-stats` band (`24/7` automated monitoring · `20` monitoring projects ·
   `1M+` salmon counted) from after the intro paragraphs to directly below the
   hero video, above the intro — matching the Pyronear layout.

2. **"Why SalmonVision" interactive pills.** Replace the four `support__card`
   cards with the interactive `threats` shortcode (already on `main`): a
   `why_salmonvision` front-matter list of `{ name, desc }` rendered via
   `{{< threats "why_salmonvision" >}}`. Clicking a pill reveals its
   description. Added the "— tap each to learn more" hint. No new CSS (the
   `.tool-content .threats` rules landed with PR #89).

3. **Remove the "See the models in action" CTA** (the `about-cta` above "Why
   SalmonVision").

4. **Integrate the interactive demos into "See SalmonVision in Action."** Remove
   the standalone "Interactive Demos" section and fold its two demo tabs
   (underwater camera, sonar smolt) into "See SalmonVision in Action", after the
   field/app videos: watch the system at work, then run the models yourself.
   Drop the now-unreferenced `#demos` anchor.

## Out of scope
- No changes to the hero video, the shared `.tool-hero`/`.threats` CSS, the
  Species/Partners/FAQ sections, or the final CTA.

## Verification
- `hugo` builds clean.
- Built HTML: stat band ordered hero → stats → intro; four `threats__chip`
  pills; no "See the models in action" CTA; both `salmonvision-videos` and
  `salmonvision-demos` tab groups under "See SalmonVision in Action"; no
  Interactive Demos heading and no `#demos` anchor.
- Screenshots confirm the stat band under the hero and the interactive pills.
