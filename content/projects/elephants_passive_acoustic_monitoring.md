---
title: Forest Elephants Passive Acoustic Monitoring
summary: Conservation efforts struggle to monitor forest elephants in dense rainforests, with acoustic monitoring providing a promising solution via accurate, user-friendly detection systems that aid in population monitoring and anti-poaching efforts while mitigating human-elephant conflicts.
tagline: Finding forest elephants — and poachers — by sound, across Central Africa's rainforest.
stats:
  - value: "60%"
    label: lost in a decade
  - value: "50"
    label: microphones
  - value: "24/7"
    label: listening
clients:
  - name: Elephant Listening Project
    link: https://www.elephantlisteningproject.org/
    logo: /images/clients/elephantlistening/logo.png
  - name: CornellLab
    link: https://www.birds.cornell.edu/
    logo: /images/clients/cornell_lab/logo.svg
related_posts:
  - how-to-analyze-elephant-rumbles-at-scale
github_repo: https://github.com/earthtoolsmaker/forest-elephants-rumble-detection
space: /demos/forest_elephant_rumble_detection/
tools:
  - Bio Acoustics
  - Passive Acoustic Monitoring
  - Machine Learning
threats:
  - name: Ivory poaching
    desc: "Forest-elephant ivory is prized for its hardness and rose-coloured tint, driving targeted killing — more than 12,000 elephants a year. It is hard to detect in dense, poorly-protected forest."
  - name: Bushmeat trade
    desc: "Hunting elephants for meat has grown into an international business, threatening animals of all ages, including calves, as human populations grow."
  - name: Resource extraction
    desc: "Logging, mining and oil extraction are the most pervasive industry pressure, reshaping the forest elephants depend on."
  - name: Roads &amp; access
    desc: "Roads cut for extraction open once-remote forest interiors to hunters and settlement, multiplying the threat to elephants deep in the range."
  - name: Slow reproduction
    desc: "Forest elephants breed slowly, so populations recover far more slowly than they are being lost — compounding every other pressure."
status: completed
pinned: true
weight: 3
date: 2024-06-26
image: /images/projects/forest_elephants_passive_acoustic_monitoring/cover.png
---

Forest elephants are vanishing: more than **60% have been lost in the past
decade**, and over **12,000 are killed each year** for their ivory. The hardest
part of protecting them is simply knowing where they are. In the vast, dense
rainforests of Central Africa they are nearly impossible to see — so instead of
watching for them, we listen.

Working with the [Elephant Listening
Project](https://www.elephantlisteningproject.org/) and the [Cornell Lab of
Ornithology](https://www.birds.cornell.edu/), we built open-source tools that
scan terabytes of forest audio to automatically detect and localize elephant
**rumbles** — turning sound into the population and anti-poaching data that
conservation has been missing.

> Our vision is to conserve the tropical forests of Africa through acoustic
> monitoring, sound science, and education, focusing on forest elephants.
>
> <cite>– The Elephant Listening Project</cite>

![From a rumble to a located elephant — the acoustic monitoring pipeline](/images/projects/forest_elephants_passive_acoustic_monitoring/diagrams/pipeline.svg)
*Microphones across the forest record around the clock, a model finds rumbles in
the audio, and the array pinpoints where each call came from.*

![A forest elephant in the rainforest undergrowth](/images/projects/forest_elephants_passive_acoustic_monitoring/main.jpg)
*A forest elephant melts into the dense undergrowth — exactly why they are so
hard to see, and why listening works where watching can't.*

## Why forest elephants matter

Forest elephants are ecosystem engineers: the rainforest is shaped by their
daily lives, and unravels without them.

<div class="support__grid">

  <div class="support__card">
    <h3 class="support__card-title">Forest gardeners</h3>
    <p class="support__card-description">They eat fruit and spread seeds across huge distances, and their movement opens clearings and trails — keeping the forest diverse, regenerating, and in balance.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Climate &amp; water engineers</h3>
    <p class="support__card-description">By promoting forest growth they help these forests store carbon, and by digging for water in dry riverbeds they create water holes that sustain other species through the dry season.</p>
  </div>

  <div class="support__card">
    <h3 class="support__card-title">Biodiversity backbone</h3>
    <p class="support__card-description">Their nutrient-rich dung fertilises the soil and feeds insects and fungi, while the dynamic habitats they maintain let countless plants and animals thrive.</p>
  </div>

</div>

## Under pressure

Forest elephants face pressure from every side — and their slow reproductive
rate means losses are hard to recover from. Tap each pressure to learn more.

{{< threats >}}

![A basket of rhino horns beside burning elephant ivory, Kenya 2016](/images/projects/forest_elephants_passive_acoustic_monitoring/threats/poaching-trophies.jpg)
*A basket of rhino horns next to a pyre of burning elephant ivory in Kenya,
2016. Photo: Ben Curtis, AP.*

> We have lost 60% of all forest elephants in the past decade.
>
> <cite>– The Elephant Listening Project</cite>

## What a rumble is

Rumbles are the low-frequency calls elephants use to communicate. Much of a
rumble sits in the **infrasound** range — below 20 Hz, often beneath the
threshold of human hearing.

![Spectrogram of elephant rumbles](/images/projects/forest_elephants_passive_acoustic_monitoring/spectrograms/rumbles_intro.png)
*A spectrogram of elephant rumbles — the low-frequency energy that carries
across the forest.*

Because their wavelength is so long, rumbles travel several kilometres and pass
through dense forest, letting elephants stay in contact across vast areas they
cannot see across. They use them to coordinate and bond as a herd, to signal
readiness to mate, to raise the alarm at danger, and to keep mothers and calves
together. That same far-carrying signal is what makes the forest listenable: if
we can reliably pick rumbles out of the noise, we can find elephants.

## Detecting rumbles at scale

Fifty microphones are arranged in a grid across the tropical forest, recording
continuously. The challenge is the sheer volume of audio — and the answer is a
model that finds rumbles in a spectrogram the way an object detector finds
objects in a photo.

![How the model turns a spectrogram into detected rumbles](/images/projects/forest_elephants_passive_acoustic_monitoring/diagrams/detection.svg)
*Each chunk of audio becomes a spectrogram; the model boxes every rumble and
scores it.*

The [open-source tools](https://github.com/earthtoolsmaker/forest-elephants-rumble-detection)
process audio in batch across all available CPU and GPU cores, so a 24-hour
recording is scanned in around 20 seconds. At that speed, a full month of
audio from all 50 recorders — roughly **1 TB** — is analysed in about
**8 hours** rather than weeks of manual review.

| Spectrogram | Detected rumbles |
|:-----------:|:----------------:|
| ![Spectrogram](/images/projects/forest_elephants_passive_acoustic_monitoring/spectrograms/spectrogram_0.png) | ![Rumble predictions](/images/projects/forest_elephants_passive_acoustic_monitoring/predictions/prediction_0.png) |
| ![Spectrogram](/images/projects/forest_elephants_passive_acoustic_monitoring/spectrograms/spectrogram_2.png) | ![Rumble predictions](/images/projects/forest_elephants_passive_acoustic_monitoring/predictions/prediction_2.png) |

> Analyzing months of audio recordings can now be done in a matter of hours, not
> weeks.

We cover how the detector was built and run in the companion post on
[analyzing elephant rumbles at scale]({{< ref "/posts/how-to-analyze-elephant-rumbles-at-scale" >}}).

## Conclusion

Listening turns the hardest part of forest-elephant conservation — finding
animals that can't be seen — into continuous, non-invasive data. Around-the-clock
acoustic monitoring reveals where elephants are over time, surfaces signs of
poaching, and gives rangers and researchers the evidence they need to act, at a
scale and cost that field surveys never could.

{{< demo_cta >}}
