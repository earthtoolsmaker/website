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

5. **FAQ cards → pills.** Convert the six FAQ `support__card` cards to the
   interactive `threats` pills via a `faq` front-matter list (`{ name: question,
   desc: answer }`) and `{{< threats "faq" >}}`, with a "Tap a question to see
   the answer" hint. This is a **second** `.threats` instance on the same page
   (alongside "Why SalmonVision"), which required the multi-instance refactor
   below.

6. **Multi-instance `threats` component refactor (shared).** The component
   previously hardcoded a single radio group (`threat-group`) and global IDs
   (`threat-0`…), so two instances on one page collided. Reworked to be
   instance-safe:
   - Shortcode: each chip wraps its own radio; the radio group name is
     namespaced per key (`threats-<key>`); no global IDs.
   - CSS (both `.tool-content` in `_tools.scss` and `.post__content` in
     `_project-single.scss`): state now uses `:has()` — active/focused chip via
     `.threats__chip:has(.threats__toggle:checked)`, and panel reveal via
     positional `nth-child` pairing scoped to each `.threats`. Works for any
     number of instances per page.
   - Affects all five consumers: salmonvision (Why + FAQ), pyronear (Why), and
     three project pages (early_forest_fire_detection, wild_salmon_*,
     elephants_*) — all re-verified.

7. **Move "Our Partners" to the very end** of the page (after the closing CTA).

## Out of scope
- No changes to the hero video or the `.tool-hero` CSS.

## Verification
- `hugo` builds clean.
- Built HTML: stat band ordered hero → stats → intro; Why + FAQ render as
  `.threats` pills with **separate** radio groups (`threats-why_salmonvision`,
  `threats-faq`); no "See the models in action" CTA; demos folded into "See
  SalmonVision in Action"; no `#demos` anchor; "Our Partners" is the last
  section. All five `threats` consumers render with namespaced groups and no
  leftover `id="threat-"`.
- Screenshots confirm the stat band under the hero and the interactive pills
  (active chip + reveal panel) under the refactored `:has()` CSS.
