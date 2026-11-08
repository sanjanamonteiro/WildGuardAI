
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed" / "wildlife"
CHART_DIR = DATA_DIR / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load summary files
yearly = pd.read_csv(DATA_DIR / "wildlife_yearly_summary.csv")
orders = pd.read_csv(DATA_DIR / "wildlife_top_bird_orders.csv")
families = pd.read_csv(DATA_DIR / "wildlife_top_bird_families.csv")
mammals = pd.read_csv(DATA_DIR / "wildlife_mammal_species.csv")

# Consistent chart settings
plt.rcParams["figure.figsize"] = (12, 7)
plt.rcParams["font.size"] = 10


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Created: {filename}")


# 1. Year-wise wildlife observations
plt.figure()
plt.bar(yearly["year"].astype(str), yearly["records"])
plt.title("Wildlife Observations in Bandipur (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Number of observations")
plt.grid(axis="y", alpha=0.3)
save_chart("wildlife_yearly_observations.png")


# 2. Top 15 bird orders
order_data = orders.sort_values("records", ascending=True)

plt.figure(figsize=(12, 8))
plt.barh(order_data["order"], order_data["records"])
plt.title("Top 15 Bird Orders Recorded in Bandipur")
plt.xlabel("Number of observations")
plt.ylabel("Bird order")
plt.grid(axis="x", alpha=0.3)
save_chart("wildlife_top_bird_orders.png")


# 3. Top 15 bird families
family_data = families.sort_values("records", ascending=True)

plt.figure(figsize=(12, 8))
plt.barh(family_data["family"], family_data["records"])
plt.title("Top 15 Bird Families Recorded in Bandipur")
plt.xlabel("Number of observations")
plt.ylabel("Bird family")
plt.grid(axis="x", alpha=0.3)
save_chart("wildlife_top_bird_families.png")


# 4. Mammal species observations
mammal_data = mammals.sort_values("records", ascending=True)

plt.figure(figsize=(12, 8))
plt.barh(mammal_data["scientificName"], mammal_data["records"])
plt.title("Mammal Species Observations in Bandipur")
plt.xlabel("Number of observations")
plt.ylabel("Scientific name")
plt.grid(axis="x", alpha=0.3)
save_chart("wildlife_mammal_species.png")


print("\nAll four wildlife visualizations generated successfully.")
print("Chart directory:", CHART_DIR)
