import geopandas as gpd
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
FOLDER = BASE / "data" / "processed" / "spatial"

# Load the original grid as the master geometry
master = gpd.read_file(
    FOLDER / "bandipur_1km_grid.gpkg",
    layer="bandipur_grid"
)

datasets = {
    "vegetation": (
        "bandipur_grid_vegetation.gpkg",
        "bandipur_grid_vegetation"
    ),
    "fire": (
        "bandipur_grid_fire.gpkg",
        "bandipur_grid_fire"
    ),
    "wildlife": (
        "bandipur_grid_wildlife.gpkg",
        "bandipur_grid_wildlife"
    ),
    "roads_settlements": (
        "bandipur_grid_roads_settlements.gpkg",
        "bandipur_grid_roads_settlements"
    )
}

# Validate and merge each dataset
for name, (filename, layer) in datasets.items():

    print(f"\nLoading {name}...")

    data = gpd.read_file(
        FOLDER / filename,
        layer=layer
    )

    if len(data) != 1084:
        raise ValueError(f"{name}: unexpected row count")

    if data["cell_id"].duplicated().any():
        raise ValueError(f"{name}: duplicate cell IDs")

    if set(data["cell_id"]) != set(master["cell_id"]):
        raise ValueError(f"{name}: grid cell IDs do not match")

    if data.crs != master.crs:
        raise ValueError(f"{name}: CRS mismatch")

    # Keep the original grid geometry only
    attributes = pd.DataFrame(
        data.drop(columns="geometry")
    )

    # Avoid duplicating columns already in the master grid
    attributes = attributes.drop(
        columns=[
            col for col in attributes.columns
            if col in master.columns and col != "cell_id"
        ],
        errors="ignore"
    )

    master = master.merge(
        attributes,
        on="cell_id",
        how="left",
        validate="one_to_one"
    )

    print(f"{name} merged successfully.")

# Final validation
print("\nMASTER SPATIAL DATASET VALIDATION")
print("---------------------------------")
print("Total rows:", len(master))
print("Unique grid cells:", master["cell_id"].nunique())
print("Total columns:", len(master.columns))
print("CRS:", master.crs)
print("Duplicate cell IDs:", int(master["cell_id"].duplicated().sum()))
print("Invalid geometries:", int((~master.geometry.is_valid).sum()))

# Save master dataset
gpkg_path = FOLDER / "bandipur_master_spatial_dataset.gpkg"
csv_path = FOLDER / "bandipur_master_spatial_dataset.csv"

master.to_file(
    gpkg_path,
    layer="bandipur_master",
    driver="GPKG"
)

master.drop(columns="geometry").to_csv(
    csv_path,
    index=False
)

print("\nMASTER DATASET CREATED")
print("GeoPackage:", gpkg_path)
print("CSV:", csv_path)

print("\nColumn names:")
print(master.drop(columns="geometry").columns.tolist())