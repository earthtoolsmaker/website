---
title: AI-BIRD
weight: 25
show_title: false
button_cta: Request a demo
icon: /images/logos/ai-bird-logo.svg
logo_container: true
card_tint: "#dbe8f1"
summary: Automated bird surveys from drone imagery. AI finds every bird, identifies its species, sex and behaviour, checks whether it is alive, and turns it all into georeferenced maps and reports.
project: /projects/bird_flu_monitoring
landing_page_url: https://ai-bird.org/
open_source: false
manual_url: https://manual.ai-bird.org/
date: 2026-09-08
partners:
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
  - name: Sovon
    link: https://www.sovon.nl/
    logo: /images/clients/sovon/logo.svg
---

<!--
  Hero background video: static/videos/ai-bird-hero.mp4
  Source: the AI-BIRD landing page hero (ai-bird.org/video/hero.mp4), re-encoded
  to 1280x720 for this site. Drone footage of a gull colony on a beach.
-->
<div class="tool-hero">
  <video class="tool-hero__video" autoplay muted loop playsinline preload="auto" aria-label="Drone footage looking straight down at gulls resting on a sandy beach beside the surf">
    <source src="/videos/ai-bird-hero.mp4" type="video/mp4">
  </video>
  <div class="tool-hero__overlay">
    <h1 class="tool-hero__title">Automated Bird Surveys, From the Sky</h1>
    <p class="tool-hero__tagline">Fly a drone over the colony. AI-BIRD finds every bird, tells you its species, sex and behaviour, checks whether it is alive, and hands you the map and the report.</p>
  </div>
</div>

<section class="about-stats about-stats--three tools-stats">
  <div class="about-stats__grid">
    <div class="about-stats__item">
      <div class="about-stats__value">10</div>
      <div class="about-stats__label">seabird species identified</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">4</div>
      <div class="about-stats__label">traits per bird: species, sex, behaviour, status</div>
    </div>
    <div class="about-stats__item">
      <div class="about-stats__value">3</div>
      <div class="about-stats__label">steps from flight to report</div>
    </div>
  </div>
</section>

AI-BIRD (Automated Intelligence for Bird Inventory and Reproduction using Drones) is a web platform that turns drone imagery into bird surveys. Upload the photos from a flight over a colony and trained vision models detect every bird, classify each one, and produce georeferenced inventory maps and exportable reports, ready to compare from one survey to the next.

<div class="tool-container-button-cta" id="container-button-demo-ai-bird">
  <a class="link-no-decoration" href="https://ai-bird.org/#contact" target="_blank" rel="noopener">
    <button class="button tool-button-cta">
      <i class="fa-solid fa-paper-plane" style="margin-right: 0.5em;"></i>Request a demo
    </button>
  </a>
  <a class="link-no-decoration" href="https://manual.ai-bird.org/" target="_blank" rel="noopener">
    <button class="button button--ghost">
      <i class="fa-solid fa-book" style="margin-right: 0.5em;"></i>Read the manual
    </button>
  </a>
</div>

## How It Works

A survey is one flight and a few clicks. The drone does the walking, the models do the counting.

![How AI-BIRD works: a drone flies the colony, every bird in the imagery is detected, each one is classified by species, sex, behaviour and status, and the results become a georeferenced map and an exportable report](/images/tools/ai-bird/diagrams/pipeline.svg)
*A drone flies the colony, every bird in the imagery is detected, each one is classified, and the results become a georeferenced map with an exportable report.*

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">1. Fly the drone</h3>
    <p class="support__card-description">Capture aerial imagery of your survey area with an off-the-shelf drone. No specialist hardware, and nobody has to walk through the colony.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">2. AI detects and classifies</h3>
    <p class="support__card-description">Upload the flight. Trained vision models find every bird in every frame, identify the species, and record sex, behaviour and whether the bird is alive.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">3. Get maps and reports</h3>
    <p class="support__card-description">Explore the georeferenced inventory map in the browser, then export detections and summaries in standard formats for your own analysis.</p>
  </div>

</div>

## One Bird, Four Answers

Counting is only the start. For every bird it finds, AI-BIRD records four things, so a single survey tells you not just how many birds there are but who they are and how they are doing.

![One detected bird with four answers: species, one of ten seabird species; sex, male or female; behaviour, what the bird is doing; status, alive or dead](/images/tools/ai-bird/diagrams/one-bird-four-answers.svg)
*Every detection carries a species (one of ten seabirds), a sex, a behaviour and a status.*

<!--
  Screenshot gallery. Drop screenshots of the app into content/tools/ai-bird/images/
  using the filenames below, then uncomment this section.

## See AI-BIRD in Action

{{</* image_carousel id="ai-bird-gallery" */>}}
  {{</* carousel_image src="./images/survey-overview.png" alt="AI-BIRD survey overview" caption="Overview: a survey opens on its map, with detection totals per species and status." shadow="false" rounded="false" */>}}
  {{</* carousel_image src="./images/upload-imagery.png" alt="Uploading drone imagery to AI-BIRD" caption="Upload: drag in the images from a flight and the platform georeferences them." shadow="false" rounded="false" */>}}
  {{</* carousel_image src="./images/run-detection.png" alt="Running bird detection on a survey" caption="Detect: run the models and watch every bird get a box and a label." shadow="false" rounded="false" */>}}
  {{</* carousel_image src="./images/explore-results.png" alt="Exploring detections on the survey map" caption="Explore: filter the map by species, sex, behaviour or status." shadow="false" rounded="false" */>}}
  {{</* carousel_image src="./images/export-data.png" alt="Exporting survey results" caption="Export: download detections and summaries in standard formats." shadow="false" rounded="false" */>}}
{{</* /image_carousel */>}}
-->

## What AI-BIRD Does

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Automated detection</h3>
    <p class="support__card-description">Find every bird in your imagery without manual counting, frame after frame, survey after survey.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Species classification</h3>
    <p class="support__card-description">Identify ten seabird species automatically with trained vision models, plus sex, behaviour and whether each bird is alive.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Geospatial maps</h3>
    <p class="support__card-description">Turn detections into georeferenced inventory maps, so every bird has a place as well as a label.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Reproducible surveys</h3>
    <p class="support__card-description">Re-run the same pipeline on the next flight for consistent, comparable results across the season and across years.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Exportable reports</h3>
    <p class="support__card-description">Download detections and summaries in standard formats and carry them into your own GIS or statistics workflow.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Avian influenza monitoring</h3>
    <p class="support__card-description">The flagship use case: survey colonies for outbreak and mortality signals without setting foot among the birds.</p>
  </div>

</div>

## Flagship Use Case: Avian Influenza

Highly pathogenic bird flu can tear through a dense seabird colony in days. Because a drone survey is fast and disturbs nothing, it can be repeated as often as an outbreak demands, and the alive-or-dead status on every detection turns each flight into a mortality count.

<div class="support__grid support__grid--two">

  <div class="support__card support__track">
    <span class="support__track-label">Survey</span>
    <h3 class="support__card-title">Count the colony without entering it</h3>
    <p class="support__card-description">Walking a colony to count by hand disturbs nesting birds, risks trampling eggs and rarely covers everything. A drone flight covers the whole colony in minutes and can be flown again next week.</p>
    <ul class="support__track-offers">
      <li>Whole-colony coverage in a single flight</li>
      <li>No disturbance to nesting adults or chicks</li>
      <li>Safe to repeat through the breeding season</li>
    </ul>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Signal</span>
    <h3 class="support__card-title">Read the outbreak in the numbers</h3>
    <p class="support__card-description">Every bird is flagged alive or dead and placed on the map, so a survey shows where mortality is clustering and how it moves. Comparing flights over time reveals survival and reproduction, not just a headcount.</p>
    <ul class="support__track-offers">
      <li>Mortality mapped, not just totaled</li>
      <li>Survey-to-survey comparison on one pipeline</li>
      <li>Early warning for conservation response</li>
    </ul>
  </div>

</div>

<div class="about-cta" style="margin-bottom: 64px;">
  <h3 class="about-cta__title">Read about the bird flu monitoring project</h3>
  <p class="about-cta__description">AI-BIRD grew out of our work with Lumax AI on monitoring avian influenza in seabird colonies. The project page covers the threat, the field context, and how the survey pipeline came together.</p>
  <a href="/projects/bird_flu_monitoring/" class="link-no-decoration button button--middle">Bird Flu Monitoring project</a>
</div>

## Our Partners

AI-BIRD is built in close collaboration with Lumax AI and Sovon, the Dutch centre for field ornithology.

{{< partner_logos "partners" >}}

<div class="support__cta-band">
  <div class="support__cta-band-text">
    <h3 class="support__cta-band-title">Ready to survey from the sky?</h3>
    <p class="support__cta-band-description">Tell us about your colony and your survey needs, and we will set you up with a demo of the platform.</p>
  </div>
  <div class="support__cta-band-buttons">
    <a class="link-no-decoration" href="https://ai-bird.org/#contact" target="_blank" rel="noopener"><button class="button">Request a demo</button></a>
    <a class="link-no-decoration" href="https://app.ai-bird.org/" target="_blank" rel="noopener"><button class="button button--ghost">Log in to the app</button></a>
  </div>
</div>
