---
title: A guide to designing a bear face recognition system
description: Identify bears with Metric Learning.
date: 2024-04-11
image: /images/posts/bear-identification-with-metric-learning-guide/cover.png 
tags: ["AI", "vision", "metric learning"]
---

In this blog post we'll delve into the technical
development of a bear face recognition system which is a
critical component of the bear identification
system developed in close collaboration with the [BearID
Project](https://bearresearch.org/) NGO.

> Our research and software tool will provide a replicable technique and
> general approach that can be applied to other species beyond bears, which
> could aid conservation efforts worldwide.
>
> <cite>– BearID Project</cite>

For a comprehensive understanding of this project, please click on the pipeline
overview below:

<a href='{{< ref "/projects/bear_identification.md" >}}' title="Project Details">
  <img src="./images/pipeline.png" />
</a>
<br/>
<br/>

## Project Scope

While many species boast distinctive fur patterns for identification,
brown bears lack consistent and unique markings. Furthermore, their
weight can fluctuate significantly between seasons and throughout their
lifetimes. Consequently, facial recognition emerges as a valuable
alternative for individual identification.

In this article, our attention is directed towards the final phase of
the bear identification system, specifically the recognition of bear
faces.

The initial stage entails acquiring a mapping capable of embedding bear
faces into a high-dimensional space, facilitating the clustering of
individuals.

![Bear Face Embedding](./images/embed_overview.png)
*Embedding bear faces into a high dimensional space*

Subsequently, we leverage this learned mapping to execute queries and
retrieve the closest matching individuals.

![Bear Face Querying](./images/query_overview.png)
*Retrieving closest individuals from the learned mapping*

Our collaboration with [The BearID Project](https://bearresearch.org)
aims to significantly enhance their current model performance, which
currently stands at precision (top-1): 0.649 and precision (top-5): 0.707.

## Provided Dataset

The [BearID Project](https://bearresearch.org) has compiled a collection
of bear images, showcasing their facial features,
captured over recent years in forests across British Columbia and Brooks
Falls.

After the development of the bear face segmentation system, as detailed
in [a prior blog post]({{< ref
"posts/bear-face-segmentation-guide" >}}), we successfully
generated approximately 4700 bear face images,
representing a total of 132 individuals.

![Generated Chips](./images/chips.png)
*Generated bear faces by the segmentation model*

### Bursts of images

When encountering a bear, photographs or camera traps often capture
multiple images of the same individual in very similar poses. Proper
handling of these bursts of images during data splitting is crucial.
Neglecting this step may lead to train/test data leakage, which can
cause the model to inaccurately overreport its performance.

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/eda/bursts/1.jpg" loading="lazy">
    <img src="./images/eda/bursts/2.jpg" loading="lazy">
    <img src="./images/eda/bursts/3.jpg" loading="lazy">
    <img src="./images/eda/bursts/4.jpg" loading="lazy">
  </div>
  <em>Gallery / Provided labels by <a href="https://bearrearch.org">The BearID Project</a> - A burst of images with the same individual</em>
</div>

### Individual counts distribution

The curated dataset primarily consists of only a few image faces for
most bears, posing a potential challenge for accurate identification.
Conversely, some bears have hundreds of image faces, largely derived
from bursts of images captured during encounters. Below, we present a
distribution plot of individual counts to provide further insight into
the data.

![Individual counts distribution](./images/eda/individual_counts_distribution.png)
*Individual counts distribution - How many image faces per individual?*

## re-IDentification

### Definition

Re-identification, often abbreviated as __re-ID__, involves identifying and
tracking individual animals across different camera traps or instances in
wildlife habitats.

### Objective

> The primary goal is to accurately identify and track individual animals over
> time, allowing researchers to study behavior, population dynamics, migration
> patterns, and other ecological factors.

### Challenges

Animal re-identification faces unique challenges compared to person or object
re-identification:

- __Variability in Appearance__: Animals may exhibit variations in
appearance due to factors such as changes in fur color, markings, or
physical condition (e.g., injuries).
- __Environmental Conditions__: Camera traps are often deployed in outdoor
environments where lighting conditions, weather, and vegetation can vary
significantly, affecting image quality and visibility of animals.
- __Species Variability__: Different species may exhibit diverse
morphologies and behaviors, requiring specialized models and approaches for
accurate re-identification.

### Common approach

Similar to other re-identification tasks, animal re-identification often
involves the following steps:

- __Feature Extraction__: Deep learning-based models, such as convolutional
neural networks (CNNs), are used to extract discriminative features from
images captured by camera traps. These features encode unique
characteristics of individual animals, such as fur patterns or facial
markings. For brown bears - which lack unique fur and body markings - facial
markings are key.
- __Matching__: Extracted features are then compared across different camera
traps or instances to identify and track individual animals. Matching
algorithms, such as nearest neighbor search or clustering, are commonly used
to find similar feature representations corresponding to the same animal
across different images.

### Applications

Animal re-identification has numerous applications in wildlife conservation and
ecological research:

- __Population Monitoring__: Researchers can use re-identification data to
estimate population sizes, monitor trends, and assess the impact of
environmental changes or human activities on wildlife populations.
- __Behavioral Studies__: Long-term tracking of individual animals allows
for detailed studies of behavior, movement patterns, habitat use, and social
interactions within animal populations.
- __Conservation Planning__: Re-identification data can inform conservation
strategies by identifying key habitats, migration corridors, and areas of
high wildlife activity for targeted conservation efforts.

Overall, animal re-identification plays a vital role in understanding and
managing wildlife populations, facilitating conservation efforts, and
supporting ecological research initiatives.

### Closed Set, Open Set, Disjoint Set

In the context of __re-ID__, understanding the concepts of open sets, closed
sets, and disjoint sets is critical.

#### Closed Set Identification

In a closed set scenario, the system is trained to recognize a
predefined set of classes or identities.
For example, in a closed set re-identification task, the system is
trained to identify a specific set of animals from a gallery of known
individuals.
The key characteristic of a closed set approach is that the identities
present in the testing or operational phase are limited to those seen
during training. In other words, the system only recognizes identities
that it has been explicitly trained on.

#### Open Set Identification

In contrast to closed set identification, open set identification deals with
scenarios where the testing data might contain identities not seen during
training.
The system needs to be able to recognize known identities (closed set) while
also detecting and handling unknown or novel identities.
This means the system must have the capability to distinguish between familiar
identities (in-distribution data) and unfamiliar ones (out-of-distribution
data).
Open set identification systems often incorporate techniques like anomaly
detection or thresholding to identify instances that don't belong to any known
class.

#### Disjoint Set Identification

Disjoint set identification refers to situations where the identities in the
training and testing datasets are completely separate.
In other words, there is no overlap between the identities seen during training
and those encountered during testing.
This scenario is common in real-world applications where the population of
identities is constantly changing, such as surveillance systems in crowded
areas or public spaces.

#### Summary

In summary, closed set identification deals with recognizing a fixed set
of known identities, open set identification extends this to handle
unknown or novel identities, and disjoint set identification involves
training and testing on completely separate sets of identities. Each
approach has its own challenges and requirements, and the choice depends
on the specific application and the nature of the data.

## Data Modeling

### Data Splits

We opted to create two distinct splits to assess the performance of the
identification system in real-world scenarios:

- __Open-set split__: This split includes a portion of newly introduced
identities in the testing phase, simulating encounters with previously unseen
entities.
- __Disjoint-set split__: In this split, the training and testing datasets
comprise entirely different identities, mimicking scenarios where the system
encounters novel entities during deployment

To avoid data leakage, we implemented a careful splitting strategy based on
both camera reference and date. This ensures that bursts of images captured by
the same camera at the same time are consistently grouped into the same split
(train, validation, or test).

### Metric Learning

#### Overview

#### Losses

3. Identification

Data splits Types of data splits and sets: closed set, open sed, disjoint set and pros and cons of each

3. Data Modeling
3.1. Data Splits
3.2. Metric Learning
3.2.1. Overview
3.2.2. Losses: Contrastive Loss, TripletMarginLoss, ArcFaceLoss
3.3. LightGlue: Local Feature Matching
3.3. Evaluation Metrics
3.4. Architecture Overview
3.5. Training
3.5.1. Baseline
3.5.2. Hyperparameters
3.5.3. Hyperparmater search

4. Evaluation
Show table of results here
4.1 Evaluation pitfalls: use reference and gallery in a good way, get rid of bursts of images

Conclusion
