# Speaker 3 (Slides 7–10, ~3:00) — Features + statistics

## What you say (verbatim)

“**Slide 7: signal to frequency.** On the left is a 10-second raw EEG snippet from channel P4 for a healthy control versus an Alzheimer’s subject. It’s very hard to separate by eye in the time domain.  
On the right, we convert the signal into the frequency domain using **Welch’s power spectral density**, and now the differences become visible. Alzheimer’s often shows **more low-frequency power** and **less alpha power**—that’s the ‘EEG slowing’ pattern we want to capture.”

“**Slide 8: the pipeline.** Raw EEG → split into **1-second epochs** → compute **Welch PSD** per channel → compute **band power** by integrating the PSD over four bands → average across all epochs for a subject.  
That gives **19 channels × 4 bands = 76 features** per subject.”

“The four bands are: **Delta (1–4 Hz)**, **Theta (4–8 Hz)**, **Alpha (8–13 Hz)**, and **Beta (13–30 Hz)**.”

“**Slide 9: statistical findings.** Before training any model, we run **Welch’s t-test** comparing AD vs HC for each feature. We see **delta and theta increase** in AD and **alpha decreases**, especially posterior and midline—matching known Alzheimer’s EEG findings.”

“**Slide 10: top features.** The strongest group differences are mostly **theta power** in channels like P3, C3, and C4, with very large t-statistics and extremely small p-values. The relative-difference heatmap shows the same pattern.”

“Next, Speaker 4 will cover the models and evaluation protocol.”

## What you must know (plain English)

- **PSD (power spectral density)**: a plot of “how much power exists at each frequency.”
- **Welch PSD**: compute PSD on overlapping windows and average them to reduce noise/variance.
- **Band power**: total power inside a band (area under PSD curve in that frequency range).
- **Why these bands**:
  - **Delta/theta**: slower rhythms; often higher in AD (“slowing”).
  - **Alpha**: prominent in relaxed wakefulness; often reduced in AD.
  - **Beta**: higher frequency; mixed effects.
- **Welch’s t-test**: checks whether the average feature differs between AD and HC; high \(|t|\) + tiny p-value = strong separation in this dataset.

## Likely professor questions + good answers

- **Why not use raw EEG directly?**  
  “Raw EEG is noisy and hard to compare across subjects. Frequency-based summaries capture known disease-related shifts more robustly.”

- **Why average over epochs?**  
  “To get stable, subject-level features and reduce the impact of transient artifacts.”

