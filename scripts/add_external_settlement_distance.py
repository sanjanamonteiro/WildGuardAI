import geopandas as gpd
from pathlib import Path

BASE = Path("data/processed/spatial")

# Load existing integrated dataset
result = gpd.read_file(
    BASE / "bandipur_grid_roads_settlements.gpkg",
    layer="bandipur_grid_roads_settlements"
)

# Load boundary and settlement data
boundary = gpd.read_file(
    "data/raw/boundaries/bandipur_boundary.geojson"
).to_crs(result.crs)

settlements = gpd.read_file(
    "data/raw/settlements/settlements.geojson"
).to_crs(result.crs)

# Separate outside settlements
check = gpd.sjoin(
    settlements,
    boundary[["geometry"]],
    how="left",
    predicate="within"
)

outside = settlements.loc[
    check["index_right"].isna()
].copy()

# Calculate grid-cell centroids
centroids = result[["cell_id", "geometry"]].copy()
centroids["geometry"] = centroids.geometry.centroid

# Find nearest outside settlement for every grid cell
nearest = gpd.sjoin_nearest(
    centroids,
    outside[["geometry"]],
    how="left",
    distance_col="nearest_external_settlement_distance_m"
)

distances = nearest.groupby("cell_id")[
    "nearest_external_settlement_distance_m"
].min()

result["nearest_external_settlement_distance_m"] = (
    result["cell_id"].map(distances)
)

result["nearest_external_settlement_distance_km"] = (
    result["nearest_external_settlement_distance_m"] / 1000
)

# Save updated outputs
gpkg = BASE / "bandipur_grid_roads_settlements.gpkg"
csv = BASE / "bandipur_grid_roads_settlements.csv"

result.to_file(
    gpkg,
    layer="bandipur_grid_roads_settlements",
    driver="GPKG"
)

result.drop(columns="geometry").to_csv(csv, index=False)

print("\nEXTERNAL SETTLEMENT DISTANCE INTEGRATION")
print("---------------------------------------")
print("Outside settlements:", len(outside))
print("Grid cells:", len(result))
print(
    "Minimum distance (km):",
    round(result["nearest_external_settlement_distance_km"].min(), 3)
)
print(
    "Maximum distance (km):",
    round(result["nearest_external_settlement_distance_km"].max(), 3)
)
print("Missing distances:", int(
    result["nearest_external_settlement_distance_km"].isna().sum()
))
print("Invalid geometries:", int((~result.geometry.is_valid).sum()))
print("Updated GeoPackage:", gpkg)
print("Updated CSV:", csv)
