---
title: How to build a benthic coral reefs analyser
description: This is a description
date: 2024-04-10
image: /images/posts/how-to-build-a-benthic-coral-reefs-analyser/cover.jpg
tags: ["AI", "vision"]
---

Welcome to our blog post where we'll explore the development process of
a benthic coral reef analyzer, created in partnership with
[ReefSupport](https://reef.support). Our goal is simple: to improve the
tools available for monitoring coral reefs and marine environments.
Let's dive into how we're making this happen!

For a comprehensive understanding of this project, please click on the
image below:

<a href='{{< ref "/projects/coral_reef_health_monitoring.md" >}}' title="Project Details">
  <img src="./images/pipeline_overview.png" />
</a>

> Leveraging computer vision for the segmentation of
coral reefs in benthic imagery holds the potential to
> quantify the long-term growth or decline of coral cover
within
> marine protected areas

## Project Scope

Our collaboration aims to lead the way in developing an advanced underwater benthic imagery model. This model is designed to accurately identify and locate various functional groups within reef ecosystems. It's flexible and can be used in different marine regions worldwide.

![Benthic Analysis System](./images/coral_ai.gif)
*Gallery / Benthic Imagery Analysis System by [Reef Support](https://reef.support)*

Initially, our main focus is on distinguishing between hard and soft coral species. However, our approach is iterative, meaning we can gradually include more detailed taxonomic classifications as the system evolves and becomes more sophisticated. By establishing a strong foundation with this broad framework, we set the stage for comprehensive analysis and management of reef ecosystems.

## Provided Dataset

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

This section outlines various data quality issues identified during the
Exploratory Data Analysis (EDA) process.

##### Empty masks
##### Low quality labels
##### Label mismatches
##### Data leakage
##### Class imbalance

### Data Preparation

#### YOLOv8 TXT format

## Data Modeling

### Data Split
### Instance Segmentation vs Semantic Segmentation
### Evaluation Metrics
### YOLOv8
#### Overview
#### Training
#### Evaluation
### Model size vs Model accuracy

## Conclusion

