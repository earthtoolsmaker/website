---
title: Temporal Smoke Verification
card_image: /images/pages/spaces/temporal_smoke_verification/card.svg
summary: Watching camera sequences over time to tell genuine wildfire smoke from look-alikes.
github_repo: https://github.com/pyronear/temporal-model
date: 2026-06-12
project: /projects/early_forest_fire_detection/
hf_space: achouffe-temporal-smoke-pyronear
hf_space_code: https://huggingface.co/spaces/achouffe/temporal-smoke-pyronear/tree/main
gradio_js_version: 6.18.0
manual_steps:
  - step_name: Pick a sequence
    description: Choose one of the real camera sequences — two early wildfires and two false-positive look-alikes (clouds, haze).
  - step_name: Watch it play
    description: The sequence loops automatically. Each box is a tracked candidate ("tube"), colored by the verdict — orange means judged smoke, gray means rejected.
  - step_name: See what the classifier sees
    description: Below the animation, each tube's stabilized crops are laid out over time — the background holds still, so the only thing moving is the candidate.
  - step_name: Run the model live (optional)
    description: Re-run the full pipeline from scratch on the Space's hardware to verify the precomputed results.
---

## Overview

Temporal Smoke Verification tackles the hardest part of automated wildfire detection: telling real smoke from things that merely look like it. A single frame of drifting cloud, morning haze, or fog can fool a detector. This model watches a candidate over a sequence of frames instead — because genuine wildfire smoke *behaves* in ways a cloud doesn't.

Built on Pyronear's [temporal model](https://github.com/pyronear/temporal-model), it complements early detection by adding a second, time-aware opinion that filters out false alarms before they reach a responder.

## How It Works

From a flagged candidate to a verdict you can see:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Tracked candidates</h3>
    <p class="support__card-description">Each potential smoke is tracked across the sequence as a "tube" — a candidate followed frame by frame rather than judged in isolation.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Verdict over time</h3>
    <p class="support__card-description">The classifier weighs how the candidate evolves and labels each tube — orange for judged smoke, gray for rejected look-alikes.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">See what it sees</h3>
    <p class="support__card-description">Stabilized crops of each tube are laid out over time, holding the background still so the only thing moving is the candidate itself.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Verify it live</h3>
    <p class="support__card-description">Re-run the full pipeline from scratch on the Space's hardware to confirm the precomputed results for yourself.</p>
  </div>

</div>

## Why Temporal Verification

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Fewer false alarms</h3>
    <p class="support__card-description">Clouds, haze, and fog are the classic triggers of false positives — watching over time filters them out.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Trust in alerts</h3>
    <p class="support__card-description">Every false alarm erodes confidence and wastes responder time. Cleaner alerts keep people acting on the ones that matter.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">A second opinion</h3>
    <p class="support__card-description">It layers on top of frame-by-frame detection, adding temporal context without slowing the first warning.</p>
  </div>

</div>

{{< space_partners >}}

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the wider early forest fire detection project and Pyronear's work — the detection system this verification step builds on.</p>
  <a href="/projects/early_forest_fire_detection/" class="link-no-decoration button button--middle">View the project</a>
</div>
