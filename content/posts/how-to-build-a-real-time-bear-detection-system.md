---
title: How to build a real time bear detection system
description: Detecting bears in real time using low-power technology.
date: 2024-04-09
image: 'https://via.placeholder.com/1200x800'
tags: ["AI", "vision", "low power", "camera traps"]
---

In this blog post, we'll delve into the successful development of a real-time
bear detection system, achieved through collaboration with the NGO
[HackThePlanet](https://www.hack-the-planet.io). Our initiative aims to
safeguard Romanian farms by deterring bear encroachments.

> Implementing non-invasive methods to deter bears from approaching farms
> and livestock holds promise in fostering harmonious relations between
> humans and bears.

TODO: add a nice image and link to the project.
For more context about this project, go read this page: 

## Project Scope

The computer vision model responsible for detecting
bears will operate on a low-power microcontroller (such
as the Raspberry Pi5). This necessitates swift operation
and minimal power consumption during inference. Ensuring
timely detection of approaching bears is critical, as
their entry onto farms can result in predation on
livestock, such as pigs. Achieving an extremely high
recall rate is imperative to prevent such incidents.
Additionally, since brown bear activities can occur day
or night, the system must remain operational around the
clock.

Maintaining a low false positive rate is essential for
two key reasons: Firstly, to uphold trust among farmers
who rely on the system daily, it must avoid triggering
unnecessarily. Secondly, to prevent excessive power
consumption when activating the bear deterrent
component, false positives must be minimized.

## Provided Dataset

We have amassed a collection of camera trap images captured over the
past years from forests near the farms in Romania.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear4.jpg" loading="lazy" alt="camera trap bear picture 4" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear1.jpg" loading="lazy" alt="camera trap bear picture 1" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear2.jpg" loading="lazy" alt="camera trap bear picture 2" \>
    <img src="/images/projects/human_wildlife_conflict_bear/bears/bear3.jpg" loading="lazy" alt="camera trap bear picture 3" \>
  </div>
  <em>Gallery / Camera trap pictures of bears in Romania, near the farms where the system is deployed</em>
</div>

### Camera Traps

The advent of camera traps has transformed wildlife observation and research,
enabling unprecedented insights into behavioral ecology and facilitating
citizen science census projects. These non-invasive monitoring tools offer the
advantage of data collection without human presence, minimizing stress on the
observed individuals. From the Arctic tundra to tropical rainforests, camera
traps have proven versatile, facilitating the study of a diverse range of
species. Initially designed for game scouting, camera traps have evolved
significantly to become indispensable tools for wildlife research, driving
advancements in design, functionality, and affordability.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/projects/bear_identification/camera_traps/camera1.png" loading="lazy" alt="Camera Trap" />
    <img src="/images/projects/bear_identification/camera_traps/camera3.jpg" loading="lazy" alt="Camera Trap" />
  </div>
  <em>Gallery / Camera Traps</em>
</div>

### Exploratory Data Analysis

Exploratory Data Analysis (EDA) is an approach to analyzing datasets to
summarize their main characteristics, often employing visual methods. The
primary goal of EDA is to uncover patterns, relationships, and anomalies in the
data, which can then inform subsequent analysis or modeling tasks.

EDA typically involves the following steps:

1. __Data Collection__: Gathering the relevant dataset(s) from various sources.
2. __Data Cleaning__: Identifying and handling missing values, outliers, and
   inconsistencies in the data.
3. __Summary Statistics__: Computing descriptive statistics such as mean,
   median, mode, standard deviation, etc., to understand the central tendencies
and variability of the data.
4. __Data Visualization__: Creating visual representations of the data using
   plots, charts, histograms, scatter plots, etc., to explore patterns,
distributions, correlations, and trends within the data.
5. __Exploratory Modeling__: Building simple models or using statistical
   techniques to further understand relationships within the data.
6. __Hypothesis Testing__: Formulating and testing hypotheses about the data to
   validate assumptions or gain insights.
7. __Iterative Analysis__: Iteratively exploring the data, refining analysis
   techniques, and generating new hypotheses as insights emerge.

EDA is a crucial initial step in any data analysis or modeling project as it
helps analysts gain a deeper understanding of the dataset, identify potential
challenges or biases, and inform subsequent analytical decisions. It provides a
foundation for more advanced analyses, such as predictive modeling, hypothesis
testing, or machine learning, by guiding feature selection, model building, and
evaluation strategies.

#### Data quality issues

##### Bursts of Images

Camera traps consist of a camera and a motion sensor.
Upon detecting movement, the camera begins recording the
scene, often resulting in numerous video frames capturing
the same animal in a similar pose. It's crucial to ensure
that these bursts of images are properly handled during
data splitting. Failure to do so can result in train/test
data leakage, potentially causing the model to
inaccurately overreport its performance.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/posts/bear_detection/camera_traps/bursts/image1.jpg" loading="lazy" alt="camera trap bear picture 1" \>
    <img src="/images/posts/bear_detection/camera_traps/bursts/image2.jpg" loading="lazy" alt="camera trap bear picture 2" \>
    <img src="/images/posts/bear_detection/camera_traps/bursts/image3.jpg" loading="lazy" alt="camera trap bear picture 3" \>
    <img src="/images/posts/bear_detection/camera_traps/bursts/image4.jpg" loading="lazy" alt="camera trap bear picture 4" \>
  </div>
  <em>Gallery / Camera trap pictures of bears in Romania, near the farms where the system is deployed - Same bear encounter</em>
</div>

##### Corrupted Images

We encountered numerous camera trap pictures that were corrupted and couldn't
be loaded properly. As data is fundamental to constructing a robust machine
learning system, it was disheartening to have to discard a significant portion
of it due to the inability to recover these corrupted images.

#### Class Imbalance

The dataset was heavily skewed towards bear images, with a prevalence
approximately five times higher than that of images featuring other animals or
empty frames.

When dealing with imbalanced datasets in machine learning, where one class is
significantly more prevalent than the others, it can lead to biased models that
perform poorly on minority classes.

After filtering out the corrupted images, we observed that the dataset was
heavily skewed towards bear images, with a prevalence approximately five times
higher than that of images featuring other animals or empty frames.

##### Resampling Techniques

- __Oversampling__: Increase the number of instances in the minority class by
duplicating or generating new instances.
- __Undersampling__: Decrease the number of instances in the majority class by
randomly removing instances. This can help balance the class distribution.

##### Data Augmentation

Augment the minority class by introducing small variations or perturbations to
the existing data, similar to techniques used in image processing.

![Data Augmentation](/images/posts/bear_detection/data_augmentation/tencrop.png)
*Data Augmentation / TenCrop - Generate 10 images from one to mitigate the class imbalance*

### Data Annotation

To annotate our dataset, we evaluated two machine
learning models: __MegaDetector__ and __GroundingDINO__.
In our decision to train an object detector, the
annotation process for each image captured by the camera
traps should include generating bounding boxes that
outline the location of each detected bear: (x, y, width,
height).

Both models successfully identified bears in camera trap images, but
GroundingDINO, when prompted with the text "bear," exhibited higher accuracy.
GroundingDINO also produced fewer false positives and false negatives.
Consequently, we opted to utilize GroundingDINO to generate the dataset.

![Annotations](/images/posts/bear_detection/annotations/labels.jpg)

___Note:___ MegaDetector and GroundingDINO, while effective for object detection and image
understanding, are not suitable for low-power, real-time applications due to
their large size and high computational requirements. However, we can leverage
these existing models to curate the dataset used for training our machine
learning model.

#### MegaDetector

__MegaDetector__ is a deep learning-based object detection model
developed by
Microsoft AI for Earth. It is specifically designed for detecting
animals in
camera trap images, including rare or previously unseen species.
MegaDetector
employs state-of-the-art convolutional neural networks (CNNs) to
automatically
identify and localize animals within images, facilitating large-scale
wildlife monitoring and conservation efforts.

<a href="https://github.com/microsoft/CameraTraps/blob/main/megadetector.md">
  <img src="/images/posts/bear_detection/pytorch_wildlife.png" alt="MegaDetector and Pytorch Wildlife" />
</a>
<br/>
<br/>

#### GroundingDINO

<a href="https://github.com/IDEA-Research/GroundingDINO"><img style="float: left; margin-right: 10px; max-height: 120px;" src="/images/posts/bear_detection/grounding_dino_logo.png" alt="GroundingDINO Logo" /></a>
<b>GroundingDINO</b> is a multimodal framework that combines Vision Transformers
(ViTs) with language grounding for image-text matching tasks. It leverages the
power of transformer-based models for both image and text modalities, enabling
efficient processing of visual and textual information. By grounding textual
descriptions with visual features, GroundingDINO achieves improved performance
in tasks such as image retrieval and cross-modal understanding.
<br style="clear:both;"/>
<br />

## Data Modeling

### Image Classification vs Object Detection

How might we approach modeling this dataset? One option is to conceptualize the
problem as a binary image classification task, where the goal is to predict
whether an image contains a bear or not. Alternatively, it could be formulated
as an object detection task, aiming to predict bounding boxes that delineate
the location of any detected bears within the image.

Both approaches have their advantages and drawbacks. Initially, when we opted
for the straightforward image classification task to model the dataset, we
encountered an issue: The model learned to rely on recurring image backgrounds
captured by the fixed camera traps to make predictions. This tendency could
potentially hinder generalization when deploying the system. However, framing
the problem as an object detection task resulted in improved performance.

### Inference Speed vs Model Accuracy

The real-time requirement of this system necessitates careful consideration of
the tradeoff between inference speed and model accuracy. Opting for a larger
model operating on a full image frame of the video feed can deliver superior
accuracy but at the expense of slower processing speed. Evaluating this
tradeoff was crucial in selecting the most suitable model for the task.

![Inference Speed vs Model Accuracy](/images/posts/bear_detection/speed_accuracy_tradeoff/tradeoff.png)

## Conclusion


