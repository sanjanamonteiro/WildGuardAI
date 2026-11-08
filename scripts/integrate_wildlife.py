import geopandas as gpd
import pandas as pd
from pathlib import Path

# File paths
grid_path = "data/processed/spatial/bandipur_1km_grid.gpkg"
wildlife_path = "data/processed/wildlife/bandipur_wildlife_observations.geojson"
output_dir = Path("data/processed/spatial")
output_dir.mkdir(parents=True, exist_ok=True)

# Read grid and wildlife observations
grid = gpd.read_file(grid_path, layer="bandipur_grid")
wildlife = gpd.read_file(wildlife_path).to_crs(grid.crs)

# Assign observations to grid cells
joined = gpd.sjoin(
    wildlife,
    grid[["cell_id", "geometry"]],
    how="left",
    predicate="within"
)

if joined["cell_id"].isna().any():
    raise ValueError("Some wildlife observations could not be assigned to grid cells.")

# Prepare observation fields
joined["class"] = joined["class"].fillna("").astype(str).str.strip()
joined["scientificName"] = joined["scientificName"].fillna("").astype(str).str.strip()

if "year" in joined.columns:
    joined["observation_year"] = pd.to_numeric(
        joined["year"], errors="coerce"
    )
else:
    joined["observation_year"] = pd.to_datetime(
        joined["eventDate"], errors="coerce"
    ).dt.year

# Overall indicators per grid cell
summary = joined.groupby("cell_id").agg(
    wildlife_observation_count=("cell_id", "size"),
    bird_observation_count=("class", lambda x: (x == "Aves").sum()),
    mammal_observation_count=("class", lambda x: (x == "Mammalia").sum()),
    distinct_species_count=(
        "scientificName",
        lambda x: x[x != ""].nunique()
    )
).reset_index()

# Annual observation counts
yearly = (
    joined[joined["observation_year"].between(2020, 2025)]
    .groupby(["cell_id", "observation_year"])
    .size()
    .unstack(fill_value=0)
)

for year in range(2020, 2026):
    if year not in yearly.columns:
        yearly[year] = 0

yearly = yearly[list(range(2020, 2026))]
yearly.columns = [f"wildlife_observations_{year}" for year in yearly.columns]
yearly = yearly.reset_index()

summary = summary.merge(yearly, on="cell_id", how="left")

# Add indicators to every grid cell
result = grid.merge(summary, on="cell_id", how="left")

count_columns = [
    "wildlife_observation_count",
    "bird_observation_count",
    "mammal_observation_count",
    "distinct_species_count"
] + [f"wildlife_observations_{year}" for year in range(2020, 2026)]

result[count_columns] = result[count_columns].fillna(0).astype(int)

# Save outputs
gpkg_path = output_dir / "bandipur_grid_wildlife.gpkg"
csv_path = output_dir / "bandipur_grid_wildlife.csv"

if gpkg_path.exists():
    gpkg_path.unlink()

result.to_file(
    gpkg_path,
    layer="bandipur_grid_wildlife",
    driver="GPKG"
)

result.drop(columns="geometry").to_csv(csv_path, index=False)

# Validation
print("\nWILDLIFE INTEGRATION COMPLETE")
print("--------------------------------")
print("Grid cells:", len(result))
print("Total wildlife observations:", result["wildlife_observation_count"].sum())
print("Bird observations:", result["bird_observation_count"].sum())
print("Mammal observations:", result["mammal_observation_count"].sum())
print("Cells with wildlife observations:", (result["wildlife_observation_count"] > 0).sum())
print("Cells without wildlife observations:", (result["wildlife_observation_count"] == 0).sum())
print("Distinct species across dataset:", joined["scientificName"].replace("", pd.NA).nunique())
print("Invalid geometries:", (~result.geometry.is_valid).sum())

print("\nAnnual wildlife observation counts:")
for year in range(2020, 2026):
    column = f"wildlife_observations_{year}"
    print(year, int(result[column].sum()))

print("\nGeoPackage:", gpkg_path)
print("CSV:", csv_path)
