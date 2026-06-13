# Pyronear page refresh — layout & copy

**Date:** 2026-06-13
**Branch:** `worktree-pyronear-page-refresh` (off `main`)
**Files touched:** `content/tools/pyronear/index.md` only.

## Goal

Bring the Pyronear tool page in line with the recent Animal reID and Biowatch
refreshes: `.about-cta` cards, a story-led section order, `support__grid` cards
replacing emoji bullet lists, a tabbed HuggingFace-demos block, and emoji removal
from body copy. Single content file plus one front-matter tweak. **No SCSS changes**
— every component used already exists (`.about-cta`, `.support__grid`,
`.support__grid--two`, `.support__card`, `.support__track`).

## Decisions

- **Reuse, don't restyle.** `.about-cta` (in `_about.scss`) and the `support__*`
  card classes (in `_support.scss`) are top-level selectors that already apply
  globally. The Animal reID refresh added the `.support__grid--two` modifier, which
  is present on `main`. Reusing the markup needs zero SCSS edits.
- **Inline raw HTML** for cards/CTAs, matching the existing file style (the page
  already uses raw HTML for its button). No new partial or shortcode (YAGNI).
- **Demos: keep the two videos standalone; tab only the two HF model demos.**
  (User decision.) The Fontainebleau end-to-end video stays as the opener; the
  35 km video stays as a standalone proof block. Only the two HuggingFace model
  demos are grouped into a tabbed block.
- **Closing CTA → pyronear.org (external).** (User decision.) Pyronear is a partner
  project; the closing card drives to the live application, matching the page's
  current primary action — not `/contact`.
- **Emoji removal is scoped to body copy this file controls.** See the caveat in
  "Out of scope" — the shared `layouts/tools/single.html` footer keeps its hardcoded
  emojis (as Biowatch does); the template is not touched.

## Front matter

```yaml
js:
  - /js/biowatch.js
  - /js/tabs.js
```

- Change `js: /js/biowatch.js` (scalar) to the two-item list above.
- `tabs.js` drives the new tabbed demos block.
- `biowatch.js` is kept: besides the (here-unused) OS-detection helper, it calls
  `Lightense(".lightense-enabled", {})` on load — the same image-zoom initializer
  that `animal-reid.js` provides on the Animal reID page. This mirrors Biowatch's own
  front matter exactly. No new `pyronear.js` is created.
- All other front matter is unchanged. `github_repo`, `landing_page_url`, and
  `project` stay — they power the standard auto-generated footer link list rendered
  by `layouts/tools/single.html` (same as Biowatch).

## Section order (story-led)

Final order, mirroring Animal reID's Why → Demos → How It Works → proof → close flow:

1. **H1 hero headline + intro.** The page currently has no content H1 (it opens with
   the button, then the video). Add an H1 headline and 1–2 tightened intro
   paragraphs reworked from the current `## Wildfire Early Real Time Detection System`
   copy. (`show_title: false` + `logo_container: true` are unchanged: the logo image
   remains the tool-info title; the content H1 is the hero headline, exactly as on
   Animal reID which shows both the icon/title and a content H1.)
2. **End-to-end demo video** (Fontainebleau YouTube embed) — kept as a standalone
   block right under the intro, with its existing `<em>` caption.
3. **Image carousel** (`pyronear-gallery`, platform screenshots) — unchanged.
4. **`.about-cta` — top CTA** → jumps to `#demos`. Replaces the current
   `tool-container-button-cta` "Visit Pyronear" button.
5. **`## Why Pyronear`** — replaces `## Key Features`. A `support__grid` of cards
   (no emojis) drawn from the summary's pillars.
6. **`## Interactive Demos {#demos}`** — tabbed block (two tabs).
7. **`## How It Works`** — a `support__grid--two` describing the two-stage pipeline.
8. **`## See Pyronear in Action`** (35 km detection video) — kept standalone as the
   proof block, placed after How It Works.
9. **Auto footer link list** — rendered by the template (project / github /
   landing). Not touched.
10. **`.about-cta` — closing CTA** → `https://pyronear.org/en` (external).

## Changes

### 1. Front matter `js` list

As described above.

### 2. Replace the top button with an `.about-cta` card

**Remove:**

```html
<div class="tool-container-button-cta">
  <a class="link-no-decoration" href="https://pyronear.org/en" target="_blank">
    <button class="button tool-button-cta">
    Visit Pyronear
    </button>
  </a>
</div>
```

**Add** (placed after the intro + video + carousel, as the top CTA):

```html
<div class="about-cta">
  <h3 class="about-cta__title">See the models in action</h3>
  <p class="about-cta__description">Run the Pyronear detector on real camera images and watch the temporal verifier judge live wildfire sequences — right from your browser.</p>
  <a href="#demos" class="link-no-decoration button button--middle">Try the live demos</a>
</div>
```

### 3. H1 hero headline + intro

Add a content H1 and rework the current `## Wildfire Early Real Time Detection System`
paragraph into 1–2 tighter intro paragraphs under it. Proposed:

> # Open, Real-Time Wildfire Detection
>
> Pyronear is a complete, open-source fire-detection system: a computer-vision
> model runs on a low-power microcomputer wired to cameras on high vantage points,
> watching the forest for the first signs of smoke. When it spots a fire, it sends
> an alert to a supervision platform used by fire departments — efficient,
> automatic, energy-efficient, and modular by design.

Exact wording finalized during implementation; keep it tight and emoji-free.

### 4. `## Why Pyronear` — `support__grid` cards

Replace the two emoji bullets (`## Key Features`) with a card grid. Proposed cards
(titles + one-line descriptions, no emojis):

- **Cutting-edge AI detection** — Computer-vision models detect wildfire smoke in
  real time and keep improving as new field data comes in.
- **Web fire-management platform** — An intuitive web app surfaces recent alerts and
  streamlines response for fire departments.
- **Open source and low-tech** — Built in the open on affordable, off-the-shelf
  hardware that communities can deploy and maintain themselves.
- **Energy-efficient and economical** — Runs on low-power microcomputers at the
  edge, keeping running costs and energy use low.
- **Modular by design** — Detection, alerting, and the supervision platform are
  separable pieces you can adapt to local needs.

Final card count/wording finalized during implementation (3–6 cards).

### 5. `## Interactive Demos {#demos}` — tabbed HF demos

A `tabs` shortcode with two tabs, copy reworked emoji-free from the current
"Try the Models in Your Browser" bullets:

```
{{< tabs labels="::Single-frame detection|::Temporal verification" id="pyronear-demos" >}}
{{< tab index="0" >}}
Upload a camera image and watch the detector draw boxes around smoke.
{{< hf_space "earthtoolsmaker-forest-fire-pyronear" >}}
{{< /tab >}}
{{< tab index="1" >}}
The second-stage model watches whole sequences: real wildfires get caught within
minutes while clouds, fog, and haze look-alikes are rejected — the model that cuts
false alarms by 4× in production.
{{< hf_space "achouffe-temporal-smoke-pyronear" "6.18.0" >}}
{{< /tab >}}
{{< /tabs >}}
```

- The single-frame space (`earthtoolsmaker-forest-fire-pyronear`) was previously only
  *linked* (to the internal `/spaces/early_forest_fire_detection` page); it is now
  *embedded* in tab 0.
- The temporal space keeps its required gradio version arg `"6.18.0"`.
- Empty-icon `::Label` form is used (the `tabs` shortcode omits the icon span when
  empty — backward-compatible change already on `main`).

### 6. `## How It Works` — `support__grid--two`

Two tracks describing the two-stage pipeline (parallel to Animal reID's two-track
section). Reuse the `support__card support__track` markup with
`support__track-label`, `support__card-title`, `support__card-description`,
`support__track-proof`, and `support__track-offers`:

- **Track 1 — "Detection" / Single-frame smoke detection:** the CV model proposes
  candidate smoke regions in each camera frame in real time.
- **Track 2 — "Verification" / Temporal smoke verification:** candidates are tracked
  over time and a temporal classifier decides whether they behave like smoke,
  cutting false alarms by 4× in production.

Final copy finalized during implementation, drawn from the existing demo descriptions
and the spaces' summaries.

### 7. `## See Pyronear in Action` — 35 km video

Keep the existing block (heading, intro sentence, YouTube embed, `<em>` caption)
essentially as-is, relocated to sit after How It Works as the proof point. Light copy
touch only.

### 8. Closing `.about-cta`

Append as the page's closer:

```html
<div class="about-cta">
  <h3 class="about-cta__title">Explore the full Pyronear platform</h3>
  <p class="about-cta__description">See live deployments, the fire-management platform, and how to get involved on the Pyronear website.</p>
  <a href="https://pyronear.org/en" class="link-no-decoration button button--middle" target="_blank">Visit Pyronear</a>
</div>
```

## Out of scope

- **No SCSS changes.**
- **No template changes.** `layouts/tools/single.html` hardcodes 🛠️ and 🚀 in the
  auto-generated footer link list (project / github / landing). Biowatch shows the
  same footer. The page therefore is **not** 100% emoji-free like Animal reID (which
  has none of those front-matter fields). Leaving the footer matches Biowatch and
  keeps the change to a single content file — a deliberate choice, not an oversight.
- No changes to the image carousel, the two YouTube embeds (beyond relocation and a
  light caption touch), or the `hf_space` shortcode.
- No changes to the spaces pages (`content/spaces/early_forest_fire_detection.md`,
  `content/spaces/temporal_smoke_verification.md`).

## Verification

- `hugo` builds with no errors.
- Section order matches the list above.
- The demos block renders exactly two tabs (Single-frame detection, Temporal
  verification) and they switch correctly in the built HTML (tab `data-tab` indexes
  align with panel `data-panel`); both Gradio spaces load.
- The top CTA's `Try the live demos` button anchors to `#demos`; the closing CTA's
  `Visit Pyronear` button points to `https://pyronear.org/en`.
- `## Key Features` emoji bullets and the "Try the Models" emoji bullets are gone;
  no emojis remain in body copy this file controls (template footer emojis excepted,
  per Out of scope).
- Image-zoom (Lightense) still initializes (biowatch.js retained).

---

## Addendum (post-implementation): resource footer redesigned

The auto-generated resource footer went through two post-implementation changes at
the maintainer's request, superseding the "No template changes / keep the footer"
decision in the *Out of scope* section above.

1. **First removed** (page-scoped): the `github_repo`/`landing_page_url`/`project`
   keys were deleted so the emoji `<ul>` footer (🛠️ / GitHub / 🚀) stopped rendering.
2. **Then redesigned** (shared template): rather than drop the resource links
   entirely, the footer in `layouts/tools/single.html` was rewritten as a clean,
   emoji-free "Resources" row — centered icon + label text-links (FA icons,
   `var(--text-alt-color)`, `·` separators, a thin `var(--border-color)` top divider),
   guarded by `{{ if $resources }}` so a tool page with none of the fields renders
   nothing (no empty `<ul>`). Styling is inline (theme CSS vars) — **no new SCSS**.

**Scope of the template change.** The footer is shared by all tool pages, so
**Biowatch** and **SalmonVision** also get the cleaner emoji-free footer; **Animal
reID** (no footer fields) renders nothing, as before. This is the one deliberate
departure from the original "single content file, no template changes" scope.

**Pyronear front matter.** `github_repo` and `project` were re-added;
`landing_page_url` was **not** (the closing "Visit Pyronear" CTA already covers
pyronear.org, so a "Live platform" footer link would duplicate it). `github_repo`
points to the Pyronear GitHub org (`https://github.com/pyronear`), not the
`pyronear-mlops` repo. Result: the Pyronear footer shows **Project overview · Source
code**.

**No other consumers:** grep of `layouts/` confirms these params are read only by the
tool footer (the `list.html` `landing_page_url` reference is commented out; the
`github_repo` sidebar widget is for project pages). No backlinks break.
