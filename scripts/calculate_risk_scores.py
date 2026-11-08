
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "data/processed/spatial/bandipur_risk_analysis_dataset.gpkg"
OUTPUT_GPKG = ROOT / "data/processed/spatial/bandipur_risk_scored_dataset.gpkg"
OUTPUT_CSV = ROOT / "data/processed/spatial/bandipur_risk_scored_dataset.csv"

LAYER = "bandipur_risk_analysis"


def log_minmax(series):
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().any() or (values < 0).any():
        raise ValueError(f"Invalid values in {series.name}")

    transformed = np.log1p(values)
    minimum = transformed.min()
    maximum = transformed.max()

    if maximum == minimum:
        return pd.Series(0.0, index=series.index)

    return (transformed - minimum) / (maximum - minimum)


def minmax(series):
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().any():
        raise ValueError(f"Missing values in {series.name}")

    minimum = values.min()
    maximum = values.max()

    if maximum == minimum:
        return pd.Series(0.0, index=series.index)

    return (values - minimum) / (maximum - minimum)


def main():
    print("Loading risk analysis dataset...")

    gdf = gpd.read_file(INPUT, layer=LAYER)

    required = [
        "cell_id",
        "fire_count",
        "fire_frp_mean",
        "road_density_km_per_km2",
        "nearest_settlement_km",
    ]

    missing = [column for column in required if column not in gdf.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if len(gdf) != 1084 or gdf["cell_id"].duplicated().any():
        raise ValueError("Grid validation failed.")

    # Fire frequency component
    gdf["fire_frequency_component"] = (
        log_minmax(gdf["fire_count"]) * 100
    )

    # Fire intensity component: detected cells only
    detected = gdf["fire_count"] > 0

    if gdf.loc[detected, "fire_frp_mean"].isna().any():
        raise ValueError("A detected-fire cell has missing mean FRP.")

    gdf["fire_intensity_component"] = 0.0

    gdf.loc[detected, "fire_intensity_component"] = (
        log_minmax(gdf.loc[detected, "fire_frp_mean"]) * 100
    )

    # Equal-weight fire threat score
    gdf["fire_threat_score"] = (
        0.5 * gdf["fire_frequency_component"]
        + 0.5 * gdf["fire_intensity_component"]
    )

    # Road density component
    gdf["road_density_component"] = (
        log_minmax(gdf["road_density_km_per_km2"]) * 100
    )

    # Settlement proximity component
    distance = pd.to_numeric(
        gdf["nearest_settlement_km"], errors="coerce"
    )

    if distance.isna().any() or (distance < 0).any():
        raise ValueError("Invalid settlement distances.")

    gdf["settlement_proximity_component"] = (
        (1 - minmax(distance)) * 100
    )

    # Equal-weight human-access pressure score
    gdf["human_access_pressure_score"] = (
        0.5 * gdf["road_density_component"]
        + 0.5 * gdf["settlement_proximity_component"]
    )

    # Validate all scores
    score_columns = [
        "fire_frequency_component",
        "fire_intensity_component",
        "fire_threat_score",
        "road_density_component",
        "settlement_proximity_component",
        "human_access_pressure_score",
    ]

    for column in score_columns:
        if gdf[column].isna().any():
            raise ValueError(f"Missing scores in {column}")

        if not gdf[column].between(0, 100).all():
            raise ValueError(f"Scores outside 0-100 in {column}")

    # Save outputs
    gdf.to_file(
        OUTPUT_GPKG,
        layer="bandipur_risk_scored",
        driver="GPKG",
    )

    gdf.drop(columns="geometry").to_csv(OUTPUT_CSV, index=False)

    print("\nRISK SCORING COMPLETED")
    print("=" * 50)
    print("Total grid cells:", len(gdf))
    print("Cells with recorded fire:", int(detected.sum()))
    print("Cells without recorded fire:", int((~detected).sum()))

    print("\nScore summaries:")

    for column in [
        "fire_threat_score",
        "human_access_pressure_score",
    ]:
        print(f"\n{column}")
        print(gdf[column].describe().round(2).to_string())

    print("\nOutput files:")
    print(OUTPUT_GPKG)
    print(OUTPUT_CSV)


if __name__ == "__main__":
    main()
