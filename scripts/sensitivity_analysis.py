
from pathlib import Path

import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "data/processed/spatial/bandipur_risk_classified.gpkg"
OUTPUT = ROOT / "data/processed/spatial/sensitivity_analysis_summary.csv"

gdf = gpd.read_file(
    INPUT,
    layer="bandipur_risk_classified"
)


def classify_tertiles(scores):
    lower = scores.quantile(0.33)
    upper = scores.quantile(0.67)

    categories = pd.Series("Low", index=scores.index)

    categories.loc[scores >= lower] = "Moderate"
    categories.loc[scores > upper] = "High"

    return categories


def compare_scores(name, baseline, alternative):
    baseline_categories = classify_tertiles(baseline)
    alternative_categories = classify_tertiles(alternative)

    correlation = baseline.rank().corr(alternative.rank())

    changed = (
        baseline_categories != alternative_categories
    ).sum()

    total = len(baseline)
    agreement = (total - changed) / total * 100

    print(f"\n{name}")
    print("-" * 55)
    print(f"Spearman rank correlation: {correlation:.4f}")
    print(f"Unchanged categories: {total - changed}")
    print(f"Changed categories: {changed}")
    print(f"Category agreement: {agreement:.2f}%")

    return {
        "scenario": name,
        "rank_correlation": correlation,
        "category_agreement_pct": agreement,
        "categories_changed": int(changed),
        "cells_compared": total,
    }


results = []

# Fire assessment: detected cells only
detected = gdf["fire_count"] > 0
fire = gdf.loc[detected]

frequency = fire["fire_frequency_component"]
intensity = fire["fire_intensity_component"]

fire_50_50 = 0.50 * frequency + 0.50 * intensity
fire_40_60 = 0.40 * frequency + 0.60 * intensity
fire_60_40 = 0.60 * frequency + 0.40 * intensity

print("=" * 60)
print("CORRECTED SENSITIVITY ANALYSIS")
print("=" * 60)

results.append(compare_scores(
    "Fire: 50/50 vs 40/60",
    fire_50_50,
    fire_40_60,
))

results.append(compare_scores(
    "Fire: 50/50 vs 60/40",
    fire_50_50,
    fire_60_40,
))

# Human-access assessment: all cells
road = gdf["road_density_component"]
settlement = gdf["settlement_proximity_component"]

access_50_50 = 0.50 * road + 0.50 * settlement
access_40_60 = 0.40 * road + 0.60 * settlement
access_60_40 = 0.60 * road + 0.40 * settlement

results.append(compare_scores(
    "Human access: 50/50 vs 40/60",
    access_50_50,
    access_40_60,
))

results.append(compare_scores(
    "Human access: 50/50 vs 60/40",
    access_50_50,
    access_60_40,
))

# Save results
pd.DataFrame(results).to_csv(OUTPUT, index=False)

print("\n" + "=" * 60)
print("CORRECTED SENSITIVITY ANALYSIS COMPLETED")
print("Report:", OUTPUT)
