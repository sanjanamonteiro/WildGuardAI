
from pathlib import Path
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "data/processed/spatial/bandipur_risk_classified.gpkg"
OUTPUT_DIR = ROOT / "data/processed/spatial/maps"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

gdf = gpd.read_file(
    INPUT,
    layer="bandipur_risk_classified"
)

# Fire threat map
fire_order = [
    "No recorded fire detection",
    "Low",
    "Moderate",
    "High",
]

fire_colors = [
    "#D9D9D9",
    "#FEE08B",
    "#F46D43",
    "#A50026",
]

gdf["fire_risk_category"] = pd.Categorical(
    gdf["fire_risk_category"],
    categories=fire_order,
    ordered=True,
)

fig, ax = plt.subplots(figsize=(12, 9))

gdf.plot(
    column="fire_risk_category",
    cmap=ListedColormap(fire_colors),
    legend=True,
    edgecolor="white",
    linewidth=0.08,
    ax=ax,
)

ax.set_title(
    "Bandipur Tiger Reserve - Recorded Fire Threat Assessment",
    fontsize=15,
    pad=15,
)
ax.set_xlabel("Easting (metres)")
ax.set_ylabel("Northing (metres)")
ax.set_aspect("equal")
ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "bandipur_fire_threat_map.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()

# Human-access pressure map
access_order = ["Low", "Moderate", "High"]

access_colors = [
    "#91CF60",
    "#FEE08B",
    "#D73027",
]

gdf["human_access_category"] = pd.Categorical(
    gdf["human_access_category"],
    categories=access_order,
    ordered=True,
)

fig, ax = plt.subplots(figsize=(12, 9))

gdf.plot(
    column="human_access_category",
    cmap=ListedColormap(access_colors),
    legend=True,
    edgecolor="white",
    linewidth=0.08,
    ax=ax,
)

ax.set_title(
    "Bandipur Tiger Reserve - Human-Access Pressure Assessment",
    fontsize=15,
    pad=15,
)
ax.set_xlabel("Easting (metres)")
ax.set_ylabel("Northing (metres)")
ax.set_aspect("equal")
ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "bandipur_human_access_pressure_map.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()

print("RISK MAP GENERATION COMPLETED")
print("=" * 50)
print("Fire map:")
print(OUTPUT_DIR / "bandipur_fire_threat_map.png")
print("\nHuman-access map:")
print(OUTPUT_DIR / "bandipur_human_access_pressure_map.png")
