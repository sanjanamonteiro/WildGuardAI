import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

INPUT = (
    BASE / "data" / "raw" / "weather"
    / "POWER_Point_Daily_20200101_20251231_011d70N_076d60E_LST.csv"
)

OUTPUT = BASE / "data" / "processed" / "weather"
OUTPUT.mkdir(parents=True, exist_ok=True)

# Find the actual CSV header
with open(INPUT, "r", encoding="utf-8") as file:
    lines = file.readlines()

header_line = next(
    i for i, line in enumerate(lines)
    if line.strip().startswith("YEAR,")
)

df = pd.read_csv(INPUT, skiprows=header_line)

# Convert weather columns to numeric
weather_columns = [
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "RH2M",
    "PRECTOTCORR"
]

for column in weather_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Replace NASA missing-data indicator
df[weather_columns] = df[weather_columns].replace(-999, pd.NA)

# Create calendar dates
df["DATE"] = pd.to_datetime(
    df["YEAR"].astype(str)
    + df["DOY"].astype(str).str.zfill(3),
    format="%Y%j",
    errors="coerce"
)

# Validate input
if df["DATE"].isna().any():
    raise ValueError("Invalid dates found.")

if df["DATE"].duplicated().any():
    raise ValueError("Duplicate dates found.")

if len(df) != 2192:
    raise ValueError("Unexpected daily record count.")

if df[weather_columns].isna().any().any():
    raise ValueError("Missing weather values found.")

# Sort daily records
df = df.sort_values("DATE").reset_index(drop=True)

# Add month and year fields
df["YEAR"] = df["DATE"].dt.year
df["MONTH"] = df["DATE"].dt.month

# Daily rainfall greater than 1 mm counts as a wet day
df["WET_DAY"] = df["PRECTOTCORR"] > 1.0

# Monthly summary
monthly = (
    df.groupby(["YEAR", "MONTH"])
    .agg(
        temperature_mean=("T2M", "mean"),
        temperature_max_mean=("T2M_MAX", "mean"),
        temperature_min_mean=("T2M_MIN", "mean"),
        humidity_mean=("RH2M", "mean"),
        rainfall_total_mm=("PRECTOTCORR", "sum"),
        rainfall_daily_mean_mm=("PRECTOTCORR", "mean"),
        wet_days=("WET_DAY", "sum"),
        daily_records=("DATE", "count")
    )
    .reset_index()
)

monthly["MONTH_START"] = pd.to_datetime(
    monthly["YEAR"].astype(str)
    + "-"
    + monthly["MONTH"].astype(str).str.zfill(2)
    + "-01"
)

# Annual summary
annual = (
    df.groupby("YEAR")
    .agg(
        temperature_mean=("T2M", "mean"),
        temperature_max_mean=("T2M_MAX", "mean"),
        temperature_min_mean=("T2M_MIN", "mean"),
        humidity_mean=("RH2M", "mean"),
        rainfall_total_mm=("PRECTOTCORR", "sum"),
        rainfall_daily_mean_mm=("PRECTOTCORR", "mean"),
        wet_days=("WET_DAY", "sum"),
        daily_records=("DATE", "count")
    )
    .reset_index()
)

# Save outputs
daily_path = OUTPUT / "daily_weather.csv"
monthly_path = OUTPUT / "monthly_weather_summary.csv"
annual_path = OUTPUT / "annual_weather_summary.csv"

df.to_csv(daily_path, index=False)
monthly.to_csv(monthly_path, index=False)
annual.to_csv(annual_path, index=False)

# Display validation
print("\nWEATHER PROCESSING COMPLETE")
print("----------------------------")
print("Daily records:", len(df))
print("Monthly records:", len(monthly))
print("Annual records:", len(annual))
print("Missing weather values:", int(df[weather_columns].isna().sum().sum()))
print("Date duplicates:", int(df["DATE"].duplicated().sum()))

print("\nAnnual weather summary:")
print(annual.round(2).to_string(index=False))

print("\nOutput files:")
print(daily_path)
print(monthly_path)
print(annual_path)