# About Page Revamp — Design

**Date:** 2026-06-12
**Status:** Approved direction, pending implementation plan

## Goal

Replace the current About page (terse intro + services + case studies + heavy team bios) with a mission-driven, field-proven narrative page. Inspiration: [hack-the-planet.io/about](https://www.hack-the-planet.io/about/) — mission language grounded in concrete proof (numbers, named projects, real photos).

## Audience and voice

- **Primary:** potential clients/partners (NGOs, research labs with a conservation challenge) → goal: start a project.
- **Secondary:** funders/donors evaluating credibility → goal: support the work.
- **Voice:** warm mission narrative up top, specifics everywhere — real numbers, named partners, outcome-first case-study titles. No agency-speak.

## Page structure (top to bottom)

### 1. Hero
Full-bleed sockeye salmon photo (the SalmonVision cover — underwater split-level shot) with text overlaid on a bottom gradient:

> **Technology for the people protecting wild places**
> We build open-source AI for conservation — listening for elephants in rainforest audio, counting salmon as they swim upriver, spotting wildfire smoke from 35 km away.

Replaces the current stock illustration hero (`/images/pages/about/hero.jpg`), which clashes with the field-proven story.

### 2. Mission paragraph

> Conservation teams collect more data than they can ever look at: years of audio, millions of camera-trap photos, endless hours of underwater video. The bottleneck isn't passion or knowledge — it's tooling. We're a small team of engineers and ecologists who close that gap, building machine learning tools side by side with the researchers and rangers who use them.
>
> Free to use. Free to modify. Open source, end to end.

### 3. Numbers strip
Compact 4-stat band: **14** projects shipped · **19** partner organizations · **9+** species monitored · **100%** open source.
Counts must be verified against `content/projects/` and `assets/images/clients/` at implementation time and are expected to drift — keep them easy to edit (data file).

### 4. What we do (services, tightened)
Intro: "From raw field data to running systems — we cover the full lifecycle." Then a compact grid, bold title + one-liner:

- **Custom ML models** — Species ID, behavior detection, environmental monitoring — trained on your data.
- **Data pipelines** — Terabytes of audio, video, and sensor data turned into usable signals.
- **Deployment & integration** — From edge devices in the field to cloud platforms — production-ready, maintained.
- **Open source by default** — Transparent, reproducible, and yours to keep — no vendor lock-in.

Replaces the current longer services descriptions in `data/services.yaml`.

### 5. Work in the field (case studies)
Keep the existing 4 case studies (elephants, salmon, fire, bears), photo-led, with rewritten outcome-first titles and one-sentence copy naming the partner:

- **Hearing elephants through the noise** — Years of Congo-basin rainforest audio, scanned automatically for elephant rumbles — and gunshots. With Cornell's Elephant Listening Project.
- **Counting every salmon, every river** — SalmonVision counts and classifies migrating salmon in real time from underwater cameras and sonar. With the Pacific Salmon Foundation.
- **Seeing smoke 35 km away** — Early wildfire detection from tower-mounted cameras across European forests. With Pyronear.
- **Knowing one bear from another** — Facial recognition for grizzlies — population monitoring without tags or tranquilizers. With the BearID Project.

Footer link: "All 14 projects on the projects page" (count kept in sync with the numbers strip).
Partner logos stay on each case study as today.

### 6. CTA — Start a project

> **Have a conservation challenge?**
> Tell us about your data and your field problem — we'll tell you honestly what AI can and can't do for it.
> [Start a project] → /contact/

### 7. The journey (timeline)
Chronological, oldest first (narrative momentum; ends on 2026 right before the support CTA). Left-border timeline style:

- **2024 — First field deployments.** EarthToolsMaker starts shipping: coral reef health monitoring, forest elephant acoustics with Cornell, bear identification, and SalmonVision counting fish on British Columbia rivers.
- **2025 — Tools others can run.** BioWatch turns camera-trap archives into maps and insights. Seal surveys take off over the Wadden Sea. Snow leopard monitoring begins in the mountains of Central Asia.
- **2026 — Earlier, faster, further.** Sonar counts smolt runs no camera could see. Fire detection spots smoke at 35 km, minutes after ignition.

Milestone facts to be sanity-checked against project front matter dates at implementation.

### 8. CTA — Support our work

> **Help us build the next tool**
> Three projects are waiting on funding — bat call classification, bird flu monitoring, snow leopard tracking.
> [Support our work] → `/sponsor/` (same destination as the existing `donate_sponsor_cta` shortcode)

Fundraising project names pulled from `status: fundraising` projects; keep editable.

### 9. The team
Compact grid (photo, name, role, social icons) replacing the current alternating full-width bio rows. Bios dropped from the page; `data/team.yaml` keeps them for possible reuse.

**Explicitly excluded:** newsletter CTA (user decision).

## Implementation shape

- `content/about.md` stays thin: front matter + shortcode calls. Hero image param points at the salmon photo.
- `layouts/page/about.html`: hero gains a text-overlay variant (gradient + headline/sub params).
- Partials:
  - new `section-about-stats.html` (numbers strip)
  - new `section-about-timeline.html` (journey)
  - `section-services.html` tightened to the compact grid + new intro line
  - `section-team.html` regridded to compact cards (keep social links)
  - case-study markup largely reused; titles/copy change in data
- Data: new `data/about.yaml` for stats + timeline; `data/services.yaml` copy rewritten; `data/team.yaml` unchanged (bios simply not rendered).
- CTAs: two contextual bands; reuse existing button styles and `donate_sponsor_cta` destination for the support CTA.
- Styling: additions to existing SASS under `assets/`, matching current section patterns (`section__info`, zigzag SVG divider, `animate` classes).
- Hero image asset: reuse the SalmonVision cover (`assets/images/projects/wild_salmon_migration_monitoring/cover.png`), processed via the existing `responsive-image.html` partial.

## To verify at implementation

- Exact counts: completed + fundraising projects (currently 14 total), partner orgs (currently 19 logo dirs), species count.
- Timeline milestone dates against `content/projects/*.md` front matter (e.g. trout identification is 2024-12, listed under 2024).
- "35 km" fire detection claim matches current project copy.
- Salmon cover resolution is sufficient for a full-bleed hero at 1600px.

## Out of scope

- Homepage, projects page, or any other page.
- Newsletter infrastructure.
- New photography or team bio rewrites beyond what's specified.
