---
title: Scaling the EarthRanger Platform
summary: A backend engineering mission with the EarthRanger team at Ai2, separating read and write query paths, partitioning the database, and speeding up the APIs that power real-time conservation across 900+ protected areas.
tags: ["infrastructure", "engineering"]
related_projects:
  - wadden_sea_seal_monitoring
  - monitoring_smolt_salmon_migration_with_sonar
  - early_forest_fire_detection
tagline: Backend engineering with the EarthRanger team, so the platform behind 900+ protected areas stays fast as it grows.
stats:
  - value: "900+"
    label: conservation sites
  - value: "80+"
    label: countries
  - value: "23K"
    label: animals tracked
clients:
  - name: EarthRanger
    link: https://www.earthranger.com/
    logo: /images/clients/earthranger/logo.png
  - name: Ai2
    link: https://allenai.org/
    logo: /images/clients/ai2/logo.png
tools:
  - Backend Engineering
  - PostgreSQL
  - Cloud Infrastructure
  - API Design
challenges:
  - name: Always-on ingestion
    desc: "Collars, sensors and radios never stop reporting. The database takes a constant stream of writes, day and night, from every time zone at once."
  - name: Reads against writes
    desc: "Every dashboard, map refresh and report is a read query landing on the same database that is busy ingesting live field data."
  - name: Ever-growing history
    desc: "Years of observations and tracking points pile into enormous tables, and every query gets a little slower as they grow."
  - name: Latency in the field
    desc: "When a ranger team responds to an alert, a slow API is not an inconvenience, it is time lost on the ground."
  - name: Growth without headroom
    desc: "Every newly onboarded protected area adds users, devices and data to infrastructure that has to keep feeling instant."
status: completed
date: 2024-09-01
weight: 4
pinned: true
image: /images/projects/earthranger_platform_scaling/cover.jpg
---

In hundreds of protected areas around the world, the day starts the same way:
someone opens [EarthRanger](https://www.earthranger.com/) and looks at the map.
Where are the collared elephants? Which patrols are out? What happened
overnight? EarthRanger is the operations platform behind that map, built and
maintained by the team at [Ai2](https://allenai.org/), the Allen Institute for
AI. In 2024, we joined its engineering team for a scaling mission: help the
backend and its database keep up with a platform that protects more parks,
more wildlife and more data every year.

{{< image_carousel id="earthranger-intro" items="2" >}}
  {{< carousel_image src="/images/projects/earthranger_platform_scaling/ops-room.jpg" alt="An EarthRanger operations room with live maps on wall screens" caption="An EarthRanger operations room. Live maps show tracked wildlife, ranger patrols and field reports in real time. Photo courtesy of EarthRanger." >}}
  {{< carousel_image src="/images/projects/earthranger_platform_scaling/leopard.jpg" alt="A leopard resting in a tree" caption="EarthRanger supports the people protecting wildlife across more than 900 conservation sites in over 80 countries. Photo courtesy of EarthRanger." >}}
{{< /image_carousel >}}

## What EarthRanger does

EarthRanger began with a crisis. The 2016 Great Elephant Census revealed that
Africa's savanna elephant population had fallen by 30% in just seven years, and
the teams on the ground had no shared picture of what was happening in their own
landscapes. Conceived by Vulcan together with Save the Elephants, and a program
of Ai2 since 2021, EarthRanger set out to give protected areas what a modern
operations room gives a city: every asset, every alert, every decision on one
screen.

Today it is one of the most widely used conservation platforms in the world,
free for the people using it, deployed at **900+ conservation sites** in over
**80 countries**, tracking some **23,000 animals** by GPS:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">One live map</h3>
    <p class="support__card-description">Wildlife, rangers, vehicles and sensors appear together in real time, giving managers a single operational picture of their protected area.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Wildlife tracking</h3>
    <p class="support__card-description">GPS collars and tags stream in the positions of elephants, rhinos, lions and dozens of other species, around the clock.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Ranger operations</h3>
    <p class="support__card-description">Patrols, incident reports and alerts flow through the platform, so teams can be dispatched to where they are needed most.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">150+ integrations</h3>
    <p class="support__card-description">Camera traps, acoustic sensors, radios, satellite feeds and field apps all plug in, turning scattered devices into one data stream.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">From data to decisions</h3>
    <p class="support__card-description">Dashboards, reports and analysis tools turn raw field data into the evidence behind anti-poaching, wildlife research and park management.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Free and open</h3>
    <p class="support__card-description">EarthRanger is free for conservationists, which is why its reach keeps growing, from national parks to community conservancies.</p>
  </div>

</div>

## The scaling challenge

Success created its own engineering problem. A platform serving 900+ sites in
real time is, underneath the map, a torrent of database traffic: every collar
ping is a write, every dashboard a burst of reads, and both keep growing with
every animal collared and every park onboarded. Tap each challenge to see why
scaling it is hard.

{{< threats "challenges" >}}

## Our mission

We worked inside EarthRanger's backend alongside the Ai2 engineering team, on
three fronts:

<div class="services__list">
  <div class="services__item">
    <span class="services__number" aria-hidden="true">01</span>
    <h4 class="services__item-title">Separate reads from writes</h4>
    <p class="services__item-description">Route the two kinds of traffic down different paths, so heavy dashboard and analysis queries never compete with live field data being written.</p>
  </div>
  <div class="services__item">
    <span class="services__number" aria-hidden="true">02</span>
    <h4 class="services__item-title">Partition the database</h4>
    <p class="services__item-description">Split the platform's largest tables into partitions, so each query touches only the slice of data it actually needs.</p>
  </div>
  <div class="services__item">
    <span class="services__number" aria-hidden="true">03</span>
    <h4 class="services__item-title">Speed up the API</h4>
    <p class="services__item-description">Profile the busiest endpoints and improve their latency and throughput, for faster maps, dashboards and integrations.</p>
  </div>
</div>

Put together, the work reshapes how a request travels through the platform:

![How the scaled backend works: field data streams in, reads and writes travel separate paths, and queries touch only the partition they need](/images/projects/earthranger_platform_scaling/diagrams/architecture.svg)
*Field devices and dashboards generate constant traffic; writes and reads are
routed down separate paths, and partitioned tables keep every query touching
only the data it needs.*

**Separating reads from writes** matters because the two workloads behave so
differently. Writes are small, constant and non-negotiable: a collar reports
where an animal is right now, and that position must land in the database.
Reads are bursty and heavy: a manager opens a dashboard and the platform
assembles months of history in one go. On a single path, the second kind of
traffic gets in the way of the first. Once each travels its own path, a heavy
report can never slow down live tracking.

**Partitioning** attacks the other axis of growth. EarthRanger's history is its
scientific value, years of positions, patrols and events, but in database terms
that history is a handful of tables growing without limit. Splitting them into
partitions means a query about last week reads last week's slice, not half a
decade of records, and the platform's performance stops degrading as its
archive deepens.

**API performance** is where users feel all of it. We profiled the endpoints
that maps, dashboards and integrations hit hardest and reworked the slowest
query patterns, lowering latency and raising the throughput the platform can
sustain at peak.

## The impact

The result is headroom. Faster maps and dashboards for the people using
EarthRanger in the field, where response time is measured against a moving
threat. A database that stays fast as its history grows instead of slowing
with age. And a backend that can keep welcoming new parks, conservancies and
partners without performance being the price of growth, so the platform's reach
can keep expanding to the places that need it.
