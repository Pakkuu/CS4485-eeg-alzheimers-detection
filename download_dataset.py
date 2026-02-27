import kagglehub
import os

path = kagglehub.dataset_download("codingyodha/largest-alzheimer-eeg-dataset")

print("Path:", path)
for root, dirs, files in os.walk(path):
    for f in files:
        print(os.path.join(root, f))
