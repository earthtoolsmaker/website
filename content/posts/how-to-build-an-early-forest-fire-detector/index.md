---
title: How to build an early forest fire detector
description: Detecting early forest fires in real time using low powered technology
date: 2024-08-21
image: /images/posts/how-to-build-an-early-forest-fire-detector/cover.png
tags: ["AI", "vision", "low power"]
draft: true
---

In this blog post we'll explore the development process of a state of the art
early forest fire detector, created in partnership with the NGO
[Pyronear](https://pyronear.org).

> Our detectors communicate fire alerts to a database that is connected
> to a supervision platform for the fire department.
>
> <cite>– Pyronear</cite>

![System Overview](./images/overview_system.png)
*Overview of the Pyronear system to monitor forests around the clock*

![Overview 360](./images/overview_360.png)
*Overview of the camera system that can cover 360 degrees angle*

![Overview ML Model](./images/overview_ai_model.png)
*Overview of the embedded ML system*

### Hardware setup

The Pyronear team developped a plug and play system composed of a central processor unit made of a Raspberry Pi connected to 4 cameras that cover 360 degrees angle to process input images around the clock.

#### Setting up the Pyronear system at Fontainebleau

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/cameras/fontainebleau/setup/tower_antenna_1.jpg" loading="lazy">
    <img src="./images/cameras/fontainebleau/setup/tower_antenna_3.jpg" loading="lazy">
  </div>
  <em>Setting up the system on the antenna tower</em>
</div>

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/cameras/fontainebleau/setup/camera_1.jpg" loading="lazy">
    <img src="./images/cameras/fontainebleau/setup/camera_2.jpg" loading="lazy">
  </div>
  <em>Covering 360 degrees with two Reolink RLC-823A 16X cameras</em>
</div>

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/cameras/fontainebleau/setup/view_1.jpg" loading="lazy">
    <img src="./images/cameras/fontainebleau/setup/view_2.jpg" loading="lazy">
  </div>
  <em>View from the antenan tower</em>
</div>

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/cameras/fontainebleau/setup/pyronear_hardware.jpg" loading="lazy">
  </div>
  <em>Pyronear hardware system case - Raspberry Pi, power chords, RJ45, and SIM card</em>
</div>

![Cameras range](./images/cameras/fontainebleau/setup/camera_range.png)
*Range covered by the two cameras by taking pictures at different angles*


#### Covered sites

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/cameras/setup/brison/pyronear_brison_1_2023_07_24T16_51_07.jpg" loading="lazy">
    <img src="./images/cameras/setup/brison/pyronear_brison_2_2023_07_09T05_50_16.jpg" loading="lazy">
    <img src="./images/cameras/setup/brison/pyronear_brison_3_2023_07_04T06_22_26.jpg" loading="lazy">
    <img src="./images/cameras/setup/brison/pyronear_brison_4_2023_07_09T12_07_07.jpg" loading="lazy">
  </div>
  <em>360 view of the <b>Brison site</b> - 4 cameras are placed on an antenna tower</em>
</div>

<p><iframe src="https://www.youtube.com/embed/i9Qy-zY16Ew" loading="lazy" frameborder="0" allowfullscreen></iframe>
</p>
The computer vision model detects a forest fire in Fontainebleau from a distance of 35 kilometers in real time. Setting a new record for the Pyronear systems.

