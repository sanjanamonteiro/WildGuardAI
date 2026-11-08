from pathlib import Path

import geopandas as gpd
import pandas as pd

GRID_FILE = Path("data/processed/spatial/bandipur_1km_grid.gpkg")
FIRE_FILE = Path("data/processed/fire/bandipur_fire_detections.geojson")

OUTPUT_DIR = Path("data/processed/spatial")
OUTPUT_GPKG = OUTPUT_DIR / "bandipur_grid_fire.gpkg"
OUTPUT_CSV = OUTPUT_DIR / "bandipur_grid_fire.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

grid = gpd.read_file(GRID_FILE, layer="bandipur_grid")
fire = gpd.read_file(FIRE_FILE).to_crs(grid.crs)

fire["acq_date"] = pd.to_datetime(fire["acq_date"], errors="coerce")
fire["year"] = fire["acq_date"].dt.year
fire["frp"] = pd.to_numeric(fire["frp"], errors="coerce")

# Assign each fire detection to one grid cell.
joined = gpd.sjoin(
    fire,
    grid[["cell_id", "geometry"]],
    how="left",
    predicate="within"
)

if joined["cell_id"].isna().any():
    raise ValueError("Some fire detections were not assigned to grid cells.")

if joined["cell_id"].duplicated().all():
    pass

# Aggregate fire characteristics by grid cell.
summary = joined.groupby("cell_id").agg(
    fire_count=("cell_id", "size"),
    fire_frp_mean=("frp", "mean"),
    fire_frp_max=("frp", "max"),
    fire_confidence_high=("confidence", lambda x: (x == "h").sum()),
    fire_confidence_nominal=("confidence", lambda x: (x == "n").sum()),
    fire_confidence_low=("confidence", lambda x: (x == "l").sum()),
).reset_index()

# Add annual detection counts.
yearly = (
    joined.groupby(["cell_id", "year"])
    .size()
    .unstack(fill_value=0)
)

for year in range(2020, 2026):
    summary = summary.merge(
        yearly[[year]].rename(
            columns={year: f"fire_count_{year}"}
        ).reset_index(),
        on="cell_id",
        how="left"
    ) if year in yearly.columns else summary.assign(
        **{f"fire_count_{year}": 0}
    )

# Merge onto the full grid so cells without fire detections remain.
integrated = grid.merge(
    summary,
    on="cell_id",
    how="left",
    validate="one_to_one"
)

count_columns = [
    "fire_count",
    "fire_confidence_high",
    "fire_confidence_nominal",
    "fire_confidence_low",
] + [f"fire_count_{year}" for year in range(2020, 2026)]

integrated[count_columns] = integrated[count_columns].fillna(0).astype(int)

if OUTPUT_GPKG.exists():
    OUTPUT_GPKG.unlink()

integrated.to_file(
    OUTPUT_GPKG,
    layer="bandipur_grid_fire",
    driver="GPKG",
    index=False
)

integrated.drop(columns="geometry").to_csv(OUTPUT_CSV, index=False)

print("\nFIRE INTEGRATION COMPLETE")
print("-------------------------")
print("Grid cells:", len(integrated))
print("Total fire detections:", int(integrated["fire_count"].sum()))
print("Cells with fire detections:", int((integrated["fire_count"] > 0).sum()))
print("Cells without fire detections:", int((integrated["fire_count"] == 0).sum()))
print("High confidence:", int(integrated["fire_confidence_high"].sum()))
print("Nominal confidence:", int(integrated["fire_confidence_nominal"].sum()))
print("Low confidence:", int(integrated["fire_confidence_low"].sum()))
print("Invalid geometries:", int((~integrated.geometry.is_valid).sum()))

print("\nAnnual fire counts:")
for year in range(2020, 2026):
    print(year, int(integrated[f"fire_count_{year}"].sum()))

print("\nGeoPackage:", OUTPUT_GPKG)
print("CSV:", OUTPUT_CSV)
