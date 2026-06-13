# Contact page — social links polish

**Date:** 2026-06-13
**Branch:** `worktree-arthur+contact-links-polish`

## Goal

Refine the GitHub / HuggingFace links on the contact page so they read as
lightweight secondary navigation rather than bold buttons, are visually
separated, and explain where each link leads.

## Changes

### 1. Tooltip copy (`config.toml`)
Add a `description` field to each `[[params.social]]` entry:

- **GitHub** → "Browse our open-source conservation code on GitHub"
- **HuggingFace** → "Try our ML models & demos on HuggingFace"

### 2. Markup (`layouts/_default/contact.html`)
On each `.contact-channels__link`, when a `description` exists, render it as a
`data-tooltip` attribute and mirror it into `aria-label` for screen-reader
accessibility.

### 3. Styling (`assets/sass/3-modules/_contact.scss`)
- **Smaller, not bold:** link `font-weight` `600` → `400`, `font-size` ~15px;
  shrink icons (22px → 18px) to match.
- **Dot separator:** a muted `·` between adjacent links via
  `.contact-channels__item:not(:last-child)::after`.
- **Custom CSS tooltip:** a rounded bubble above the link on `:hover` /
  `:focus-within`, using site colors, with a small arrow and fade-in. Hidden by
  default, no layout shift. Pure CSS — no JS dependency.

## Scope

Only the contact page's social channel links change. Form, hero, and page
layout are untouched.
