---
title: Wild Salmon Migration Monitoring
card_image: /images/pages/spaces/wild_salmon_migration_monitoring/card.svg
summary: Classifying and counting wild salmon from underwater camera streams as they migrate back to spawn.
github_repo: https://github.com/Salmon-Computer-Vision/salmon-computer-vision/tree/master
date: 2024-08-20
hero_image: /images/pages/spaces/wild_salmon_migration_monitoring/hero.png
project: /projects/wild_salmon_migration_monitoring/
hf_space: earthtoolsmaker-salmon-vision
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/salmon-vision/tree/main
manual_steps:
  - step_name: Video Selection
    description: Choose a video file containing salmons from the examples provided below, or upload your own video.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will generate an annotated video with bouding boxes around salmons and will count the number of individuals.
---

## Overview

Wild Salmon Migration Monitoring counts and classifies salmon straight from underwater camera streams as they return upriver to spawn. It's the model behind [SalmonVision](https://salmonvision.org/), built with the [Pacific Salmon Foundation](https://psf.ca/), the [Wild Salmon Center](https://wildsalmoncenter.org/), [Lumax AI](https://lumax.ai/), and [Simon Fraser University](https://sfu.ca/) to monitor a wide range of salmon species across British Columbia.

Knowing how many salmon make it back is essential for management — escapement targets exist to ensure enough fish pass through, and populations face mounting pressure from fisheries, dams, and a changing climate. Automating the count turns continuous underwater video into reliable numbers without hours of manual review.

## How It Works

From an underwater clip to a counted run:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Video input</h3>
    <p class="support__card-description">Works on underwater camera footage of the river — choose an example clip or upload your own video.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Detection</h3>
    <p class="support__card-description">Locates each salmon in the stream and marks it with a bounding box, even in busy, low-visibility water.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Tracking &amp; counting</h3>
    <p class="support__card-description">Follows fish across frames and tallies individuals, producing an annotated video and a count you can trust.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Built for many species</h3>
    <p class="support__card-description">Designed to monitor a range of salmon species returning to their natal streams, not just one.</p>
  </div>

</div>

## Why It Matters

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Meeting escapement targets</h3>
    <p class="support__card-description">Accurate counts confirm whether enough salmon are passing through to satisfy conservation regulations.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Pressure on populations</h3>
    <p class="support__card-description">Fisheries, dams, and habitat change all threaten salmon runs — monitoring is the first step to managing them.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Ecosystem &amp; culture</h3>
    <p class="support__card-description">Wild salmon are woven into BC's ecology, economy, and culture, carrying nutrients from ocean to stream as they return.</p>
  </div>

</div>

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full wild salmon migration monitoring project and the SalmonVision partnership behind this tool.</p>
  <a href="/projects/wild_salmon_migration_monitoring/" class="link-no-decoration button button--middle">View the project</a>
</div>

