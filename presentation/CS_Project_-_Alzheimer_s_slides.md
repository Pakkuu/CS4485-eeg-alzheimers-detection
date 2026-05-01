# Extracted slides: CS_Project_-_Alzheimer_s.pptx


## Slide 1

### On-slide text

- CS 4485 / PROFESSOR SAMADI / SENIOR DESIGN

- EEG-based detection of Alzheimer's disease.

- By: Aashay, Ajay, Ethan, Ram, Venkat, Venkatasai

- FINAL PROJECT PRESENTATION · MAY 01 2026

### Speaker notes

- SLIDE 1 — COVER. Title slide. Team: Aashay, Ajay, Ethan, Ram, Venkat, Venkatasai. Course: CS 4485 Capstone. SCRIPT: Hi everyone. This is our semester capstone project on EEG-based Alzheimer's detection. We used a public EEG dataset and trained two machine learning models to distinguish healthy people from Alzheimer's patients. I'll cover the problem, the data, the pipeline, the two models, and the results.
- 1


## Slide 2

### On-slide text

- 02

- PROBLEM

- Alzheimer's is usually caught too late.

- Standard diagnostics — PET scans and CSF biomarkers — are expensive, invasive, and not widely available.

- By the time a patient reaches them, significant neurodegeneration has already occurred.

- $3,000+

- Typical cost of an amyloid PET scan

- ~$200

- Typical cost of a clinical EEG session

- EEG · ALZHEIMER'S DETECTION

- 02

### Speaker notes

- SLIDE 2 — THE PROBLEM. Title: Alzheimer's is usually caught too late. Shows two cost figures: PET scan $3,000+ versus EEG ~$200. SCRIPT: Alzheimer's is often diagnosed late because the standard tests are expensive — PET scans cost thousands, CSF biomarkers need a spinal tap. EEG is cheap and non-invasive. So we asked: can a model classify Alzheimer's from EEG?
- 2


## Slide 3

### On-slide text

- 03

- WHY EEG

- EEG is cheap, fast, and non-invasive.

- ~15×

- CHEAPER THAN PET

- 19

- SCALP CHANNELS, STANDARD MONTAGE

- Early

- SPECTRAL CHANGES PRECEDE SYMPTOMS

- EEG · ALZHEIMER'S DETECTION

- 03

### Speaker notes

- SLIDE 3 — WHY EEG. Title: EEG is cheap, fast, and non-invasive. Three large stats: ~15x cheaper than PET, 19 standard channels, Early spectral changes. SCRIPT: EEG costs about 15 times less than a PET scan, uses a standard 19-channel cap, and brain-frequency changes in Alzheimer's appear early. That makes EEG a useful signal to study for detection.
- 3


## Slide 4

### On-slide text

- 04

- OBJECTIVE

- Can EEG band-power features classify Alzheimer's Disease?

- INPUT

- 19-channel resting-state EEG

- TASK

- Healthy Control vs. Alzheimer's (binary)

- APPROACH

- Logistic Regression vs. Random Forest

- EVALUATION

- 5-fold subject-level cross-validation

- EEG · ALZHEIMER'S DETECTION

- 04

### Speaker notes

- SLIDE 4 — OBJECTIVE. Title: Can EEG band-power features classify Alzheimer's Disease? Four-row table: Input (19-channel EEG), Task (HC vs AD), Approach (LR vs RF), Evaluation (5-fold CV). SCRIPT: Our goal was to build a binary Healthy Control versus Alzheimer's classifier from EEG features, compare Logistic Regression against Random Forest on the same input, and evaluate with 5-fold subject-level cross-validation.
- 4


## Slide 5

### On-slide text

- PART 02

- DATA & FEATURES

- 5 — 9

- PART TWO

- From scalp signal to a 76-feature vector.

- EEG · ALZHEIMER'S DETECTION

- 05

### Speaker notes

- SLIDE 5 — SECTION HEADER: DATA. Divider slide. SCRIPT: Let's look at the data and how we turned raw EEG into features a model can use.
- 5


## Slide 6

### On-slide text

- 06

- DATASET

- LARGEST ALZHEIMER EEG · KAGGLE

- DATASET

- 241 subjects across three groups, ~28 hours of resting-state EEG.

- Alzheimer's (AD)

- 122

- Healthy Controls (HC)

- 78

- Frontotemporal (FTD)

- 41

- FTD subjects excluded from the binary HC vs. AD task; 200 subjects remain.

- PROPERTY

- VALUE

- EEG channels

- 19

- Sampling rate

- 128 Hz

- Total duration

- ~28.3 h

- Avg per subject

- ~423 s

- Epoch length

- 1 s

- Matrix per epoch

- 19 × 128

- EEG · ALZHEIMER'S DETECTION

- 06

### Speaker notes

- SLIDE 6 — THE DATASET. Title: 241 subjects, ~28 hours of EEG. Bar chart: 122 AD, 78 HC, 41 FTD. Table: 19 channels, 128 Hz, ~28.3 h total, ~423 s per subject, 1-second epochs. SCRIPT: We used the Largest Alzheimer EEG Dataset from Kaggle — 122 Alzheimer's, 78 healthy, 41 frontotemporal dementia. We dropped FTD for the binary task, leaving 200 subjects. 19 channels at 128 Hz, about 7 minutes per subject on average.
- 6


## Slide 7

### On-slide text

- 07

- SIGNAL → FREQUENCY

- WELCH PSD

- FROM TIME-DOMAIN TO FREQUENCY-DOMAIN

- The disease shows up in the spectrum, not in the raw waveform.

- RAW EEG · 10S · CHANNEL P4 · HC VS. AD

- GRAND-AVERAGE PSD · ALL CHANNELS · HC VS. AD

- EEG · ALZHEIMER'S DETECTION

- 07

### Speaker notes

- SLIDE 7 — SIGNAL TO FEATURES. Two plots side by side. Left: 10 seconds raw EEG at channel P4, HC vs AD. Right: Grand-average power spectral density across all channels. SCRIPT: The left plot is raw EEG — hard to distinguish by eye. The right converts the same signal to the frequency domain using Welch's method. Now you can see the difference: AD subjects have more low-frequency power and less alpha-band power. This EEG slowing pattern is what we capture as features.
- 7


## Slide 8

### On-slide text

- 08

- PIPELINE

- 19 CHANNELS × 4 BANDS = 76 FEATURES

- FEATURE EXTRACTION PIPELINE

- Welch PSD → band power → subject vector.

- 01

- Raw EEG

- 19 ch · 128 Hz

- 02

- 1-s epochs

- Hann window · 50% overlap

- 03

- Welch PSD

- 1 Hz resolution per channel

- 04

- Band power

- Integrate over 4 bands

- 05

- Subject vector

- Average epochs → 76 features

- THE FOUR BANDS

- Delta

- 1 – 4 Hz

- Slow waves; elevated in AD.

- Theta

- 4 – 8 Hz

- Slowing marker; broadly elevated in AD.

- Alpha

- 8 – 13 Hz

- Relaxed wakefulness; reduced in AD.

- Beta

- 13 – 30 Hz

- Active cognition; mixed effects.

- EEG · ALZHEIMER'S DETECTION

- 08

### Speaker notes

- SLIDE 8 — FEATURE PIPELINE. Title: Welch PSD to band power to subject vector. Five-step pipeline, then four band definitions: Delta 1–4 Hz, Theta 4–8 Hz, Alpha 8–13 Hz, Beta 13–30 Hz. SCRIPT: Raw EEG → 1-second epochs → Welch PSD per channel → integrate over four frequency bands → average across epochs. Final result: 19 channels × 4 bands = 76 features per subject. That 76-number vector is what goes into each model.
- 8


## Slide 9

### On-slide text

- 09

- STATISTICAL FINDINGS

- WELCH'S T-TEST · AD VS. HC

- EEG slowing is visible before any model is trained.

- BAND POWER HEATMAP · ALL CHANNELS · HC VS. AD

- SUBJECT-LEVEL BAND POWER BOXPLOTS

- ↑ Delta & Theta in AD

- ↓ Alpha in AD (posterior & midline)

- EEG · ALZHEIMER'S DETECTION

- 09

### Speaker notes

- SLIDE 9 — STATISTICAL FINDINGS. Title: EEG slowing is visible before any model is trained. Left: band-power heatmap. Right: subject-level boxplots. Bottom callouts: Delta and Theta up in AD, Alpha down in AD. SCRIPT: We ran Welch's t-test on all 76 features before training anything. The heatmap shows theta and delta are elevated in AD, and alpha is reduced in posterior and midline channels. The boxplots show the same at the subject level. This matches the known AD EEG literature — our pipeline is reproducing a real signal.
- 9


## Slide 10

### On-slide text

- 10

- TOP FEATURES

- LARGEST |T| · AD VS. HC

- Theta power separates the groups most strongly.

- CHANNEL

- BAND

- |T|

- P-VALUE

- P3

- Theta

- 7.56 · p < 1e-11

- C3

- Theta

- 7.48 · p < 1e-11

- C4

- Theta

- 7.39 · p < 1e-11

- F3

- Theta

- 7.11 · p < 1e-10

- F4

- Theta

- 7.03 · p < 1e-10

- Fp1

- Beta

- 6.67 · p < 1e-9

- F7

- Theta

- 6.40 · p < 1e-8

- RELATIVE BAND POWER DIFFERENCE (AD − HC) / HC

- EEG · ALZHEIMER'S DETECTION

- 10

### Speaker notes

- SLIDE 10 — TOP DISCRIMINATIVE FEATURES. Title: Theta power separates the groups most strongly. Left: ranked t-statistic table (P3 7.56, C3 7.48, C4 7.39, F3 7.11, F4 7.03, Fp1 6.67, F7 6.40). Right: relative band-power difference heatmap. SCRIPT: The strongest features are theta-band in central and parietal channels — t-statistics above 7, p-values below 10 to the minus 10. The heatmap on the right shows where AD power is higher or lower than HC across all channels and bands. The signal is concentrated in theta.
- 10


## Slide 11

### On-slide text

- PART 03

- MODELING

- 11 — 16

- PART THREE

- Two models, same 76 features, same folds.

- EEG · ALZHEIMER'S DETECTION

- 11

### Speaker notes

- SLIDE 11 — SECTION HEADER: MODELS. Divider slide. SCRIPT: The features look informative. Now let's look at the two classifiers and how we compared them.
- 11


## Slide 12

### On-slide text

- 12

- MODELS

- SAME 76 FEATURES · SAME FOLDS

- Two classifiers, same input.

- Logistic Regression

- Linear model. Each coefficient directly shows which channel-band pushes toward AD.

- log1p transform · StandardScaler · class_weight='balanced'

- VS

- Random Forest

- Ensemble of decision trees. Captures non-linear interactions across channels.

- 100 trees · class_weight='balanced' · no scaling needed

- EEG · ALZHEIMER'S DETECTION

- 12

### Speaker notes

- SLIDE 12 — MODELING APPROACH. Title: Two classifiers, same input. Left: Logistic Regression — linear, log1p transform, StandardScaler, class_weight balanced. Right: Random Forest — 100 trees, class_weight balanced, no scaling. SCRIPT: Logistic Regression is linear — its coefficients show directly which channel-band features push toward an AD prediction. Random Forest is a non-linear ensemble of decision trees that can capture interactions between features. Both use the same 76 features and class-balanced weights to handle the 122 AD vs 78 HC imbalance.
- 12


## Slide 13

### On-slide text

- 13

- EXPERIMENTAL SETUP

- SUBJECT-LEVEL · STRATIFIED · 5-FOLD

- Same data. Same folds. Only the model changes.

- 200

- SUBJECTS (122 AD · 78 HC)

- 76

- FEATURES PER SUBJECT

- 5-fold

- SUBJECT-LEVEL STRATIFIED CV · SEED 42

- Sensitivity = how many AD patients we caught. Specificity = how many healthy subjects we correctly cleared.

- EEG · ALZHEIMER'S DETECTION

- 13

### Speaker notes

- SLIDE 13 — EXPERIMENTAL SETUP. Title: Same data. Same folds. Only the model changes. Three stats: 200 subjects, 76 features, 5-fold stratified CV seed 42. One line defining sensitivity and specificity. SCRIPT: Everything is fixed: 200 subjects, 76 features, 5-fold subject-level stratified cross-validation, seed 42. Only the classifier changes. Sensitivity is how many AD patients we caught. Specificity is how many healthy subjects we correctly cleared.
- 13


## Slide 14

### On-slide text

- 14

- HEADLINE RESULTS

- 5-FOLD CV · N = 200

- HEADLINE RESULTS

- Both models land in roughly the same ballpark.

- Logistic Regression

- LINEAR

- 0.83

- ACCURACY

- 0.918

- ROC-AUC

- 0.754

- SENSITIVITY (AD)

- 0.949

- SPECIFICITY (HC)

- Random Forest

- NON-LINEAR

- 0.84

- ACCURACY

- 0.929

- ROC-AUC

- 0.877

- SENSITIVITY (AD)

- 0.782

- SPECIFICITY (HC)

- Best run per model · 5-fold subject-level stratified CV · 200 subjects (122 AD, 78 HC) · seed = 42.

- EEG · ALZHEIMER'S DETECTION

- 14

### Speaker notes

- SLIDE 14 — HEADLINE RESULTS. Two result cards. LR: accuracy 0.83, AUC 0.918, sensitivity 0.754, specificity 0.949. RF: accuracy 0.84, AUC 0.929, sensitivity 0.877, specificity 0.782. SCRIPT: Both models are near 83–84% accuracy with AUC around 0.92. The difference is in sensitivity versus specificity. LR has 95% specificity but 75% sensitivity — it rarely flags a healthy person but misses 25% of AD cases. RF has 88% sensitivity and 78% specificity — it catches more AD cases but raises more false alarms.
- 14


## Slide 15

### On-slide text

- 15

- SIDE-BY-SIDE

- WHERE THE MODELS ACTUALLY DIFFER

- LOGISTIC REGRESSION VS. RANDOM FOREST

- Same overall score. Opposite operating point.

- METRIC

- LOGISTIC REGRESSION

- RANDOM FOREST

- Δ (RF − LR)

- WINNER

- Accuracy

- 0.830

- 0.840

- +0.010

- RF

- ROC-AUC

- 0.918

- 0.929

- +0.012

- RF

- Sensitivity (AD recall)

- 0.754

- 0.877

- +0.123

- RF

- Specificity (HC recall)

- 0.949

- 0.782

- −0.167

- LR

- False negatives (missed AD)

- 30

- 15

- −15

- RF

- False positives (alarmed HC)

- 4

- 17

- +13

- LR

- The interesting result is not which model wins overall — it's that LR and RF land at very different operating points. LR rarely flags healthy subjects; RF catches more disease cases.

- EEG · ALZHEIMER'S DETECTION

- 15

### Speaker notes

- SLIDE 15 — LR vs RF COMPARISON TABLE. Six-row table: Accuracy +0.010 RF, AUC +0.012 RF, Sensitivity +0.123 RF (big gap), Specificity −0.167 LR (big gap), False negatives LR 30 vs RF 15, False positives LR 4 vs RF 17. SCRIPT: Accuracy and AUC are basically tied. The real difference is sensitivity — RF is 12 points higher — and specificity — LR is 17 points higher. In raw counts: LR misses 30 AD patients but only false-alarms 4 healthy subjects. RF misses only 15 AD patients but false-alarms 17. Same data, same features, very different error profiles.
- 15


## Slide 16

### On-slide text

- 16

- CONFUSION MATRICES

- COUNTS · POOLED ACROSS FOLDS

- WHERE EACH MODEL MAKES ITS MISTAKES

- Logistic Regression misses cases; Random Forest over-flags healthy.

- Logistic Regression

- misses 30 AD · alarms 4 HC

- PREDICTED HC

- PREDICTED AD

- ACTUAL HC

- 92

- TRUE NEGATIVES

- 4

- FALSE POSITIVES

- ACTUAL AD

- 30

- FALSE NEGATIVES

- 74

- TRUE POSITIVES

- Random Forest

- misses 15 AD · alarms 17 HC

- PREDICTED HC

- PREDICTED AD

- ACTUAL HC

- 107

- TRUE NEGATIVES

- 17

- FALSE POSITIVES

- ACTUAL AD

- 15

- FALSE NEGATIVES

- 61

- TRUE POSITIVES

- EEG · ALZHEIMER'S DETECTION

- 16

### Speaker notes

- SLIDE 16 — CONFUSION MATRICES. Two 2×2 matrices. LR: 92 TN, 4 FP, 30 FN, 74 TP. RF: 107 TN, 17 FP, 15 FN, 61 TP. SCRIPT: The confusion matrices show the same story in counts. LR correctly clears 92 of 96 healthy subjects but only catches 74 of 104 AD patients — missing 30. RF catches more AD cases, missing only 15, but misclassifies 17 healthy subjects. Similar overall accuracy, different types of mistakes.
- 16


## Slide 17

### On-slide text

- 17

- TRADE-OFFS

- Two models, two different types of errors.

- Logistic Regression

- +

- Specificity 0.949 — rarely flags healthy subjects

- +

- Fully interpretable coefficients

- −

- Sensitivity 0.754 — misses 30 AD cases

- Random Forest

- +

- Sensitivity 0.877 — catches more AD cases

- +

- Best overall accuracy and ROC-AUC

- −

- Specificity 0.782 — flags 17 healthy subjects

- EEG · ALZHEIMER'S DETECTION

- 17

### Speaker notes

- SLIDE 17 — TRADE-OFFS. Title: Two models, two different types of errors. LR card: specificity 0.949 pro, interpretable pro, sensitivity 0.754 con (misses 30 AD). RF card: sensitivity 0.877 pro, best accuracy and AUC pro, specificity 0.782 con (flags 17 HC). SCRIPT: Use Logistic Regression if interpretability matters or false alarms are costly. Use Random Forest if catching AD cases is the priority. Neither is universally better — it depends on which type of error is more costly. We're reporting both and letting the numbers speak.
- 17


## Slide 18

### On-slide text

- 18

- OBSERVATIONS

- What we learned along the way.

- 01

- Class imbalance matters.

- 122 AD vs. 78 HC — class weighting helped but didn't fully fix the bias.

- 02

- Subject-level CV is critical.

- An early epoch-level split inflated our scores — fixing this was the biggest post-midterm change.

- 03

- The EEG slowing signal is real.

- Statistical tests confirmed our features matched known AD biomarkers.

- 04

- Better preprocessing would help.

- We kept it minimal — artifact rejection improvements would likely lift both models.

- EEG · ALZHEIMER'S DETECTION

- 18

### Speaker notes

- SLIDE 18 — OBSERVATIONS. Title: What we learned along the way. Four points: class imbalance, subject-level CV fixed post-midterm, EEG slowing confirmed by stats, minimal preprocessing. SCRIPT: Four takeaways. One: class imbalance biased early results — class weighting helped. Two: our original epoch-level split inflated AUC — switching to subject-level CV after the midterm was the most important fix. Three: statistical tests confirmed our features match known AD biomarkers. Four: minimal preprocessing left room for improvement — better artifact rejection would likely help both models.
- 18


## Slide 19

### On-slide text

- 19

- FUTURE WORK

- Next steps.

- 01

- Add FTD as a third class.

- The 41 FTD subjects were excluded — a 3-class model is the logical next step.

- 02

- Richer features.

- Inter-channel coherence and complexity measures beyond band power.

- 03

- More baselines.

- SVM and gradient boosting — to see how robust the LR vs. RF comparison is.

- 04

- Better preprocessing and multi-seed CV.

- Proper artifact rejection and multiple random seeds for reliable error bars.

- EEG · ALZHEIMER'S DETECTION

- 19

### Speaker notes

- SLIDE 19 — FUTURE WORK. Title: Next steps. Four items: add FTD as third class, richer features (coherence, complexity), more baselines (SVM, gradient boosting), better preprocessing and multi-seed CV. SCRIPT: Next steps would be: include FTD for a 3-class problem, add richer features like inter-channel coherence and entropy, try SVM and gradient boosting to stress-test the LR vs RF comparison, and run multi-seed CV to get proper error bars on all metrics.
- 19


## Slide 20

### On-slide text

- 20

- CLOSING

- Q & A

- Thank you. Questions?

- DATASET

- Largest Alzheimer EEG · Kaggle

- FEATURES

- Welch PSD · 19 × 4 = 76

- MODELS

- Logistic Regression · Random Forest

- PROTOCOL

- 5-fold subject-level stratified CV

- EEG · ALZHEIMER'S DETECTION

- 20 / 20

### Speaker notes

- SLIDE 20 — THANK YOU. Closing slide with team and four summary tags: dataset, features, models, protocol. SCRIPT: To wrap up — Welch PSD features, two classifiers, subject-level cross-validation, 200 subjects. Both models hit 83–84% accuracy and ~0.92 AUC. Random Forest catches more AD cases; Logistic Regression raises fewer false alarms. Thanks — happy to take questions.
- 20
