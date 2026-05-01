# Speaker 2 (Slides 4–6, ~2:30) — Objective + dataset

## What you say (verbatim)

“**Slide 4: objective.** Our objective is: **Can EEG band-power features classify Alzheimer’s disease?**  
Our input is **19-channel resting-state EEG**. The task is binary: **Healthy Control versus Alzheimer’s**. We compare two models—**Logistic Regression** and **Random Forest**—and we evaluate using **5-fold subject-level cross-validation**.”

“**Slide 5 is a section divider**: we’re moving from raw EEG to a **76-feature vector** per subject.”

“**Slide 6: the dataset.** We used the Kaggle dataset called the **Largest Alzheimer EEG Dataset**. It contains **241 subjects** total, about **28 hours** of resting-state EEG. The groups are: **122 AD**, **78 HC**, and **41 FTD**.”  
“For our binary HC vs AD task, we **exclude FTD**, leaving **200 subjects**.”

“Key properties: **19 EEG channels**, **128 Hz sampling rate**, and we process the recordings into **1-second epochs**, where each epoch is a **19 by 128** matrix—19 channels and 128 time samples.”  
“Next, Speaker 3 will show how we convert those time signals into frequency features and why those features are meaningful.”

## What you must know (plain English)

- **Resting-state EEG**: EEG recorded while resting. Easier to collect consistently than task-based EEG.
- **Sampling rate (128 Hz)**: each channel is measured 128 times per second.
- **Epoch (1 second)**: a 1-second chunk used for frequency analysis; EEG changes over time, so shorter windows help.
- **Why exclude FTD**: the deck’s task is binary HC vs AD. Including FTD would turn it into a 3-class problem (future work).
- **Leakage risk**: if you split by epochs, the same subject can appear in train and test. That inflates results and is why subject-level CV matters later.

## Likely professor questions + good answers

- **Why is FTD excluded?**  
  “To keep the scope strictly HC vs AD as a clean binary baseline. The next step is a 3-class model including FTD.”

- **How much data per subject?**  
  “On average about 423 seconds per subject in this dataset summary.”

