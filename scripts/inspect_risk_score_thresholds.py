
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "data/processed/spatial/bandipur_risk_scored_dataset.csv"

df = pd.read_csv(INPUT)

print("=" * 55)
print("FIRE THREAT SCORE THRESHOLDS")
print("=" * 55)

detected = df[df["fire_count"] > 0]["fire_threat_score"]

print("\nCells with recorded fire:", len(detected))
print("\nDetected-cell score distribution:")
print(detected.describe(percentiles=[0.33, 0.67]).round(2))

fire_thresholds = detected.quantile([0.33, 0.67])

print("\nProposed fire thresholds:")
print("33rd percentile:", round(fire_thresholds.loc[0.33], 2))
print("67th percentile:", round(fire_thresholds.loc[0.67], 2))

print("\nUnique detected-fire scores:", detected.nunique())

print("\n" + "=" * 55)
print("HUMAN-ACCESS PRESSURE THRESHOLDS")
print("=" * 55)

access = df["human_access_pressure_score"]

print("\nAll-cell score distribution:")
print(access.describe(percentiles=[0.33, 0.67]).round(2))

access_thresholds = access.quantile([0.33, 0.67])

print("\nProposed human-access thresholds:")
print("33rd percentile:", round(access_thresholds.loc[0.33], 2))
print("67th percentile:", round(access_thresholds.loc[0.67], 2))

print("\nUnique human-access scores:", access.nunique())

print("\nThreshold inspection completed.")
