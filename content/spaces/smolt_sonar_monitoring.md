---
title: Smolt Sonar Monitoring
card_image: /images/pages/spaces/smolt_sonar_monitoring/card.svg
summary: Detecting, tracking and counting juvenile salmon in ARIS sonar as they migrate downstream.
date: 2026-01-10
project: /projects/monitoring_smolt_salmon_migration_with_sonar/
hf_space: Lumax-eco-sonar-smolt
hf_space_code: https://huggingface.co/spaces/Lumax/eco-sonar-smolt/tree/main
manual_steps:
  - step_name: Video Selection
    description: Choose a preprocessed sonar video from the examples provided below, or upload your own sonar footage.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the detection and tracking pipeline.
  - step_name: Visualize the results
    description: The system will generate an annotated video with bounding boxes around detected smolt, track their movement, and count individuals by migration direction.
---

## Overview

Smolt Sonar Monitoring detects, tracks, and counts juvenile salmon as they migrate downstream — straight from ARIS sonar footage. Developed with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/), it was built around sonar collected at Jansen Lake on Vancouver Island, British Columbia.

Sonar is essential here because smolt migrate in turbid water, at night, and in dense bursts where optical cameras fail. ARIS produces video-like acoustic images that make small fish visible in those conditions — but reviewing that footage by hand is slow and error-prone. This tool automates the count.

## How It Works

From a sonar clip to a directional count:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Sonar video input</h3>
    <p class="support__card-description">Works directly on ARIS acoustic imagery — choose a preprocessed example sequence or upload your own sonar footage.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Smolt detection</h3>
    <p class="support__card-description">Deep-learning object detection finds individual smolt in noisy acoustic frames and marks each with a bounding box.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Movement tracking</h3>
    <p class="support__card-description">A tracker follows each fish across frames, so the same smolt isn't counted twice as it passes through the sonar beam.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Directional counting</h3>
    <p class="support__card-description">Counts individuals by migration direction, separating genuine downstream migrants from fish drifting the other way.</p>
  </div>

</div>

## Why Count Smolt

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Population trends</h3>
    <p class="support__card-description">Smolt counts over multiple years reveal whether a salmon population is growing, stable, or heading toward collapse.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Dam impact</h3>
    <p class="support__card-description">Counts above and below infrastructure quantify how dams and turbines affect downstream fish survival.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Compliance &amp; management</h3>
    <p class="support__card-description">Consistent, auditable counts feed regulatory reporting and decisions on dam operations and habitat restoration.</p>
  </div>

</div>

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full smolt sonar monitoring project and our work with BC Hydro and Lumax AI — the ARIS pipeline behind this tool.</p>
  <a href="/projects/monitoring_smolt_salmon_migration_with_sonar/" class="link-no-decoration button button--middle">View the project</a>
</div>
