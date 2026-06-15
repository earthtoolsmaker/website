---
title: Wadden Sea Seal Monitoring
summary: Automated seal population monitoring system using AI to count, classify, and identify individual seals from aerial imagery in the Wadden Sea.
tagline: Counting, classifying and recognising individual seals from aerial surveys of the Wadden Sea.
stats:
  - value: "2"
    label: seal species
  - value: "5"
    label: attributes per seal
  - value: "90%"
    label: less manual work
clients:
  - name: Wageningen Marine Research
    link: https://www.wur.nl/en/Research-Results/Research-Institutes/marine-research.htm
    logo: /images/clients/wageningen-marine-research/logo.png
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
space: /demos/seal_identification/
tools:
  - Computer Vision
  - Machine Learning
  - Deep Learning
challenges:
  - name: Labour-intensive
    desc: "Counting and classifying thousands of seals across aerial photos takes hundreds of researcher-hours every survey season."
  - name: Five attributes at once
    desc: "Each seal has to be recorded by species, life stage, position, vitality and sex — all at the same time."
  - name: Breeding-season counts
    desc: "Accurate pup counts and sex ratios during the breeding season are vital for population health, yet hard to get by hand."
  - name: Variable imagery
    desc: "Aerial photos vary in lighting, angle, resolution and seal density, demanding expert judgement for every call."
  - name: Tracking individuals
    desc: "Understanding movement and site fidelity needs a way to recognise individual seals — without tagging them."
  - name: Consistency over years
    desc: "Keeping counting standards stable across seasons and different observers is hard without automation."
status: completed
date: 2025-11-24
pinned: true
image: /images/projects/wadden_sea_seal_monitoring/cover.jpg
---

The Wadden Sea — a UNESCO World Heritage Site spanning the Dutch, German and
Danish coasts — is one of Europe's most important nurseries for grey seals and
harbour seals. To track the health of those colonies, researchers at
[Wageningen Marine Research](https://www.wur.nl/en/Research-Results/Research-Institutes/marine-research.htm)
photograph them from light aircraft several times a year, building a record of
population size, age structure and breeding success.

But turning those photos into numbers has meant hundreds of hours of painstaking
work — counting and classifying every seal by hand. Together with Wageningen
Marine Research and [Lumax AI](https://lumax.ai/), we built an AI system that
does it automatically: it **detects, counts and classifies** every seal in an
aerial image, and even **recognises individuals** by their natural markings —
freeing researchers to spend their time on the science.

{{< image_carousel id="wadden-sea-intro" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/wadden-sea.jpg" alt="Aerial view of the Wadden Sea" caption="The Wadden Sea, a UNESCO World Heritage Site, features extensive tidal flats and sandbanks that serve as critical haul-out sites for seal colonies." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/cover.jpg" alt="Seals on a sandbank in the Wadden Sea" caption="Grey seals and harbour seals hauled out on a sandbank in the Wadden Sea, the focus of our automated monitoring system." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/wadden-sea-map.png" alt="Map of the Wadden Sea" caption="The Wadden Sea stretches along the coasts of the Netherlands, Germany, and Denmark." >}}
{{< /image_carousel >}}

From a survey flight to a validated count, the system runs in four steps:

![From an aerial survey to a seal census — detect every seal, classify it five ways, and review the counts](/images/projects/wadden_sea_seal_monitoring/diagrams/pipeline.svg)
*Aircraft photograph the colony; a model finds every seal, classifies each one
five ways, and the counts are reviewed and exported in a web app.*

## Why seals matter

Seals sit near the top of the Wadden Sea food web, which makes them a sensitive
barometer for the health of the whole ecosystem.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Apex predators</h3>
    <p class="support__card-description">As top predators they help keep fish populations and the wider marine food web in balance.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Health indicators</h3>
    <p class="support__card-description">Their numbers rise and fall with prey availability and water quality, so population trends reveal the state of the whole ecosystem.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity &amp; heritage</h3>
    <p class="support__card-description">Iconic animals of this World Heritage Site, seals support eco-tourism, and long-term monitoring tracks how climate change is reshaping coastal life.</p>
  </div>

</div>

## The monitoring challenge

Doing this well, by hand, is genuinely hard. Tap each challenge to see why.

{{< threats "challenges" >}}

## Two systems working together

Two AI systems work side by side, across both grey seals (*Halichoerus grypus*)
and harbour seals (*Phoca vitulina*): one **counts and classifies** every seal
in a photo, the other **recognises individuals** over time. Both feed a single
web app where researchers check the AI's work and export validated data.

## Counting and classifying every seal

The first system starts with a **detector** that finds every seal in an aerial
photo — even animals that are partly submerged, overlapping, or caught in
awkward light. It then classifies each one five different ways:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Species</h3>
    <p class="support__card-description">Grey or harbour seal — told apart by size, head shape and coat. Grey seals are larger with longer snouts; harbour seals are rounder and spotted.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Life stage</h3>
    <p class="support__card-description">Adult or pup. Pup counts during the breeding season drive birth-rate and population-growth estimates.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Location</h3>
    <p class="support__card-description">Hauled out on land or swimming in the water — a window into habitat use and behaviour.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Vitality</h3>
    <p class="support__card-description">Alive or dead, so mortality can be monitored — especially important through the breeding season.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Sex</h3>
    <p class="support__card-description">Male or female, where it can be told — feeding the sex ratios that inform breeding biology and population structure.</p>
  </div>

</div>

Every prediction lands in a web app that keeps researchers firmly in control:
detected seals are drawn with colour-coded labels for all five attributes,
uncertain cases are flagged for a closer look, any label can be fixed (or a
missed seal added) in one click, and the validated counts export straight to a
spreadsheet.

{{< image_carousel id="webapp-review" items="2" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-screen-2.png" alt="Web Application Review Interface" caption="Researchers review and validate AI predictions through an intuitive web interface." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-screen-3.png" alt="Web Application Review Interface" caption="Every detection can be checked, corrected, and confirmed before the counts are exported." >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/seals/webapp-detour-screen-2.png" alt="Web Application Review detouring tools" caption="Tools for adjusting AI predictions and adding any seals the model missed." >}}
{{< /image_carousel >}}

## Recognising individual seals

Tracking individual animals usually means tagging them — capture, handling,
stress for the seal and logistics for the team. Our second system avoids all of
that. Seals carry **stable, distinctive markings** — whisker spots, coat
patterns, facial features — that stay with them for life, so the AI can
recognise an individual from a photo alone, the way facial recognition works for
people.

![How seal re-identification works — a face becomes a unique fingerprint that is matched against a database of known individuals](/images/projects/wadden_sea_seal_monitoring/diagrams/reid.svg)
*The model turns each seal's face into a compact "fingerprint", then compares it
against a database of known individuals to find the best match.*

When a new photo comes in, the model condenses the seal's face into that
fingerprint and compares it with every seal already on file, returning the
closest matches for a researcher to confirm — or registering a brand-new
individual. The matches below were all made this way, from natural markings
alone:

{{< image_carousel id="seal-reid-matches" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_different_seasons.png" alt="Same seal photographed in different seasons" caption="The same individual seal, re-identified across different survey seasons." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_whisker_patterns.png" alt="Matching whisker patterns between sightings" caption="A match made on unique whisker-spot patterns, which stay stable for life." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_spot_patterns.png" alt="Matching spot patterns between sightings" caption="Distinctive coat spots provide reliable identification markers across photos." shadow="false" rounded="false" >}}
  {{< carousel_image src="/images/projects/wadden_sea_seal_monitoring/reid/match_facial_patterns.png" alt="Matching facial patterns between sightings" caption="Facial features — head shape and markings — identify the same individual." shadow="false" rounded="false" >}}
{{< /image_carousel >}}

Recognising individuals over time turns a population count into a living record:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Site fidelity &amp; movement</h3>
    <p class="support__card-description">Which seals return to the same haul-out year after year, and how individuals move across the Wadden Sea between seasons.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Survival &amp; reproduction</h3>
    <p class="support__card-description">Re-sightings across years yield survival rates, and following individual females reveals their pupping success over time.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Colony dynamics</h3>
    <p class="support__card-description">Immigration, emigration and social structure within breeding colonies come into focus once individuals can be told apart.</p>
  </div>

</div>

## The impact

The system has reshaped the work at Wageningen Marine Research. Analysis that
once took hundreds of hours now takes a fraction of the time, and the counts are
more consistent from one survey year to the next. Researchers can focus on
biology and conservation strategy instead of data entry — and the
re-identification system opens an entirely new, individual-level view of seal
life that simply wasn't possible before. The same framework can extend to other
colonies, regions, or marine-mammal species.

## Try the seal re-identification system

Upload images of seal faces and watch the model extract their features and match
individuals — right in your browser:

{{< demo_cta >}}
