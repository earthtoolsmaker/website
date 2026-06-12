# Support Page — Design

**Date:** 2026-06-12
**Status:** Approved direction, pending implementation plan

## Goal

Replace the thin `/sponsor/` page (one paragraph + contact form) with a full "Support our work" page at `/support/`. Inspiration: [hack-the-planet.io/donate](https://www.hack-the-planet.io/donate/) — adapted to our reality: no payment processor, so the page routes visitors to concrete actions instead of a donation widget.

This page is the landing target for the about-page revamp's "Support our work" CTA and the `donate_sponsor_cta` shortcode on project pages.

## Decisions made

- **Channels:** fund a specific project, partner/hire us, non-monetary support. **No direct donations** — no Stripe/GitHub Sponsors/Open Collective widget.
- **URL:** `/support/`, with a Hugo alias from `/sponsor/` so existing links redirect.
- **Navigation:** top-level "Support" main-menu item between About and Contact; footer entry too.
- **CTA mechanism:** one embedded Formspree contact form at the bottom of the page; section CTAs scroll to it. GitHub and social cards link out directly.
- **Structure:** action-led (organized by what the visitor can do), not audience tracks.

## Audience and voice

- Visitors arriving from project pages or the about page who want to help — individuals, companies, foundations, NGOs, researchers.
- Voice matches the about revamp: warm, honest, specific. Small team, open source, partnerships are what turn project ideas into deployed tools.

## Page structure (top to bottom)

### 1. Hero

Full-bleed photo with text overlaid on a bottom gradient — same overlay style as the about revamp hero. Image: the snow leopard cover (`/images/projects/snow_leopard_monitoring/cover.png`), one of the projects waiting on funding.

> **Help us build the next tool**
> Every tool we ship is free and open source for the people protecting wild places. None of them get built without support.

### 2. Intro paragraph

Two or three sentences: we're a small team of engineers and ecologists; sponsorships and partnerships are what turn scoped project ideas into deployed tools; here's how to be part of that.

### 3. Fund a project (centerpiece)

A curated list of fundraising projects rendered as photo cards, listed by page path in `data/support.yaml` (currently Snow Leopard Monitoring and Bird Flu Monitoring), reusing the homepage fundraising-card markup from `section-projects.html`. Each card links to its project page. Section intro:

> These projects are designed, scoped, and waiting on funding.

(Curated rather than a dynamic `status: fundraising` query — the user wants editorial control over which fundraising projects the page features; the intro copy carries no hardcoded count.)

Section CTA: **Sponsor this project** → scrolls to `#get-in-touch`.

### 3b. Proven in the field

Proof that funded projects keep running: ongoing high-impact projects rendered as the same photo cards, listed by page path in `data/support.yaml` (currently Early Forest Fire Detection and Wild Salmon Migration Monitoring). Intro:

> Support doesn't stop at launch. These systems run in the field every day — spotting wildfire smoke minutes after ignition and counting wild salmon as they migrate upriver.

### 4. Partner with us

A band for organizations — three compact tracks, each a bold title + one-liner:

- **Companies** — Sponsor engineering time on a project and align your CSR with shipped conservation tools.
- **Foundations & philanthropy** — Multi-year support that lets us start the projects no single client funds.
- **NGOs & researchers** — Bring us your field problem and co-develop a tool you'll own and run.

Named real partners as proof points (drawn from existing client/partner logos), like the about page does. CTA scrolls to the form.

### 5. More ways to help

Compact 4-card grid:

- **Contribute code** → direct link to https://github.com/earthtoolsmaker
- **Spread the word** — share projects, follow on social, introduce us to conservation orgs that need tools.
- **Volunteer your expertise** — ML engineers, designers, ecologists → form
- **Share data or hardware** — labeled datasets, camera-trap archives, field equipment → form

### 6. Get in touch

Existing Formspree contact form, anchored `id="get-in-touch"`, headed: *Tell us how you'd like to help.*

## Implementation shape

- **Content & URL:** `content/sponsor.md` → `content/support.md` with `aliases: ["/sponsor/"]`. Front matter stays thin (title, hero image + overlay text, layout). Partner tracks and ways-to-help cards live in a small `data/support.yaml`, following the about revamp's data-file pattern.
- **Layout:** new `layouts/page/support.html`, following the `layouts/page/about.html` pattern: hero with text-overlay variant, then sections. Built self-contained — the about revamp branch specs the same hero overlay variant, but neither branch depends on the other; whichever lands second reconciles the shared partial.
- **Fundraising cards:** reuse the card markup from `section-projects.html`; extract a small card partial if it doesn't reuse cleanly, so homepage and support page render from one source.
- **Form:** reuse the `contact_form` shortcode/partial with the `#get-in-touch` anchor.
- **Navigation:** `config.toml` — add main-menu "Support" at weight 5, bump Contact to 6; add footer entry.
- **Shortcode:** `donate_sponsor_cta.html` button → `/support/`, reworded to "Support our work 🌍".
- **Styling:** additions to existing SASS under `assets/`, matching current section patterns (`section__info`, dividers, `animate` classes); lean on existing card/grid styles for the tracks band and ways-to-help grid.

## To verify at implementation

- Fundraising card list in `data/support.yaml` stays in sync with which projects actually seek funding (it is curated, not queried).
- Snow leopard cover resolution is sufficient for a full-bleed hero.
- All inbound links to `/sponsor/` (shortcode, about spec CTA, any content links) resolve after the rename.

## Out of scope

- Payment processing of any kind.
- Newsletter.
- Changes to the homepage or the about page (the about revamp is its own branch).
