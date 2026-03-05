# EEG Alzheimer's Detection

This project explores and analyzes the [Largest Alzheimer EEG Dataset](https://www.kaggle.com/datasets/codingyodha/largest-alzheimer-eeg-dataset) to build models for automated Alzheimer's Disease (AD) detection using electroencephalogram (EEG) signals.

## 📊 Dataset Overview

The dataset is an integrated collection of EEG recordings from multiple sources, standardized for Alzheimer's research.

### Key Statistics
| Metric | Value |
| :--- | :--- |
| **Total Subjects** | 241 |
| **Healthy Controls (HC)** | 78 |
| **Alzheimer's Disease (AD)** | 122 |
| **Frontotemporal Dementia (FTD)** | 41 |
| **EEG Channels** | 19 |
| **Sampling Rate** | 128 Hz |
| **Total Duration** | 101,916 seconds (~28.3 hours) |
| **Epoch Duration** | 1 second |
| **Data Matrix Shape** | 19 Channels × 128 Time samples |

*Labels: `0.0` = Healthy Control (HC), `1.0` = Alzheimer's Disease (AD), `2.0` = Frontotemporal Dementia (FTD)*

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Kaggle API Credentials:
  - Download `kaggle.json` from your Kaggle Account settings.
  - Place it in `~/.kaggle/kaggle.json`.

### 2. Environment Setup
Create and activate a virtual environment, then install the dependencies:

```bash
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## 🚀 Running the Code

### Dataset Inspection
To verify the dataset structure and report statistics:
```bash
python inspect_dataset.py
```

### Subject Analysis
To see a detailed breakdown of subject counts per label:
```bash
python count_subjects.py
```

### Visual Exploration
For interactive data analysis and signal visualization, use the provided Jupyter notebooks:
- [explore_alzheimer_eeg_dataset.ipynb](explore_alzheimer_eeg_dataset.ipynb)
- [eeg_dataset_statistics.ipynb](eeg_dataset_statistics.ipynb)

### Frequency Band Analysis
For full Welch PSD feature extraction and AD vs HC statistical comparison:
- [eeg_frequency_band_analysis.ipynb](eeg_frequency_band_analysis.ipynb)

## 🧠 Frequency Band Analysis

The notebook `eeg_frequency_band_analysis.ipynb` implements a full EEG frequency-domain feature extraction pipeline comparing Alzheimer's Disease (AD), Healthy Controls (HC), and Frontotemporal Dementia (FTD) subjects.

### Methodology
1. **Welch PSD** — Power Spectral Density is estimated using Welch's method (`scipy.signal.welch`) with a 1-second Hann window and 50% overlap, giving 1 Hz frequency resolution.
2. **Band Power Extraction** — Average power is computed via the trapezoid rule over four clinically relevant bands:

   | Band | Range |
   | :--- | :--- |
   | Delta | 1–4 Hz |
   | Theta | 4–8 Hz |
   | Alpha | 8–13 Hz |
   | Beta | 13–30 Hz |

3. **Feature Aggregation** — Per-epoch band powers are averaged across all epochs per subject to produce stable per-subject, per-channel, per-band features.
4. **Statistical Comparison** — Welch's independent-samples t-test compares AD vs HC at every channel × band combination.

### Generated Outputs

#### CSV Files
| File | Description |
| :--- | :--- |
| `eeg_band_power_features.csv` | Full feature table — one row per subject × channel with all 4 band powers and group label |
| `eeg_band_power_subject_level.csv` | Subject-level summary — band powers averaged across all 19 channels per subject |
| `eeg_band_power_stats.csv` | Statistical results — t-statistic, p-value, and significance flag per channel × band |

#### NumPy Arrays
| File | Description |
| :--- | :--- |
| `eeg_subject_features.npy` | Precomputed feature array, shape `(n_subjects, 19, 4)` — reload without re-running extraction |
| `eeg_subject_groups.npy` | Group label array (`'HC'`, `'AD'`, `'FTD'`) aligned with `eeg_subject_features.npy` |

#### Figures (`figures/`)
| File | Description |
| :--- | :--- |
| `psd_single_epoch_example.png` | Welch PSD for one HC and one AD epoch at channel Pz — pipeline sanity check |
| `grand_avg_psd_ad_vs_hc.png` | Grand-average PSD across all channels comparing AD vs HC |
| `band_power_bar_all_channels.png` | Bar chart of mean band power per channel (HC vs AD) with significance markers |
| `band_power_boxplot_subjects.png` | Box plots of subject-level band power per group per band |
| `band_power_heatmap.png` | Heatmap of mean band power by channel and group |
| `band_power_relative_diff_heatmap.png` | Heatmap of relative (%) band power difference: (AD − HC) / HC |

## 📁 Source Files
- `eeg_frequency_band_analysis.ipynb`: Welch PSD pipeline, band power feature extraction, and AD vs HC statistical analysis.
- `explore_alzheimer_eeg_dataset.ipynb`: Interactive EEG signal visualization and dataset exploration.
- `eeg_dataset_statistics.ipynb`: Dataset statistics and summary reporting.
- `inspect_dataset.py`: Main reporting tool for dataset metrics and matrix shapes.
- `count_subjects.py`: Script to calculate unique subjects across different diagnostic labels.
- `download_dataset.py`: Utility to ensure the Kaggle dataset is synced locally.
- `requirements.txt`: Project dependencies.
