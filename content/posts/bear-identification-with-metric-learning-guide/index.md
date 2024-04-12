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

2. Provided Dataset

Generated chips

2.1. EDA
2.1.1. Data Distributions
2.1.1. Class imbalance - Bursts of images
2.1.2. 

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
