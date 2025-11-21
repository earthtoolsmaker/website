---
title: Early Forest Fire Detection
summary: Democratize open and low-tech solutions for fighting wildfires, for the benefit of the ecosystems and the citizens.
clients:
  - name: Pyronear
    link: https://pyronear.org
    logo: /images/clients/pyronear/logo.png
related_posts:
  - protecting-the-forest-early-forest-fire-detector
github_repo: https://github.com/earthtoolsmaker/pyronear-mlops
space: /spaces/early_forest_fire_detection/
tools:
  - Computer Vision
  - Machine Learning
  - MLOps
status: completed
pinned: true
date: 2024-04-23
image: /images/projects/early_forest_fire_detection/cover.png
---

## Context

Pyronear offers a holistic solution for managing fire risks. Central to its
capabilities is an innovative early wildfire detection algorithm, seamlessly
operated on a compact microcomputer. This core system is augmented by a network
of high-resolution cameras strategically positioned at elevated vantage points,
providing panoramic coverage of forested regions. Together, these components
form a resilient and proactive strategy for wildfire prevention and management.

> Our detectors communicate fire alerts to a database that is connected
> to a supervision platform for the fire department.
>
> <cite>– Pyronear</cite>

![System Overview](/images/projects/early_forest_fire_detection/overview_system.png)
*Overview of the Pyronear system to monitor forests around the clock*

## Forests Protection

Protecting forests from fire is crucial for several reasons:

- __Biodiversity Conservation:__ Forests are home to a
vast array of plant and animal species. Wildfires can
devastate habitats, leading to the loss of biodiversity
and potentially driving species to extinction.
- __Carbon Sequestration:__ Forests act as carbon sinks,
absorbing carbon dioxide from the atmosphere and storing
it in trees and soil. When forests burn, this stored
carbon is released back into the atmosphere,
exacerbating climate change.
- __Water Resources:__ Healthy forests play a critical
role in regulating water cycles. They help maintain soil
moisture, reduce erosion, and sustain the flow of rivers
and streams. Wildfires can disrupt these processes,
leading to soil degradation and affecting water quality
and availability.
- __Economic Impact:__ Forests provide various ecosystem
services, including timber, non-timber forest products,
and recreational opportunities. Wildfires can damage
these resources, impacting industries such as forestry,
tourism, and agriculture, leading to economic losses for
communities.
- __Human Health:__ Wildfires produce smoke and air
pollution, which can pose significant health risks,
especially to vulnerable populations such as children,
the elderly, and individuals with respiratory
conditions. Protecting forests from fire helps safeguard
public health and well-being.

Overall, preserving forests from fire is essential for
maintaining ecological balance, mitigating climate
change, sustaining livelihoods, and safeguarding human
health and biodiversity.

## Project Scope and Objectives

Our partnership is focused on __enhancing the precision of
the early forest fire detection system__, with the goal of
minimizing false alarms to bolster confidence among
firefighters and stakeholders. Additionally, we aspire
to incorporate industry-leading methodologies for
effectively managing, deploying, and maintaining Machine
Learning Models, ensuring optimal performance and
reliability over time.

![Overview 360](/images/projects/early_forest_fire_detection/overview_360.png)
*Overview of the camera system that can cover 360 degrees angle*

Our work is centered on enhancing the core of the Pyronear system, which
analyzes real-time images from cameras mounted on tower antennas.

![Overview ML Model](/images/projects/early_forest_fire_detection/overview_ai_model.png)
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

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/tower_antenna_1.jpg" loading="lazy">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/tower_antenna_3.jpg" loading="lazy">
  </div>
  <em>Setting up the system on the antenna tower</em>
</div>

Two cameras are mounted on top of the antenna tower, providing 360-degree
coverage of the area. These cameras can be programmed to capture images at
specific angles.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_1.jpg" loading="lazy">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_2.jpg" loading="lazy">
  </div>
  <em>Covering 360 degrees with two Reolink RLC-823A 16X cameras</em>
</div>

The map below illustrates how the chosen set of angles enables complete
360-degree coverage.

![Cameras range](/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/camera_range.png)
*Range covered by the two cameras by taking pictures at different angles*

From the top of the antenna, the forest can be observed over a vast distance,
allowing a single Pyronear system to effectively monitor and protect a large
area. In practice, antennas are often positioned on hills, enabling the
detection of forest fires from 30 to 60 kilometers away.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/view_1.jpg" loading="lazy">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/view_2.jpg" loading="lazy">
  </div>
  <em>Forest views from the antena tower</em>
</div>

Shown below is the installed Pyronear system, housed in a secure enclosure. The
Pyronear team developed a plug-and-play setup featuring a central processing
unit built around a Raspberry Pi, connected to four cameras that provide
360-degree coverage. This system processes images continuously, around the
clock.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/early_forest_fire_detection/cameras/fontainebleau/setup/pyronear_hardware.jpg" loading="lazy">
  </div>
  <em>Pyronear hardware system case - Raspberry Pi, power chords, RJ45, and SIM card</em>
</div>

The computer vision model detected a forest fire in Fontainebleau from a
distance of 35 kilometers in real time, setting a new record for the Pyronear
system. The video below shows a thin black smoke rising in the distance.

{{< youtube id=i9Qy-zY16Ew >}}
<br/>

## Conclusion

In summary, an advanced computer vision model for detecting early signs of
forest fires provides a cost-effective and efficient means of safeguarding our
forests. This technology facilitates the swift deployment of firefighters,
greatly improving our capacity to protect forests that are increasingly
threatened by the impacts of global warming.

One can try out the model from the [ML Space]({{< ref
"/spaces/early_forest_fire_detection" >}}) or directly from the snippet below:

{{< hf_space "earthtoolsmaker-forest-fire-pyronear" >}}
