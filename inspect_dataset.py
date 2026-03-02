import numpy as np
import kagglehub
import os

# Download the dataset and get the path
dataset_dir = kagglehub.dataset_download("codingyodha/largest-alzheimer-eeg-dataset")
path = os.path.join(dataset_dir, "integrated_eeg_dataset.npz")

print(f"Loading dataset from: {path}\n")
data = np.load(path, allow_pickle=True)

X = data['X_raw']
y = data['y_labels']

# 1. Total Subjects and Class Distribution
global_sub_ids = [f"{src}_{sub}" for src, sub in zip(y[:, 2], y[:, 1])]
unique_subjects = np.unique(global_sub_ids)

# Labels cleanup and grouping
labels = np.array([float(x) for x in y[:, 0]])
hc_subs = np.unique(np.array(global_sub_ids)[labels == 0.0])
ad_subs = np.unique(np.array(global_sub_ids)[labels == 1.0])

# 2. Extract Shape and Rates
# X shape is (Epochs, Time_Samples, Channels)
num_epochs, time_samples, num_channels = X.shape
sampling_rate = time_samples # Each epoch is 1 second

print("=== DATASET REPORT ===")
print(f"Total number of subjects: {len(unique_subjects)}")
print(f"Number of Healthy Controls (HC): {len(hc_subs)}")
print(f"Number of Alzheimer’s Disease (AD) subjects: {len(ad_subs)}")
print(f"Number of EEG channels: {num_channels}")
print(f"Sampling rate (Hz): {sampling_rate}")
print(f"Total Recording duration: {len(y)} seconds (~{len(y)/3600:.2f} hours)")
print(f"Shape of the data matrix (per epoch): {num_channels} Channels × {time_samples} Time samples")
print(f"Full Data Matrix Shape: {X.shape}")
print("======================\n")

