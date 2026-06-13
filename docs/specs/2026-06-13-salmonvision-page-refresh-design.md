# SalmonVision page refresh — layout & copy

**Date:** 2026-06-13
**Branch:** `worktree-salmonvision-page-refresh` (off `main`)
**Files touched:** `content/tools/salmonvision/index.md` only.

## Goal

Bring the thin SalmonVision tool page (currently ~1.8k: a button, an emoji bullet
list, one video) in line with the recent Pyronear / Biowatch / Animal reID
refreshes: `.about-cta` cards (top + closing), a story-led section order,
`support__grid` cards replacing emoji bullets, a three-modality "How It Works"
grid, a tabbed HuggingFace-demos block, and emoji removal from body copy. Single
content file plus front-matter tweaks. **No SCSS changes, no template changes** —
every component already exists on `main` (`.about-cta`, `support__grid`,
`support__card`, `support__track`, the `tabs` shortcode, the `image_carousel`
shortcode).

SalmonVision is the closest analog to Pyronear — an external partner tool with a
landing page and HuggingFace demos — so the section order mirrors Pyronear's
Why → How It Works → Demos → proof → close flow.

## Decisions

- **Reuse, don't restyle.** `.about-cta` and the `support__*` card classes are
  top-level selectors that already apply globally. Reusing the markup needs zero
  SCSS edits.
- **Inline raw HTML** for cards/CTAs, matching the existing file style (and
  Pyronear/Biowatch). No new partial or shortcode (YAGNI).
- **Both HF demos in a tabbed block.** (User decision.) Two tabs: the
  underwater-camera salmon counter (`earthtoolsmaker-salmon-vision`) and the sonar
  smolt detector (`Lumax-eco-sonar-smolt`). Both spaces are embedded directly via
  `hf_space`, mirroring Pyronear's two-tab demos section. The camera space was
  previously only linked (from the project page); the sonar space gets its first
  embed on a tool page.
- **Carousel reuses existing project screenshots in place.** (User decision.) The
  tool's `images/` bundle is empty; the `carousel_image` shortcode resolves
  `src` paths beginning with `/images/` from `assets/` via `resources.Get`, so the
  existing `assets/images/projects/wild_salmon_migration_monitoring/*` images are
  referenced directly — no copying, no new assets.
- **Three-modality "How It Works".** (User decision.) One `support__card
  support__track` per sensing modality: underwater cameras, sonar, drones —
  faithful to the actual multi-sensor system.
- **Closing CTA → salmonvision.org (external).** SalmonVision has its own landing
  page; the closing card drives to it, matching the page's current primary action
  — not `/contact`. Same call Pyronear made.
- **Footer: drop `landing_page_url`, add `github_repo`.** Because the closing CTA
  already covers salmonvision.org, keeping `landing_page_url` would duplicate it as
  a "Live platform" footer link (the exact reasoning from the Pyronear addendum).
  Adding `github_repo` (the Salmon-Computer-Vision repo) yields a clean
  **Project overview · Source code** resource footer, parallel to Pyronear's.

## Front matter

Current:

```yaml
title: SalmonVision
weight: 20
show_title: false
button_cta: Visit SalmonVision
icon: /images/logos/salmon-vision-logo.svg
logo_container: true
card_tint: "#dceef1"
summary: Underwater cameras, sonar and drones combined with innovative AI technology to enable precise and automated salmon counting in rivers.
landing_page_url: https://salmonvision.org
project: /projects/wild_salmon_migration_monitoring
date: 2024-10-01
```

Changes:

- **Add** a two-item `js` list:
  ```yaml
  js:
    - /js/biowatch.js
    - /js/tabs.js
  ```
  `tabs.js` drives the new tabbed demos block. `biowatch.js` matches Pyronear's
  setup: besides the (here-unused) OS-detection helper it calls `Lightense(...)`
  for image-zoom on load. Carousel JS (tiny-slider) is already loaded globally
  (Pyronear renders a carousel with exactly this `js` list).
- **Remove** `landing_page_url` (closing CTA covers salmonvision.org).
- **Add** `github_repo: https://github.com/Salmon-Computer-Vision/salmon-computer-vision`.
- Everything else unchanged. `show_title: false` + `logo_container: true` stay: the
  logo image remains the tool-info title; the content H1 is the hero headline
  (same arrangement as Pyronear / Animal reID).

The tool footer (`layouts/tools/single.html`) reads `project`, `github_repo`,
`landing_page_url`, `all_downloads_url`. Result after the change:
**Project overview · Source code**.

## Section order (story-led)

1. **H1 hero headline + intro.** Keep a content H1 reworked from the current
   `# Automate Salmon Monitoring`, with 1–2 tightened, emoji-free intro
   paragraphs reworked from the current intro copy.
2. **Image carousel** — reuses existing project screenshots:
   - `/images/projects/wild_salmon_migration_monitoring/system_overview.png`
   - `/images/projects/wild_salmon_migration_monitoring/webapp_overview.png`
   - `/images/projects/wild_salmon_migration_monitoring/sonar/haida-sonar.jpg`
   - `/images/projects/wild_salmon_migration_monitoring/drone/drone_imagery.webp`

   Captions reworked from the project page's existing captions. (Final image
   selection/order finalized during implementation; 3–4 images.)
3. **`.about-cta` — top CTA** → `#demos` ("Try the live demos"). Replaces the
   current `tool-container-button-cta` "Visit SalmonVision" button.
4. **`## Why SalmonVision`** — replaces `## Key Features`. A `support__grid` of
   cards (no emojis) drawn from the summary's pillars. Proposed (3–4 cards, final
   wording during implementation):
   - **Automated counting** — Computer-vision models count and classify fish
     migrating upstream, replacing manual tallies.
   - **Multi-sensor coverage** — Underwater cameras, sonar, and drones work in
     unison to track populations across diverse river conditions.
   - **Species classification** — Models recognize the main Pacific salmon
     species (and other fish) on the fly.
   - **Exportable reports** — Daily count reports are generated and exported for
     management and regulatory decisions.
5. **`## How It Works`** — a three-card `support__grid` of `support__card
   support__track`, one per modality, each with a `support__track-label`, title,
   and description reworked from the project page:
   - **Underwater cameras** — motion-triggered cameras feed the CV system that
     counts and classifies fish.
   - **Sonar** — ARIS-style sonar counts fish in low-visibility water, including
     juvenile smolt migrating downstream.
   - **Drones** — aerial photogrammetry surveys stream reaches to estimate fish
     populations and movement.
6. **`## Interactive Demos {#demos}`** — a `tabs` block with two tabs:
   ```
   {{< tabs labels="::Underwater camera|::Sonar smolt" id="salmonvision-demos" >}}
   {{< tab index="0" >}}
   Upload a clip from an underwater camera and watch the model count and classify salmon.
   {{< hf_space "earthtoolsmaker-salmon-vision" >}}
   {{< /tab >}}
   {{< tab index="1" >}}
   Run the sonar pipeline on ARIS footage to detect, track, and count migrating smolt.
   {{< hf_space "Lumax-eco-sonar-smolt" >}}
   {{< /tab >}}
   {{< /tabs >}}
   ```
   Empty-icon `::Label` form (the `tabs` shortcode omits the icon span when empty).
   Gradio version arg: start with the shortcode default (5.4.0); if either embed
   fails to load, pass the space's required version as the second arg (as Pyronear
   does with `"6.18.0"`). **Verify both embeds render in a browser.**
7. **`## See SalmonVision in Action`** — keep the existing Bear Creek
   underwater-camera YouTube embed (`V-rZSeM5YtY`) with its `<em>` caption as the
   standalone proof block, placed after the demos. Light copy touch only.
8. **Auto resource footer** — rendered by the template from front matter
   (Project overview · Source code). Not touched.
9. **`.about-cta` — closing CTA** → `https://salmonvision.org` (external,
   `target="_blank"`), "Visit SalmonVision".

## Out of scope

- **No SCSS changes.**
- **No template changes.** The `layouts/tools/single.html` resource footer is
  already the clean, emoji-free row (redesigned during the Pyronear work). Nothing
  to touch.
- **No new image assets.** The carousel reuses images already in `assets/`.
- No changes to the project pages (`wild_salmon_migration_monitoring.md`,
  `monitoring_smolt_salmon_migration_with_sonar.md`) or the spaces pages.
- The current page's second sonar video is not added (the project page covers it);
  keep a single proof video to match the established "light proof block" pattern.

## Verification

- `hugo` builds with no errors.
- Section order matches the list above.
- The demos block renders exactly two tabs (Underwater camera, Sonar smolt) and
  they switch correctly in the built HTML (tab `data-tab` indexes align with panel
  `data-panel`); **both Gradio spaces load in a browser**.
- The top CTA's "Try the live demos" button anchors to `#demos`; the closing CTA's
  "Visit SalmonVision" button points to `https://salmonvision.org`.
- The `🎥/🧠/📊` Key Features emoji bullets are gone; no emojis remain in body copy.
- The resource footer shows **Project overview · Source code** (no "Live platform"
  duplicate).
- The carousel renders the reused project images (resolved from `assets/`).
- Image-zoom (Lightense) still initializes (biowatch.js retained).

---

## Addendum (post-approval): hero video, stats band, FAQ

Three additions requested by the maintainer after the initial refresh shipped.
These extend the original "single content file, no SCSS" scope — deliberately.

### 1. Hero video banner

The looping background video from the official SalmonVision site
(`https://salmonvision.org/images/hero-banner.mp4`, 1280×720, ~6 s, 6.1 MB) is
**hosted locally** at `static/videos/salmonvision-hero.mp4` (not hotlinked — avoids
a runtime dependency on their server). It is presented as a full-width, rounded,
autoplay/muted/loop hero banner at the top of the content, with the page title and
a tagline ("Empowering wild salmon conservation through collaborative, AI-powered
monitoring.") overlaid on a bottom dark-gradient scrim for legibility. The plain
`# Automate Salmon Monitoring` markdown H1 is replaced by the hero's
`h1.tool-hero__title`. New `.tool-hero*` styles live in `assets/sass/3-modules/_tools.scss`.

### 2. Stats band

A three-stat band reusing the `.about-stats` component (as the projects/spaces
pages do), placed right after the intro: **24/7 automated monitoring · 20
monitoring projects · 1M+ salmon counted** (values supplied by the maintainer).
Because the shared `.about-stats__grid` is hardcoded to four columns — and the
tools *list* page already uses `.tools-stats` with four items — a new
`.about-stats--three` modifier was added to `assets/sass/4-layouts/_about.scss`
(placed after the base `.about-stats` rule so it wins the cascade; 3 columns
desktop, 1 column mobile). The band reuses `.tools-stats` only for its margin.

### 3. FAQ section

A `## Frequently Asked Questions` section (six `support__card`s in a
`support__grid`) was added before the closing CTA, with copy adapted from the
official FAQ at `https://salmonvision.org/contact/`: accuracy (>95% detection,
90–95% species), supported footage, species coverage, open-source licensing
(MIT models / CC BY-NC-SA datasets), cost (free for education/research; subsidized
for conservation groups and Indigenous communities), and custom-model development.

### SCSS touched (departure from original "no SCSS" scope)

- `assets/sass/4-layouts/_about.scss` — `.about-stats--three` modifier.
- `assets/sass/3-modules/_tools.scss` — `.tool-hero*` hero-video styles.

### New asset

- `static/videos/salmonvision-hero.mp4` (6.1 MB) — copied from salmonvision.org.

### 4. Gradio runtime collision fix (mirrors the Pyronear fix on main)

The two demo embeds required different gradio runtimes (salmon-vision 5.5.0 served
by the default 5.4.0 loader; sonar 5.49.1). The `<gradio-app>` custom element
registers once per document, so two loaders collide and the **salmon RGB counter
fails to mount** — the same bug fixed for Pyronear in `0704cfd`. Fix: keep the
primary salmon-vision space as `{{< hf_space "earthtoolsmaker-salmon-vision" >}}`
(default 5.4.0 runtime, as it mounts on the spaces page) and embed the sonar space
via an isolated `<iframe src="https://lumax-eco-sonar-smolt.hf.space" ...>`. Only
one gradio runtime remains on the page, so the salmon counter mounts correctly.

### 5. Manual footage + "User guide" footer link

Footage pulled from the official user guide (`https://salmonvision.org/user-guide/`):

- **Tracking video** (`SV tracking vid.mp4` from the *Incorrect detection* page) hosted
  locally at `static/videos/salmonvision-tracking.mp4` (1.1 MB) and featured in
  *See SalmonVision in Action* as a looping review-session clip.
- **Review-interface screenshot** — a frame extracted from that video showing a
  bounding-boxed fish, species labels (Pink, Sockeye…), and the counting timeline —
  saved to `assets/images/tools/salmonvision/review-interface.png` and added as the
  lead carousel slide (optimized to webp by the carousel shortcode).

A **"User guide" link** was added to the shared resource footer: a new
`manual_url` param + a `fa-solid fa-book` "User guide" entry in
`layouts/tools/single.html` (guarded with `with`, so other tool pages are
unaffected). SalmonVision sets `manual_url: https://salmonvision.org/user-guide/`,
giving a footer of **Project overview · Source code · User guide**.
