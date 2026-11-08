from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.enums import Resampling
from rasterio.mask import mask
from rasterio.warp import calculate_default_transform, reproject

GRID_FILE = Path("data/processed/spatial/bandipur_1km_grid.gpkg")
SOURCE_RASTER = Path("data/processed/vegetation/bandipur_worldcover_2021.tif")

OUTPUT_DIR = Path("data/processed/spatial")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALIGNED_RASTER = OUTPUT_DIR / "bandipur_worldcover_2021_utm43n_10m.tif"
OUTPUT_GPKG = OUTPUT_DIR / "bandipur_grid_vegetation.gpkg"
OUTPUT_CSV = OUTPUT_DIR / "bandipur_grid_vegetation.csv"

TARGET_CRS = "EPSG:32643"
RESOLUTION = 10

CLASSES = {
    10: "tree",
    20: "shrubland",
    30: "grassland",
    40: "cropland",
    50: "builtup",
    60: "bare_sparse",
    80: "water",
}

grid = gpd.read_file(GRID_FILE, layer="bandipur_grid")

if grid.crs.to_string() != TARGET_CRS:
    raise ValueError("Grid CRS must be EPSG:32643")

# Reproject the original categorical raster to an exact 10 m grid.
with rasterio.open(SOURCE_RASTER) as src:
    transform, width, height = calculate_default_transform(
        src.crs,
        TARGET_CRS,
        src.width,
        src.height,
        *src.bounds,
        resolution=RESOLUTION
    )

    profile = src.profile.copy()
    profile.update(
        driver="GTiff",
        crs=TARGET_CRS,
        transform=transform,
        width=width,
        height=height,
        count=1,
        dtype="uint8",
        nodata=0,
        compress="lzw"
    )

    with rasterio.open(ALIGNED_RASTER, "w", **profile) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.transform,
            src_crs=src.crs,
            src_nodata=src.nodata,
            dst_transform=transform,
            dst_crs=TARGET_CRS,
            dst_nodata=0,
            resampling=Resampling.nearest
        )

print("Aligned raster created:", ALIGNED_RASTER)

# Calculate land-cover composition per clipped grid cell.
records = []

with rasterio.open(ALIGNED_RASTER) as src:
    print("Raster CRS:", src.crs)
    print("Raster resolution:", src.res)

    for index, cell in grid.iterrows():
        try:
            image, _ = mask(
                src,
                [cell.geometry],
                crop=True,
                all_touched=False,
                filled=True,
                nodata=0
            )

            values = image[0]
            valid = values[values != 0]
            total = len(valid)

        except ValueError:
            valid = np.array([], dtype=np.uint8)
            total = 0

        record = {
            "cell_id": cell["cell_id"],
            "valid_pixels": total
        }

        for code, name in CLASSES.items():
            count = int(np.count_nonzero(valid == code))
            record[f"{name}_pixels"] = count
            record[f"{name}_pct"] = (
                round(count / total * 100, 4)
                if total > 0 else np.nan
            )

        records.append(record)

        if (index + 1) % 100 == 0:
            print("Processed:", index + 1)

vegetation = pd.DataFrame(records)

integrated = grid.merge(
    vegetation,
    on="cell_id",
    how="left",
    validate="one_to_one"
)

if OUTPUT_GPKG.exists():
    OUTPUT_GPKG.unlink()

integrated.to_file(
    OUTPUT_GPKG,
    layer="bandipur_grid_vegetation",
    driver="GPKG",
    index=False
)

vegetation.to_csv(OUTPUT_CSV, index=False)

percentage_columns = [f"{name}_pct" for name in CLASSES.values()]
valid_cells = integrated[integrated["valid_pixels"] > 0]

print("\nCORRECTED VEGETATION INTEGRATION")
print("--------------------------------")
print("Grid cells:", len(integrated))
print("Cells with valid pixels:", len(valid_cells))
print("Cells without valid pixels:", int((integrated["valid_pixels"] == 0).sum()))
print("Total valid pixels:", int(integrated["valid_pixels"].sum()))
print("Invalid geometries:", int((~integrated.geometry.is_valid).sum()))
print(
    "Maximum percentage-sum deviation:",
    round(
        (valid_cells[percentage_columns].sum(axis=1) - 100).abs().max(),
        4
    )
)
print("\nGeoPackage:", OUTPUT_GPKG)
print("CSV:", OUTPUT_CSV)
