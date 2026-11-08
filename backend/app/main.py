
from functools import lru_cache
from pathlib import Path
import json

import geopandas as gpd
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WildGuard AI",
    description="Wildlife Habitat Threat Assessment and Conservation Monitoring API",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:4173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RISK_DATASET = (
    PROJECT_ROOT / "data" / "processed" / "spatial"
    / "bandipur_risk_classified.gpkg"
)

WILDLIFE_DATASET = (
    PROJECT_ROOT / "data" / "processed" / "wildlife"
    / "bandipur_wildlife_observations.csv"
)

WEATHER_DATASET = (
    PROJECT_ROOT / "data" / "processed" / "weather"
    / "monthly_weather_summary.csv"
)


@app.get("/")
def home():
    return {
        "message": "WildGuard AI backend is running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "application": "WildGuard AI",
        "message": "Backend API is operational"
    }


@lru_cache(maxsize=1)
def load_risk_grid():
    if not RISK_DATASET.exists():
        raise FileNotFoundError(
            f"Risk dataset not found: {RISK_DATASET}"
        )

    grid = gpd.read_file(
        RISK_DATASET,
        layer="bandipur_risk_classified"
    )

    grid = grid.to_crs(epsg=4326)
    grid.geometry = grid.geometry.force_2d()

    return json.loads(grid.to_json())


@app.get("/api/risk-map")
def get_risk_map():
    try:
        geojson = load_risk_grid()

        return {
            "total_cells": len(geojson["features"]),
            "crs": "EPSG:4326",
            "data": geojson
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@lru_cache(maxsize=1)
def load_wildlife_summary():
    if not WILDLIFE_DATASET.exists():
        raise FileNotFoundError(
            f"Wildlife dataset not found: {WILDLIFE_DATASET}"
        )

    wildlife = pd.read_csv(
        WILDLIFE_DATASET,
        low_memory=False
    )

    class_counts = (
        wildlife["class"]
        .fillna("Unknown")
        .value_counts()
        .rename_axis("animal_class")
        .reset_index(name="observations")
    )

    annual_counts = (
        wildlife.groupby("year")
        .size()
        .reset_index(name="observations")
        .sort_values("year")
    )

    return {
        "total_observations": int(len(wildlife)),
        "unique_species": int(wildlife["species"].nunique()),
        "class_distribution": json.loads(
            class_counts.to_json(orient="records")
        ),
        "annual_observations": json.loads(
            annual_counts.to_json(orient="records")
        ),
        "data_warning": (
            "These are recorded wildlife observations, "
            "not population estimates. Observation coverage "
            "varies by year. The 2025 dataset contains only "
            "26 records and should not be interpreted as a "
            "wildlife population decline."
        )
    }


@app.get("/api/wildlife-summary")
def get_wildlife_summary():
    try:
        return load_wildlife_summary()

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@lru_cache(maxsize=1)
def load_weather_summary():
    if not WEATHER_DATASET.exists():
        raise FileNotFoundError(
            f"Weather dataset not found: {WEATHER_DATASET}"
        )

    weather = pd.read_csv(WEATHER_DATASET)

    weather = weather.sort_values(
        ["YEAR", "MONTH"]
    )

    latest = weather.iloc[-1]

    columns = [
        "YEAR",
        "MONTH",
        "temperature_mean",
        "temperature_max_mean",
        "temperature_min_mean",
        "humidity_mean",
        "rainfall_total_mm",
        "wet_days",
        "daily_records",
        "MONTH_START"
    ]

    monthly_records = weather[columns]

    return {
        "total_months": int(len(weather)),
        "latest_available_month": str(latest["MONTH_START"]),
        "latest_temperature_mean": float(
            latest["temperature_mean"]
        ),
        "latest_humidity_mean": float(
            latest["humidity_mean"]
        ),
        "latest_rainfall_total_mm": float(
            latest["rainfall_total_mm"]
        ),
        "monthly_records": json.loads(
            monthly_records.to_json(orient="records")
        ),
        "data_note": (
            "Weather data represents one NASA POWER study-area "
            "reference point, not separate measurements for "
            "individual grid cells."
        )
    }


@app.get("/api/weather-summary")
def get_weather_summary():
    try:
        return load_weather_summary()

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
