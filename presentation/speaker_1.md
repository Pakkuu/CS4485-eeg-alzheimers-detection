# Speaker 1 (Slides 1–3, ~2:30) — Problem + motivation

## What you say (verbatim)

“Hi everyone. We’re presenting our CS 4485 capstone: **EEG-based detection of Alzheimer’s disease**.  
Our big idea is simple: EEG is **cheap and non-invasive**, and Alzheimer’s changes brain rhythms—so we asked whether we can classify Alzheimer’s from EEG using machine learning.”

“**Slide 2: the problem.** Alzheimer’s is often caught too late. The most common high-confidence diagnostics—like **amyloid PET scans** or **cerebrospinal fluid biomarkers**—are expensive or invasive, and they’re not accessible for everyone. By the time a patient reaches those tests, a lot of neurodegeneration may already have occurred.  
On this slide, we compare typical costs: a PET scan can be **$3,000+**, while a clinical EEG session can be around **$200**.”

“**Slide 3: why EEG.** EEG is fast to run, it’s non-invasive, and it uses a **standard 19-channel scalp montage** that’s widely available. Most importantly for our project: Alzheimer’s is associated with **early spectral changes**—meaning changes in brain activity at different frequencies—often described as ‘EEG slowing’.  
So our project asks: can we take EEG, extract frequency-based features, and train a model to distinguish **healthy controls** from **Alzheimer’s**?”

“With that motivation, I’ll hand it off to Speaker 2 for our objective and dataset.”

## What you must know (plain English)

- **PET scan (positron emission tomography)**: an imaging test that can detect biomarkers (like amyloid). It’s expensive and not always available.
- **CSF biomarkers**: proteins measured in cerebrospinal fluid; requires a lumbar puncture, so it’s invasive.
- **EEG slowing**: in AD, EEG often shifts toward **more slow-wave activity** (delta/theta) and **less alpha**, reflecting changes in brain network function.
- **Scope**: you’re not claiming to replace clinical diagnosis; you’re presenting a **baseline ML classifier** on a public dataset.

## Likely professor questions + good answers

- **Are you diagnosing Alzheimer’s?**  
  “Not clinically. We’re evaluating machine learning on a labeled dataset to see how well EEG features separate groups. It’s best framed as a research baseline or screening support.”

- **Why would EEG show changes early?**  
  “EEG reflects neural synchronization and rhythms. Neurodegeneration can disrupt these rhythms before severe symptoms, which can appear as changes in spectral power.”

