#!/usr/bin/env python3
"""
Task 1: Plot 10 seconds of EEG from channel P4 for one HC and one AD subject.
Generates figures/eeg_10s_hc_vs_ad_p4.png for the Midterm Proposal.
"""

import numpy as np
import matplotlib.pyplot as plt
import kagglehub
import os

# Constants
FS = 128  # Hz
EPOCH_LEN = 128  # samples per epoch = 1 second
CHANNEL_NAMES = [
    'Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4',
    'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6',
    'Fz', 'Cz', 'Pz'
]
P4_IDX = CHANNEL_NAMES.index('P4')

# Subject IDs from reports (HC: AD-Auditory_10, AD: AD-Auditory_17)
HC_SUBJECT = "AD-Auditory_10"  # Healthy Control
AD_SUBJECT = "AD-Auditory_17"  # Alzheimer's Disease
N_SECONDS = 10
N_EPOCHS = N_SECONDS  # 1 epoch = 1 second


def main():
    # Load dataset
    dataset_dir = kagglehub.dataset_download("codingyodha/largest-alzheimer-eeg-dataset")
    path = os.path.join(dataset_dir, "integrated_eeg_dataset.npz")
    print(f"Loading: {path}")
    data = np.load(path, allow_pickle=True)
    X = data['X_raw']  # (n_epochs, time_samples, n_channels)
    y = data['y_labels']

    labels = np.array([float(v) for v in y[:, 0]])
    subject_ids = y[:, 1]
    sources = y[:, 2]
    global_sub_ids = np.array([f"{src}_{sub}" for src, sub in zip(sources, subject_ids)])

    # Find subject IDs (format: "AD-Auditory_10", "AD-Auditory_17"
    global_sub_ids_str = np.array([str(s) for s in global_sub_ids])
    hc_mask = global_sub_ids_str == HC_SUBJECT
    ad_mask = global_sub_ids_str == AD_SUBJECT

    if not np.any(hc_mask) or not np.any(ad_mask):
        hc_subs = np.unique(global_sub_ids_str[labels == 0.0])
        ad_subs = np.unique(global_sub_ids_str[labels == 1.0])
        HC_SUBJECT_USE = hc_subs[0] if len(hc_subs) > 0 else HC_SUBJECT
        AD_SUBJECT_USE = ad_subs[0] if len(ad_subs) > 0 else AD_SUBJECT
        print(f"Fallback: HC={HC_SUBJECT_USE}, AD={AD_SUBJECT_USE}")
        hc_mask = global_sub_ids_str == HC_SUBJECT_USE
        ad_mask = global_sub_ids_str == AD_SUBJECT_USE
    else:
        HC_SUBJECT_USE = HC_SUBJECT
        AD_SUBJECT_USE = AD_SUBJECT

    hc_epoch_indices = np.where(hc_mask)[0]
    ad_epoch_indices = np.where(ad_mask)[0]
    print(f"Found {len(hc_epoch_indices)} HC epochs, {len(ad_epoch_indices)} AD epochs")

    if len(hc_epoch_indices) < N_EPOCHS or len(ad_epoch_indices) < N_EPOCHS:
        n_epochs_use = min(len(hc_epoch_indices), len(ad_epoch_indices), N_EPOCHS)
        print(f"Warning: Using {n_epochs_use} epochs (requested {N_EPOCHS})")
        N_EPOCHS_USE = n_epochs_use
    else:
        N_EPOCHS_USE = N_EPOCHS

    # Extract first N_EPOCHS epochs, channel P4
    hc_epochs = X[hc_epoch_indices[:N_EPOCHS_USE], :, P4_IDX]  # (n_epochs, 128)
    ad_epochs = X[ad_epoch_indices[:N_EPOCHS_USE], :, P4_IDX]

    # Flatten to continuous 10-second signal
    hc_signal = hc_epochs.flatten()
    ad_signal = ad_epochs.flatten()

    # Time axis (seconds)
    n_samples = len(hc_signal)
    time_vector = np.arange(n_samples) / FS

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    fig.suptitle('10-Second EEG Signal: Healthy Control vs Alzheimer\'s Disease at Channel P4',
                 fontsize=14, fontweight='bold')

    axes[0].plot(time_vector, hc_signal, color='#2196F3', linewidth=0.8)
    axes[0].set_ylabel('Amplitude (µV)')
    axes[0].set_title(f'Healthy Control ({HC_SUBJECT_USE})')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(time_vector, ad_signal, color='#F44336', linewidth=0.8)
    axes[1].set_xlabel('Time (seconds)')
    axes[1].set_ylabel('Amplitude (µV)')
    axes[1].set_title(f'Alzheimer\'s Disease ({AD_SUBJECT_USE})')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    # Save
    os.makedirs('figures', exist_ok=True)
    out_path = 'figures/eeg_10s_hc_vs_ad_p4.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
