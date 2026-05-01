# EEG-based detection of Alzheimer's disease (15 minutes, 6 speakers)

This script is based on your deck `CS_Project_-_Alzheimer_s.pptx` (20 slides) and aligns to the capstone rubric: **problem → objective → data prep/features → models → experiments/results → observations/future work → Q&A**.

## Time + ownership map (non-overlapping)

- **Speaker 1 (2:30)**: Slides **1–3** (title + problem + why EEG)
- **Speaker 2 (2:30)**: Slides **4–6** (objective + dataset overview)
- **Speaker 3 (3:00)**: Slides **7–10** (signal→frequency, pipeline, stats, top features)
- **Speaker 4 (2:30)**: Slides **11–13** (models + experimental setup)
- **Speaker 5 (2:30)**: Slides **14–16** (headline results + comparison + confusion matrices)
- **Speaker 6 (2:00)**: Slides **17–20** (trade-offs, observations, future work, closing)

**Buffer (0:30)**: natural slide transitions / brief pauses.

## Shared glossary (use during Q&A)

- **EEG (electroencephalogram)**: electrical activity measured at the scalp using electrodes. It’s cheap, fast, and non-invasive, but noisy.
- **AD (Alzheimer’s Disease)**: neurodegenerative disease causing progressive cognitive decline.
- **HC (Healthy Control)**: a subject without Alzheimer’s in the dataset.
- **FTD (frontotemporal dementia)**: a different dementia type; in your binary task you excluded it.
- **Sampling rate (128 Hz)**: 128 measurements per second per channel.
- **Epoch (1 second)**: a fixed-length segment of EEG used for analysis.
- **PSD (power spectral density)**: how signal power is distributed across frequencies.
- **Welch PSD**: a stable PSD estimate made by splitting into windows, applying a window function, and averaging.
- **Band power**: PSD integrated (area under the curve) over a frequency band (delta/theta/alpha/beta).
- **Cross-validation (5-fold stratified)**: split subjects into 5 groups (“folds”), train on 4 folds and validate on 1, repeat 5 times; “stratified” preserves class ratios.
- **Subject-level split**: all data from a subject stays in one fold; prevents leakage.
- **Accuracy**: fraction of correct predictions.
- **ROC-AUC**: threshold-independent ranking quality (1.0 best, 0.5 random).
- **Sensitivity (AD recall)**: out of all AD subjects, how many were caught as AD.
- **Specificity (HC recall)**: out of all HC subjects, how many were correctly cleared as HC.
- **Confusion matrix**: counts of true/false positives/negatives.

---

## Speaker 1 script (Slides 1–3) — Problem + motivation (target ~2:30)

### What you say (verbatim)

“Hi everyone. We’re presenting our CS 4485 capstone: **EEG-based detection of Alzheimer’s disease**.  
Our big idea is simple: EEG is **cheap and non-invasive**, and Alzheimer’s changes brain rhythms—so we asked whether we can classify Alzheimer’s from EEG using machine learning.”

“**Slide 2: the problem.** Alzheimer’s is often caught too late. The most common high-confidence diagnostics—like **amyloid PET scans** or **cerebrospinal fluid biomarkers**—are expensive or invasive, and they’re not accessible for everyone. By the time a patient reaches those tests, a lot of neurodegeneration may already have occurred.  
On this slide, we compare typical costs: a PET scan can be **$3,000+**, while a clinical EEG session can be around **$200**.”

“**Slide 3: why EEG.** EEG is fast to run, it’s non-invasive, and it uses a **standard 19-channel scalp montage** that’s widely available. Most importantly for our project: Alzheimer’s is associated with **early spectral changes**—meaning changes in brain activity at different frequencies—often described as ‘EEG slowing’.  
So our project asks: can we take EEG, extract frequency-based features, and train a model to distinguish **healthy controls** from **Alzheimer’s**?”

“With that motivation, I’ll hand it off to Speaker 2 for our objective and dataset.”

### What Speaker 1 must know (to answer questions)

- **PET scan (positron emission tomography)**: imaging method that can detect amyloid plaques or other biomarkers; expensive and not always available.
- **CSF biomarkers**: proteins measured in cerebrospinal fluid (requires lumbar puncture/spinal tap), making it invasive.
- **Why EEG can help**: it’s not a definitive diagnostic on its own, but it’s scalable and could be a screening or triage signal.
- **“EEG slowing” in AD (plain English)**: compared to healthy older adults, AD patients often show more power in **slow frequencies** (delta/theta) and less in **alpha** (especially posterior regions). Your later slides quantify this.
- **Your claim boundaries**: you are not claiming EEG replaces PET/CSF; you’re showing **a baseline ML approach** that achieves strong classification on this dataset.

### Likely Q&A for Speaker 1

- **Q: Are you diagnosing Alzheimer’s?**  
  **A:** “Not clinically. We’re building and evaluating ML classifiers on a public dataset to see how well EEG features can separate groups. It’s best thought of as a research baseline and potentially a screening aid.”

- **Q: Why focus on cost?**  
  **A:** “Because a practical screening method must be accessible. EEG’s low cost and availability make it worth studying.”

- **Q: Why would EEG show changes before symptoms?**  
  **A:** “EEG reflects neural network dynamics. Neurodegeneration and synaptic dysfunction can shift rhythmic activity patterns before severe behavioral impairment.”

---

## Speaker 2 script (Slides 4–6) — Objective + dataset (target ~2:30)

### What you say (verbatim)

“**Slide 4: objective.** Our objective is: **Can EEG band-power features classify Alzheimer’s disease?**  
Our input is **19-channel resting-state EEG**. The task is binary: **Healthy Control versus Alzheimer’s**. We compare two models—**Logistic Regression** and **Random Forest**—and we evaluate using **5-fold subject-level cross-validation**.”

“**Slide 5 is a section divider**: we’re moving from raw EEG to a **76-feature vector** per subject.”

“**Slide 6: the dataset.** We used the Kaggle dataset called the **Largest Alzheimer EEG Dataset**. It contains **241 subjects** total, about **28 hours** of resting-state EEG. The groups are: **122 AD**, **78 HC**, and **41 FTD**.”  
“For our binary HC vs AD task, we **exclude FTD**, leaving **200 subjects**.”

“Key properties: **19 EEG channels**, **128 Hz sampling rate**, and we process the recordings into **1-second epochs**, where each epoch is a **19 by 128** matrix—19 channels and 128 time samples.”  
“Next, Speaker 3 will show how we convert those time signals into frequency features and why those features are meaningful.”

### What Speaker 2 must know

- **Resting-state EEG**: EEG recorded while the subject is at rest (not doing a task). It’s common for dementia research because it’s easier to collect consistently.
- **Why exclude FTD for binary**: FTD is a different disease process; including it changes the problem to multi-class. Your slide explicitly says binary HC vs AD, so exclusion keeps the scope focused and consistent.
- **Why epoching (1 second) is used**: EEG is nonstationary; analyzing shorter windows helps compute stable PSD estimates and reduces the impact of transient artifacts.
- **What “19 channels” means**: standard scalp electrode locations (e.g., Fp1/Fp2 frontal pole, C3/C4 central, P3/P4 parietal, etc.). You don’t need to name all, just know it’s the standard montage.
- **Data leakage concept (teaser)**: if you split by epochs, you can accidentally have the same subject’s EEG in train and test, inflating performance. You later fixed this with subject-level CV (Slide 18).

### Likely Q&A for Speaker 2

- **Q: Why only 200 subjects when the dataset has 241?**  
  **A:** “We excluded the 41 FTD subjects because the task we presented is binary HC vs AD.”

- **Q: How long is each subject recording?**  
  **A:** “Average is about **423 seconds** per subject, per the dataset summary in the deck.”

- **Q: Are the classes imbalanced?**  
  **A:** “Yes—122 AD vs 78 HC. We use class-weighting in both models to compensate.”

---

## Speaker 3 script (Slides 7–10) — Features + statistics (target ~3:00)

### What you say (verbatim)

“**Slide 7: signal to frequency.** On the left is a 10-second raw EEG snippet from channel P4 for a healthy control versus an Alzheimer’s subject. It’s very hard to separate by eye in the time domain.  
On the right, we convert the signal into the frequency domain using **Welch’s power spectral density**, and now the differences become visible. Alzheimer’s often shows **more low-frequency power** and **less alpha power**—that’s the ‘EEG slowing’ pattern we want to capture.”

“**Slide 8: the pipeline.** Our feature extraction pipeline is: raw EEG → split into **1-second epochs** → compute **Welch PSD** per channel → compute **band power** by integrating the PSD over four clinically relevant bands → average across all epochs for a subject.  
That produces **19 channels × 4 bands = 76 features** per subject.”

“The four bands are:  
**Delta (1–4 Hz)**, slow waves often elevated in AD;  
**Theta (4–8 Hz)**, another slowing marker often elevated in AD;  
**Alpha (8–13 Hz)**, linked to relaxed wakefulness and often reduced in AD;  
and **Beta (13–30 Hz)**, linked to more active cognition and can show mixed effects.”

“**Slide 9: statistical findings.** Before training any model, we run **Welch’s t-test** comparing AD vs HC for each of the 76 features. We see the expected pattern: **delta and theta increase** in AD, and **alpha decreases**, especially in posterior and midline channels. This matches known findings in Alzheimer’s EEG literature and validates our pipeline.”

“**Slide 10: top features.** The strongest group differences are mostly **theta-band power** in channels like P3, C3, and C4, with very large t-statistics and extremely small p-values. The heatmap shows where the relative difference \((AD−HC)/HC\) is concentrated—again largely in theta.”

“Next, Speaker 4 will show the two models and our evaluation protocol.”

### What Speaker 3 must know

- **Why frequency-domain features help**: raw EEG is noisy and phase-shifted; many disease signatures appear as changes in the distribution of power over frequencies, which PSD summarizes.
- **Welch PSD (plain English)**:
  - Split a signal into overlapping windows.
  - Multiply each window by a taper (Hann window) to reduce edge effects.
  - Compute a periodogram for each window and average them → reduces variance/noise.
- **Band power (plain English)**: “how much total power lives between, say, 4 and 8 Hz,” computed as the area under the PSD curve in that range.
- **Welch’s t-test**: compares the mean of a feature between AD and HC while allowing unequal variances; yields a t-statistic (effect size relative to noise) and a p-value (how unlikely the difference is under ‘no difference’).
- **Interpret the slide 10 table**: big \(|t|\) and tiny p-values mean that feature differs strongly and consistently between groups in this dataset.
- **Important limitation**: lots of features means multiple comparisons; your deck uses this as a validation signal, not as a final medical claim.

### Likely Q&A for Speaker 3

- **Q: Why only four bands?**  
  **A:** “They’re standard clinically meaningful bands and keep the model lightweight. Future work is to add richer features like coherence and complexity measures.”

- **Q: Why average across epochs for each subject?**  
  **A:** “To get stable subject-level features and prevent the model from overfitting to transient artifacts.”

- **Q: What does ‘alpha decreases’ mean in real terms?**  
  **A:** “Alpha is a dominant rhythm in relaxed wakefulness, often strongest in posterior regions. In AD, that rhythm weakens, so power in 8–13 Hz drops relative to controls.”

---

## Speaker 4 script (Slides 11–13) — Models + evaluation protocol (target ~2:30)

### What you say (verbatim)

“**Slide 11** is a divider: now we move into modeling. The key point is: **two models, same 76 features, same folds**—so the comparison is fair.”

“**Slide 12: models.** We compare **Logistic Regression** against a **Random Forest**.  
Logistic Regression is a linear classifier: each feature gets a coefficient, so it’s interpretable—you can see which channel-band features push the prediction toward AD. We use a **log1p transform** and **standardization**, and set `class_weight='balanced'` to handle the AD vs HC imbalance.”

“Random Forest is an ensemble of decision trees. It can capture **non-linear interactions** across channels and bands, and it doesn’t require scaling. We also use class balancing.”

“**Slide 13: experimental setup.** We train on **200 subjects**, each represented by **76 features**. We use **5-fold stratified cross-validation at the subject level** with a fixed seed.  
And we report not just accuracy and AUC, but also **sensitivity**—how many AD cases we catch—and **specificity**—how many healthy subjects we correctly clear.”

“With that setup, Speaker 5 will walk through the results and what the two models do differently.”

### What Speaker 4 must know

- **Logistic regression (plain English)**: produces a weighted sum of features; passes through a sigmoid to output probability. Coefficients are interpretable: positive coefficient increases AD probability.
- **Random forest (plain English)**: many decision trees; each tree votes; the forest averages votes; handles non-linear relationships.
- **Why `class_weight='balanced'` matters**: without it, a model can bias toward the larger class (AD) or optimize accuracy in a way that sacrifices minority-class performance.
- **Why log1p + scaling for LR**:
  - band powers can vary across orders of magnitude
  - `log1p(x)=log(1+x)` compresses large values
  - scaling ensures features contribute comparably in a linear model
- **Subject-level CV is critical**: ensures the model is tested on completely unseen subjects; avoids overly optimistic scores.

### Likely Q&A for Speaker 4

- **Q: Why only these two models?**  
  **A:** “We chose two lightweight, standard baselines: one linear interpretable model and one non-linear model. Future work includes SVM and gradient boosting.”

- **Q: Why not deep learning?**  
  **A:** “Our goal was a strong baseline with minimal compute and clear interpretability. Deep learning would need more careful preprocessing, more data, and more extensive tuning.”

---

## Speaker 5 script (Slides 14–16) — Results + interpretation (target ~2:30)

### What you say (verbatim)

“**Slide 14: headline results.** Using 5-fold subject-level cross-validation on 200 subjects, both models land in a similar overall range.  
For **Logistic Regression**, accuracy is **0.83** and ROC-AUC is **0.918**. Sensitivity is **0.754** and specificity is **0.949**.  
For **Random Forest**, accuracy is **0.84** and ROC-AUC is **0.929**. Sensitivity is **0.877** and specificity is **0.782**.”

“So the overall scores—accuracy and AUC—are close. The main difference is the **operating point**: Logistic Regression is very conservative and rarely flags healthy controls, while Random Forest catches more Alzheimer’s cases but produces more false alarms.”

“**Slide 15 makes that explicit.** Random Forest improves sensitivity by about **+0.123**, meaning it misses fewer AD cases. But Logistic Regression has specificity higher by about **+0.167**, meaning it clears healthy subjects more reliably.”

“**Slide 16: confusion matrices.** In counts pooled across folds:  
Logistic Regression correctly clears **92** healthy subjects but raises **4** false positives, and it catches **74** AD subjects while missing **30**.  
Random Forest clears **107** healthy subjects with **17** false positives, and it catches **61** AD with **15** missed AD cases.”  
“Same features, same cross-validation—just a different error profile.”

“Next, Speaker 6 will summarize the trade-offs, what we learned, and future work.”

### What Speaker 5 must know

- **Interpret accuracy vs AUC**:
  - Accuracy depends on a specific threshold (here effectively 0.5).
  - ROC-AUC measures ranking ability across all thresholds; it can be high even if a particular threshold yields a sensitivity/specificity imbalance.
- **Explain ‘operating point’**: the threshold choice trades sensitivity vs specificity. Even with similar AUC, two models can choose different trade-offs at the default threshold.
- **Interpret false negatives vs false positives in healthcare**:
  - False negative (missed AD): might delay treatment/referral.
  - False positive (alarmed HC): might cause anxiety and extra testing.
  - Which is “worse” depends on intended use (screening vs confirmatory testing).

### Likely Q&A for Speaker 5

- **Q: Which model is better?**  
  **A:** “Overall accuracy/AUC are similar. The better choice depends on whether you prioritize catching AD (sensitivity → Random Forest) or avoiding false alarms (specificity → Logistic Regression).”

- **Q: Could you tune a threshold to change the trade-off?**  
  **A:** “Yes. Both models output probabilities; choosing a different threshold can increase sensitivity at the cost of specificity, or vice versa.”

- **Q: Are these results reliable?**  
  **A:** “They are cross-validated at the subject level, which is the key reliability step. Future work includes running multiple random seeds to add error bars.”

---

## Speaker 6 script (Slides 17–20) — Trade-offs, observations, future work, close (target ~2:00)

### What you say (verbatim)

“**Slide 17: trade-offs.** Our takeaway is not that one model dominates—it’s that they make different types of mistakes.  
Logistic Regression has **high specificity** and is interpretable, but misses more AD cases.  
Random Forest has **higher sensitivity** and slightly higher overall metrics, but flags more healthy subjects.”

“**Slide 18: observations.** We learned four important things:  
One, class imbalance matters—122 AD vs 78 HC—and class weighting helped.  
Two, **subject-level cross-validation is critical**: an earlier epoch-level split inflated our scores, and fixing that was our biggest post-midterm improvement.  
Three, the EEG slowing signal is real—statistical tests confirmed our features match known AD biomarkers.  
Four, we kept preprocessing minimal; better artifact rejection would likely improve both models.”

“**Slide 19: future work.** Next steps: expand to a **3-class model** including FTD, add richer features like **inter-channel coherence** and **complexity measures**, add more baselines like **SVM** and **gradient boosting**, and run better preprocessing and **multi-seed cross-validation** to report error bars.”

“**Slide 20: closing.** To wrap up: using the Kaggle dataset, Welch PSD band-power features \((19×4=76)\), and 5-fold subject-level stratified CV, both models achieved about **83–84% accuracy** with **AUC around 0.92**. Random Forest catches more AD; Logistic Regression raises fewer false alarms.  
Thank you—happy to take questions.”

### What Speaker 6 must know

- **Why epoch-level splitting inflates performance (plain English)**: EEG from the same person is highly “signature-like.” If epochs from the same person appear in both train and test, the model can partially recognize the person rather than the disease.
- **Artifact rejection**: removing or correcting segments contaminated by eye blinks, muscle activity, movement, or electrode pops; reduces noise in PSD estimates.
- **Inter-channel coherence (plain English)**: a measure of how synchronized two channels are at certain frequencies; can capture network-level changes.
- **Complexity measures (examples)**: entropy-based metrics, fractal dimension, or other measures of signal irregularity; sometimes change in dementia.
- **Multi-seed CV**: repeat CV with different random splits to report variability, not just one point estimate.

### Likely Q&A for Speaker 6

- **Q: What’s the single biggest methodological lesson?**  
  **A:** “Subject-level cross-validation. It prevents leakage and gives a realistic estimate of performance.”

- **Q: If you had one more week, what would you do?**  
  **A:** “Add artifact rejection + multi-seed CV to produce confidence intervals, and try one additional baseline like gradient boosting.”

---

## “If I get asked outside my section” rescue answers (for everyone)

- **If asked “What features did you use?”**: “We used Welch PSD band power in delta/theta/alpha/beta for each of 19 channels, averaged at the subject level → 76 features.”
- **If asked “How did you avoid leakage?”**: “We evaluated with subject-level stratified 5-fold CV so each subject appears in only one validation fold.”
- **If asked “Main result in one sentence?”**: “Two lightweight models on 76 EEG band-power features achieved ~83–84% accuracy and ~0.92 AUC; Random Forest increased sensitivity, Logistic Regression increased specificity.”

