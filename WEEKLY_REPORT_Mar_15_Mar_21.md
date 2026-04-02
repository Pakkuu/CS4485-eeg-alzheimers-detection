# Weekly Progress Report — Mar 15 – Mar 21, 2026

**Project:** EEG-Based Alzheimer’s Disease Detection (CS 4485)  
**Team:** Venkatasai Gudisa, Ajay Alluri, Ethan Varghese, Aashay Vishwakarma, Venkat Sai Eshwar Varma Sagi, Ram Gudur  
**Repository:** [CS4485-eeg-alzheimers-detection](https://github.com/Pakkuu/CS4485-eeg-alzheimers-detection)

---

## Summary

This week the team **submitted the Midterm project proposal** (deadline Mar 15), including Tasks 1–3 results, future ML roadmap, and project-management / ethics sections. We began **Phase 1 of the ML roadmap**: subject-level baseline models (HC vs AD) with stratified evaluation and class-imbalance handling.

---

## Member progress

| Member | Done | Planned | Roadblocks |
| :--- | :--- | :--- | :--- |
| **Venkatasai Gudisa** | Finalized Task 1 narrative and figure placement in the Midterm proposal; coordinated 10-second EEG plot (`figures/eeg_10s_hc_vs_ad_p4.png`) for Section 2.3. | Produce **confusion matrices and ROC curves** for baseline classifiers; support slide deck for any class presentation. | None |
| **Ajay Alluri** | Documented dataset statistics, class imbalance (78 HC vs 122 AD), and data-quality notes in the Midterm doc. | Track **per-fold class counts** in cross-validation; summarize distribution of predictions vs true labels for the weekly sync. | None |
| **Ethan Varghese** | README updates for Midterm PDF export (`md_to_pdf.py`), Task 1 plot script (`plot_10s_eeg_task1.py`), and repo structure. | Keep **Google Colab** path documented for teammates running heavy notebooks; test `train_baseline_models.py` in a clean venv. | Long Kaggle dataset download on first run; mitigated by cache after first download. |
| **Aashay Vishwakarma** | Confirmed Welch PSD / band-power pipeline and figure outputs referenced in Tasks 2–3 of the proposal. | **Integrate** subject-level CSV features with the new training script; optional: experiment with feature scaling (StandardScaler) in a branch. | None |
| **Venkat Sai Eshwar Varma Sagi** | Wrote AD vs HC **observations** (Delta/Theta/Alpha) and linked findings to known EEG biomarkers in the proposal. | Interpret **coefficients / feature importances** from logistic regression and random forest; draft short “what the model uses” summary for the team. | None |
| **Ram Gudur** | Ethics, leadership, and literature placeholder sections in the Midterm proposal; evaluation metrics defined for later benchmarking. | Compare our **baseline AUC / accuracy** to ranges reported in open-access AD–EEG papers; maintain reference list for final report. | Some full-text journals still paywalled; using open-access summaries where needed. |

---

## Team-level milestones

| Milestone | Status |
| :--- | :--- |
| Midterm proposal / requirements document submitted | Done |
| Reproducible 10-second EEG figure (Task 1) in repo | Done |
| Baseline HC vs AD classifier (subject-level, stratified CV) | In progress (`train_baseline_models.py`) |
| Final course deliverable | Future weeks |

---

## Next week focus (Mar 22–28)

- Run and document baseline metrics (accuracy, AUC-ROC, sensitivity, specificity).
- Decide on optional **class weighting** vs **threshold tuning** for imbalance.
- Begin **feature-selection** experiments (e.g., top channels/bands) if time permits.

---

## Baseline ML (initial `train_baseline_models.py` run)

Subject-level HC vs AD (*n* = 200: 122 AD, 78 HC), 4 features (Delta, Theta, Alpha, Beta band powers averaged across channels), stratified 5-fold CV, `class_weight='balanced'`.

| Model | Accuracy | ROC-AUC | Sensitivity (AD) | Specificity (HC) |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.765 | 0.857 | 0.697 | 0.872 |
| Random Forest | 0.765 | 0.837 | 0.754 | 0.782 |

*Figures depend on sklearn version and random seed; re-run `python train_baseline_models.py` to reproduce.*
