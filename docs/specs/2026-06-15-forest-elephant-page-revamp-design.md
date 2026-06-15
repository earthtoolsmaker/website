# Forest Elephants Passive Acoustic Monitoring — Page Content Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** `origin/main` (worktree `worktree-forest-elephant-revamp`). One PR per project page.
**Scope:** Body + front matter of `content/projects/elephants_passive_acoustic_monitoring.md`, two new animated SVG diagrams, and reuse of the established `threats` shortcode. Mirrors the revamped fire & salmon project pages.

## Goal

Rewrite the bullet-heavy body into a **hybrid editorial** page matching the fire/salmon pages: lede + blockquote, card grids and interactive chips replacing the long bullet lists, two custom animated SVG diagrams in the site teal/coral system, and the existing spectrogram/prediction imagery used well. The editorial template (hero, facts bar, partner strip, CTA band) is reused untouched.

## Front matter

Add `tagline` + `stats` (none today). Stats (**Mixed**, validated): `60%` lost in a decade · `50` microphones · `24/7` listening. Tagline: *"Finding forest elephants — and poachers — by sound, across Central Africa's rainforest."* Keep `space: /demos/forest_elephant_rumble_detection/` (origin/main renamed spaces→demos).

## Body structure (top → bottom)

1. **Lede** (existing strong opening: 60% lost, 12,000 killed/yr, data gap) + ELP blockquote + **Diagram A** + the `main.jpg` field photo.
2. **Why forest elephants matter** — 6-bullet ecosystem dump → 3-card `support__grid`: *Forest gardeners* (seed dispersal + clearings), *Climate & water engineers* (carbon, water holes), *Biodiversity backbone*.
3. **Under pressure** — interactive **`threats` shortcode** (reused from salmon): Ivory poaching · Bushmeat trade · Resource extraction · Roads & access · Slow reproduction — click reveals detail. Keep the `poaching-trophies.jpg` photo + ELP "60% lost" quote.
4. **What a rumble is** — `rumbles_intro` spectrogram + tightened prose (infrasound < 20 Hz, travels kilometres through dense forest; used for contact, mating, alarm, mother–calf).
5. **Detecting rumbles at scale** — **Diagram B** + the spectrogram→prediction pairs (kept as a 2-col compare) + throughput stats ("months of audio in hours"; 1 TB in ~8.3 h on GPU+CPU); link the open-source GitHub tools + the blog post.
6. Partner strip (auto) + **Conclusion** + `{{< demo_cta >}}`.

## Diagrams (new animated SVG, teal/coral system)

Reuse the card system (212×212 cards, coral arrows, step/title/desc, `prefers-reduced-motion` guard) and the neural-net **Model** card. New primitives: a flat **elephant** silhouette, **sound-wave** arcs, a **spectrogram** tile (grey vertical streaks + red rumble box + "rumble 0.92" pill), and a **mic-grid map** (dots = the 50-mic array; one pinned).

- **Diagram A — `pipeline.svg` "From rumble to alert"** — 4 cards: **Listen** (elephant emitting rumble waves → microphone in the forest) → **Record** (mic-grid map, 24/7 recording) → **Detect** (spectrogram + red rumble box + AI chip) → **Locate** (rumble pinned on the grid map via the array).
- **Diagram B — `detection.svg` "Detecting a rumble"** — 3 cards: Input (spectrogram tile) → reused neural-net **Model** → Output (spectrogram with red box + "rumble 0.92").

Positioning transform on an outer `<g>`, animation class on an inner `<g>` (avoid the SVG transform-attribute override bug). Build **A first → render → adjust → B**.

## Reuse / constraints

- `threats` shortcode + `.threats` CSS (already in `_project-single.scss`); `support__grid`/`support__card`; `.media-caption`; `demo_cta`.
- Embed SVG via markdown image syntax (render hook handles `.svg`).
- One-emoji-or-none headings; don't duplicate the cover in the body.

## Non-goals

- No template/shortcode changes (the `threats` and diagram patterns already exist).
- No changes to other pages.

## Verification

- `hugo` builds clean; screenshot the rendered page (hero+stats, Diagram A, card grids, threats, spectrogram sections, Diagram B); both SVGs render/animate and degrade with reduced motion.
