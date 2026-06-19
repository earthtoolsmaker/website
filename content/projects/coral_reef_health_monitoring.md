---
title: Coral Reefs Health Monitoring
summary: Segmentation of coral reefs in benthic imagery to quantify the long-term growth or decline of coral cover within marine protected areas.
tags: ["marine", "vision"]
related_projects:
  - wild_salmon_migration_monitoring
  - monitoring_smolt_salmon_migration_with_sonar
related_spaces:
  - /demos/wild_salmon_migration_monitoring/
  - /demos/smolt_sonar_monitoring/
tagline: Mapping hard and soft coral in underwater imagery to track reef health over time.
stats:
  - value: "25%"
    label: of marine life
  - value: "<1%"
    label: of the seafloor
  - value: "open-source"
    label: models
clients:
  - name: ReefSupport
    link: https://reef.support
    logo: /images/clients/reefsupport/logo.png
related_posts:
  - how-to-build-a-benthic-coral-reefs-analyser
github_repo: https://github.com/earthtoolsmaker/coralreef-conservation
space: /demos/coral_reef_health_monitoring/
tools:
  - Computer Vision
  - Machine Learning
pressures:
  - name: Warming &amp; bleaching
    desc: "Rising sea temperatures make corals expel their algae and bleach — turning white, weakening, and falling prey to disease. Acidification weakens their skeletons too."
  - name: Pollution
    desc: "Runoff, sewage and debris smother corals and feed the algae that compete with them for light and space."
  - name: Overfishing
    desc: "Removing grazing fish lets algae overgrow corals, and destructive methods like blast and cyanide fishing damage reefs directly."
  - name: Coastal development
    desc: "Dredging, construction and land clearing bury reefs in sediment and nutrient-laden runoff."
  - name: Unsustainable tourism
    desc: "Anchoring, trampling and over-visiting fragile sites — and harvesting for souvenirs — wear reefs down."
  - name: Invasive species
    desc: "Non-native species outcompete or prey on reef life and reshape the habitat."
  - name: Weak governance
    desc: "Limited awareness and patchy enforcement let reef degradation continue unchecked."
status: completed
pinned: true
date: 2024-01-30
image: /images/projects/coral_reef_segmentation/cover.jpg
---

Coral reefs are among the richest ecosystems on Earth — and among the most
threatened. Marine biologists track their health by photographing the seabed on
research dives, but turning thousands of those images into numbers is slow,
painstaking work, and the reporting lag blunts conservation's ability to respond
in time.

Together with [ReefSupport](https://reef.support), we built a computer-vision
pipeline that **maps coral in benthic imagery** — outlining and classifying each
colony automatically — so researchers can measure how coral cover is growing or
declining across a protected area, far faster than by hand.

![From a dive photo to coral cover — capture, segment each colony, classify hard vs soft, and measure coral cover over time](/images/projects/coral_reef_segmentation/diagrams/pipeline.svg)
*A diver photographs the reef; the model outlines and classifies every coral
colony, and the result becomes a coral-cover figure that can be tracked over
time.*

> Our tools tap on AI and computer vision for increasing the capabilities of
> coral reef and marine monitoring in examining benthic/seabed features.
>
> <cite>– ReefSupport</cite>

## Why coral reefs matter

Reefs cover a sliver of the ocean yet underpin a huge share of marine life — and
the livelihoods of millions of people.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity hotspots</h3>
    <p class="support__card-description">Less than 1% of the seafloor, yet home to around 25% of all marine species — habitat, nursery and shelter for countless fish and invertebrates.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Coastal &amp; economic backbone</h3>
    <p class="support__card-description">Reefs sustain the fisheries and tourism that millions rely on, and act as natural breakwaters that shield coastlines from storms and erosion.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Climate, medicine &amp; culture</h3>
    <p class="support__card-description">They help cycle carbon, yield compounds with real medical promise, and hold deep cultural meaning for coastal and Indigenous communities.</p>
  </div>

</div>

## Reefs under pressure

Coral reefs are squeezed by many forces at once — most of them driven, directly
or indirectly, by people. Tap each to learn more.

{{< threats "pressures" >}}

## Mapping coral, colony by colony

The system is built around **instance segmentation**: rather than just labelling
a photo, it finds each individual coral colony, traces its exact outline, and
classifies it. We started with the key distinction — **hard versus soft coral** —
with the framework designed to grow into finer functional groups and to adapt to
reefs anywhere in the world.

![How the model maps a reef — a benthic photo runs through the segmentation model, which outlines and labels every coral colony](/images/projects/coral_reef_segmentation/diagrams/segmentation.svg)
*Instance segmentation traces the exact outline of each colony — hard coral in
teal, soft coral in orange — rather than just drawing boxes.*

The models are open source and come in a range of sizes that trade speed against
accuracy, so a survey team can pick the right balance for their hardware and
their reef.

![The open-source instance-segmentation model outlining hard and soft corals on real underwater imagery](/images/projects/coral_reef_segmentation/instance_segmentation.png)
*The open-source model segmenting hard and soft corals on real benthic imagery.*

## Why underwater vision is hard

Reading a reef from a photo is far harder than it looks — water itself works
against the camera.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Light &amp; colour loss</h3>
    <p class="support__card-description">Water absorbs and bends light, so underwater images lose contrast and colour and grow hazier the further away the subject is.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Visual noise</h3>
    <p class="support__card-description">Caustics, backscatter and drifting particles add artifacts, and busy reef backgrounds blur the line between a coral and its surroundings.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Variable &amp; scarce data</h3>
    <p class="support__card-description">Conditions shift constantly and gear isn't standardised — and well-labelled underwater datasets are rare, which makes models hard to train and to generalise.</p>
  </div>

</div>

Models are trained on reef imagery from around the world to cope with this
variety:

{{< image_carousel id="coral-reefs" items="2" >}}
  {{< carousel_image src="/images/projects/coral_reef_segmentation/reefs/reef1.jpg" alt="A coral reef sample" caption="A coral reef photographed in the field." >}}
  {{< carousel_image src="/images/projects/coral_reef_segmentation/reefs/reef2.jpg" alt="A coral reef sample" caption="A coral reef photographed in the field." >}}
  {{< carousel_image src="/images/projects/coral_reef_segmentation/reefs/reef3.jpg" alt="A coral reef sample" caption="A coral reef photographed in the field." >}}
  {{< carousel_image src="/images/projects/coral_reef_segmentation/reefs/reef4.jpg" alt="A coral reef sample" caption="A coral reef photographed in the field." >}}
{{< /image_carousel >}}
<p class="media-caption">Coral reefs photographed in different regions across the world.</p>

## Conclusion

Automated benthic analysis turns a reporting bottleneck into fast, repeatable
measurement — quantifying the long-term growth or decline of coral cover, and
giving reef managers the timely picture they need to act.

![The benthic imagery analysis system in action, by ReefSupport](/images/projects/coral_reef_segmentation/coral_ai.gif)
*The benthic imagery analysis system in action — courtesy of [ReefSupport](https://reef.support).*

{{< demo_cta >}}
