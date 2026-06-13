---
title: Bear Identification
card_image: /images/pages/spaces/bear_identification/card.svg
summary: Facial recognition that tells individual bears apart from photos — tracking British Columbia's black bear population over time.
github_repo: https://github.com/earthtoolsmaker/bear-conservation
date: 2024-04-03
hero_image: /images/projects/bear_identification/cover.png
project: /projects/bear_identification/
hf_space: earthtoolsmaker-bear-face-recognition
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/bear-face-recognition/tree/main
manual_steps:
  - step_name: Image Selection
    description: Choose an image from the examples provided below, or upload your own data.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will segment bear faces from the images and compare them against our database of bear faces from British Columbia. It then identifies the individual bear with the highest probability match.
---

## Overview

Bear Identification uses facial recognition to tell individual bears apart from ordinary photos — no collars, tags, or handling required. Developed in collaboration with the [BearID Project](https://bearresearch.org/), the system segments a bear's face from an image and compares it against a catalog of known individuals from British Columbia, returning the closest match.

Because a bear's facial features stay recognizable over time, the same animal can be re-identified across seasons and camera trap locations — turning everyday wildlife photos into long-term population data.

## Key Features

What powers the identification:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Face detection &amp; segmentation</h3>
    <p class="support__card-description">Isolates the bear's face from a busy background so matching focuses on the features that actually distinguish one animal from another.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Metric-learning embeddings</h3>
    <p class="support__card-description">Turns each face into a compact signature that captures the subtle traits separating individuals — the approach proven in our British Columbia work.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Catalog matching</h3>
    <p class="support__card-description">Compares the query face against a database of known bears and ranks the most likely individuals by probability.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Confidence-ranked results</h3>
    <p class="support__card-description">Surfaces the highest-probability match first, so reviewers can confirm an identity at a glance instead of scanning the whole catalog.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Fully non-invasive</h3>
    <p class="support__card-description">Works from camera-trap and field photographs, with no tagging, collaring, or handling of the animals.</p>
  </div>

</div>

## Use Cases

Where it supports bear conservation:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Population monitoring</h3>
    <p class="support__card-description">Estimate how many distinct individuals use an area from camera-trap surveys, and track how that changes over time without physical capture.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Tracking individuals over time</h3>
    <p class="support__card-description">Follow specific bears across seasons and camera locations to study survival, movement, and behavior.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Scalable field research</h3>
    <p class="support__card-description">Automate identification that would otherwise take experts many hours of manual photo comparison, freeing time for analysis and fieldwork.</p>
  </div>

</div>

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full bear identification project and our collaboration with the BearID Project — the field context and research behind this system.</p>
  <a href="/projects/bear_identification/" class="link-no-decoration button button--middle">View the project</a>
</div>
