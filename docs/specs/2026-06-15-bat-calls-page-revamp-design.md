# Tropical Bat Call Detection — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-bat-calls-revamp`). One PR per project page.

## Goal

Bring the bat-call page in line with the other revamped project pages: tightened
non-technical copy, a card grid + interactive threat pills for the bullet/prose
sections, and one animated SVG diagram of the bioacoustics pipeline. The page is
**fundraising** status and has no photo assets beyond the cover, so the diagram
+ cards + pills carry the visuals.

## Front matter

- Add `tagline`: *"Teaching machines to recognise bats by their calls — so citizen scientists across Cambodia can map species no one has counted."*
- Add `stats`: **70+** species recorded · **5** new to science · **Citizen-science** powered.
- Keep `status: fundraising` (status-aware CTA band stays).

## Body structure

1. **Lede** — tighten the "Context" prose into a strong intro (Cambodia's bats, the data gap), keep the "What more is waiting to be found?" quote and the discovery story (30 → 70+ species).
2. **Why bats matter** → 3-card `support__grid`: pest control · seed dispersal · pollination.
3. **Under pressure** → interactive pills (`{{< threats "pressures" >}}`): habitat loss · pesticides · bushmeat & medicine trade · the knowledge gap.
4. **From a call to a species** (Project Scope, non-technical pass; fixes the "visualize and classification" typo) → short intro + the **diagram**; explain the citizen-science recording → spectrogram → classification → open data on iNaturalist flow in prose.
5. Keep the citizen-science framing and the iNaturalist link.

## Diagram (new animated SVG, house teal/coral + night palette)

`pipeline.svg` (804×380, 3 cards) — **Record → Spectrogram → Classify**:
- **Record** — night scene, a bat with expanding ultrasonic sound-waves, a handheld bat detector catching it; "ultrasound" chip.
- **Spectrogram** — a dark spectrogram with FM-sweep chirps and a sweeping playhead; kHz / time axes.
- **Classify** — a results panel of likely species (Myotis 0.94 highlighted · Hipposideros · Rhinolophus — real SE-Asian echolocating genera) with a "top match" chip.

New primitives: flying `bat`, mini `batmini`. Animation classes on inner `<g>`, positioning on outer `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills + `pressures` front matter, `support__grid`.
- No new photos (none exist); keep the cover. No template/shortcode/SCSS changes.

## Verification

- `hugo` builds clean; rendered HTML has the diagram, 3 cards, pills; diagram animates and degrades under reduced motion.
