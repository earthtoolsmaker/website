---
title: Animal reID
weight: 40
show_title: true
button_cta: Try Demo
icon: /images/logos/reid-icon.png
card_tint: "#ffe8df"
summary: A modular computer vision framework for individual animal identification using state-of-the-art techniques including metric learning, local feature matching, and spot pattern analysis across multiple species.
date: 2025-11-24
js:
  - /js/animal-reid.js
  - /js/tabs.js
---

# Individual Animal Identification Across Species

Animal reID is a modular computer vision framework for identifying individual animals. It adapts to each species by choosing the right technique — facial recognition, spot-pattern matching, or local feature analysis.

From bears in British Columbia and trout in river systems to snow leopards in Central Asia and seals in coastal waters, it gives researchers non-invasive tools for wildlife monitoring and conservation.

{{< image_carousel id="animal-reid-gallery" >}}
  {{< carousel_image src="./images/animal_reid_leopard_1.png" alt="Snow Leopard Identification" caption="Local feature matching identifies individual snow leopards by analyzing their unique spot patterns across camera trap images." >}}
  {{< carousel_image src="./images/animal_reid_leopard_2.png" alt="Leopard Spot Analysis" caption="LightGLUE matches keypoints between a query image and database entries to find the same individual across different sightings." >}}
  {{< carousel_image src="./images/animal_reid_seal_1.png" alt="Seal Pattern Matching" caption="Seal identification uses facial features and whisker patterns to track individuals in the Wadden Sea monitoring program." >}}
  {{< carousel_image src="./images/animal_reid_trout_1.png" alt="Trout Identification" caption="LightGLUE local feature matching identifies individual trout by analyzing their unique spot patterns along the body." >}}
{{< /image_carousel >}}

<div class="about-cta">
  <h3 class="about-cta__title">See it in action</h3>
  <p class="about-cta__description">Upload a photo to the live demos and watch Animal reID pick out the individual — bear, trout, seal, or snow leopard.</p>
  <a href="#demos" class="link-no-decoration button button--middle">Try the demos</a>
</div>

<br/>
<br/>

## Why Animal reID

Animal reID combines proven techniques into one adaptable system for individual identification.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">One framework, many species</h3>
    <p class="support__card-description">Proven on bears, trout, seals, and snow leopards, and extensible to new species.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">The right technique for your data</h3>
    <p class="support__card-description">Metric learning, local feature matching, or a hybrid, matched to your species and imagery.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Non-invasive by design</h3>
    <p class="support__card-description">Identify individuals from camera-trap and observation images, with no tagging or marking.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Population trends over time</h3>
    <p class="support__card-description">Match new sightings against historical databases to track survival, movement, and behavior.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Built to scale in the field</h3>
    <p class="support__card-description">Automate identification to cut field costs and cover larger areas with existing networks.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Research-grade and open source</h3>
    <p class="support__card-description">Built on peer-reviewed methods, with open-source implementations you can run and adapt.</p>
  </div>

</div>

<br/>
<br/>

## Interactive Demos {#demos}

Experience Animal reID in action with our live demonstrations. These systems are currently monitoring real wildlife populations.

{{< tabs labels="::Bear|::Trout|::Seal|::Snow Leopard" id="animal-reid-demos" >}}
{{< tab index="0" >}}

Upload bear photographs and watch as the system segments facial features and matches them against our database of known individuals from British Columbia.

{{< hf_space "earthtoolsmaker-bear-face-recognition" >}}

{{< /tab >}}
{{< tab index="1" >}}

See local feature matching in action as the system analyzes spot patterns to identify individual trout from river monitoring programs.

{{< hf_space "earthtoolsmaker-trout-reid" >}}

{{< /tab >}}
{{< tab index="2" >}}

Upload seal photographs and see how the system identifies individual seals through their unique whisker patterns and facial features from the Wadden Sea monitoring program.

{{< hf_space "earthtoolsmaker-seal-reid" >}}

{{< /tab >}}
{{< tab index="3" >}}

Upload snow leopard photographs and watch as the system analyzes unique coat patterns to identify individuals from Central Asian mountain ranges.

{{< hf_space "earthtoolsmaker-snowleopard-reid" >}}

{{< /tab >}}
{{< /tabs >}}

<br/>
<br/>

## How It Works

Animal reID matches the identification technique to the species. Two approaches cover most cases:

<div class="support__grid support__grid--two">

  <div class="support__card support__track">
    <span class="support__track-label">Facial recognition</span>
    <h3 class="support__card-title">Metric Learning</h3>
    <p class="support__card-description">Used successfully for bear identification, this approach combines instance segmentation to isolate animal faces with deep metric learning to create unique embeddings for each individual. The system learns to recognize subtle facial features and marking patterns that distinguish one animal from another.</p>
    <div class="support__track-proof">Applications: bears, primates, big cats, and other species with distinctive facial characteristics.</div>
    <ul class="support__track-offers">
      <li>Highly accurate for species with distinctive facial features</li>
      <li>Robust to pose variations and lighting conditions</li>
      <li>Proven in production for British Columbia bear monitoring</li>
    </ul>
  </div>

  <div class="support__card support__track">
    <span class="support__track-label">Spot patterns</span>
    <h3 class="support__card-title">Local Feature Matching</h3>
    <p class="support__card-description">Pioneered in our trout identification work, this technique uses advanced local feature matching (LightGLUE) to analyze unique spot patterns on fish bodies. The system standardizes fish orientations and matches keypoint patterns against a reference database.</p>
    <div class="support__track-proof">Applications: trout, leopards, cheetahs, whale sharks, and other spot-patterned species.</div>
    <ul class="support__track-offers">
      <li>Non-invasive identification from natural markings</li>
      <li>Works with partial views and occlusions</li>
      <li>Effective for species with complex, unique pattern distributions</li>
    </ul>
  </div>

</div>

<br/>
<br/>

## Resources & Documentation

Explore the open-source projects and technical guides behind Animal reID.

{{< tabs labels="::Projects|::Guides" id="resources-tabs" >}}
{{< tab index="0" >}}

<p class="tabs__intro">Each implementation is open-source with detailed documentation:</p>

<div class="container">
  <div class="row">

{{< project_card title="Bear Identification" link="/projects/bear_identification/" image="/images/projects/bear_identification/cover.png" excerpt="Noninvasive technologies to identify and monitor bears, facilitating their conservation." >}}

{{< project_card title="Trout Identification" link="/projects/trout_identification/" image="/images/projects/trout_identification/cover.png" excerpt="Non-invasive technology for monitoring trout populations using computer vision to accurately identify individual fish." >}}

{{< project_card title="Snow Leopard Monitoring" link="/projects/snow_leopard_monitoring/" image="/images/projects/snow_leopard_monitoring/cover.png" excerpt="Non-invasive snow leopard monitoring using computer vision analysis of camera trap photos to identify individual animals." >}}

{{< project_card title="Wadden Sea Seal Monitoring" link="/projects/wadden_sea_seal_monitoring/" image="/images/projects/wadden_sea_seal_monitoring/cover.jpg" excerpt="Automated seal population monitoring using AI to count, classify, and identify individual seals from aerial imagery in the Wadden Sea." >}}

  </div>
</div>

{{< /tab >}}
{{< tab index="1" >}}

<p class="tabs__intro">In-depth technical guides covering the design and implementation of animal identification systems:</p>

<div class="container">
  <div class="row">

{{< article_card title="A guide to designing a bear face segmentation system" link="/posts/bear-face-segmentation-guide/" image="/images/posts/bear-face-segmentation-guide/cover.png" description="Detecting bears in real time using low-power technology." date="11 Apr, 2024" reading_time="8" tags="AI, vision, camera traps" >}}

{{< article_card title="A guide to designing a bear face recognition system" link="/posts/bear-identification-with-metric-learning-guide/" image="/images/posts/bear-identification-with-metric-learning-guide/cover.png" description="Identify bears with Metric Learning." date="12 Apr, 2024" reading_time="13" tags="AI, vision, metric learning, identification" >}}

{{< article_card title="How to prepare data for IDentification?" link="/posts/how-to-prepare-data-for-identification/" image="/images/posts/how-to-prepare-data-for-identification/cover.png" description="An in-depth look at the common preprocessing stages required to perform identification using computer vision." date="8 Dec, 2024" reading_time="11" tags="AI, vision, identification" >}}

{{< article_card title="Identify individuals with Local Feature Matching" link="/posts/local-feature-matching-lightglue/" image="/images/posts/local-feature-matching-lightglue/cover.png" description="A comprehensive examination of using local feature matching for individual identification." date="9 Dec, 2024" reading_time="14" tags="AI, vision, identification, local feature" >}}

  </div>
</div>

{{< /tab >}}
{{< /tabs >}}

<div class="about-cta">
  <h3 class="about-cta__title">Have a species to identify?</h3>
  <p class="about-cta__description">Tell us about your animals and your image data — we'll give you an honest read on which identification approach fits and what it would take.</p>
  <a href="/contact/" class="link-no-decoration button button--middle">Start a project</a>
</div>
