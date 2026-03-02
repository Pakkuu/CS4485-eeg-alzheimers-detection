import numpy as np
import kagglehub
import os

# Download the dataset and get the path
dataset_dir = kagglehub.dataset_download("codingyodha/largest-alzheimer-eeg-dataset")
path = os.path.join(dataset_dir, "integrated_eeg_dataset.npz")
data = np.load(path, allow_pickle=True)
y = data['y_labels']

# Clean up labels because there are '0' and '0.0'
labels = np.array([float(x) for x in y[:, 0]])

# subject ID is column 1
subject_ids = y[:, 1]

# Create global unique ID by combining dataset source + subject ID just in case subject IDs overlap between datasets
global_sub_ids = [f"{src}_{sub}" for src, sub in zip(y[:, 2], y[:, 1])]

for L in np.unique(labels):
    mask = labels == L
    subs = np.unique(np.array(global_sub_ids)[mask])
    print(f"Label {L} has {len(subs)} unique subjects")

total_subjects = len(np.unique(global_sub_ids))
print(f"Total unique subjects (global): {total_subjects}")

total_duration_sec_per_sub = []
for sub in np.unique(global_sub_ids):
    sub_mask = np.array(global_sub_ids) == sub
    total_duration_sec_per_sub.append(np.sum(sub_mask)) # 1 sec per epoch

print(f"Average duration per subject: {np.mean(total_duration_sec_per_sub):.2f} seconds")
print(f"Total dataset duration: {len(y)} seconds")
