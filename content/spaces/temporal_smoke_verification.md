---
title: Temporal Smoke Verification
card_image: /images/pages/spaces/temporal_smoke_verification/card.svg
summary: Watching camera sequences over time to tell genuine wildfire smoke from look-alikes.
github_repo: https://github.com/pyronear/temporal-model
date: 2026-06-12
project: /projects/early_forest_fire_detection/
hf_space: achouffe-temporal-smoke-pyronear
hf_space_code: https://huggingface.co/spaces/achouffe/temporal-smoke-pyronear/tree/main
gradio_js_version: 6.18.0
manual_steps:
  - step_name: Pick a sequence
    description: Choose one of the real camera sequences — two early wildfires and two false-positive look-alikes (clouds, haze).
  - step_name: Watch it play
    description: The sequence loops automatically. Each box is a tracked candidate ("tube"), colored by the verdict — orange means judged smoke, gray means rejected.
  - step_name: See what the classifier sees
    description: Below the animation, each tube's stabilized crops are laid out over time — the background holds still, so the only thing moving is the candidate.
  - step_name: Run the model live (optional)
    description: Re-run the full pipeline from scratch on the Space's hardware to verify the precomputed results.
---
