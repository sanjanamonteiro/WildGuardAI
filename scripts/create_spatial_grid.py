import math
from pathlib import Path

import geopandas as gpd
from shapely.geometry import box

BOUNDARY_FILE = Path("data/raw/boundaries/bandipur_boundary.geojson")
OUTPUT_DIR = Path("data/processed/spatial")
OUTPUT_FILE = OUTPUT_DIR / "bandipur_1km_grid.gpkg"

CELL_SIZE = 1000
TARGET_CRS = "EPSG:32643"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

boundary = gpd.read_file(BOUNDARY_FILE).to_crs(TARGET_CRS)
reserve = boundary.geometry.union_all()

minx, miny, maxx, maxy = reserve.bounds

grid_records = []

rows = math.ceil((maxy - miny) / CELL_SIZE)
cols = math.ceil((maxx - minx) / CELL_SIZE)

for row in range(rows):
    for col in range(cols):
        cell = box(
            minx + col * CELL_SIZE,
            miny + row * CELL_SIZE,
            minx + (col + 1) * CELL_SIZE,
            miny + (row + 1) * CELL_SIZE
        )

        if not cell.intersects(reserve):
            continue

        clipped = cell.intersection(reserve)

        if clipped.is_empty or clipped.area == 0:
            continue

        grid_records.append({
            "cell_id": f"B{row:02d}_{col:02d}",
            "grid_row": row,
            "grid_col": col,
            "area_km2": round(clipped.area / 1_000_000, 6),
            "geometry": clipped
        })

grid = gpd.GeoDataFrame(
    grid_records,
    geometry="geometry",
    crs=TARGET_CRS
)

if OUTPUT_FILE.exists():
    OUTPUT_FILE.unlink()

grid.to_file(
    OUTPUT_FILE,
    layer="bandipur_grid",
    driver="GPKG",
    index=False
)

print("\nSPATIAL GRID CREATED")
print("--------------------")
print("Output:", OUTPUT_FILE)
print("CRS:", grid.crs)
print("Grid cells:", len(grid))
print("Total clipped area (sq. km):", round(grid.area.sum() / 1_000_000, 2))
print("Invalid geometries:", int((~grid.geometry.is_valid).sum()))
print("Empty geometries:", int(grid.geometry.is_empty.sum()))
print("Minimum cell area (sq. km):", round(grid.area.min() / 1_000_000, 4))
print("Maximum cell area (sq. km):", round(grid.area.max() / 1_000_000, 4))
print("\nFirst five cells:")
print(grid[["cell_id", "area_km2"]].head().to_string(index=False))
