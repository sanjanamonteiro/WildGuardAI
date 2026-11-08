
from pathlib import Path

import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "data/processed/spatial/bandipur_risk_scored_dataset.gpkg"
OUTPUT_GPKG = ROOT / "data/processed/spatial/bandipur_risk_classified.gpkg"
OUTPUT_CSV = ROOT / "data/processed/spatial/bandipur_risk_classified.csv"

gdf = gpd.read_file(INPUT, layer="bandipur_risk_scored")

# Fire categories: apply only to cells with recorded detections
gdf["fire_risk_category"] = "No recorded fire detection"

detected = gdf["fire_count"] > 0
fire_scores = gdf.loc[detected, "fire_threat_score"]

gdf.loc[detected & (gdf["fire_threat_score"] < 29.67),
        "fire_risk_category"] = "Low"

gdf.loc[detected & (gdf["fire_threat_score"] >= 29.67)
        & (gdf["fire_threat_score"] <= 38.26),
        "fire_risk_category"] = "Moderate"

gdf.loc[detected & (gdf["fire_threat_score"] > 38.26),
        "fire_risk_category"] = "High"

# Human-access pressure categories: all cells
gdf["human_access_category"] = "Low"

gdf.loc[gdf["human_access_pressure_score"] >= 25.99,
        "human_access_category"] = "Moderate"

gdf.loc[gdf["human_access_pressure_score"] > 39.00,
        "human_access_category"] = "High"

# Save outputs
gdf.to_file(
    OUTPUT_GPKG,
    layer="bandipur_risk_classified",
    driver="GPKG"
)

gdf.drop(columns="geometry").to_csv(OUTPUT_CSV, index=False)

# Print verification
print("=" * 55)
print("RISK CLASSIFICATION COMPLETED")
print("=" * 55)

print("\nFire risk categories:")
print(gdf["fire_risk_category"].value_counts().to_string())

print("\nHuman-access pressure categories:")
print(gdf["human_access_category"].value_counts().to_string())

print("\nValidation:")
print("Total grid cells:", len(gdf))
print("Unique cell IDs:", gdf["cell_id"].nunique())
print("Missing fire categories:", gdf["fire_risk_category"].isna().sum())
print("Missing access categories:", gdf["human_access_category"].isna().sum())

print("\nOutput files:")
print(OUTPUT_GPKG)
print(OUTPUT_CSV)
