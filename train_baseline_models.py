#!/usr/bin/env python3
"""
Baseline HC vs AD classification using subject-level band-power features.

Uses eeg_band_analysis_csv/eeg_band_power_subject_level.csv (from
eeg_frequency_band_analysis.ipynb). Binary labels only: HC vs AD (FTD excluded).

Evaluation: stratified k-fold cross-validation at the subject level (no epoch leakage).

Metrics: accuracy, ROC-AUC, sensitivity (recall on AD), specificity.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

FEATURE_COLS = ["Delta_Power", "Theta_Power", "Alpha_Power", "Beta_Power"]


def load_subject_table(csv_path: Path) -> pd.DataFrame:
    if not csv_path.is_file():
        print(
            f"Missing: {csv_path}\n"
            "Generate it by running eeg_frequency_band_analysis.ipynb "
            "(writes eeg_band_power_subject_level.csv).",
            file=sys.stderr,
        )
        sys.exit(1)
    df = pd.read_csv(csv_path)
    return df


def prepare_xy(df: pd.DataFrame):
    sub = df[df["Group"].isin(["HC", "AD"])].copy()
    if len(sub) < 10:
        raise ValueError("Too few HC/AD subjects after filtering.")
    X = sub[FEATURE_COLS].values.astype(np.float64)
    y = (sub["Group"] == "AD").astype(int).values
    return X, y, sub["Subject"].values


def specificity_score(y_true, y_pred) -> float:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fp) if (tn + fp) > 0 else 0.0


def sensitivity_score(y_true, y_pred) -> float:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0


def evaluate_model(name: str, clf, X, y, n_splits: int = 5, random_state: int = 42):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    y_proba = cross_val_predict(
        clf, X, y, cv=skf, method="predict_proba", n_jobs=-1
    )[:, 1]
    y_hat = (y_proba >= 0.5).astype(int)

    acc = accuracy_score(y, y_hat)
    try:
        auc = roc_auc_score(y, y_proba)
    except ValueError:
        auc = float("nan")
    sens = sensitivity_score(y, y_hat)
    spec = specificity_score(y, y_hat)

    print(f"\n=== {name} (stratified {n_splits}-fold CV, subject-level) ===")
    print(f"  Accuracy   : {acc:.4f}")
    print(f"  ROC-AUC    : {auc:.4f}")
    print(f"  Sensitivity (AD recall): {sens:.4f}")
    print(f"  Specificity (HC recall): {spec:.4f}")
    print(f"  Confusion (rows=true AD/HC as 1/0, cols=pred): ")
    cm = confusion_matrix(y, y_hat, labels=[1, 0])
    print(f"               pred AD  pred HC")
    print(f"    true AD    {cm[0,0]:6d}   {cm[0,1]:6d}")
    print(f"    true HC    {cm[1,0]:6d}   {cm[1,1]:6d}")


def main():
    parser = argparse.ArgumentParser(description="Baseline HC vs AD models")
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path("eeg_band_analysis_csv/eeg_band_power_subject_level.csv"),
        help="Subject-level band power CSV",
    )
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    df = load_subject_table(args.csv)
    X, y, subjects = prepare_xy(df)
    print(f"Subjects: {len(subjects)} (AD={y.sum()}, HC={len(y) - y.sum()})")
    print(f"Features: {FEATURE_COLS}")

    lr = Pipeline(
        [
            ("scale", StandardScaler()),
            (
                "clf",
                LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced",
                    random_state=args.seed,
                ),
            ),
        ]
    )
    rf = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        class_weight="balanced",
        random_state=args.seed,
        n_jobs=-1,
    )

    evaluate_model("Logistic Regression", lr, X, y, n_splits=args.folds, random_state=args.seed)
    evaluate_model("Random Forest", rf, X, y, n_splits=args.folds, random_state=args.seed)
    print("\nDone.")


if __name__ == "__main__":
    main()
