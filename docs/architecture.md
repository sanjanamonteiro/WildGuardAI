# WildGuard AI – System Architecture

## 1. Project Overview

WildGuard AI is an AI-powered wildlife habitat threat assessment and conservation monitoring system designed for the Bandipur Tiger Reserve region in Karnataka, India.

The system integrates wildlife observations, fire detections, vegetation information, road networks, settlement locations, and weather records to support spatial analysis of potential habitat threats.

The project currently uses processed datasets and rule-based risk scoring to identify areas with relatively higher fire threat and human access pressure.

## 2. System Architecture

The application consists of three main layers:

1. **Data Processing and Analysis Layer**
2. **Backend API Layer**
3. **Frontend Visualization Layer**

### 2.1 Data Processing and Analysis Layer

This layer collects, processes, and integrates environmental and geographical datasets.

The project uses the following data sources:

- GBIF wildlife occurrence records.
- NASA FIRMS satellite-based fire detections.
- NASA POWER weather data.
- ESA WorldCover land-cover data.
- OpenStreetMap road and settlement data.
- Bandipur Tiger Reserve boundary data.

Python scripts perform data cleaning, coordinate processing, spatial grid creation, dataset integration, risk scoring, classification, and visualization.

The study area is divided into approximately 1 km spatial grid cells for geographical analysis.

### 2.2 Risk Assessment

The current risk assessment focuses on two dimensions:

**Fire Threat Assessment**
- Fire detection frequency.
- Mean Fire Radiative Power (FRP).
- Normalized fire threat scoring.

**Human Access Pressure Assessment**
- Road density.
- Distance to the nearest settlement.
- Normalized human access scoring.

The component scores are combined using expert-defined weights and classified into relative Low, Moderate, and High categories.

These categories represent relative threat levels within the study area. They are not validated probabilities of future incidents.

### 2.3 Backend API Layer

The backend is developed using Python and FastAPI.

It provides API endpoints to supply processed data to the frontend.

Current endpoints include:

| Endpoint | Purpose |
|---|---|
| `/api/health` | Checks API availability |
| `/api/risk-map` | Provides spatial risk classification data |
| `/api/wildlife-summary` | Provides wildlife observation summaries |
| `/api/weather-summary` | Provides weather summary information |

The backend reads the final processed datasets from the project's `data/processed/` directory.

### 2.4 Frontend Visualization Layer

The frontend is developed using React and Vite.

It provides the dashboard interface through which users can explore the available conservation and habitat-threat information.

The interface uses:
- React components for the dashboard.
- CSS for styling and layout.
- Leaflet and React Leaflet for geographical visualization.
- Backend API requests to retrieve processed information.

The dashboard presents spatial risk information, wildlife summaries, and weather information.

## 3. Data Flow

The overall data flow is:

1. Collect environmental, wildlife, fire, and geographical datasets.
2. Clean and preprocess the collected datasets.
3. Integrate relevant datasets using spatial analysis.
4. Generate spatial grid cells across the study area.
5. Calculate fire threat and human access pressure scores.
6. Classify the resulting scores into relative risk categories.
7. Store the final processed outputs.
8. Serve the processed information through the FastAPI backend.
9. Retrieve and visualize the information through the React frontend.

## 4. Technology Stack

| Component | Technologies |
|---|---|
| Programming | Python, JavaScript |
| Data Processing | Pandas, GeoPandas |
| Geospatial Analysis | GeoPandas, Shapely, Rasterio |
| Backend | FastAPI |
| Frontend | React, Vite, CSS |
| Mapping | Leaflet, React Leaflet |
| Data Visualization | Matplotlib |
| Data Formats | CSV, GeoJSON, GeoPackage, GeoTIFF |
| Version Control | Git, GitHub |

## 5. Current Implementation Scope

The current implementation supports:

- Historical wildlife observation analysis.
- Satellite fire detection analysis.
- Land-cover and vegetation analysis.
- Road and settlement accessibility analysis.
- Weather data summaries.
- Spatial risk scoring and classification.
- Sensitivity analysis of risk scoring.
- Interactive dashboard visualization.

## 6. Limitations and Future Enhancements

The current system is based primarily on historical and preprocessed datasets. It does not yet provide continuous live satellite monitoring or validated predictions of future wildlife threats.

Potential future enhancements include:

- Automated ingestion of updated satellite and environmental data.
- Integration of additional wildlife monitoring sources.
- Machine learning models for validated predictive tasks.
- Time-based habitat threat monitoring.
- Automated alerts for newly detected environmental changes.
- Expanded conservation monitoring and reporting features.

## 7. Project Goal

The overall goal of WildGuard AI is to combine geospatial analytics, environmental datasets, and interactive visualization to support evidence-based wildlife habitat monitoring and conservation planning in the Bandipur Tiger Reserve region.