---
title: Forest Elephant Rumbles Detection
card_image: /images/pages/spaces/forest_elephant_rumble_detection/card.svg
summary: Listening to African forests to detect and classify elephant rumbles from audio recordings.
github_repo: https://github.com/earthtoolsmaker/forest-elephants-rumble-detection
date: 2024-06-26
hero_image: /images/projects/forest_elephants_passive_acoustic_monitoring/cover.png
image: /images/projects/forest_elephants_passive_acoustic_monitoring/cover.png
project: /projects/elephants_passive_acoustic_monitoring/
hf_space: earthtoolsmaker-forest-elephant-rumbles-detection
hf_space_code: https://huggingface.co/spaces/earthtoolsmaker/forest-elephant-rumbles-detection/tree/main
manual_steps:
  - step_name: Audio Selection
    description: Choose an audio file containing elephant rumbles from the examples provided below, or upload your own audio data.
  - step_name: Run the ML model
    description: Click the 'Submit' button to initiate the machine learning model.
  - step_name: Visualize the results
    description: The system will generate spectrograms in the infrasound range and detect the elephant rumbles using the ML model.
  - step_name: Export the data
    description: A CSV file will be created, containing a comprehensive analysis of the audio file, including the localization of the detected elephant rumbles.
---

## Overview

Forest Elephant Rumbles Detection listens to the soundscape of Central Africa's rainforests and picks out elephant rumbles — the low-frequency calls that travel far through dense forest where the animals themselves are almost impossible to see. Developed with the [Elephant Listening Project](https://elephantlisteningproject.org/) at the Cornell Lab's K. Lisa Yang Center for Conservation Bioacoustics, it turns long audio recordings into structured data on when and where elephants called.

Forest elephants have declined by more than 60% in a decade, and a critical obstacle to protecting them is simply not knowing where they are over time. Passive acoustic monitoring offers a way to close that data gap at the scale of an entire forest.

## How It Works

From raw audio to a localized rumble log:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Audio input</h3>
    <p class="support__card-description">Works with recordings from the forest soundscape — choose an example clip or upload your own audio.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Infrasound spectrograms</h3>
    <p class="support__card-description">Generates spectrograms in the infrasound range, making the low-frequency rumbles visible to the model and to you.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Rumble detection</h3>
    <p class="support__card-description">The model detects and classifies elephant rumbles against the background noise of the forest.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">CSV export</h3>
    <p class="support__card-description">Produces a CSV with a full analysis of the recording, including the time localization of each detected rumble — ready for downstream research.</p>
  </div>

</div>

## Why Acoustic Monitoring Matters

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Population insight</h3>
    <p class="support__card-description">Sound carries where cameras can't see, giving researchers a way to track presence and activity across vast, dense forest.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Anti-poaching</h3>
    <p class="support__card-description">Knowing where and when elephants are active helps prioritize patrols and protection in the areas that need it most.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Reducing conflict</h3>
    <p class="support__card-description">Better data on elephant movement supports efforts to anticipate and mitigate human–elephant conflict.</p>
  </div>

</div>

{{< space_partners >}}

<div class="about-cta">
  <h3 class="about-cta__title">Learn more about the project</h3>
  <p class="about-cta__description">See the full passive acoustic monitoring project and our work with the Elephant Listening Project and the Cornell Lab.</p>
  <a href="/projects/elephants_passive_acoustic_monitoring/" class="link-no-decoration button button--middle">View the project</a>
</div>
