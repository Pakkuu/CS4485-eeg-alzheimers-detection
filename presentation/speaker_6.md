# Speaker 6 (Slides 17–20, ~2:00) — Takeaways + observations + future work + closing

## What you say (verbatim)

“**Slide 17: trade-offs.** Our takeaway is not that one model dominates—it’s that they make different types of mistakes.  
Logistic Regression has **high specificity** and is interpretable, but misses more AD cases.  
Random Forest has **higher sensitivity** and slightly higher overall metrics, but flags more healthy subjects.”

“**Slide 18: observations.** We learned four important things: class imbalance matters; **subject-level CV is critical** because epoch-level splitting inflated scores; the EEG slowing signal shows up even before modeling; and better preprocessing—especially artifact rejection—would likely improve both models.”

“**Slide 19: future work.** Next: include **FTD as a third class**, add richer features like **inter-channel coherence** and **complexity measures**, add more baselines like **SVM** and **gradient boosting**, and run multi-seed cross-validation for reliable error bars.”

“**Slide 20: closing.** Using the Kaggle dataset, Welch PSD band-power features \((19×4=76)\), and 5-fold subject-level stratified CV, both models achieved about **83–84% accuracy** with **AUC around 0.92**. Random Forest catches more AD; Logistic Regression raises fewer false alarms.  
Thank you—happy to take questions.”

## What you must know (plain English)

- **Why epoch-level splitting inflates results**: EEG from the same subject can look similar across epochs; if the same subject appears in train and test, the model can “recognize the person” and performance looks too good.
- **Artifact rejection**: removing EEG segments contaminated by blinks, muscle activity, movement, or electrode noise.
- **Coherence**: measures how synchronized two channels are at a given frequency—captures connectivity/network changes.
- **Complexity measures**: quantify irregularity of EEG (e.g., entropy); can change in dementia.
- **Multi-seed CV**: repeat CV with different random splits to report variability (confidence in results).

## Likely professor questions + good answers

- **Biggest methodology improvement you made?**  
  “Switching to subject-level cross-validation to prevent leakage.”

- **If you had one more week?**  
  “Add artifact rejection and multi-seed CV, then try gradient boosting to see if results hold with another strong baseline.”

