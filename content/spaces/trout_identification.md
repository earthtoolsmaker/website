---
title: Trout Identification
card_image: /images/pages/spaces/trout_identification/card.svg
summary: Reading the spot patterns on trout to identify individual fish — a non-invasive way to monitor populations.
github_repo: https://github.com/earthtoolsmaker/trout-reid
date: 2024-12-08
hero_image: /images/pages/spaces/trout_identification/hero.jpg
project: /projects/trout_identification/
hf_space: earthtoolsmaker-trout-reid
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/trout-reID/tree/main
manual_steps:
  - step_name: Image Selection
    description: Choose an image from the examples provided below, or upload your own data.
  - step_name: Run the ML model
    description: Click the 'Identify' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will standardize the fish images and compare them to our database of trout from British Columbia. It then identifies the individual fish that has the highest probability of matching. If no match is found, the fish is classified as a new entry.
---

## Overview

Trout Identification reads the spot patterns on a trout the way a fingerprint scanner reads a thumb. Each fish carries a unique, stable arrangement of black spots that stays consistent throughout its life — so a clear photo is enough to recognize the same individual again. Developed with [Lumax AI](https://lumax.ai/), the system was built around Westslope Cutthroat Trout monitored in the Elk River, British Columbia.

It compares a new image against a catalog of known fish and returns the most likely match — or flags the trout as a new entry when it hasn't been seen before. No tagging, no handling, no stress on the animal.

## How It Works

From a photo to a confident match:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Image input</h3>
    <p class="support__card-description">Works from ordinary trout photographs — choose an example or upload your own image of the fish.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Standardization</h3>
    <p class="support__card-description">Aligns and standardizes the fish so spot patterns can be compared consistently, regardless of how the photo was taken.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Spot-pattern matching</h3>
    <p class="support__card-description">Matches the unique spot arrangement against a catalog of known trout and ranks the most likely individual.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">New-entry detection</h3>
    <p class="support__card-description">When no confident match exists, the fish is logged as a new individual — growing the catalog over time.</p>
  </div>

</div>

## Why It Matters

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">An indicator species</h3>
    <p class="support__card-description">Westslope Cutthroat Trout need cold, clean water, so their numbers are a sensitive gauge of freshwater ecosystem health.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Non-invasive</h3>
    <p class="support__card-description">Identification from natural markings means no tags or handling — monitoring that doesn't disturb the fish.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Population tracking</h3>
    <p class="support__card-description">Re-identifying individuals over time supports survival estimates, movement studies, and long-term population monitoring.</p>
  </div>

</div>

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full trout identification project and our work with Lumax AI on the Elk River — the research behind this tool.</p>
  <a href="/projects/trout_identification/" class="link-no-decoration button button--middle">View the project</a>
</div>
