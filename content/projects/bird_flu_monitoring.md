---
title: Bird Flu Monitoring
summary: Utilize drones for precise monitoring of breeding seabird colonies by detection of live and dead adults and chicks to determine survival and reproduction and asses the impact of avian influenza.
tags: ["vision"]
related_projects:
  - wadden_sea_seal_monitoring
  - wild_salmon_migration_monitoring
related_spaces:
  - /demos/seal_identification/
tagline: Counting every bird in a seabird colony — alive or lost — from a drone overhead, to measure avian flu's toll without setting foot inside.
stats:
  - value: "Aerial"
    label: drone survey
  - value: "Adults & chicks"
    label: counted apart
  - value: "Non-invasive"
    label: no colony disturbance
clients:
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
tools:
  - Computer Vision
  - Machine Learning
  - Photogrammetry
  - Drones
impacts:
  - name: Mortality
    desc: "Infected birds sicken and die — and in a densely packed colony, losses can climb fast."
  - name: Breeding disruption
    desc: "Sick adults abandon nests or stop feeding their young, so few chicks make it through the season."
  - name: Spread to chicks
    desc: "Adults pass the virus to their offspring, putting the colony's next generation at risk."
  - name: Population decline
    desc: "Where highly pathogenic strains take hold, a colony can shrink year after year."
  - name: Ecological ripple
    desc: "Colonies anchor food webs and nutrient cycling, so their collapse reaches far beyond the birds."
status: fundraising
date: 2024-06-23
image: /images/projects/bird_flu_monitoring/cover.png
---

Many seabirds breed in dense colonies on low-lying sandbanks, beaches and
isolated islands — out of reach of ground predators, but increasingly exposed to
erosion, flooding and a fast-moving new threat: **avian influenza**. To protect
these colonies, conservationists need accurate, up-to-date counts of how many
birds are there, and how they are faring. That has always been hard to do
without disturbing the very birds you are trying to count.

Together with [Lumax AI](https://lumax.ai/), we're building a system that surveys
an entire colony **from the air** and turns the imagery into numbers — counting
live and dead adults and chicks to track survival, reproduction, and the toll of
bird flu, all without setting foot among the birds.

## The monitoring challenge

Seabird colonies are some of the hardest places in conservation to get good
numbers from — and bird flu raises the stakes.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Remote &amp; fragile sites</h3>
    <p class="support__card-description">Colonies cluster on low-lying sandbanks and islands that rising seas increasingly erode and flood — remote, exposed, and easily damaged.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Counting harms them</h3>
    <p class="support__card-description">Walking a colony to count by hand disturbs nesting birds, risks trampling eggs, and is slow, dangerous and rarely complete.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Flu moves fast</h3>
    <p class="support__card-description">A highly pathogenic outbreak can tear through a colony in days, so counts have to be quick, repeatable and safe to gather often.</p>
  </div>

</div>

## How bird flu hits a colony

Avian influenza is a viral infection of birds that ranges from mild to highly
contagious and deadly. When a severe strain reaches a breeding colony, the
damage compounds. Tap each to learn more.

{{< threats "impacts" >}}

## How we monitor it

Rather than send people in, we send a drone over the top.

![How it works — a drone surveys the colony, its photos are stitched into one map, a model counts live and dead adults and chicks, and the totals reveal the colony's health](/images/projects/bird_flu_monitoring/diagrams/pipeline.svg)
*A drone flies the colony, its overlapping photos are stitched into a single
high-resolution map, a computer-vision model finds and classifies every bird,
and the totals reveal how the colony is faring.*

Flying a fixed grid, the drone captures hundreds of overlapping photos that are
stitched into one high-resolution **orthomosaic** of the colony. A computer-vision
model then finds and classifies every bird — **live or dead, adult or chick** —
and the totals reveal both how many birds the colony holds and where an outbreak
is biting hardest. Because a survey is fast and disturbs nothing, it can be
repeated as often as needed to watch a colony through the breeding season.

## Conclusion

Managing bird flu in wild populations relies on surveillance and early detection,
followed by measures like quarantine, vaccination where it's feasible, and
occasionally culling to slow the spread. None of it works without good data.
Fast, repeatable, non-invasive counts give conservationists the early warning and
the population picture they need to act — and to understand how avian influenza
moves through wild colonies over time.
