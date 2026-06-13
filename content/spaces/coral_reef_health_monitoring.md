---
title: Coral Reef Health Monitoring
card_image: /images/pages/spaces/coral_reef_health_monitoring/card.svg
summary: Detecting and identifying coral species in benthic imagery to track reef health over time.
github_repo: https://github.com/earthtoolsmaker/coralreef-conservation
date: 2024-01-30
hero_image: /images/pages/spaces/coral_reef_health_monitoring/hero.jpg
project: /projects/coral_reef_health_monitoring/
hf_space: earthtoolsmaker-coral-segmentation-reef-support
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/coral-segmentation-reef-support/tree/main
manual_steps:
  - step_name: Image Selection
    description: Choose an image from the examples provided below, or upload your own data.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will generate bounding boxes and segmentation masks for the detected coral species, each accompanied by a corresponding probability score.
---

## Overview

Coral Reef Health Monitoring brings computer vision to benthic (seabed) imagery, detecting and segmenting corals so reef surveys can be analyzed in a fraction of the time. Built in collaboration with [ReefSupport](https://reef.support/), it turns the photos and video collected on research dives into measurable data on what lives on the reef — and how that changes over time.

Marine biologists spend a large share of their time manually processing dive footage. By automating the segmentation step, this tool removes the reporting bottleneck and helps quantify the long-term growth or decline of coral cover within marine protected areas.

## How It Works

From a single benthic image to quantified reef cover:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Benthic image input</h3>
    <p class="support__card-description">Works with the imagery already gathered on research dives — pick an example or upload your own seabed photo.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Detection &amp; segmentation</h3>
    <p class="support__card-description">Draws bounding boxes and pixel-level segmentation masks around each coral, isolating it from sand, water, and other substrate.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Probability scores</h3>
    <p class="support__card-description">Every detection comes with a confidence score, so analysts can prioritize review and keep only reliable results.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Coral-cover quantification</h3>
    <p class="support__card-description">Segmentation masks translate into measurable coral cover — the foundation for tracking reef change survey after survey.</p>
  </div>

</div>

## Why Reef Monitoring Matters

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity hotspots</h3>
    <p class="support__card-description">Reefs shelter roughly a quarter of all marine species on under 1% of the ocean floor — monitoring their health protects an outsized share of ocean life.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Faster reporting</h3>
    <p class="support__card-description">Automating image analysis clears the reporting backlog, so conservation guidance can reach the field while it still makes a difference.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Tracking change in MPAs</h3>
    <p class="support__card-description">Consistent, repeatable cover estimates reveal whether protected reefs are recovering or declining over the long term.</p>
  </div>

</div>

{{< space_partners >}}

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full coral reef health monitoring project and our collaboration with ReefSupport — the pipeline and research behind this tool.</p>
  <a href="/projects/coral_reef_health_monitoring/" class="link-no-decoration button button--middle">View the project</a>
</div>


