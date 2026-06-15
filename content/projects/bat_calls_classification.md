---
title: "Tropical Bat Call Detection and Classification"
summary: Transforming bat population monitoring in Cambodia through advanced bio-acoustic analysis driven by Machine Learning algorithms.
tagline: Teaching machines to recognise bats by their calls — so citizen scientists across Cambodia can map species no one has counted.
stats:
  - value: "70+"
    label: species recorded
  - value: "5"
    label: new to science
  - value: "Citizen-science"
    label: powered
clients: 
  - name: Citibats Cambodia
    link: https://www.inaturalist.org/projects/citibats-cambodia
    logo: /images/clients/citibats_cambodia/logo.png
# github_repo: https://gitlab.com/fruitpunch/projects/ai-for-coral-reefs-2/supervised-learning/yolov8
tools:
  - Machine Learning
  - Bio Acoustics
pressures:
  - name: Habitat loss
    desc: "Rapidly disappearing roosts and foraging grounds shrink the spaces bats need to feed, breed and shelter."
  - name: Pesticides
    desc: "Heavy pesticide use poisons the insects bats feed on — and the bats themselves."
  - name: Hunting &amp; trade
    desc: "Bats are taken for the illegal bushmeat and traditional-medicine trades, thinning already fragile populations."
  - name: Knowledge gap
    desc: "With so little research published, species can decline — or vanish — before they are ever documented."
status: fundraising
date: 2024-04-23
image: /images/projects/bat_calls_classification/cover.png
---

Bats are a familiar sight across Cambodia — colonies of fruit bats such as
**Lyle's flying fox**, one of 31 species endemic to southeast Asia, roost in the
trees of pagodas and national monuments. Cambodia is even the only country in the
world with a living tradition of bat-guano cultivation. Yet for all their
visibility, bats are among the country's least-studied animals — and that gap in
knowledge makes them hard to protect.

## Why bats matter

As pollinators, seed-dispersers and pest-controllers, bats quietly keep tropical
ecosystems — and the farms that depend on them — running.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Pest control</h3>
    <p class="support__card-description">A single colony devours vast numbers of insects every night, protecting rice and other crops — naturally, without pesticides.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Seed dispersal</h3>
    <p class="support__card-description">Fruit bats carry seeds far across the landscape as they forage, helping regenerate forests and the fruit trees people rely on.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Pollination</h3>
    <p class="support__card-description">Many tropical plants — including valuable fruit trees — depend on bats to pollinate their night-blooming flowers.</p>
  </div>

</div>

## Under pressure

Cambodia's bats face mounting pressure, and a shortage of data leaves them
especially exposed. Tap each to learn more.

{{< threats "pressures" >}}

## Hidden diversity

Just ten years ago, only 30 bat species were recorded in Cambodia — against more
than 100 each in neighbouring Thailand and Vietnam. Today the count is over
**70**, five of them new to science. One, the Hayes' thick-thumbed myotis, was
identified only recently after being caught in the heart of Phnom Penh.

> What more is waiting to be found?
>
> <cite>– Cambodian Urban Bat Project</cite>

## From a call to a species

The **Cambodian Urban Bat Project** puts that question to citizen scientists.
Volunteers walk and ride transects through a diversity of urban spaces — and run
stationary recordings in the hotspots their surveys reveal — capturing the
ultrasonic calls bats use to navigate in the dark.

![How it works — a bat's ultrasonic call is recorded in the field, rendered as a spectrogram, then classified to species by a machine-learning model](/images/projects/bat_calls_classification/diagrams/pipeline.svg)
*Each recording is turned into a spectrogram — a picture of sound — and a model
reads that picture to identify the species behind the call.*

Together with **Citibats Cambodia**, we're building bioacoustics tools that turn
those recordings into species. The model lets researchers classify the huge
volume of calls the community gathers, and share
the results openly on
[iNaturalist](https://www.inaturalist.org/projects/citibats-cambodia) for further
research by anyone, anywhere.

It's a blueprint for community-powered conservation: low-cost recorders,
volunteer effort and open data adding up to a clearer picture of Cambodia's
bats — and a faster route to protecting them.
