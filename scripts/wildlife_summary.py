
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "processed" / "wildlife" / "bandipur_wildlife_observations.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed" / "wildlife"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load wildlife observations
df = pd.read_csv(INPUT_FILE, low_memory=False)

# Normalize year
df["year"] = pd.to_datetime(df["eventDate"], errors="coerce").dt.year

# Basic summary
summary = {
    "total_observations": len(df),
    "unique_species": df["scientificName"].nunique(),
    "bird_observations": (df["class"] == "Aves").sum(),
    "mammal_observations": (df["class"] == "Mammalia").sum(),
    "missing_species_names": df["scientificName"].isna().sum(),
    "duplicate_gbif_ids": df["gbifID"].duplicated().sum(),
    "duplicate_occurrence_ids": df["occurrenceID"].duplicated().sum(),
    "missing_coordinate_uncertainty": df["coordinateUncertaintyInMeters"].isna().sum(),
}

# Save basic summary
pd.DataFrame(
    list(summary.items()),
    columns=["metric", "value"]
).to_csv(OUTPUT_DIR / "wildlife_quality_summary.csv", index=False)

# Save observations by year
df.groupby("year").size().reset_index(name="records").to_csv(
    OUTPUT_DIR / "wildlife_yearly_summary.csv", index=False
)

# Save top bird orders
df[df["class"] == "Aves"]["order"].value_counts().head(15).rename_axis(
    "order"
).reset_index(name="records").to_csv(
    OUTPUT_DIR / "wildlife_top_bird_orders.csv", index=False
)

# Save top bird families
df[df["class"] == "Aves"]["family"].value_counts().head(15).rename_axis(
    "family"
).reset_index(name="records").to_csv(
    OUTPUT_DIR / "wildlife_top_bird_families.csv", index=False
)

# Save mammal species counts
df[df["class"] == "Mammalia"]["scientificName"].value_counts().rename_axis(
    "scientificName"
).reset_index(name="records").to_csv(
    OUTPUT_DIR / "wildlife_mammal_species.csv", index=False
)

# Save source distribution
source_columns = [
    col for col in ["year", "institutionCode", "datasetKey"]
    if col in df.columns
]

df.groupby(source_columns, dropna=False).size().reset_index(
    name="records"
).to_csv(
    OUTPUT_DIR / "wildlife_source_year_summary.csv", index=False
)

print("WILDLIFE SUMMARY GENERATED SUCCESSFULLY")
print("\nBASIC SUMMARY")

for metric, value in summary.items():
    print(f"{metric}: {value}")

print("\nOutput files saved in:", OUTPUT_DIR)
