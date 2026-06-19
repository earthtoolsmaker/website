---
title: Monitoring Smolt Salmon Migration with Sonar
summary: An innovative use of sonar imagery to monitor and analyze the migration patterns of smolt salmon as they journey from freshwater to the ocean
tags: ["aquatic", "freshwater", "vision"]
related_projects:
  - wild_salmon_migration_monitoring
  - coral_reef_health_monitoring
related_spaces:
  - /demos/wild_salmon_migration_monitoring/
  - /demos/coral_reef_health_monitoring/
tagline: Counting juvenile salmon by sonar as they run the gauntlet downstream to the ocean.
stats:
  - value: "8–14 cm"
    label: smolt detected
  - value: "Day & night"
    label: sonar imaging
  - value: "Automated"
    label: counting
clients:
  - name: BC Hydro 
    link: https://www.bchydro.com/
    logo: /images/clients/bc-hydro/logo.png
  - name: Lumax AI
    link: https://lumax.ai/
    logo: /images/clients/lumax-ai/logo.png
tools:
  - Machine Learning
  - Computer Vision
  - Sonar
why_count:
  - name: Population trends
    desc: "Tracking smolt numbers year over year reveals whether a salmon population is growing, stable or declining — an early warning of collapse."
  - name: Dam impact
    desc: "Counts above and below a dam quantify how hydroelectric infrastructure affects downstream fish survival."
  - name: Regulatory compliance
    desc: "Facilities must monitor and mitigate their impact on fish; automated counting provides the consistent, auditable data regulators require."
  - name: Management actions
    desc: "Smolt abundance feeds decisions on dam operations, habitat-restoration priorities, and fishing quotas for the adults that return."
date: 2026-01-10
space: /demos/smolt_sonar_monitoring/
status: completed
pinned: true
image: /images/projects/monitoring_smolt_salmon_migration_with_sonar/cover.png
---

Each spring, young salmon called **smolt** leave the rivers where they hatched and ride the current down to the sea — running a gauntlet of predators, dams and turbines along the way. How many survive that journey is one of the clearest measures of a salmon population's health. Together with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/), we're building a system that detects, tracks and counts smolt automatically from **ARIS sonar** footage recorded at Cho':lhsh?ta Lake (Jansen Lake), British Columbia.

{{< image_carousel id="smolt-monitoring-intro" items="2" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_overview.png" alt="Jansen Lake Map" caption="Jansen Lake, British Columbia, located on Vancouver Island" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_satellite.png" alt="Jansen Lake Satellite" caption="Jansen Lake, British Columbia, Satellite close up" >}}
{{< /image_carousel >}}

From a raw sonar recording to a verified count, the system runs four automated steps:

![From a sonar recording to a counted smolt — the analysis pipeline](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/pipeline.svg)
*ARIS sonar records the water, a model detects and measures each smolt, and fish are tallied as they cross a virtual line.*

## Why count smolt?

### What are smolt?

Smolt are juvenile salmon (8–14 cm) going through **smoltification** — the bodily changes that turn a freshwater fish into one ready for the sea. It's the stage when they leave the river behind, slipping downstream past whatever infrastructure stands between them and the ocean.

![Salmon lifecycle](/images/projects/monitoring_smolt_salmon_migration_with_sonar/lifecycle_salmon.png)
*Salmon lifecycle — courtesy of the [Pacific Salmon Foundation](https://psf.ca/learn/species-lifecycle/)*

### Why the smolt stage is critical

The trip downstream is one of the most dangerous stretches of a salmon's life. Smolt have to slip past dams and turbines that can kill or disorient them, they swim near the surface where predators wait, and they move in dense pulses packed into a few short windows. Climate change tightens the squeeze further — altering river flows and warming the water, which compresses those windows and piles stress onto already-vulnerable juveniles.

### Why accurate counting matters

Reliable smolt counts are fundamental for salmon conservation — tap each to learn more.

{{< threats "why_count" >}}

### The challenge of current methods

Today, counting mostly means a person watching hours of footage and tallying fish by hand in grainy, noisy acoustic images. During a peak run, thousands of smolt can pass in a short burst — far more than anyone can keep up with frame by frame. The approach is slow, easy to get wrong, and impossible to scale to the continuous, reliable counts conservation actually needs.

## What is ARIS Sonar?

ARIS sonar "sees" with sound instead of light, building video-like images from the echoes that bounce back off objects in the water. That lets it pick out fish where an ordinary camera is blind — in murky water, total darkness, at night — and its resolution is fine enough to catch something as small as a smolt.

![Sonar Aris Frame](/images/projects/monitoring_smolt_salmon_migration_with_sonar/sonar_aris_frame.png)
*Example ARIS sonar frame — acoustic image showing fish targets in the sonar beam.*

## Our Approach

### Project scope

The goal is to find out whether smolt can be counted automatically from ARIS sonar — and to build the pipeline that does it. We surveyed the existing methods, picked the most promising, and assembled an end-to-end workflow that pairs deep-learning object detection with tracking.

### Sonar analysis challenges

Acoustic imaging is a proven way to count fish, but turning the footage into numbers is hard work: the signal is noisy, and a fish's echo varies in both strength and shape. Tools like [Echoview](https://echoview.com/) and [ArisFish](https://arisfish.software.informer.com/) have pushed background subtraction and detection forward, yet a fully automated detect-track-count workflow has stayed out of reach. Recent progress in deep neural networks is finally changing that.

Smolt make it harder still. Next to adult salmon they're tiny (8–14 cm) and easily lost in noise, they hug the cluttered water surface, and they arrive in dense groups over short windows — exactly the conditions that trip up older methods.

### Key technical achievements

The pipeline now does four things end to end:

<div class="services__list">
  <div class="services__item">
    <span class="services__number" aria-hidden="true">01</span>
    <h4 class="services__item-title">Convert &amp; clean</h4>
    <p class="services__item-description">Convert the proprietary <code>.aris</code> format and clean it up, with motion-aware noise reduction.</p>
  </div>
  <div class="services__item">
    <span class="services__number" aria-hidden="true">02</span>
    <h4 class="services__item-title">Detect &amp; track</h4>
    <p class="services__item-description">Detect and follow each individual smolt across frames with deep learning.</p>
  </div>
  <div class="services__item">
    <span class="services__number" aria-hidden="true">03</span>
    <h4 class="services__item-title">Estimate length</h4>
    <p class="services__item-description">Estimate every tracked fish's body length and convert it to real-world centimetres.</p>
  </div>
  <div class="services__item">
    <span class="services__number" aria-hidden="true">04</span>
    <h4 class="services__item-title">Count by direction</h4>
    <p class="services__item-description">Count smolt as they cross a virtual line, recording each fish's direction of travel.</p>
  </div>
</div>

### Study site

The [Alouette River](https://en.wikipedia.org/wiki/Alouette_River) is the eventual deployment site. Because data collection there wasn't possible in 2025, this first year drew on smolt data from the outflow of Jansen Lake.

## Preprocessing

Before any analysis, each raw `.aris` file runs through five preprocessing steps that turn a noisy acoustic recording into clean, analysis-ready video.

The output is encoded as an RGB image, with each channel carrying a different layer: the raw sonar sits in the blue background, while moving fish light up in bright red — easy for both a person and the model to pick out from the static clutter.

![How preprocessing works — five steps turn a raw ARIS frame into a clean, colour-encoded one where fish show up in red](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/preprocess.svg)
*Five steps turn a raw, noisy ARIS frame into clean video — the colour encoding makes fish (red) stand out from the static sonar background (blue).*

Large sonar files are split into smaller chunks so the downstream detection and tracking steps can process them efficiently.

## Detection and Tracking

### Finding each fish

First the system has to *find* the fish. We trained a **detector** — a model shown thousands of example frames until it learned what a smolt looks like in sonar. Shown a new frame, it draws a box around every fish it spots and gives each one a confidence score, while leaving the static background and noise alone. (Under the hood it's a fine-tuned [YOLOv11](https://github.com/ultralytics/ultralytics) model, a fast, widely-used object detector.)

![How the detector works — it reads a sonar frame and boxes each smolt with a confidence score](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/detection.svg)
*The detector reads a noisy sonar frame and returns a box — and a confidence score — around each smolt, ignoring the background clutter.*

### Following each fish

Finding a fish in a single frame isn't enough: the same smolt shows up in dozens of frames as it swims past, and we must count it only **once**. So the system *follows* each fish from frame to frame, linking its boxes into a single path — and holding on to it even when two fish cross or one briefly slips behind the noise. Every smolt becomes exactly one track, and one count. (This uses [BoTSort](https://github.com/NirAharon/BoT-SORT), which combines each fish's motion and appearance to keep it on the right track.)

![How tracking works — detections are linked across frames into one path per fish, keeping their IDs when paths cross](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/tracking.svg)
*Each fish's detections are linked across frames into a single track, so it keeps its identity — and is counted once — even when paths cross.*

<p><iframe src="https://www.youtube.com/embed/UY08mjPBHbc" loading="lazy" frameborder="0" allowfullscreen></iframe></p>
<p class="media-caption">Automated smolt detection and tracking in action on preprocessed ARIS sonar footage.</p>

## Size Estimation

Length is one of the most telling things you can know about a fish — it helps separate species and life stages — so the pipeline estimates it for every smolt it tracks, working from the size of the detection boxes.

For each detection the system reads whether the fish is swimming roughly horizontally or vertically and picks the box dimension that best matches its body. Single detections are noisy, so it gathers measurements across the whole track, discards the outliers, and combines the rest — trusting the estimate more the more consistent readings back it up.

That yields a length for the vast majority of tracked fish. A known-size reference placed in the sonar's field of view at installation then converts the pixel measurements into real-world centimetres.

![How length is estimated — many per-frame measurements are filtered down to one length](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/size.svg)
*A length is read in every frame; the outliers are dropped, the rest are combined at the median, and the result is converted from pixels to centimetres.*

## Counting

Counting turns those tracks into migration numbers. A smolt is counted when its track crosses a **trigger line** drawn across the image; to avoid double-counting, a crossing only registers on an odd number of passes, and the direction of travel — upstream or downstream — is read from the sonar's orientation.

Rather than stretch that line across the full sonar range, we place a focused **regional trigger** right at the weir-box exit. That keeps detections from outside the migration corridor from ever counting, and lets us tune the model for a single zone — which matters because sonar imagery changes with distance from the transducer, so a region-specific model beats one stretched across the whole range.

![How counting works — a smolt is tallied as its track crosses the regional trigger line at the weir-box exit](/images/projects/monitoring_smolt_salmon_migration_with_sonar/diagrams/counting.svg)
*A focused trigger line at the weir-box exit: each smolt is counted once as it crosses, and its direction of travel is recorded.*

## Interactive Demo

See the model work for yourself. Upload preprocessed sonar footage, or run one of the built-in examples, and watch it detect and track smolt in real time:

{{< demo_cta >}}

## Conclusion

Counting smolt automatically from ARIS sonar works. By chaining deep-learning detection with robust tracking, length estimation and directional counting, the pipeline turns hours of manual review into a workflow that produces reliable migration data on its own.

Built with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/), it handles the whole chain — from raw sonar files to per-fish counts with lengths and travel direction. Faster, more consistent smolt monitoring means the people protecting salmon get the data they depend on, season after season.

<p><iframe src="https://www.youtube.com/embed/Tg-gyDn8zfk" loading="lazy" frameborder="0" allowfullscreen></iframe></p>
<p class="media-caption">Full pipeline demo — detection, tracking, counting, and size estimation on ARIS sonar footage.</p>
