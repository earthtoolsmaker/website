---
title: Early Forest Fire Detection
summary: Democratize open and low-tech solutions for fighting wildfires, for the benefit of the ecosystems and the citizens.
clients:
  - name: Pyronear
    link: https://pyronear.org
    logo: /images/clients/pyronear/logo.png
related_posts:
  - smoke-is-a-behavior
  - racing-models-not-opinions
  - protecting-the-forest-early-forest-fire-detector
github_repo: https://github.com/earthtoolsmaker/pyronear-mlops
space: /spaces/early_forest_fire_detection/
tools:
  - Computer Vision
  - Machine Learning
  - MLOps
status: completed
pinned: true
weight: 1
date: 2026-06-12
image: /images/projects/early_forest_fire_detection/cover.jpg
stats:
  - value: "24/7"
    label: monitoring
  - value: "50"
    label: sites monitored
  - value: "500+"
    label: fires detected
---

Pyronear takes a whole-system approach to wildfire risk. At its core is an
early-detection model that runs on a compact, low-power microcomputer, fed by a
network of high-resolution cameras mounted at high vantage points for panoramic
coverage of the forest. Together they form a proactive line of defense against
wildfires — spotting smoke early and getting the alert to the people who can act
on it.

> Our detectors communicate fire alerts to a database that is connected
> to a supervision platform for the fire department.
>
> <cite>– Pyronear</cite>

![System Overview](/images/projects/early_forest_fire_detection/overview_system.svg)
*Overview of the Pyronear system to monitor forests around the clock*

The video below, filmed in the Forest of Fontainebleau, shows how the system
works end to end: a firefighter walks through the full pipeline, from the
cameras spotting the first signs of smoke to the alert reaching the fire
department.

{{< youtube id=W3DxacGsdks >}}
<br/>

## Forests Protection

Protecting forests from fire is crucial for several reasons:

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity Conservation</h3>
    <p class="support__card-description">Forests shelter countless plant and animal species. Wildfire destroys their habitats, eroding biodiversity and pushing vulnerable species toward extinction.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Carbon Sequestration</h3>
    <p class="support__card-description">Forests act as carbon sinks, pulling CO₂ from the air and locking it into trees and soil. When they burn, that stored carbon is released back into the atmosphere, accelerating climate change.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Water Resources</h3>
    <p class="support__card-description">Healthy forests regulate the water cycle — holding soil moisture, curbing erosion, and feeding rivers and streams. Fire disrupts all of it, degrading soil and harming water quality and supply.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Economic Impact</h3>
    <p class="support__card-description">Forests underpin livelihoods — timber, non-timber products, and recreation. Wildfire damages these resources and the forestry, tourism, and agriculture that depend on them, costing local communities dearly.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Human Health</h3>
    <p class="support__card-description">Wildfire smoke drifts far beyond the fire line, and its air pollution hits the vulnerable hardest — children, the elderly, and people with respiratory conditions. Stopping fires early protects public health.</p>
  </div>

</div>

Preserving forests from fire is essential — for ecological balance, a stable
climate, the livelihoods forests support, and the health of people and wildlife
alike.

## Project Scope and Objectives

Our partnership is focused on __enhancing the precision of
the early forest fire detection system__, with the goal of
minimizing false alarms to bolster confidence among
firefighters and stakeholders. Additionally, we aspire
to incorporate industry-leading methodologies for
effectively managing, deploying, and maintaining Machine
Learning Models, ensuring optimal performance and
reliability over time.

![Overview 360](/images/projects/early_forest_fire_detection/overview_360.svg)
*Overview of the camera system that can cover 360 degrees angle*

Our work is centered on enhancing the core of the Pyronear system, which
analyzes real-time images from cameras mounted on tower antennas.

![Overview ML Model](/images/projects/early_forest_fire_detection/overview_ai_model.svg)
*Overview of the embedded ML system*

### Setting up the Pyronear system

In this section, we detail the setup of the Pyronear system in Fontainebleau
before the summer of 2024. This pilot project, initiated by the fire
department, aims to evaluate Pyronear's effectiveness in detecting early forest
fires.

By placing cameras on top of tower antennas, the system can monitor the
surrounding forest over a long range, detecting fires from tens of kilometers
away.

The image below shows the antenna where the Pyronear system is installed.

{{< gallery caption="Setting up the system on the antenna tower" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/tower_antenna_1.jpg" alt="Tower antenna setup 1" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/tower_antenna_3.jpg" alt="Tower antenna setup 2" >}}
{{< /gallery >}}

Two cameras are mounted on top of the antenna tower, providing 360-degree
coverage of the area. These cameras can be programmed to capture images at
specific angles.

{{< gallery caption="Covering 360 degrees with two Reolink RLC-823A 16X cameras" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_1.jpg" alt="Reolink camera 1" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_2.jpg" alt="Reolink camera 2" >}}
{{< /gallery >}}

The map below illustrates how the chosen set of angles enables complete
360-degree coverage.

![Cameras range](/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_range.png)
*Range covered by the two cameras by taking pictures at different angles*

From the top of the antenna, the forest can be observed over a vast distance,
allowing a single Pyronear system to effectively monitor and protect a large
area. In practice, antennas are often positioned on hills, enabling the
detection of forest fires from 30 to 60 kilometers away.

{{< gallery caption="Forest views from the antenna tower" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/view_1.jpg" alt="Forest view 1" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/view_2.jpg" alt="Forest view 2" >}}
{{< /gallery >}}

Shown below is the installed Pyronear system, housed in a secure enclosure. The
Pyronear team developed a plug-and-play setup featuring a central processing
unit built around a Raspberry Pi, connected to four cameras that provide
360-degree coverage. This system processes images continuously, around the
clock.

![A Raspberry Pi board next to a credit card of the same size](/images/projects/early_forest_fire_detection/raspberry_pi_credit_card.svg)
*The brain of the whole system is no bigger than a credit card.*

{{< gallery caption="Pyronear hardware system case - Raspberry Pi, power chords, RJ45, and SIM card" >}}
  {{< gallery_image src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/pyronear_hardware.jpg" alt="Pyronear hardware system" >}}
{{< /gallery >}}

The computer vision model detected a forest fire in Fontainebleau from a
distance of 35 kilometers in real time, setting a new record for the Pyronear
system. The video below shows a thin black smoke rising in the distance.

{{< youtube id=i9Qy-zY16Ew >}}
<br/>

## Telling smoke from look-alikes

A single frame can only tell you so much. Early wildfire smoke is a faint grey
wisp — easy to confuse with a passing cloud, a bank of fog, or kicked-up dust —
and every false alarm that reaches a fire crew chips away at their trust in the
system.

So we taught the system to look at *how a candidate behaves over time*. Real
smoke does things a cloud doesn't: it stays anchored to one spot on the
hillside, grows, and slowly drifts. To make that easy to read, the system locks
onto the candidate and holds the view steady — so the background sits still and
the smoke becomes the one thing that moves.

![The same hillside across twenty frames; with the view held steady, a faint plume grows and drifts while everything around it stays put](/images/projects/early_forest_fire_detection/temporal_patches.jpg#noround)
*The same candidate across twenty frames. Hold the view steady and real smoke
gives itself away — it's the one thing that grows and drifts.*

That extra, time-aware look cuts false alarms by around **4×** while still
catching the real fires — a far cleaner stream of alerts for the people acting
on them. If you want the full story, we wrote up [how we built and raced the
candidate models]({{< ref "/posts/racing-models-not-opinions" >}}) and [how the
model reads smoke over time]({{< ref "/posts/smoke-is-a-behavior" >}}).

## Conclusion

A computer vision model that catches the first signs of forest fire is a
practical, low-cost way to protect them. It gets firefighters to the scene
sooner — and as climate change leaves forests increasingly exposed, that head
start matters more every year.

{{< demo_cta >}}
