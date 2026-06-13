---
title: Seal Identification
card_image: /images/pages/spaces/seal_identification/card.svg
summary: Re-identifying individual seals by their whisker and face patterns — non-invasive, across seasons.
date: 2025-01-24
hero_image: /images/pages/spaces/seal_identification/hero.png
project: /projects/wadden_sea_seal_monitoring/
hf_space: earthtoolsmaker-seal-reid
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/seal-reid/tree/main
manual_steps:
  - step_name: Upload Seal Image
    description: Select a clear image of a seal's face showing whisker patterns and facial features. The image should ideally show the seal from a frontal or slight angle for best results.
  - step_name: Run the Model
    description: Click the 'Submit' button to process the image. The model will extract unique facial features and search for matches in the database of known individuals.
  - step_name: Review Matches
    description: The system will display the top-k most similar seals from the database with confidence scores. High confidence matches typically indicate the same individual across different sightings.
---

## Overview

Seal Identification lets researchers track individual seals over time without tagging or any invasive procedure. By reading the unique whisker patterns, facial markings, and head shape of each animal, the model builds a distinctive "fingerprint" that stays stable across seasons and years. Developed with [Wageningen Marine Research](https://www.wur.nl/en/research-results/research-institutes/marine-research.htm), it supports the grey and harbour seal colonies of the Wadden Sea — a UNESCO World Heritage Site.

## Key Features

What the re-identification system brings:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Whisker &amp; face fingerprints</h3>
    <p class="support__card-description">Combines whisker patterns, facial markings, and head shape into a signature unique to each individual.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Top-k matching</h3>
    <p class="support__card-description">Searches a database of known seals and returns the most similar individuals for review, not just a single guess.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Confidence scores</h3>
    <p class="support__card-description">Each match comes with a confidence score, so a high-confidence hit signals the same seal seen again across sightings.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Non-invasive, across seasons</h3>
    <p class="support__card-description">Identification from photographs alone means individuals can be followed year after year without ever handling them.</p>
  </div>

</div>

## Use Cases

Where it supports seal conservation:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Long-term population studies</h3>
    <p class="support__card-description">Re-identify individuals across survey years to estimate survival rates and build complete life histories without invasive tagging.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Movement ecology</h3>
    <p class="support__card-description">Map how seals move between haul-out sites across the Wadden Sea, informing conservation planning and protected-area design.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Reproductive monitoring</h3>
    <p class="support__card-description">Track individual females and their reproductive success to understand breeding frequency, pup survival, and population growth.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Behavioral research</h3>
    <p class="support__card-description">Link identities to observations to study social networks, site fidelity, and behavior within colonies.</p>
  </div>

</div>

## Beyond the Wadden Sea

Though built for the Wadden Sea, the same re-identification approach transfers to other seal populations and marine mammals worldwide — from Arctic ice seals to Antarctic fur seals — wherever non-invasive individual tracking can support conservation.

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full Wadden Sea seal monitoring project and our work with Wageningen Marine Research — including the detection system and researcher web app.</p>
  <a href="/projects/wadden_sea_seal_monitoring/" class="link-no-decoration button button--middle">View the project</a>
</div>
