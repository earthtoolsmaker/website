---
title: Monitoring Smolt Salmon Migration with Sonar
summary: An innovative use of sonar imagery to monitor and analyze the migration patterns of smolt salmon as they journey from freshwater to the ocean
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
date: 2026-01-10
space: /spaces/smolt_sonar_monitoring/
status: completed
pinned: true
image: /images/projects/monitoring_smolt_salmon_migration_with_sonar/cover.png
---

Monitoring smolt — juvenile salmon migrating downstream toward the ocean — is essential for understanding salmon population health and evaluating the impact of hydroelectric infrastructure on fish survival. In partnership with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/), we are developing an automated system to detect, track, and count smolt from ARIS sonar imagery collected at Cho':lhsh?ta Lake (Jansen Lake), British Columbia.

{{< image_carousel id="smolt-monitoring-intro" items="2" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_overview.png" alt="Jansen Lake Map" caption="Jansen Lake, British Columbia, located on Vancouver Island" >}}
  {{< carousel_image src="/images/projects/monitoring_smolt_salmon_migration_with_sonar/map_satellite.png" alt="Jansen Lake Satellite" caption="Jansen Lake, British Columbia, Satellite close up" >}}
{{< /image_carousel >}}

## Why count smolt?

### What are smolt?

Smolt are juvenile salmonids (8–14 cm) undergoing smoltification — the physiological transformation that prepares them for the transition from freshwater to saltwater. During this critical life stage, they migrate downstream through rivers and past infrastructure on their way to the ocean.

![Salmon lifecycle](/images/projects/monitoring_smolt_salmon_migration_with_sonar/lifecycle_salmon.png)
*Salmon lifecycle — courtesy of the [Pacific Salmon Foundation](https://psf.ca/learn/species-lifecycle/)*

### Why the smolt stage is critical

The downstream migration is one of the most dangerous periods in a salmon's life. Smolt must navigate past dams, turbines, and other infrastructure that can cause direct mortality or disorientation. They swim close to the water surface where they are vulnerable to predators, and they often travel in dense groups over short time windows. Climate change is adding further pressure through altered river flows and rising water temperatures, compressing migration windows and increasing stress on already vulnerable juveniles.

### Why accurate counting matters

Reliable smolt counts are fundamental for salmon conservation:

- __Population trend assessment__: Tracking smolt numbers over multiple years reveals whether salmon populations are growing, stable, or declining — providing early warning of population collapse.
- __Evaluating dam impact__: Hydroelectric operators like [BC Hydro](https://www.bchydro.com/) need to understand how their infrastructure affects downstream fish survival. Accurate counts above and below dams quantify this impact.
- __Regulatory compliance__: Hydroelectric facilities operate under environmental regulations that require monitoring and mitigating impacts on fish populations. Automated counting provides the consistent, auditable data needed for compliance.
- __Informing management actions__: Smolt abundance data feeds directly into decisions about dam operations, habitat restoration priorities, and fishing quotas for returning adults.

### The challenge of current methods

Traditional smolt counting relies on manual review of sonar footage, which is time-consuming and error-prone. Analysts must watch hours of recordings by hand, identifying and counting individual fish in noisy acoustic images. Dense migration events — where thousands of smolt pass in a short period — make manual review particularly impractical. The sheer volume of data generated during peak migration windows means that manual methods simply cannot scale to provide the continuous, reliable counts that conservation demands.

## What is ARIS Sonar?

ARIS sonar creates acoustic images using sound reflections, enabling fish detection in conditions where optical cameras fail: turbid water, zero visibility, and nighttime. It produces high-resolution, video-like acoustic image sequences that are well suited for detecting and counting small fish like smolt.

![Sonar Aris Frame](/images/projects/monitoring_smolt_salmon_migration_with_sonar/sonar_aris_frame.png)
*Example ARIS sonar frame — acoustic image showing fish targets in the sonar beam.*

## Our Approach

### Project scope

The overarching goal of this project is to assess the feasibility of automated smolt enumeration from ARIS sonar data. We do this by reviewing existing methods, selecting the most promising candidates, and developing an end-to-end analysis pipeline combining deep learning-based object detection with tracking algorithms.

### Sonar analysis challenges

Hydroacoustic imaging is a widely used and effective method to enumerate fish in waterways, but the analysis of large amounts of data is time-consuming and requires trained personnel. Methods to facilitate the analysis of sonar data are much needed but challenging to develop, especially due to background noise and variation in the intensity and type of the return signal of fish. Significant progress has been made in background subtraction and object detection in software such as [Echoview](https://echoview.com/) and [ArisFish](https://arisfish.software.informer.com/), but reliable algorithms to detect, track, and enumerate fish in an automated workflow remain elusive.

Over the last years, the fast development of Artificial Intelligence (AI), in particular Deep Neural Networks, has led to rapid progress in image analysis, including automated detection and tracking of fish in sonar imagery. Smolt present unique challenges compared to adult salmon: their small size (8–14 cm) makes them harder to detect and separate from noise, they swim close to the noisy water surface, and they can migrate in dense groups over short time periods.

### Key technical achievements

Some key technical achievements of this project include:
- Automated conversion and preprocessing of proprietary .aris format with motion-enhanced noise reduction
- Detection and tracking of individual smolt using deep learning
- Length estimation of the detected smolt
- Directional counting of smolt migrating past a virtual trigger segment

### Study site

The [Alouette River](https://en.wikipedia.org/wiki/Alouette_River) is the target site for deployment of sonar smolt enumeration. For the first year we used smolt data from the outflow of Jansen Lake, as data collection at the Alouette River was not possible in 2025.

## Preprocessing

Raw ARIS sonar files go through a five-step preprocessing pipeline before analysis: file conversion from the proprietary `.aris` format to `.mp4`, frame stabilization, noise reduction, colour channel adjustment, and chunking into manageable segments. Together these steps transform noisy acoustic recordings into clean, analysis-ready video.

The preprocessed output is visualized as an RGB image where each colour channel encodes a different layer of information. The blue background represents the original raw sonar input, while fish appear as bright red regions that stand out clearly against it, making them easy to distinguish from the static sonar information.

![Preprocessing before and after](/images/projects/monitoring_smolt_salmon_migration_with_sonar/preprocess.png)
*Before and after preprocessing — the RGB encoding makes fish (red) clearly distinguishable from the static sonar information (blue).*

Large sonar files are split into smaller chunks so the downstream detection and tracking steps can process them efficiently.

## Detection and Tracking

We fine-tuned a pretrained [YOLOv11](https://github.com/ultralytics/ultralytics) model for smolt detection in preprocessed sonar frames. YOLO (You Only Look Once) is a family of real-time object detection models known for their excellent balance of speed and accuracy — critical when processing thousands of sonar frames per recording session. The model learns to locate smolt in each frame and output bounding boxes with confidence scores.

![YOLO tasks](/images/projects/monitoring_smolt_salmon_migration_with_sonar/yolo_tasks.png)
*Overview of YOLO tasks — detection, segmentation, classification, pose estimation, and oriented bounding boxes (courtesy of [Ultralytics](https://github.com/ultralytics/ultralytics)).*

To follow individual smolt across consecutive frames we use [BoTSort](https://github.com/NirAharon/BoT-SORT) (Robust Associations Multi-Pedestrian Tracking). Unlike simpler tracking approaches such as SORT that rely solely on bounding-box overlap, BoTSort combines motion prediction with visual appearance features and camera-motion compensation. This makes it far more robust when fish cross paths or temporarily disappear behind noise, providing continuous trajectories that allow us to count each smolt exactly once as it migrates past the sonar.

<p><iframe src="https://www.youtube.com/embed/UY08mjPBHbc" loading="lazy" frameborder="0" allowfullscreen></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Automated smolt detection and tracking in action on preprocessed ARIS sonar footage.</em>

## Size Estimation

Estimating the length of each detected smolt is an important step in the pipeline because fish length is one of the key characteristics used to distinguish species and life stages. Our approach uses the dimensions of the bounding boxes drawn around each detection to estimate fish length.

For each detection the algorithm determines whether the fish is swimming roughly horizontally or vertically and selects the bounding-box dimension that best represents its body length. Because individual detections can vary, the system collects multiple measurements across a fish's tracked trajectory and filters out extreme values as outliers, keeping the estimates reliable. Each final length estimate is assigned a confidence rating based on how many consistent measurements were available — more observations mean higher confidence.

This method provides length estimates for the vast majority of tracked fish. As a final step, pixel measurements are converted to real-world centimetres using a known-size reference object placed in the sonar's field of view during installation.

![Length estimation process](/images/projects/monitoring_smolt_salmon_migration_with_sonar/length_estimation.png)
*Length estimation — multiple detections across frames are collected, filtered for outliers, and combined into a single length estimate in pixels.*

## Counting

The counting step translates the tracked fish trajectories into actual migration counts. A fish is counted when its track crosses a defined trigger segment — a virtual line drawn across the sonar image. To avoid double-counting, the system only registers a crossing when the track has crossed the segment an odd number of times, and it records the direction of travel (upstream or downstream) based on the sonar's orientation.

Rather than spanning the trigger segment across the entire sonar range, this project uses a regional trigger segment focused on the area of interest — specifically the weir box exit. This focused approach brings several advantages: it eliminates false detections from outside the migration corridor, and it allows more targeted optimization of the detection and tracking models. This matters because sonar imagery characteristics change with distance from the transducer, so a model tuned for one region performs better than one stretched across the full range.

![Counting trigger](/images/projects/monitoring_smolt_salmon_migration_with_sonar/counting_trigger.png)
*Regional trigger segment — a fish is counted when its track crosses the segment placed at the weir box exit.*

## Interactive Demo

Experience the smolt detection and counting model in action. Upload preprocessed sonar footage or use the provided examples to see automated detection and tracking:

{{< hf_space "Lumax-eco-sonar-smolt" >}}

## Conclusion

This project demonstrates that automated smolt enumeration from ARIS sonar imagery is feasible and effective. By combining deep learning-based detection with robust tracking, size estimation, and directional counting, the pipeline transforms hours of manual sonar review into an automated workflow that delivers reliable migration data.

The system developed in partnership with [BC Hydro](https://www.bchydro.com/) and [Lumax AI](https://lumax.ai/) handles the full analysis chain — from raw sonar files through to individual fish counts with length estimates and migration direction. By making smolt monitoring faster and more consistent, this approach supports the data-driven conservation decisions that are essential for protecting salmon populations.

<p><iframe src="https://www.youtube.com/embed/Tg-gyDn8zfk" loading="lazy" frameborder="0" allowfullscreen></iframe></p>
<em style="font-size:14px;line-height:1.4em;display:block;">Full pipeline demo — detection, tracking, counting, and size estimation on ARIS sonar footage.</em>
