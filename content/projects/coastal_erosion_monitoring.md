---
title: Coastal Erosion and Land Cover Monitoring
summary: Drone-based monitoring of coastal erosion, sedimentation and land cover change on the Wadden Sea coast, served through an interactive web portal.
tags: ["aquatic", "marine", "vision"]
related_projects:
  - wadden_sea_seal_monitoring
tagline: Tracking how the Wadden coast at Wierum erodes, builds up and greens over, from drone surveys to an interactive map.
stats:
  - value: "6"
    label: drone flights
  - value: "2+"
    label: years of monitoring
  - value: "cm"
    label: elevation change precision
clients:
  - name: Rijkswaterstaat
    link: https://www.rijkswaterstaat.nl/en
    logo: /images/clients/rijkswaterstaat/logo.svg
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
space: https://app.codaportal.org
tools:
  - Computer Vision
  - Machine Learning
  - Geospatial Analysis
challenges:
  - name: A coastline in motion
    desc: "The marsh edge shifts with every storm, tide and season. A single survey is a snapshot; understanding the trend takes repeated, comparable measurements over years."
  - name: Subtle, slow change
    desc: "Erosion and sedimentation often amount to a few centimetres of elevation change per year, invisible to the eye but decisive for how the coast evolves."
  - name: Hard-to-reach terrain
    desc: "Tidal flats and salt marshes are only accessible in narrow tide windows, and walking surveys across soft mud are slow, exhausting and risky."
  - name: Gigapixel imagery
    desc: "Each drone flight produces an orthophoto with billions of pixels. Mapping vegetation, mud and sand by hand at that scale is simply not feasible."
  - name: Consistency across surveys
    desc: "Comparing flights only works if every survey is classified the same way, regardless of season, lighting or water level."
status: completed
date: 2026-09-01
pinned: true
image: /images/projects/coastal_erosion_monitoring/cover.jpg
---

Near the village of Wierum, on the Frisian coast of the Wadden Sea, a salt
marsh meets the open tidal flats. Whether that marsh edge grows seaward or
retreats tells coastal managers a great deal: salt marshes damp incoming waves,
trap sediment and form a natural first line of defence in front of the dikes
that keep the land behind them dry.

Together with [Rijkswaterstaat](https://www.rijkswaterstaat.nl/en) and
[Lumax AI](https://lumax.ai/), we built **CODAP**, the Coastal Data Portal:
an end-to-end monitoring pipeline that turns repeated drone surveys of this
coast into maps of land cover and elevation change, and serves them on an
[interactive web portal](https://app.codaportal.org) anyone can explore in a
browser.

{{< image_carousel id="codap-portal-intro" >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/site-overview.png" alt="The CODAP portal showing the Wierum site with land cover predictions over a drone orthophoto" caption="The monitoring site at Wierum in the portal. AI land cover predictions are draped over the drone orthophoto, with the survey boundary in yellow and the class legend on the right." >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/landcover-detail.png" alt="Zoomed view of land cover predictions along the marsh edge, with a tooltip identifying dike vegetation" caption="Zooming in on the marsh edge. Hovering any spot reveals what the model sees there, here the grassy face of the sea dike." >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/erosion-ddem.png" alt="Elevation change map of the Wierum site between January 2024 and March 2026" caption="The Erosion tab distils two years of change into one map: blue where sediment builds up, red where the coast is eroding." >}}
{{< /image_carousel >}}

## Why this coastline matters

The Wadden Sea, a UNESCO World Heritage Site, is the largest unbroken system
of intertidal sand and mud flats in the world. Its edges are working
landscapes as much as natural ones.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Natural coastal defence</h3>
    <p class="support__card-description">Salt marshes absorb wave energy and trap sediment, sheltering the dikes behind them. A healthy, growing marsh is cheaper and more resilient than concrete.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Rising seas</h3>
    <p class="support__card-description">Whether marshes and mudflats can keep pace with sea level rise depends on their sediment budget. Only long-term measurement shows which way the balance tips.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">A living habitat</h3>
    <p class="support__card-description">Mudflats and marshes feed millions of migratory birds and act as a nursery for fish. Tracking their extent tracks the health of the whole ecosystem.</p>
  </div>

</div>

## The monitoring challenge

Watching a coastline change sounds simple. Doing it rigorously is not. Tap
each challenge to see why.

{{< threats "challenges" >}}

## From drone flights to a living map

![From a drone survey to a change map: fly, map, classify, compare](/images/projects/coastal_erosion_monitoring/overview_system.svg)

Every few months, a drone surveys the site and the imagery is processed into
two precise products: an **orthophoto**, a distortion-free aerial image of the
whole site, and a **digital elevation model** that records the height of every
point on the marsh and flats.

A **semantic segmentation model** then classifies the orthophoto pixel by
pixel into coastal land cover types such as intertidal mud, salt marsh
vegetation, macro algae, shells and the built surfaces of the sea dike,
following a 16-class annotation scheme designed with coastal ecologists. The
predictions, orthophotos and elevation data are published as map tiles that
the [CODAP portal](https://app.codaportal.org) streams straight to the
browser. No GIS software needed, just a link.

## Comparing surveys through time

The heart of the portal is comparison. A timeline slider picks any two
flights, and three view modes make the differences jump out: a **swipe**
handle you drag across the map to reveal one date beneath the other, a
side-by-side **split** view that pans and zooms in sync, and a **single**
mode for studying one survey in depth.

{{< image_carousel id="codap-portal-compare" >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/overlay-compare.png" alt="Swipe comparison of the Wierum marsh edge between January 2024 and March 2026" caption="Dragging the swipe handle across the marsh edge, January 2024 against March 2026. Two winters apart, the vegetated fringe below the dike visibly changes shape." >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/split-compare.png" alt="Split-screen comparison of two drone surveys of the same stretch of coast" caption="Split view, the same stretch of coast on two dates, panning and zooming in lockstep. The timeline slider below selects any pair of flights." >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/landcover-winter.png" alt="Single mode showing the bare winter mudflat of the January 2024 baseline flight" caption="Single mode on the January 2024 baseline: the same marsh edge in the depth of winter, bare mud where the summer surveys show green." >}}
{{< /image_carousel >}}

## Measuring erosion, centimetre by centimetre

Land cover tells you what the surface is; elevation tells you where it is
going. By differencing the elevation models of two flights, the portal
computes a **change map** of the entire site: blue where sediment has
accumulated, red where the surface has eroded, at centimetre resolution.

{{< image_carousel id="codap-portal-erosion" items="1" items_tablet="1" >}}
  {{< carousel_image src="/images/projects/coastal_erosion_monitoring/portal/erosion-ddem.png" alt="Elevation change map of the Wierum site between January 2024 and March 2026" caption="Two years of elevation change in one image. Blue marks sediment building up on the flats; the red scar along the marsh edge is erosion, exactly where the coastline is retreating." >}}
{{< /image_carousel >}}

Patterns that would take years of ground surveys to establish become visible
at a glance: the flats in front of Wierum are accreting while a narrow band
along the marsh edge erodes, the kind of insight that directly informs where
protection or restoration effort should go.

## The impact

CODAP turns coastal monitoring from an occasional, labour-intensive campaign
into a routine: fly, process, publish, compare. Every survey lands in the
same portal, classified the same way, comparable with every survey before it.
Coastal managers at Rijkswaterstaat can watch the marsh edge evolve at
centimetre precision without leaving their desk, and the same pipeline is
ready to take on new sites along the coast.

<div class="about-cta demo-cta">
  <h3 class="about-cta__title">Explore the live portal</h3>
  <p class="about-cta__description">The CODAP portal is public. Pick a flight, drag the swipe handle, and watch two years of coastal change unfold in your browser.</p>
  <a href="https://app.codaportal.org" target="_blank" rel="noopener noreferrer" class="link-no-decoration button button--middle"><i class="fa-solid fa-circle-play"></i>&nbsp;Open the portal</a>
</div>
