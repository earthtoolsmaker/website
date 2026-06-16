---
title: How to detect elephant rumbles at scale
description: Learn how to leverage audio processing to localize elephant rumbles on terabytes of data.
date: 2024-06-29
params:
  math: true
image: /images/posts/how-to-detect-elephant-rumbles-at-scale/cover2.png
tags: ["AI", "audio"]
spectrogram_reasons:
  - name: Frequency–time view
    desc: "A spectrogram shows which frequencies are present and how they change over time — exactly what tasks like sound-event detection need."
  - name: Visual features
    desc: "Turning audio into an image lets convolutional networks bring their powerful pattern-recognition to bear on sound."
  - name: Noise robustness
    desc: "Seeing the frequency content makes it easier for a model to focus on the signal and ignore the noisy parts of a recording."
  - name: Task adaptation
    desc: "Spectrograms can be tuned per task — Mel-spectrograms for speech and music, for instance — to highlight the features that matter."
---

This post walks through the development of an elephant rumble audio analyzer,
built in partnership with [The Elephant Listening
Project](https://www.elephantlisteningproject.org).

> Our vision is to conserve the tropical forests of Africa through acoustic
> monitoring, sound science, and education, focusing on forest elephants
>
> <cite>– The Elephant Listening Project</cite>

For a comprehensive understanding of this project, one can read more on the
detailed project page on [passive acoustic monitoring for forest elephants]({{<
ref "/projects/elephants_passive_acoustic_monitoring" >}}).

## What is sound?

Sound is produced by variations in air pressure. These pressure variations can
be measured and plotted over time to create a visual representation of the
sound.

Sound waves often repeat at regular intervals, forming patterns where each wave
has the same shape. The height of these waves, known as amplitude, indicates
the intensity of the sound.

![A sound wave as a variation of air pressure, labeled with amplitude and period](./images/sound.svg)
*A soundwave as a variation of air pressure*

The time required for a signal to complete one full wave is called the period.
The number of waves produced by the signal in one second is known as the
frequency. Frequency is the reciprocal of the period and is measured in Hertz
(Hz).

Most sounds we encounter do not follow simple, regular periodic patterns.
However, signals of different frequencies can be combined to form composite
signals with more complex repeating patterns. All the sounds we hear, including
the human voice, are made up of such composite waveforms.

![The amplitude of a recorded elephant rumble over time](./images/elephant_rumble_waveform.svg)
*Elephant rumble recorded in an African forest*

### Encoding sound digitally

To digitize a sound wave, the signal is converted into a series of numbers.
This process involves measuring the amplitude of the sound at regular time
intervals.

![A continuous signal sampled at regular intervals into discrete values](./images/signal_sampling.svg)
*A continuous signal, sampled at regular intervals into discrete values*

Each measurement is called a sample, and the sampling rate is the number of
samples taken per second. For example, a common sampling rate is 44,100 samples
per second. This means a 10-second music clip would contain 441,000 samples.

### Human hearing range

The human ear can detect sounds within a specific range of frequencies,
typically from about 20 Hz to 20,000 Hz (20 kHz). Sounds below this range are
known as infrasounds, while sounds above this range are referred to as
ultrasounds.

![The frequency spectrum split into infrasound, the human audible range, and ultrasonic](./images/sound_frequencies.svg)
*Audible range for humans, between infrasound and ultrasonic*

__Infrasounds__, with frequencies below 20 Hz, are used by animals like elephants.
Elephants communicate using these low-frequency sounds, which can travel long
distances and penetrate through obstacles like dense vegetation.

On the other end of the spectrum, __ultrasounds__ have frequencies above 20 kHz.

Bats are well-known for their use of ultrasound in echolocation. They emit
high-frequency sound waves that bounce off objects and return as echoes,
allowing bats to navigate and hunt in complete darkness.

Human hearing is limited compared to these examples, but our ability to
perceive a wide range of frequencies is crucial for understanding speech,
enjoying music, and detecting environmental sounds.

### Spectrograms

A spectrogram is a visual representation of the frequency content of a
sound signal over time. It provides a detailed picture of how the
different frequencies present in the sound change and evolve.

To understand the relationship between a spectrogram and a raw audio waveform, let's break down the process:

1. **Raw Audio Waveform**: The raw audio waveform is a plot of the
amplitude of the sound signal over time. It shows how the pressure
variations (which we perceive as sound) fluctuate. While the waveform
gives a clear representation of the sound's amplitude at each moment, it
doesn't provide detailed information about the frequency components of
the sound.

2. **Spectrogram**: To create a spectrogram from the raw audio waveform,
the sound signal is divided into small time segments, typically using a
process called the Short-Time Fourier Transform (STFT). Each segment is
analyzed to determine the frequencies present and their respective
amplitudes.

![Time vs Frequency](./images/FFT-Time-Frequency-View.png "Time Frequency view")
*Fourier Transform Frequency View*

In a spectrogram:

- The horizontal axis represents time.
- The vertical axis represents frequency.
- The intensity or color at each point represents the amplitude of a particular frequency at a given time.

This visualization allows us to see how the frequencies of a sound
change over time. For example, in a speech signal, we can observe the
varying frequencies produced by different phonemes, while in music, we
can see the different notes and their harmonics.

### Machine Learning and audio

State-of-the-art techniques in audio processing with machine learning convert
raw waveforms into images and utilize computer vision methods. Most audio
applications transform raw audio waveforms into spectrograms before inputting
the data into vision models. Examples include the bird classifier
[BirdNet](https://birdnet.cornell.edu/) and [Rainforest
Connection](https://rfcx.org/), which help prevent illegal deforestation and
perform bioacoustic monitoring.

As a result, spectrograms are vital in audio deep learning because they
transform audio signals into a format that is more suitable for analysis by
machine learning models, especially those based on deep learning techniques.

Spectrograms matter for a few reasons — tap each:

{{< threats "spectrogram_reasons" >}}

## Elephant Rumbles

Elephant rumbles are low-frequency vocalizations produced by elephants,
primarily for communication.

![Spectrogram of two elephant rumbles shown as stacks of harmonics, mostly below the infrasound boundary](./images/elp_spectrogram_rumble.svg)
*Spectrogram of two elephant rumbles*

- Two elephant rumbles are shown as stacks of parallel lines.
- The white line marks the upper boundary of infrasound, indicating frequencies
below this line are inaudible to humans.
- The bracketed areas represent the speaking frequency ranges for men (70-200
Hz) and women (140-400 Hz).
- The stacks of lines above the white line represent the harmonics of the
fundamental frequency, which in these calls is infrasonic.

Have a listen:

<audio controls src="audio/rumble.mp3"></audio>


These rumbles are a fundamental part of elephant
social interactions and serve various purposes within their groups. Here’s a
detailed explanation:

### Characteristics of Elephant Rumbles

<div class="support__grid">
  <div class="support__card">
    <h3 class="support__card-title">Low frequency</h3>
    <p class="support__card-description">Most rumbles sit in the infrasound range, below 20 Hz — often beneath the threshold of human hearing, though some carry a low, throaty edge we can hear.</p>
  </div>
  <div class="support__card">
    <h3 class="support__card-title">Long-distance</h3>
    <p class="support__card-description">Their low frequency lets rumbles travel several kilometres and pass through dense forest, so elephants stay in contact even out of sight.</p>
  </div>
  <div class="support__card">
    <h3 class="support__card-title">Vocal production</h3>
    <p class="support__card-description">Produced by the larynx, rumbles vary in frequency, duration, and modulation — different rumbles carry different messages.</p>
  </div>
</div>

### Functions of Elephant Rumbles

<div class="support__grid">
  <div class="support__card">
    <h3 class="support__card-title">Coordination &amp; bonding</h3>
    <p class="support__card-description">Rumbles keep the herd in contact, coordinate movement, and reinforce social bonds — a matriarch might lead the group with one.</p>
  </div>
  <div class="support__card">
    <h3 class="support__card-title">Reproduction</h3>
    <p class="support__card-description">Bulls rumble to advertise their readiness to mate; females signal their estrus status to potential mates.</p>
  </div>
  <div class="support__card">
    <h3 class="support__card-title">Alarm &amp; distress</h3>
    <p class="support__card-description">Rumbles can warn of danger, mobilising the herd and prompting protective behaviour.</p>
  </div>
  <div class="support__card">
    <h3 class="support__card-title">Mother &amp; calf</h3>
    <p class="support__card-description">Mothers and calves rumble to stay in contact when separated; a calf may rumble to signal hunger or distress.</p>
  </div>
</div>

## Designing an ML pipeline to process large audio files

About 50 sound recorders are recording forest sounds around the clock in a
forest in Congo. Terabytes of data are commonly generated in about a couple of
months. Being able to process this amount of audio data fast and with accuracy
is key to monitor the forest elephant population.

![The passive acoustic monitoring pipeline: a microphone catches a rumble, 50 mics record around the clock, the model detects each rumble, and its source is located](/images/projects/forest_elephants_passive_acoustic_monitoring/diagrams/pipeline.svg)
*From microphone to located rumble — the passive acoustic monitoring pipeline*

The system must be capable of analyzing terabytes of data within a few hours.
The primary bottlenecks in the data pipeline are:

- __Spectrogram Generation:__ Converting raw audio into spectrograms that
accurately capture the frequency range relevant for detecting elephant rumbles.
- __Model Inference:__ Performing object detection on these spectrograms to
identify elephant rumbles and report bounding boxes with associated
probabilities.

To address these bottlenecks, the pipeline should:

1. Generate spectrograms in the 0-250 Hz frequency range, which encompasses all
   elephant rumbles.
2. Apply the rumble object detector to batches of these spectrograms.
3. Save the detection results, including bounding boxes and probabilities, into
   a CSV file.

| Spectrogram | Prediction |
|:-----------:|:----------:|
| ![Spectrogram 0](./images/spectrograms/spectrogram_0.png) | ![Prediction 0](./images/predictions/prediction_0.png) |
| ![Spectrogram 1](./images/spectrograms/spectrogram_1.png) | ![Prediction 1](./images/predictions/prediction_1.png) |
| ![Spectrogram 2](./images/spectrograms/spectrogram_2.png) | ![Prediction 2](./images/predictions/prediction_2.png) |

Below is a sample of a generated CSV file:

| freq_start | freq_end  | t_start | t_end    |  probability | audio_filepath                                |
|-----------:|:---------:|:-------:|:--------:|:------------:|:---------------------------------------------:|
|  185.3     | 238.9     | 6.1     | 11.5     | 0.78         |  data/08_artifacts/audio/rumbles/sample_0.wav |
|  187.4     | 237.1     | 107.4   | 112.3    | 0.77         |  data/08_artifacts/audio/rumbles/sample_0.wav |
|  150.8     | 238.4     | 89.0    | 94.3     | 0.69         |  data/08_artifacts/audio/rumbles/sample_0.wav |
|  203.1     | 231.6     | 44.1    | 47.5     | 0.65         |  data/08_artifacts/audio/rumbles/sample_0.wav |
| ...        | ...       | ...     | ...      | ...          |  ...                                          |

### Provided dataset

The [Elephant Listening Project](https://www.elephantlisteningproject.org)
provided hundreds of gigabytes of annotated audio files recorded in the African
forest. These files were annotated using two distinct approaches. The first set
was annotated using their current machine learning (ML) model, while the second
set was meticulously annotated and reviewed by human experts. The annotations
were exported from [RavenPro](https://www.birds.cornell.edu/ccb/raven-pro/), a
comprehensive software tool for visualizing and analyzing audio recordings,
widely used in bioacoustic research.

![Dataset Overview](./images/dataset.png)
*Provided dataset as raw audio files and annotations from RavenPro*

The ML model-generated annotations typically identify most sound patterns
within the 0-250 Hz frequency range but exhibit issues with overlapping rumbles
and occasional false positives. Conversely, the human-curated dataset, though
smaller, offers much higher quality annotations, despite some rumbles being
unannotated. This meticulous attention to overlapping rumbles in the human
annotations provides a valuable resource for training accurate ML models.

Given the higher quality of the human-curated dataset, we chose to use it for
training and evaluating our ML models. To prepare the model inputs for
training, the provided dataset needs to be transformed into an image dataset of
spectrograms with bounding boxes that localize the rumbles.

#### Exploratory Data Analysis

Before training, we explored the dataset to understand the rumbles we were
working with. A few findings shaped the rest of the pipeline:

- __Rumble Duration:__ The typical duration of an elephant rumble ranges from 2
to 6 seconds, with some lasting up to 10 seconds. This information is
crucial for determining the length and overlap of generated spectrograms.
- __Frequency Range:__ All elephant rumbles occur within the 0-250 Hz frequency
range. By focusing on this range, we can optimize spectrogram generation by
excluding irrelevant frequencies.
- __Communication Timing:__ Elephants primarily communicate with rumbles during
dawn and dusk, when ambient noise is lower, allowing their low-frequency calls
to travel more effectively. Consequently, the majority of our data points are
concentrated at these times, which will guide our data splitting strategy.

#### Data split

We implemented a standard 80/10/10 data split on the provided dataset to ensure
effective model evaluation. To prevent data leakage between training and
testing phases, we meticulously split the audio files into non-overlapping time
ranges. Each annotated audio file is divided into three distinct time segments:
80% of the rumbles are allocated to the training set, 10% to the validation
set, and 10% to the testing set.

![An 80/10/10 split of a 24-hour audio file into non-overlapping training, validation, and testing segments](./images/data_split.svg)
*80/10/10 split of a 24-hour audio file into 3 non-overlapping segments*

### Fast Spectrogram Generation

Spectrograms are a fundamental tool in audio analysis, providing a visual
representation of the spectrum of frequencies in a sound signal as it varies
with time. Generating spectrograms quickly and efficiently is crucial in
numerous applications such as speech recognition, music analysis, and
environmental sound classification. Fast spectrogram generation allows for
real-time processing and analysis of audio signals, which is essential in
scenarios where immediate feedback is necessary, such as live sound monitoring
and interactive audio applications.
Two powerful libraries for generating spectrograms in Python are `librosa` and
`torchaudio`.

#### [Librosa](https://librosa.org/)

`librosa` is a widely-used library in the audio analysis
community, known for its user-friendly interface and comprehensive suite of
tools for audio processing. It provides robust functions for loading audio
files, computing spectrograms, and various other audio transformations.

<p style="text-align:center; margin: 24px 0;">
  <img src="./images/logo/librosa.png" alt="Librosa logo" style="max-width: 160px; width: 100%;" />
</p>

We began evaluating spectrogram generation using the librosa library. Loading
raw audio files proved to be slow because librosa, by default, operates in a
single-threaded manner, utilizing only one CPU core. Additionally, while
generating spectrograms as images is time-consuming, the resulting visuals are
highly aesthetic, thanks to the ability to apply various color maps.

![Librosa Spectrogram](./images/generation/librosa/spectrogram.png)
*Spectrogram generated with Librosa*

To enhance efficiency, we designed and implemented a multiprocessing pipeline
that leverages all available CPU cores for loading audio files and generating
spectrograms. On a 10-core machine, this approach resulted in approximately a
tenfold increase in speed. However, maintaining such a multiprocessing pipeline
can be complex. As an alternative, we considered using the torchaudio library,
which natively supports multiprocessing and GPU acceleration. We aimed to
compare the performance of both libraries to make an informed decision on the
best approach for our needs.

#### [TorchAudio](https://pytorch.org/audio/stable/index.html)

`torchaudio`, on the other hand, is a part of the PyTorch ecosystem, which
allows for seamless integration with deep learning models. It is optimized for
performance and can leverage GPU acceleration to speed up spectrogram
generation and other audio processing tasks.

<p style="text-align:center; margin: 24px 0;">
  <img src="./images/logo/torchaudio.png" alt="TorchAudio logo" style="max-width: 200px; width: 100%;" />
</p>

Loading raw audio files with torchaudio is significantly faster because it
uses multiple cores by default, and spectrogram generation is quicker too — with
GPU acceleration speeding it up further. After benchmarking both, we chose
torchaudio for its speed, GPU support, and tight fit with our PyTorch stack.

Loading a 24-hour raw audio file takes approximately 4 seconds, while
generating 560 spectrograms to cover the entire recording takes around 11
seconds using torchaudio.

![Torchaudio Spectrogram](./images/generation/torchaudio/spectrogram_0.png)
*Spectrogram generated with Torchaudio*

### Fast ML model inference

By adopting our approach, we have transitioned from dealing with raw audio data
to addressing an object detection problem using spectrograms. Although there is
a minor preprocessing cost involved in converting audio waveforms into
spectrograms, this shift simplifies the problem to a well-understood computer
vision challenge.

![Localizing rumbles on Spectrograms](/images/projects/forest_elephants_passive_acoustic_monitoring/spectrograms/rumbles_intro.png "Localizing rumbles on spectrograms")
*Visual detection of elephant rumbles in spectrograms*

#### YOLO Overview

We took a pretrained
[YOLOv8](https://github.com/ultralytics/ultralytics) model and fine-tuned it for
our object detection task. YOLOv8 is fast, accurate, and easy to work with, and
it handles a range of tasks — object detection, tracking, instance
segmentation, image classification, and pose estimation.

![A spectrogram goes into the detection model and comes out with rumbles boxed and scored](/images/projects/forest_elephants_passive_acoustic_monitoring/diagrams/detection.svg)
*Detection on a spectrogram: an audio frame in, boxed and scored rumbles out*

#### Spectrogram Generation and YOLOv8 Model Constraints

Pretrained YOLOv8 models require square images resized to 640 pixels. We face a
trade-off between speed and accuracy when generating spectrograms. A smaller
time range in each spectrogram yields higher resolution for detecting elephant
rumbles, but requires generating more spectrograms to cover the entire time
span.

Given that elephant rumbles typically last between 2 to 6 seconds, with some
extending up to 10 seconds, a larger time range in a 640-pixel wide spectrogram
can make these rumbles difficult to detect. To balance these factors, we
decided to cover a 164-second time range in each 640-pixel wide spectrogram.
Additionally, each spectrogram overlaps the next by 10 seconds, which
corresponds to the maximum rumble duration and helps in deduplicating predicted
rumbles.

![560 generated spectrograms](./images/spectrograms_generation.svg)
*Generation of 560 spectrograms to cover the 24-hour time range*


This approach results in the generation of approximately 560 spectrograms to
cover a full 24-hour period.

### Inference Speed and Performance Optimization

The model is designed to process batches of spectrograms simultaneously,
utilizing multiprocessing when no GPU is available and leveraging GPU
acceleration when present. Through experimentation, we determined an optimal
batch size that balances memory usage with inference speed. With this setup,
the model can process the 560 spectrograms in under 20 seconds on an 8-core
machine and in under 4 seconds when using a GPU.

The table below provides a summary of the overall pipeline speed on a 24-hour
audio file, highlighting the two key bottlenecks: spectrogram generation and
model inference.

| Pipeline Step                  | GPU      | CPU (8 cores) |
|--------------------------------|----------|---------------|
| Load the audio file            | 4s       | 4s            |
| Generate the spectrograms      | 11s      | 11s           |
| Run the model inference        | __4s__   | 19s           |
| Miscellaneous tasks            | 1s       | 1s            |
| Total for a 24-hour audio file | __20s__  | 35s           |
| Total for 1TB of audio data    | __8.3h__ | 14.6h         |

> Analyzing months of audio recordings can now be done in a matter of
> hours, not weeks!

1 terabyte of audio data currently represents one month of recordings collected
from 50 microphones distributed throughout the forest.

## Conclusion

This article outlines the engineering approach used to develop a
state-of-the-art elephant rumble detector with a strong emphasis on
speed. Designing efficient data pipelines is crucial in conservation
efforts, where vast amounts of data are continuously generated. The
[open-source tools](https://github.com/earthtoolsmaker/forest-elephants-rumble-detection)
developed in this project make a significant contribution to advancing global
conservation initiatives. Moreover, the methods and techniques presented can be
adapted to various conservation applications, including rare species
identification and biodiversity monitoring.

You can try the detector yourself — the interactive demo runs the full
spectrogram-and-detection pipeline right in your browser.

{{< demo_cta "/demos/forest_elephant_rumble_detection/" >}}
