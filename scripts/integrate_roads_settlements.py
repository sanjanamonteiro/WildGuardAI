import geopandas as gpd
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUTPUT = BASE / "data" / "processed" / "spatial"
OUTPUT.mkdir(parents=True, exist_ok=True)

CRS = "EPSG:32643"

# Load grid
grid = gpd.read_file(
    OUTPUT / "bandipur_1km_grid.gpkg",
    layer="bandipur_grid"
).to_crs(CRS)

# Load roads and retain actual road lines
roads = gpd.read_file(
    BASE / "data" / "raw" / "roads" / "export.geojson"
).to_crs(CRS)

roads = roads[
    (roads.geometry.geom_type == "LineString")
    & roads["highway"].notna()
].copy()

# Calculate road length inside each grid cell
road_intersections = gpd.overlay(
    roads[["highway", "geometry"]],
    grid[["cell_id", "geometry"]],
    how="intersection",
    keep_geom_type=True
)

road_intersections["length_km"] = (
    road_intersections.geometry.length / 1000
)

road_summary = (
    road_intersections
    .pivot_table(
        index="cell_id",
        columns="highway",
        values="length_km",
        aggfunc="sum",
        fill_value=0
    )
)

road_summary.columns = [
    f"road_{str(col).replace('-', '_')}_km"
    for col in road_summary.columns
]

road_summary["road_length_km"] = road_summary.sum(axis=1)

# Separate selected road categories
for category in ["residential", "track"]:
    column = f"road_{category}_km"

    if column not in road_summary.columns:
        road_summary[column] = 0.0

other_columns = [
    col for col in road_summary.columns
    if col.startswith("road_")
    and col.endswith("_km")
    and col not in [
        "road_length_km",
        "road_residential_km",
        "road_track_km"
    ]
]

road_summary["road_other_km"] = (
    road_summary[other_columns].sum(axis=1)
)

# Merge road indicators into every grid cell
result = grid.merge(
    road_summary.reset_index(),
    on="cell_id",
    how="left"
)

road_columns = [
    col for col in result.columns
    if col.startswith("road_")
]

result[road_columns] = result[road_columns].fillna(0)

result["road_density_km_per_km2"] = (
    result["road_length_km"] / result["area_km2"]
)

# Load settlements
settlements = gpd.read_file(
    BASE / "data" / "raw" / "settlements" / "settlements.geojson"
).to_crs(CRS)

settlements = settlements[
    settlements.geometry.geom_type == "Point"
].copy()

# Count settlements inside each grid cell
settlement_join = gpd.sjoin(
    settlements[["place", "geometry"]],
    grid[["cell_id", "geometry"]],
    how="left",
    predicate="within"
)

settlement_counts = (
    settlement_join.groupby("cell_id")
    .size()
    .rename("settlement_count")
)

result = result.merge(
    settlement_counts,
    on="cell_id",
    how="left"
)

result["settlement_count"] = (
    result["settlement_count"].fillna(0).astype(int)
)

# Calculate distance from each grid centroid
# to the nearest mapped settlement
centroids = result[["cell_id", "geometry"]].copy()
centroids["geometry"] = centroids.geometry.centroid

nearest = gpd.sjoin_nearest(
    centroids,
    settlements[["geometry"]],
    how="left",
    distance_col="nearest_settlement_m"
)

nearest = nearest[
    ["cell_id", "nearest_settlement_m"]
].drop_duplicates("cell_id")

nearest["nearest_settlement_km"] = (
    nearest["nearest_settlement_m"] / 1000
)

result = result.merge(
    nearest[["cell_id", "nearest_settlement_km"]],
    on="cell_id",
    how="left"
)

# Validation
print("\nROAD AND SETTLEMENT INTEGRATION")
print("--------------------------------")
print("Grid cells:", len(result))
print("Road features used:", len(roads))
print("Settlement points:", len(settlements))
print("Cells with roads:", int((result["road_length_km"] > 0).sum()))
print("Cells without roads:", int((result["road_length_km"] == 0).sum()))
print("Total road length (km):", round(result["road_length_km"].sum(), 3))
print("Cells with settlements:", int((result["settlement_count"] > 0).sum()))
print("Total settlements assigned:", int(result["settlement_count"].sum()))
print("Cells without nearest settlement:", int(result["nearest_settlement_km"].isna().sum()))
print("Invalid geometries:", int((~result.geometry.is_valid).sum()))
print("Duplicate cell IDs:", int(result["cell_id"].duplicated().sum()))

# Save outputs
result.to_file(
    OUTPUT / "bandipur_grid_roads_settlements.gpkg",
    layer="bandipur_grid_roads_settlements",
    driver="GPKG"
)

result.drop(columns="geometry").to_csv(
    OUTPUT / "bandipur_grid_roads_settlements.csv",
    index=False
)

print("\nGeoPackage: data\\processed\\spatial\\bandipur_grid_roads_settlements.gpkg")
print("CSV: data\\processed\\spatial\\bandipur_grid_roads_settlements.csv")