---
title: "How to prepare data for identification?"
description: An in-depth look at the common preprocessing stages required to perform identification using computer vision.
date: 2024-12-08
image: /images/posts/how-to-prepare-data-for-identification/cover.png
tags: ["AI", "vision", "identification"]
augmentations:
  - name: Random Scaling
    desc: "Varying the size of the images to simulate different distances from the camera."
  - name: Random Rotation
    desc: "Rotating images by a random angle to account for variations in orientation."
  - name: Mosaic
    desc: "Combining multiple images into a single mosaic to create a more complex training example."
  - name: Flipping
    desc: "Flipping images horizontally or vertically to introduce mirror variations."
  - name: Color Jittering
    desc: "Randomly adjusting brightness, contrast, saturation, and hue to simulate different lighting conditions."
  - name: Cropping
    desc: "Randomly cropping sections of the image to focus on different parts of the animal, helping the model learn features in varied contexts."
  - name: Gaussian Noise
    desc: "Adding random noise so the model is more resilient to variations in input quality."
---

In this post, we will explore essential preprocessing techniques for
normalizing animal images, preparing them for individual identification.

We will focus on the initial stages of the machine learning pipelines developed
for various projects, specifically bear and trout identification. In both
cases, similar computer vision techniques and strategies were employed to
successfully create robust identification systems.

![Identification Pipeline Overview](/images/projects/bear_identification/pipeline.png)
*Overview of the ML pipeline to identify __bears__ using their facial
markings with Metric Learning*

In the [bear identification project]({{< ref "projects/bear_identification.md"
>}}), the processing stage encompasses bear face detection, head segmentation,
and head normalization.

![ML Pipeline for Trout Identification](/images/projects/trout_identification/pipeline.png)
*Overview of the ML pipeline developed to identify __trouts__ using
their spot patterns with Local Feature Matching*

In the [trout identification project]({{< ref
"projects/trout_identification.md" >}}), the processing stage includes trout
detection, pose estimation, and image normalization.

Both projects use similar preprocessing techniques, detailed and illustrated
throughout this post.

## Segmentation

To identify individuals reliably, we first isolate the animal and strip away the
background. This lets the identification model focus only on the signal that
matters — the markings — instead of being distracted by surrounding pixels.

In the case of bears, both existing literature and our research indicate that
their facial markings and shapes are unique, making them effective for
individual identification. Similarly, for trout, individuals can be identified
by their distinct and stable spot patterns.

### Segmentation 101

Semantic segmentation assigns a class label to each pixel in an image,
such as 'person,' 'dog,' or 'flower,' grouping together pixels of the
same class. Conversely, instance segmentation distinguishes between
individual instances of objects within the same class, treating each one
as a separate entity.

![Semantic Segmentation vs Instance Segmentation](./images/semantic_segmentation_vs_instance_segmentation.png)
*Semantic segmentation vs Instance segmentation*

Instance segmentation techniques are generally more effective for isolating
individual subjects in images.

### GroundingDINO + SAM = Mask Dataset

Generating a segmentation dataset for a diverse array of animals has become
straightforward by combining an open-set object detector like GroundingDINO,
which localizes and detects animals using text prompts, with a promptable
segmentation model such as the Segment Anything Model (SAM).

![Generating Bear Face Masks](./images/bears/gdino_sam_pipeline.png)
*Generating Bear Face Masks combining GroundingDINO and SAM*

![Generating Trout Masks](./images/trouts/gdino_sam_pipeline.png)
*Generating Trout Masks combining GroundingDINO and SAM*

Both of these computer vision models are large and tend to run slowly on a CPU.
Therefore, it is often beneficial to use the generated dataset of masks to
train a smaller, faster instance segmentation model capable of localizing and
segmenting the animal in a single pass.

#### GroundingDINO

<a href="https://github.com/IDEA-Research/GroundingDINO">
  <img style="float: left; margin-right: 10px; max-height: 120px;" src="./images/grounding_dino_logo.png" alt="GroundingDINO Logo" />
</a>
<b>GroundingDINO</b> is a multimodal model that combines a Vision Transformer
(ViT) with language grounding. By tying a text prompt to visual features, it
detects and localizes objects from a free-text description rather than a fixed
list of classes — which is exactly what lets it find animals in our images
without a purpose-trained detector.

<br style="clear:both;"/>
<br />

#### Segment Anything Model - SAM

The __Segment Anything Model__ (SAM) produces high quality object masks
from input prompts such as points or boxes, and it can be used to
generate masks for all objects in an image. It has been trained on a
dataset of 11 million images and 1.1 billion masks, and has strong
zero-shot performance on a variety of segmentation tasks.

![SAM example](./images/sam_mask_sample.jpg)
*SAM Github / SAM output example*

### Finetune an Instance Segmentation model

Once the dataset of masks is generated using GroundingDINO and SAM, the next
step is to train a compact model that can perform both tasks simultaneously and
operate efficiently on a CPU. Enter YOLO!

#### YOLO Overview

[YOLO](https://github.com/ultralytics/ultralytics) is a fast, accurate, and
widely used computer-vision model. It excels at a range of tasks — object
detection, tracking, and image classification — and, crucially for us, instance
segmentation: it not only identifies and localizes objects but also separates
individual instances. It is easy to use and efficient enough for real-time work,
which makes it a strong fit for segmenting our animals on a CPU.

![YOLOv8 CV Tasks](./images/yolov8_tasks.png)
*YOLOv8 Computer Vision Tasks*

#### Training

##### Data Augmentation

We can employ various data augmentation techniques to artificially
enhance our training set. These techniques help increase the diversity
of the data and improve the model's robustness.

![Eight panels showing the same trout under each augmentation: original, random scaling, random rotation, mosaic, flipping, color jittering, cropping, and Gaussian noise](./images/augmentations.svg)
*The same fish under each augmentation — the model learns to recognize it through all of these variations*

Tap each method to see what it does:

{{< threats "augmentations" >}}

By applying these augmentation techniques before feeding the images to the
model, we can significantly enhance the training dataset, leading to improved
model performance and generalization.

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/segmentation/model/train_batch0.jpg" loading="lazy" alt="Batch 0" title="Annotated Dataset - Batch 0">
    <img src="./images/segmentation/model/train_batch1.jpg" loading="lazy" alt="Batch 1" title="Annotated Dataset - Batch 1">
    <img src="./images/segmentation/model/train_batch2.jpg" loading="lazy" alt="Batch 2" title="Annotated Dataset - Batch 2">
    <img src="./images/segmentation/model/train_batch910.jpg" loading="lazy" alt="Batch 910" title="Annotated Dataset - Batch 910">
  </div>
  <em>Data Augmentation (rotation, scaling, cropping) of the annotated trout dataset - Random batches.</em>
</div>

##### Training Results

Typically, training a satisfactory segmentation model requires only a
relatively small number of epochs. This allows for efficient model
development while still achieving effective performance on the task.

![Finetuning of a Segmentation Model on Trouts](./images/segmentation/model/results.png#noround)
*Results of the training of a segmentation model on trouts for 100 epochs*

##### Qualitative Results

A qualitative evaluation of segmentation model was conducted on a random
batch from the validation set. The results demonstrate that the model
performs with high accuracy, effectively localizing and segmenting out
trouts.

| Ground Truth | Prediction |
|:------------:|:----------:|
| ![Val batch 0 label](./images/segmentation/model/val_batch0_labels.jpg) | ![Val batch 0 pred](./images/segmentation/model/val_batch0_pred.jpg) |

## Normalization

Producing normalized images for the identification stage is critical. It makes it easier to compare different individuals in a consistent manner and it boosts the model accuracy.

For bears, the head crops must be resized and padded to a fixed size, since the identification model expects fixed-size input. With a segmentation mask in hand this is straightforward: cut out the head and pad the result with black pixels to reach that size.

![Generated Chips](./images/bears/chips.png)
*Normalized bear faces*

For trouts, we want to realign the fish to face the same direction and then apply the segmentation masks to cut out the background too.

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/trouts/normalized/2.webp" loading="lazy" alt="Normalized Trout 2">
    <img src="./images/trouts/normalized/3.webp" loading="lazy" alt="Normalized Trout 3">
    <img src="./images/trouts/normalized/1.webp" loading="lazy" alt="Normalized Trout 1">
    <img src="./images/trouts/normalized/4.webp" loading="lazy" alt="Normalized Trout 4">
  </div>
  <em>Normalized trouts</em>
</div>

### Rotation

Images often need to be rotated so they all share a consistent angle. This
alignment matters because identification models are sensitive to variations in
rotation.

To determine the appropriate rotation angle for consistent alignment, we can
leverage a class of machine learning models known as pose estimation models.
These models are trained to predict specific anatomical features of the animal,
such as the eye, nose, mouth, tail, and other keypoints. By accurately
localizing these features, we can calculate the required rotation angle to
standardize the orientation of the images.

#### Pose Estimation 101

![Pose Estimation Human Example](./images/pose/pose-estimation-examples.avif)
*Pose estimation to localize the key points on a human body*

Pose estimation is the computer-vision task of working out the spatial
configuration of a subject in an image or video. It pinpoints key points on the
body — joints, facial landmarks — or the orientation of an object. From those
detected keypoints, we can normalize images: realigning them into a consistent
representation based on the pose.

This capability to accurately identify these keypoints with a machine learning
model enables us to realign and normalize images, ensuring that all trout are
oriented in the same direction. Additionally, it allows for the detection of
the side of the trout that is visible in the image, enhancing our ability to
analyze and interpret the data effectively.

![Pose Estimation Trout](./images/pose/keypoints.png)
*Pose estimation to localize the keypoints of a trout: eye, tail, fins*

To realign the trout images, we utilize the predicted keypoints, particularly
the pelvic and anal fins, to determine the appropriate rotation angle needed
for horizontal alignment. By calculating this angle based on the positions of
these keypoints, we can effectively adjust the orientation of the image,
ensuring that the trout is consistently aligned for analysis.

The green line in the images below, drawn between the pelvic and anal fins,
serves as a reference point for rotating the image. This line acts as an
anchor, allowing us to accurately adjust the orientation of the trout for
consistent alignment.

| Original | Keypoints | Rotated | Final |
|:--------:|:---------:|:-------:|:-----:|
| ![Original 1](./images/pose/rotation/1_original.png) | ![Keypoints 1](./images/pose/rotation/1_keypoints.png) | ![Rotated](./images/pose/rotation/1_rotation.png) | ![Final 1](./images/pose/rotation/1_final.png) |
| ![Original 2](./images/pose/rotation/2_original.png) | ![Keypoints 2](./images/pose/rotation/2_keypoints.png) | ![Rotated](./images/pose/rotation/2_rotation.png) | ![Final 2](./images/pose/rotation/2_final.png) |
| ![Original 3](./images/pose/rotation/3_original.png) | ![Keypoints 3](./images/pose/rotation/3_keypoints.png) | ![Rotated](./images/pose/rotation/3_rotation.png) | ![Final 3](./images/pose/rotation/3_final.png) |

#### Finetuning a Pose Estimation model

By utilizing a pretrained model designed for human pose estimation, we can
apply transfer learning techniques to adapt the model for localizing specific
keypoints on trout, such as the eye, pelvic fin, dorsal fin, tail, and others.

We can annotate a small dataset with the identified keypoints that we want the
pose estimation model to learn. For the trout identification project, a few
hundred annotated images proved sufficient to train a highly accurate model.
The annotation process is typically conducted in stages, where an initial model
can bootstrap the expansion of the annotated dataset, allowing for iterative
improvements and enhanced performance over time.

##### Data Augmentation

<div class="gallery-box">
  <div class="gallery">
    <img src="./images/pose/model/train_batch0.jpg" loading="lazy" alt="Batch 0" title="Annotated Dataset - Batch 0">
    <img src="./images/pose/model/train_batch1.jpg" loading="lazy" alt="Batch 1" title="Annotated Dataset - Batch 1">
    <img src="./images/pose/model/train_batch2.jpg" loading="lazy" alt="Batch 2" title="Annotated Dataset - Batch 2">
    <img src="./images/pose/model/train_batch910.jpg" loading="lazy" alt="Batch 910" title="Annotated Dataset - Batch 910">
  </div>
  <em>Data Augmentation (rotation, scaling, cropping) of the annotated trout dataset - Random batches.</em>
</div>

##### Training Results

Typically, only a limited number of epochs are required to train a satisfactory
initial pose estimation model. This foundational model can then be further
enhanced by incorporating additional data points into the annotated dataset,
allowing for continuous improvement in accuracy and performance.

![Finetuning of a Pose Estimation Model on Trouts](./images/pose/model/results.png#noround)
*Results of the training of a pose estimation model for trout keypoints localization for 100 epochs*

##### Qualitative Results

A qualitative evaluation of the pose estimation model was conducted on a
random batch from the validation set. The results demonstrate that the
model performs with high accuracy, effectively identifying and
localizing keypoints on the trout.

| Ground Truth | Prediction |
|:------------:|:----------:|
| ![Val batch 0 label](./images/pose/model/val_batch0_labels.jpg) | ![Val batch 0 pred](./images/pose/model/val_batch0_pred.jpg) |

## Conclusion

In this article, we have explored various standard computer vision
techniques that often complement each other effectively. An open-set
object detector, such as GroundingDINO, combined with a promptable
segmentation model like SAM, can facilitate the curation of a training
mask dataset. If necessary, a smaller segmentation model designed for
real-time performance and capable of running on CPU, such as YOLO, can
be trained on this generated dataset.

Normalizing and standardizing the dataset used for downstream
identification models is crucial. This can be achieved through various
methods, including training a pose estimation model to realign images
based on specific keypoints.

These techniques are versatile and applicable to a wide range of
problems, making them essential tools in the modern computer vision
toolkit.

<div class="about-cta">
  <h3 class="about-cta__title">See these techniques in action</h3>
  <p class="about-cta__description">These preprocessing steps feed our real identification systems — explore the full projects they power.</p>
  <div class="button--cta-container">
    <a class="link-no-decoration" href="/projects/bear_identification/">
      <button class="button button--middle">Bear identification</button>
    </a>
    <a class="link-no-decoration" href="/projects/trout_identification/">
      <button class="button button--middle">Trout identification</button>
    </a>
  </div>
</div>
