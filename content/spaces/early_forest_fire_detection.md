---
title: Early Forest Fire Detection
card_image: /images/pages/spaces/early_forest_fire_detection/card.svg
summary: Real-time camera analysis that spots wildfires early and raises the alarm fast.
github_repo: https://github.com/earthtoolsmaker/pyronear-mlops
date: 2024-04-23
hero_image: /images/pages/spaces/early_forest_fire_detection/hero.jpg
project: /projects/early_forest_fire_detection/
hf_space: earthtoolsmaker-forest-fire-pyronear
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/forest-fire-pyronear/tree/main
manual_steps:
  - step_name: Image Selection
    description: Choose an image from the examples provided below, or upload your own data.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will generate bounding boxes on the detected fire smokes with an associated probability.
---

## Overview

Early Forest Fire Detection analyzes camera imagery to spot the first wisps of wildfire smoke and flag them fast. It is the detection model behind [Pyronear](https://pyronear.org/), whose network of high-resolution cameras watches forested regions around the clock from elevated vantage points — turning a panoramic view of the landscape into an early warning the moment smoke appears.

When the model spots smoke, it draws a bounding box with an associated probability. In the field, that detection becomes an alert routed to a supervision platform connected to the fire department, so responders can act while a fire is still small.

## How Detection Works

From a camera frame to an actionable alert:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Always-on cameras</h3>
    <p class="support__card-description">High-resolution cameras at elevated vantage points give panoramic coverage of the forest, day and night.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Real-time analysis</h3>
    <p class="support__card-description">The model runs on a compact, low-power microcomputer at the camera, so detection happens on-site without heavy infrastructure.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Smoke localization</h3>
    <p class="support__card-description">Detected smoke is marked with a bounding box and a probability, pinpointing where in the frame the threat is emerging.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Fast alerting</h3>
    <p class="support__card-description">Detections feed a supervision platform connected to the fire department, turning a sighting into a response within minutes.</p>
  </div>

</div>

## Why Early Detection Matters

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity</h3>
    <p class="support__card-description">Wildfires can wipe out habitats and the species that depend on them — catching fires early limits the damage.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Carbon storage</h3>
    <p class="support__card-description">Forests lock away carbon. Every fire prevented or contained keeps that carbon out of the atmosphere.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Communities &amp; responders</h3>
    <p class="support__card-description">Earlier warnings mean smaller fires, safer firefighting, and more time to protect the people living near forests.</p>
  </div>

</div>

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full early forest fire detection project and our work with Pyronear — the end-to-end system from camera to fire department.</p>
  <a href="/projects/early_forest_fire_detection/" class="link-no-decoration button button--middle">View the project</a>
</div>

