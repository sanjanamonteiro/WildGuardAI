
from pathlib import Path

import geopandas as gpd
import pandas as pd


# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "spatial"
    / "bandipur_master_spatial_dataset.gpkg"
)

OUTPUT_DIR = PROJECT_DIR / "data" / "processed" / "spatial"

OUTPUT_GPKG = OUTPUT_DIR / "bandipur_risk_analysis_dataset.gpkg"
OUTPUT_CSV = OUTPUT_DIR / "bandipur_risk_analysis_dataset.csv"

VEGETATION_COLUMNS = [
    "tree_pct",
    "shrubland_pct",
    "grassland_pct",
    "cropland_pct",
    "builtup_pct",
    "bare_sparse_pct",
    "water_pct",
]


def main():
    print("PREPARING RISK ANALYSIS DATASET")
    print("--------------------------------")

    # Check that the original dataset exists
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input dataset not found: {INPUT_FILE}")

    # Load the original master spatial dataset
    gdf = gpd.read_file(
        INPUT_FILE,
        layer="bandipur_master"
    )

    print("Original grid cells:", len(gdf))

    # Validate essential columns
    required_columns = [
        "cell_id",
        "valid_pixels",
        "fire_count",
        "fire_frp_mean",
        "fire_frp_max",
        *VEGETATION_COLUMNS,
    ]

    missing_columns = [
        column for column in required_columns
        if column not in gdf.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Required columns are missing: {missing_columns}"
        )

    if gdf["cell_id"].duplicated().any():
        raise ValueError("Duplicate cell IDs found.")

    if gdf["fire_count"].isna().any():
        raise ValueError("Fire count contains missing values.")

    if (gdf["fire_count"] < 0).any():
        raise ValueError("Negative fire counts found.")

    # Identify cells with valid vegetation information
    gdf["vegetation_data_available"] = (
        gdf["valid_pixels"].gt(0)
        & gdf[VEGETATION_COLUMNS].notna().all(axis=1)
    )

    # Identify cells with recorded fire detections
    gdf["fire_detected"] = gdf["fire_count"].gt(0)

    # FRP is available only when both FRP measurements exist
    gdf["frp_available"] = (
        gdf["fire_frp_mean"].notna()
        & gdf["fire_frp_max"].notna()
    )

    # Check consistency between fire detections and FRP availability
    inconsistent_fire_cells = (
        gdf["fire_detected"] != gdf["frp_available"]
    )

    if inconsistent_fire_cells.any():
        raise ValueError(
            "Fire detection and FRP availability are inconsistent."
        )

    # Prepare output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save a fresh GeoPackage
    if OUTPUT_GPKG.exists():
        OUTPUT_GPKG.unlink()

    gdf.to_file(
        OUTPUT_GPKG,
        layer="bandipur_risk_analysis",
        driver="GPKG",
        index=False
    )

    # Save a CSV without geometry
    csv_df = pd.DataFrame(gdf.drop(columns="geometry"))
    csv_df.to_csv(OUTPUT_CSV, index=False)

    # Final validation
    print("\nDATASET VALIDATION")
    print("------------------")
    print("Total grid cells:", len(gdf))
    print("Total columns:", len(gdf.columns))
    print("Unique cell IDs:", gdf["cell_id"].nunique())
    print("CRS:", gdf.crs)
    print("Invalid geometries:", (~gdf.geometry.is_valid).sum())

    print("\nDATA AVAILABILITY")
    print("-----------------")
    print(
        "Cells with vegetation data:",
        int(gdf["vegetation_data_available"].sum())
    )
    print(
        "Cells without vegetation data:",
        int((~gdf["vegetation_data_available"]).sum())
    )
    print(
        "Cells with fire detections:",
        int(gdf["fire_detected"].sum())
    )
    print(
        "Cells without recorded fire detections:",
        int((~gdf["fire_detected"]).sum())
    )
    print(
        "Cells with FRP data:",
        int(gdf["frp_available"].sum())
    )

    print("\nOUTPUT FILES")
    print("------------")
    print(OUTPUT_GPKG)
    print(OUTPUT_CSV)

    print("\nRISK ANALYSIS DATASET PREPARATION COMPLETE")


if __name__ == "__main__":
    main()
