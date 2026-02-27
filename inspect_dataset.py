import numpy as np

path = "/Users/ajayalluri/.cache/kagglehub/datasets/codingyodha/largest-alzheimer-eeg-dataset/versions/1/integrated_eeg_dataset.npz"

print("Loading dataset...")
data = np.load(path, allow_pickle=True)

y = data['y_labels']
print("y_labels sample:", y[0])
print("y_labels unique values in column 0:", np.unique(y[:, 0]))
print("y_labels unique values in column 1:", np.unique(y[:, 1]))
print("y_labels unique values in column 2:", len(np.unique(y[:, 2])), "unique subjects? Sample:", np.unique(y[:, 2])[:5])

# Calculate sampling rate logic if there's any duration info or let's check

