---
title: How to build a real time bear detection system
description: Detecting bears in real time using low-power technology.
date: 2024-04-09
# image: 'https://via.placeholder.com/1200x800'
image: /images/posts/bear_detection/cover.png 
tags: ["AI", "vision", "low power", "camera traps"]
---

In this blog post, we'll delve into the successful development of a real-time
bear detection system, achieved through collaboration with the NGO
[HackThePlanet](https://www.hack-the-planet.io). Our initiative aims to
safeguard Romanian farms by deterring bear encroachments.

> Implementing non-invasive methods to deter bears from approaching farms
> and livestock holds promise in fostering harmonious relations between
> humans and bears.

For a comprehensive understanding of this project, please click on the pipeline
overview below:

<a href='{{< ref "/projects/human_wildlife_bear_conflict.md" >}}' title="Project Details">
  <img src="/images/posts/bear_detection/pipeline_overview.png" />
</a>

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

![RPi5 Microcontroller](/images/posts/bear_detection/rpi5.png)
*Gallery / Raspberry Pi5 - Low Power device*

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

This section outlines various data quality issues identified during the
Exploratory Data Analysis (EDA) process.

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
*Data Augmentation / [TenCrop](https://pytorch.org/vision/main/generated/torchvision.transforms.TenCrop.html) - Generate 10 images from one to mitigate the class imbalance*

We conducted thorough testing and evaluation of common resampling and
data augmentation methods. In our experiments, we observed that data
augmentation yielded particularly effective results when applied to
empty frames and images featuring other animals. This approach allowed
us to maintain a high number of bear images while introducing subtle
variations into the dataset.

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

### Data split

The annotated dataset has been divided into three sets: train,
validation, and test, with the following ratios: 80%, 10%, and 10%,
respectively. To prevent any potential data leakage between training and
testing phases, we partitioned the data based on camera reference and
date information extracted from the picture's exif metadata

### Image Classification vs Object Detection

How might we approach modeling this dataset? One option is to conceptualize the
problem as a binary image classification task, where the goal is to predict
whether an image contains a bear or not. Alternatively, it could be formulated
as an object detection task, aiming to predict bounding boxes that delineate
the location of any detected bears within the image.

<div class="gallery-box">
  <div class="gallery">
    <img src="/images/posts/bear_detection/cv_tasks/image_classification.png" loading="lazy" alt="Image Classification" \>
    <img src="/images/posts/bear_detection/cv_tasks/object_detection.png" loading="lazy" alt="Object Detection" \>
  </div>
  <em>Image Classification (left) vs Object Detection (right)</em>
</div>

Both approaches have their advantages and drawbacks. Initially, when we opted
for the straightforward image classification task to model the dataset, we
encountered an issue: The model learned to rely on recurring image backgrounds
captured by the fixed camera traps to make predictions. This tendency could
potentially hinder generalization when deploying the system. However, framing
the problem as an object detection task resulted in improved performance.

### YOLOv8

#### Overview

We opted to utilize a pretrained
[YOLOv8](https://github.com/ultralytics/ultralytics) model and fine-tune it for
our specific object detection task. Renowned for its speed, accuracy, and
user-friendly interface, YOLOv8 stands out as an ideal solution for various
tasks, including object detection, tracking, instance segmentation, image
classification, and pose estimation.

![YOLOv8 CV Tasks](/images/posts/bear_detection/yolov8_tasks.png)
*YOLOv8 Computer Vision Tasks*

#### Model size

As we aim to deploy our solution on a low-power microcontroller, we selected
the most compact variant of YOLOv8, known as the `'nano'` version or `'YOLOv8n'`.
The table below illustrates the tradeoff between model size (a proxy for
accuracy) and processing speed.

| Model                                                                                     | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n-oiv7.pt) | 640                   | 18.4                 | 142.4                          | 1.21                                | 3.5                | 10.5              |
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s-oiv7.pt) | 640                   | 27.7                 | 183.1                          | 1.40                                | 11.4               | 29.7              |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m-oiv7.pt) | 640                   | 33.6                 | 408.5                          | 2.26                                | 26.2               | 80.6              |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l-oiv7.pt) | 640                   | 34.9                 | 596.9                          | 2.43                                | 44.1               | 167.4             |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x-oiv7.pt) | 640                   | 36.3                 | 860.6                          | 3.56                                | 68.7               | 260.6             |

#### Training

We conducted training over 200 epochs on the training set, with
continuous monitoring of model performance using mean Intersection over
Union (IoU), Box Precision, and Box Recall as primary metrics, utilizing
the validation set. To enhance model robustness and generalization, we
employed various common data augmentation techniques, including random
horizontal flipping, random cropping, mosaic image aggregation,
rotation, color filtering, among others.

![Data Augmentation](/images/posts/bear_detection/data_augmentation/mosaic_rotation.jpg)
*Data augmentation during training - Mosaic, rotation, etc*

Throughout the training process, these metrics were continuously
evaluated on both the training and validation sets.

![Training Results](/images/posts/bear_detection/training_results.png)

#### Evaluation

The evaluation is conducted on the test set, and the performance is
reported using a confusion matrix. In this evaluation, the model acts as
a binary classifier: if the probability of a bear being localized
exceeds a specific threshold, the image is classified as containing a
bear.

![Confusion Matrix Normalized - imgsz 1024](/images/posts/bear_detection/speed_accuracy_tradeoff/1024/confusion_matrix_normalized.png)
*Confusion Matrix Normalized - imgsz 1024*

### Inference Speed vs Model Accuracy

The real-time requirement of this system necessitates careful consideration of
the tradeoff between inference speed and model accuracy. Opting for a larger
model operating on a full image frame of the video feed can deliver superior
accuracy but at the expense of slower processing speed. Evaluating this
tradeoff was crucial in selecting the most suitable model for the task.

![Inference Speed vs Model Accuracy](/images/posts/bear_detection/speed_accuracy_tradeoff/tradeoff.png)
*Inference speed and model accuracy tradeoff on the Raspberry Pi 5*

## Conclusion

This guide has outlined the methodology employed to construct an
advanced Machine Learning model for real-time bear detection. The
Exploratory Data Analysis phase meticulously addressed various data
quality concerns within the dataset and examined multiple modeling
strategies. Utilizing GroundingDINO proved instrumental in swiftly
annotating the camera trap images. Furthermore, we underscored the
significance of striking a balance between speed and accuracy when
selecting a model suitable for deployment on low-power devices.

Notably, this framework possesses the potential to transcend bear
management, offering promising avenues for mitigating human-wildlife
conflicts across a spectrum of species.
