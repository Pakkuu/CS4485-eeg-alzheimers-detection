# EEG Alzheimer's Detection

This project explores and analyzes the [Largest Alzheimer EEG Dataset](https://www.kaggle.com/datasets/codingyodha/largest-alzheimer-eeg-dataset) to build models for automated Alzheimer's Disease (AD) detection using electroencephalogram (EEG) signals.

## 📊 Dataset Overview

The dataset is an integrated collection of EEG recordings from multiple sources, standardized for Alzheimer's research.

### Key Statistics
| Metric | Value |
| :--- | :--- |
| **Total Subjects** | 241 |
| **Healthy Controls (HC)** | 78 |
| **Alzheimer’s Disease (AD)** | 122 |
| **EEG Channels** | 19 |
| **Sampling Rate** | 128 Hz |
| **Total Duration** | 101,916 seconds (~28.3 hours) |
| **Epoch Duration** | 1 second |
| **Data Matrix Shape** | 19 Channels × 128 Time samples |

*Note: The remaining subjects in the dataset represent other conditions such as MCI (Mild Cognitive Impairment).*

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

## 📁 Source Files
- `inspect_dataset.py`: Main reporting tool for dataset metrics and matrix shapes.
- `count_subjects.py`: Script to calculate unique subjects across different diagnostic labels.
- `download_dataset.py`: Utility to ensure the Kaggle dataset is synced locally.
- `requirements.txt`: Project dependencies.
