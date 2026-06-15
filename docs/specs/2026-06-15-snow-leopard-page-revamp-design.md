# Snow Leopard Monitoring — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `main` (worktree `worktree-snow-leopard-revamp`). One PR for this page.

## Goal

Bring the Snow Leopard Monitoring page in line with the revamped bear/coral pages:
tagline + stats hero, interactive threat pills, card grids for the concept lists,
tightened non-technical copy (~40% leaner), and consistent media treatment. Keep
the project's **fundraising** framing — except the individual-ID work, which now
exists and should be described in the present tense (Animal reID).

## Front matter

Keep `status: fundraising`, `pinned`, `clients` (OSI Panthera, OSI), `tools`,
existing `cover.png`. Add:

- **tagline:** *"Identifying individual snow leopards in camera-trap photos to track a population almost no one ever sees."*
- **stats (3):**
  - `4,000–7,500` — left in the wild
  - `Individual ID` — from spot patterns
  - `Open-source` — models & tools
- **pressures:** 5 entries (see Under pressure) for the `threats` shortcode.

No `github_repo`/`space` on the page (work is partly planned; the reID tool is
linked inline instead).

## Body structure

1. **Lede** — tighten the Context section to ~2 paragraphs: an elusive, threatened
   high-mountain cat, only 4,000–7,500 left, almost impossible to count by eye.
2. **Why snow leopards matter** — replace the 7-item "Vital Roles" bullet list
   with a `support__grid` of **3 cards**:
   - **Apex predator** — keeps blue sheep, ibex and other ungulates in balance, preventing overgrazing.
   - **Indicator & umbrella species** — their health signals the whole ecosystem's; protecting their vast ranges shelters countless other species.
   - **Cultural keystone** — a charismatic flagship for Central Asian conservation and a creature of deep spiritual significance for the communities who share its range.
   (Consolidates apex/prey-control/nutrient-cycling, indicator/flagship, cultural;
   drops "seed dispersal," dubious for an obligate carnivore.)
3. **Under pressure** — convert the five `###` sections to `{{< threats "pressures" >}}`
   pills, each condensed to 1–2 sentences: **Poaching · Retaliatory killings ·
   Loss of prey · Habitat fragmentation & degradation · Climate change.** Keep the
   **poaching photo** (`poaching_fur.jpg`, with its attribution caption) as a single
   image after the pills. Move the **prey-species carousel** to just below, with a
   one-line lead-in (their prey is itself under pressure).
4. **Monitoring with OSI Panthera** — tighten the partnership prose; keep the
   **snow-leopards carousel**, the **reserve map** (`reserve_map.png`), and the
   **endemic-species carousel**, with consistent captions/alignment.
5. **What we're building** — three subsections, copy trimmed:
   - **Automated species classification** — keep `ml_model_detection.png`; still planned/in-progress wording.
   - **Mapping detections over space and time** — keep the **CocoMap carousel**; still in-progress.
   - **Identifying individuals** — **present tense:** individual ID by spot pattern
     via local feature matching (LightGLUE) works today and is built into
     **[Animal reID](/tools/animal-reid/)** (link the tool page; no live-demo link).
     Show a **2-image carousel** of the real reID screenshots; drop the schematic
     `ml_model_identification.png` from use.
6. **Conclusion** — tighten to a short closing paragraph. The fundraising CTA band
   ("Help fund this project") is auto-rendered by `layouts/projects/single.html`;
   no `demo_cta`.

## Assets

- Copy the two reID screenshots from the Animal reID tool bundle into the project's
  assets so they resolve through the normal image pipeline:
  - `content/tools/animal-reid/images/animal_reid_leopard_1.png` → `assets/images/projects/snow_leopard_monitoring/reid/leopard_1.png`
  - `content/tools/animal-reid/images/animal_reid_leopard_2.png` → `assets/images/projects/snow_leopard_monitoring/reid/leopard_2.png`
  Captions reused from the tool page (local feature matching by spot pattern; LightGLUE keypoint matching across sightings).
- `ml_model_identification.png` becomes unused — leave the file in place (pre-existing
  asset, not removing), noted here.

## Copy / factual notes

- IUCN reclassified the snow leopard from *Endangered* to **Vulnerable** in 2017.
  Decision: avoid any IUCN-status badge/claim; keep informal "threatened/endangered"
  phrasing light in prose. No stat asserts a Red List status.
- All numbers retained from the existing page (4,000–7,500 wild) — no new claims invented.

## Reuse / non-goals

- Reuse existing `threats` pills, `support__grid`, `image_carousel`/`carousel_image`,
  and the fundraising CTA band. **No template or shortcode changes.**
- Inherits the GIF-passthrough + standalone-image centering already shipped in the
  coral PR (not part of this PR's diff).

## Verification

- `hugo` builds clean.
- Screenshot: hero (tagline + stats), the 3-card grid, the threat pills (a panel
  open), the reID carousel, and the Animal reID link present.
- Confirm the two reID images publish and the carousel renders; old gallery/section
  markup gone where replaced.
