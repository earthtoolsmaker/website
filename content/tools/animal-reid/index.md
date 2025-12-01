---
title: Animal reID
show_title: true
button_cta: Try Demo
icon: /images/logos/reid-icon.png
summary: A modular computer vision framework for individual animal identification using state-of-the-art techniques including metric learning, local feature matching, and spot pattern analysis across multiple species.
date: 2025-11-24
js:
  - /js/animal-reid.js
  - /js/tabs.js
---

<div class="tool-container-button-cta">
  <a class="link-no-decoration" href="#demos" >
    <button class="button tool-button-cta">
      Try Interactive Demos
    </button>
  </a>
</div>

# Individual Animal Identification Across Species

Animal reID is a modular framework that enables precise identification of individual animals using computer vision. Built on years of conservation technology research, our approach adapts to different species by employing the most appropriate identification technique—whether that's facial recognition, spot pattern matching, or local feature analysis.

From monitoring bear populations in British Columbia to tracking individual trout in river systems, and extending to snow leopards in Central Asia and seals in coastal waters, Animal reID provides researchers with powerful, non-invasive tools for wildlife monitoring and conservation.

{{< image_carousel id="animal-reid-gallery" >}}
  {{< carousel_image src="./images/animal_reid_leopard_1.png" alt="Snow Leopard Identification" caption="Local feature matching identifies individual snow leopards by analyzing their unique spot patterns across camera trap images." >}}
  {{< carousel_image src="./images/animal_reid_leopard_2.png" alt="Leopard Spot Analysis" caption="LightGLUE matches keypoints between a query image and database entries to find the same individual across different sightings." >}}
  {{< carousel_image src="./images/animal_reid_seal_1.png" alt="Seal Pattern Matching" caption="Seal identification uses facial features and whisker patterns to track individuals in the Wadden Sea monitoring program." >}}
{{< /image_carousel >}}

## Key Features

- 🧬 **Multi-Species Support**: Proven techniques for bears, trout, seals, and snow leopards, with extensibility for other species
- 🎯 **Modular Architecture**: Choose from metric learning, local feature matching, or hybrid approaches based on your species and data
- 🔬 **Research-Grade Accuracy**: Built on peer-reviewed techniques including Instance Segmentation + Metric Learning and LightGLUE local feature matching
- 🌍 **Conservation Focused**: Designed for real-world field applications with non-invasive monitoring capabilities
- 📊 **Database Integration**: Compare new observations against historical databases to track population dynamics over time

<br/>

## Conservation Impact

Animal reID technology enables researchers to:

- **Monitor population dynamics** without invasive tagging or marking
- **Track individual animals** across seasons and years to understand behavior, migration, and survival
- **Assess conservation effectiveness** by quantifying population trends with individual-level precision
- **Reduce field costs** by automating identification from camera trap and observation images
- **Scale monitoring efforts** to cover larger geographic areas with existing observation networks

<br/>
<br/>

## Interactive Demos {#demos}

Experience Animal reID in action with our live demonstrations. These systems are currently monitoring real wildlife populations.

{{< tabs labels="🐻 Bear |🐠 Trout |🦭 Seal |🐆 Snow Leopard" id="animal-reid-demos" >}}
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

## Resources & Documentation

{{< tabs labels="🚀 Try |🔬 Techniques|📁 Projects|📖 Guides" id="resources-tabs" >}}
{{< tab index="0" >}}

<p class="tabs__intro">Experience Animal reID systems in action through our interactive demonstration spaces. Each space provides hands-on access to production-grade identification models.</p>

<div class="container">
  <div class="row">

{{< space_card title="Bear Identification" link="/spaces/bear_identification/" emoji="🐻" summary="A computer vision system utilizes facial recognition technology to analyze bear photographs and identify individual bears. This innovative system aims to monitor the population size of bears in British Columbia over time, ultimately supporting and enhancing conservation efforts in the region." >}}

{{< space_card title="Trout Identification" link="/spaces/trout_identification/" emoji="🐠" summary="A computer vision system analyzes the spot patterns of trout to identify individual fish. This innovative, non-invasive approach aims to monitor trout populations in British Columbia over time, ultimately supporting and enhancing conservation efforts in the region." >}}

{{< space_card title="Seal Identification" link="/spaces/seal_identification/" emoji="🦭" summary="Non-invasive seal re-identification using computer vision to track individual animals across seasons through unique whisker patterns and facial features in the Wadden Sea." >}}

{{< space_card title="Snow Leopard Identification" link="/spaces/snowleopard_identification/" emoji="🐆" summary="Computer vision system for identifying individual snow leopards using feature matching and machine learning, supporting conservation efforts in Central Asia." >}}

  </div>
</div>

{{< /tab >}}
{{< tab index="1" markdown="true" >}}

### Metric Learning for Facial Recognition

Used successfully for **bear identification**, this approach combines instance segmentation to isolate animal faces with deep metric learning to create unique embeddings for each individual. The system learns to recognize subtle facial features and marking patterns that distinguish one animal from another.

**Key advantages:**
- Highly accurate for species with distinctive facial features
- Robust to pose variations and lighting conditions
- Proven in production for British Columbia bear monitoring

**Applications**: Bears, primates, big cats, and other species with distinctive facial characteristics

### Local Feature Matching for Spot Patterns

Pioneered in our **trout identification** work, this technique uses advanced local feature matching (LightGLUE) to analyze unique spot patterns on fish bodies. The system standardizes fish orientations and matches keypoint patterns against a reference database.

**Key advantages:**
- Non-invasive identification from natural markings
- Works with partial views and occlusions
- Effective for species with complex, unique pattern distributions

**Applications**: Trout, leopards, cheetahs, whale sharks, and other spot-patterned species

{{< /tab >}}
{{< tab index="2" >}}

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
{{< tab index="3" >}}

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

<br/>

## Get Started

Interested in applying Animal reID to your conservation project? We offer consultation on selecting the right identification approach, custom development for new species, and collaborative research opportunities.

<br/>
<div style="text-align: center;">
  <a href="/contact/" class="button">Get in Touch</a>
</div>
