# Speaker 4 (Slides 11–13, ~2:30) — Models + evaluation protocol

## What you say (verbatim)

“**Slide 11** is a divider: now we move into modeling. The key point is: **two models, same 76 features, same folds**—so the comparison is fair.”

“**Slide 12: models.** We compare **Logistic Regression** against a **Random Forest**.  
Logistic Regression is a linear classifier: each feature gets a coefficient, so it’s interpretable—you can see which channel-band features push the prediction toward AD. We use a **log1p transform** and **standardization**, and set `class_weight='balanced'` to handle the AD vs HC imbalance.”

“Random Forest is an ensemble of decision trees. It can capture **non-linear interactions** across channels and bands, and it doesn’t require scaling. We also use class balancing.”

“**Slide 13: experimental setup.** We train on **200 subjects**, each represented by **76 features**. We use **5-fold stratified cross-validation at the subject level** with a fixed seed.  
And we report **sensitivity**—how many AD cases we catch—and **specificity**—how many healthy subjects we correctly clear.”

“Speaker 5 will walk through the results and the error trade-offs.”

## What you must know (plain English)

- **Logistic Regression**: outputs a probability using a weighted sum of features. Coefficients are interpretable.
- **Random Forest**: many decision trees whose votes are averaged; handles non-linear patterns.
- **Class imbalance**: 122 AD vs 78 HC. `class_weight='balanced'` reduces bias toward the majority class.
- **log1p transform**: compresses very large band-power values so LR trains more stably.
- **Scaling**: important for LR because it’s sensitive to feature magnitudes; not needed for RF.
- **Subject-level stratified CV**: prevents leakage and preserves class ratios per fold.

## Likely professor questions + good answers

- **Why these two models?**  
  “They’re strong lightweight baselines: one interpretable linear model and one non-linear ensemble, both common in biomedical ML.”

- **Why not deep learning?**  
  “This project focused on an interpretable baseline and a fair protocol; deep learning would require more preprocessing and tuning to be defensible.”

