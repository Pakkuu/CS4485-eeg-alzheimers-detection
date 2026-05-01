# Speaker 5 (Slides 14–16, ~2:30) — Results + interpretation

## What you say (verbatim)

“**Slide 14: headline results.** Using 5-fold subject-level cross-validation on 200 subjects:  
For **Logistic Regression**, accuracy is **0.83** and ROC-AUC is **0.918**. Sensitivity is **0.754** and specificity is **0.949**.  
For **Random Forest**, accuracy is **0.84** and ROC-AUC is **0.929**. Sensitivity is **0.877** and specificity is **0.782**.”

“So accuracy and AUC are close. The main difference is the **operating point**: Logistic Regression rarely flags healthy controls, while Random Forest catches more Alzheimer’s cases but produces more false alarms.”

“**Slide 15:** Random Forest improves sensitivity by **+0.123**, while Logistic Regression improves specificity by **+0.167**. Same data, same features—different trade-off.”

“**Slide 16: confusion matrices.** In counts pooled across folds:  
Logistic Regression clears **92** healthy subjects and false-alarms **4**, but misses **30** AD cases.  
Random Forest misses only **15** AD cases, but false-alarms **17** healthy subjects.”

“Speaker 6 will close with takeaways, observations, and future work.”

## What you must know (plain English)

- **Accuracy**: overall percent correct, but can hide which type of mistake dominates.
- **ROC-AUC**: measures ranking quality across thresholds; it’s not tied to a single cutoff.
- **Operating point**: the chosen decision threshold; moving it trades sensitivity vs specificity.
- **False negatives vs false positives**:
  - **False negative (missed AD)**: could delay treatment or referral.
  - **False positive (flagged HC)**: could cause anxiety and extra testing.

## Likely professor questions + good answers

- **Which model is better?**  
  “They’re similar on accuracy/AUC; the difference is sensitivity vs specificity. For screening, higher sensitivity can matter more (RF). For minimizing false alarms, LR is better.”

- **Could you tune the threshold?**  
  “Yes—both models output probabilities, so you can choose a threshold to target a desired sensitivity/specificity trade-off.”

