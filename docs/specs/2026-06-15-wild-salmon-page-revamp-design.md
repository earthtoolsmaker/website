# Wild Salmon Migration Monitoring — Page Content Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** `origin/main` (worktree `worktree-salmon-revamp`). Mirrors the editorial quality of the already-revamped `early_forest_fire_detection.md`.
**Scope:** Body content of `content/projects/wild_salmon_migration_monitoring.md` + two new animated SVG diagrams. No template, shortcode, or front-matter changes.

## Goal

Rewrite the SalmonVision project page body from three long bullet-list sections + a wide markdown species table into a **hybrid editorial** page matching the revamped fire page: a lede + article spine, card grids replacing bullet dumps, tightened prose, two custom animated SVG diagrams in the site's teal/coral style, and reused photos/videos from the SalmonVision tool & space pages.

The project renders through the editorial single-column template (`layouts/projects/single.html`), which supplies the full-bleed cover hero, kicker, tagline, stats row, facts bar, partner strip, and status-aware CTA band. Front matter already carries `tagline` + `stats` — **unchanged**.

## Key discoveries (drove the approach)

- The fire page now uses **hand-authored animated SVG diagrams** (`overview_system.svg`, `overview_ai_model.svg`, …), referenced with **plain markdown image syntax** `![alt](/images/.../x.svg)`.
- The image render hook (`layouts/_default/_markup/render-image.html`) was updated to **pass `.svg` through directly** (no `.Resize`). So **no new shortcode is needed** — author SVG files and reference them normally.
- The diagram style is a cohesive system to reuse verbatim:
  - 212×212 rounded cards (`fill #fbf6f6`, `stroke #ede0d4`, `cardshadow`), 259px horizontal pitch, coral (`#e29578`) connector arrows with the `#arrow` marker.
  - Below each card: step number (`.step`, coral, letter-spaced), title (`.title`, Newsreader 26px), description (`.desc`, grey 15px).
  - Palette: teal `#006d77`, coral `#e29578`, mints `#83c5be`/`#bfe0d6`/`#cfe9e0`, deep green `#15463f`.
  - Reusable motifs: the **neural-net-on-teal-board "Model" card** (modality-agnostic — reuse as-is) and the **bounding-box + species pill** output.
  - Animation classes (`.wave`, `.ray`, `.water` flow, `.box` pulse, `.node`/`.synapse`) + a `prefers-reduced-motion: reduce` guard. Reuse the same vocabulary (swimming fish, water shimmer, sonar waves).
- The revamped fire page **opens with a lede paragraph (no "Context" heading)**, then blockquote, then the system SVG. Mirror this.

## Section structure (top → bottom of body)

1. **Lede (no heading)** — punchy intro prose (anadromous run, BC ecological/cultural/economic keystone, the PSF/WSC/Lumax/SFU partnership behind SalmonVision). Then the **PSF climate blockquote**. Then **Diagram A** ("From river to count") with an `*italic caption*`. Then the hero video `salmonvision-hero.mp4`.
2. **Why wild salmon matter** — 1 short lead + **3-card `support__grid`**: Nutrient highway · Cultural keystone · Economy & biodiversity. Replaces the 7-bullet dump.
3. **Salmon under pressure** — 1 tight paragraph + **6 threat chips** (Habitat loss · Dams & barriers · Overfishing · Climate change · Pollution · Disease). The old "how monitoring benefits conservation" 7-bullet section collapses into a one-line bridge ("That's why accurate counts matter…").
4. **How SalmonVision counts a run** — the heart:
   - Short prose + **Diagram B** (underwater-camera detection close-up) with caption.
   - **Three ways we count** — Optical / Acoustic / Aerial as a 3-card `support__track` grid (content adapted from the tool page), each followed by its media:
     - Optical — Bear Creek underwater-camera YouTube clip.
     - Acoustic — `haida-sonar.jpg` + sonar YouTube clip; one line linking to the smolt sonar sub-project.
     - Aerial — `drone_imagery.webp`.
   - **In the web app** — `webapp_overview.png` + `review-interface.png` + `salmonvision-tracking.mp4` review clip.
5. **The species we recognize** — replace the markdown table with `{{< salmon_species >}}` + the "also recognizes Bull Trout, Rainbow Trout, …" line.
6. **Built with First Nations** — one short crediting paragraph (full nation-by-nation grid stays on the tool page). Partner logos auto-render from `clients`.
7. **Conclusion** — tightened paragraph + `{{< demo_cta >}}` (kept).

## Diagrams (new assets)

Hand-authored animated SVG under `assets/images/projects/wild_salmon_migration_monitoring/diagrams/`, matching the fire diagram system above. New salmon-specific illustration primitives: a stylized salmon (coral/red body, forked tail, fins), a river/underwater water band (shimmer), an underwater camera on a mount, sonar emitter + wave arcs, a small drone, a count/report board.

- **Diagram A — `pipeline.svg` ("From river to count")** — 4 cards (≈1062×380 viewBox):
  1. **Watch** — river band with an underwater camera + sonar wave arcs + a small drone above (multi-sensor). desc "Sensors track the river".
  2. **Detect** — viewfinder brackets over a swimming salmon + AI chip badge. desc "AI spots each fish".
  3. **Classify** — salmon with a teal species pill "Sockeye 0.94". desc "Identifies the species".
  4. **Count** — a tally/report board with a running count + up-trend. desc "Tallies the run".
- **Diagram B — `detection.svg` (underwater-camera close-up)** — 3 cards (≈804×380), analogous to `overview_ai_model.svg`:
  1. **Input** — an underwater camera frame: salmon in greenish water. desc "An underwater frame".
  2. **Model** — **reuse the neural-net-on-teal-board card verbatim**. desc "Runs the vision model".
  3. **Output** — salmon with red bounding box + pill "Sockeye 0.94". desc "Fish boxed and identified".

Build **A first → render/screenshot → adjust style → then B** and wire up the rest.

## Reuse (no changes to these)

- Shortcodes: `salmon_species`, `demo_cta`; `support__grid`/`support__card`/`support__track` card markup; the `*caption*` convention.
- Media: `salmonvision-hero.mp4`, `salmonvision-tracking.mp4`, `review-interface.png`, `webapp_overview.png`, `haida-sonar.jpg`, `drone_imagery.webp`, the two YouTube clips.
- Template `layouts/projects/single.html`, render-image hook (already handles SVG) — untouched.

## Styling

Threat **chips**: small rounded pills. Reuse existing tool-chip / tag styling if present; otherwise a tiny scoped SCSS addition in the project-single partial. Card grids reuse existing `.support__*` classes — no new card CSS.

## Edge cases / constraints

- SVG embeds via markdown image syntax (render hook handles it) — do NOT pipe SVG through `.Resize`.
- One-emoji-or-none headings per house style (titles are now emoji-free site-wide); match About/Support tone.
- Don't duplicate the cover image in the body (template shows it as the hero).
- `.article__*` blog-card classes are shared — not touched here.

## Non-goals

- No front-matter changes (tagline/stats already present).
- No template / shortcode / render-hook changes.
- No changes to the tool page, space page, or the smolt sibling project.
- No new photography; the two diagrams are the only new visual assets.

## Verification

- `hugo` builds clean (static build is ground truth; `hugo server` can serve stale).
- Screenshot-check the rendered project page: cover hero, lede + Diagram A, card grids, Three-ways-we-count media, Diagram B, species grid, CTA band; both SVGs render crisp/animated and degrade with reduced-motion.
- Chromium screenshots use `$HOME` paths + a virtual-time-budget.
