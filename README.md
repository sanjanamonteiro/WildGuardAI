# WildGuard AI ðŸ¾

### AI-Powered Wildlife Habitat Threat Assessment and Conservation Monitoring System

**Study Area:** Bandipur Tiger Reserve, Karnataka, India

WildGuard AI is a spatial analytics and conservation monitoring project designed to assess wildlife habitat threats across Bandipur Tiger Reserve. It integrates satellite-derived fire observations, weather information, wildlife occurrence records, land-cover data, roads, and settlement information to develop spatial threat indicators.

The project provides an interactive dashboard for exploring fire threat, human access pressure, wildlife observations, and weather patterns.

> **Methodological note:** The current system uses expert-defined spatial risk scoring and geospatial analysis. It does not claim to be a trained or validated machine-learning prediction model.

---

## Key Features

- **Spatial Risk Mapping:** Interactive 1 km grid-based maps of fire threat and human access pressure.
- **Fire Threat Assessment:** Analysis of satellite fire detections and Fire Radiative Power (FRP).
- **Human Access Assessment:** Road density and proximity to settlements as indirect indicators of human access.
- **Wildlife Observation Intelligence:** Species records, taxonomic groups, and annual observation summaries.
- **Weather Intelligence:** Monthly temperature, rainfall, and humidity analysis.
- **Interactive Dashboard:** Web dashboard with maps, charts, summaries, and data interpretation notes.
- **Backend API:** FastAPI endpoints serving spatial and analytical results.

## Project Objectives

1. Assess the spatial distribution of fire-related threats.
2. Examine human access pressure using roads and settlement locations.
3. Explore wildlife occurrence patterns using biodiversity records.
4. Analyse weather conditions relevant to habitat monitoring.
5. Integrate heterogeneous datasets into a unified geospatial framework.
6. Present analytical outputs through an interactive conservation dashboard.

## Study Area

**Bandipur Tiger Reserve**, located in Karnataka, India, is the geographical focus of this project.

The study area is divided into a regular 1 km spatial grid. Each grid cell is used as a common unit for integrating and comparing spatial indicators.

## Data Sources

| Dataset | Source | Purpose |
|---|---|---|
| Study area boundary | Bandipur boundary data | Define the geographical extent |
| Fire detections | NASA FIRMS VIIRS | Satellite-based fire threat indicators |
| Weather | NASA POWER | Temperature, rainfall, and humidity |
| Wildlife observations | GBIF | Species occurrence analysis |
| Roads and settlements | OpenStreetMap | Human access indicators |
| Land cover | ESA WorldCover 2021 | Land-cover context |

Data coverage and limitations vary by source. See the `docs/` directory for additional documentation.

## Methodology

### 1. Geospatial preprocessing

- Prepare the Bandipur study-area boundary.
- Establish a common projected coordinate reference system.
- Generate a 1 km grid.
- Process and align spatial datasets with the grid.

### 2. Fire threat assessment

Fire detections and mean Fire Radiative Power (FRP) are transformed using log scaling and Min-Max normalization.

The fire threat score is calculated using:

`Fire Threat Score = (0.5 Ã— Normalized Fire Count) + (0.5 Ã— Normalized Mean FRP)`

The score is scaled to 0â€“100.

### 3. Human access pressure assessment

Road density and distance to the nearest settlement are used as indirect indicators of human access.

`Human Access Score = (0.5 Ã— Normalized Road Density) + (0.5 Ã— Reverse-Normalized Settlement Distance)`

The score is scaled to 0â€“100.

### 4. Risk classification

Grid cells are classified into Low, Moderate, and High categories using relative tertile thresholds.

The weights are expert-defined, not statistically learned. The resulting scores represent relative indicators within the study area, not probabilities of an incident.

### 5. Wildlife and weather analysis

Wildlife occurrence records are summarised by species, taxonomic group, and year. Weather records are analysed using monthly and annual summaries.

## System Architecture

```text
        DATA SOURCES
             |
             v
    DATA COLLECTION
             |
             v
   DATA PREPROCESSING
             |
             v
    GEOSPATIAL GRID
       INTEGRATION
             |
             v
    SPATIAL ANALYSIS
             |
      +------+------+
      |             |
      v             v
  FIRE THREAT   HUMAN ACCESS
   SCORING        SCORING
      |             |
      +------+------+
             |
             v
    RISK CLASSIFICATION
             |
             v
       FASTAPI BACKEND
             |
             v
      REACT DASHBOARD
```

## Technology Stack

| Component | Technologies |
|---|---|
| Programming | Python, JavaScript |
| Data analysis | Pandas, NumPy |
| Geospatial analysis | GeoPandas, Shapely |
| Backend | FastAPI, Uvicorn |
| Frontend | React, Vite |
| Mapping | Leaflet, React Leaflet |
| Visualisation | Charts and interactive maps |
| Testing | Pytest, HTTPX |
| Version control | Git, GitHub |

## Repository Structure

```text
WildGuardAI/
â”‚
â”œâ”€â”€ backend/
â”‚   â”œâ”€â”€ app/
â”‚   â””â”€â”€ requirements.txt
â”‚
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ raw/
â”‚   â””â”€â”€ processed/
â”‚
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ architecture.md
â”‚   â”œâ”€â”€ historical-incidents.md
â”‚   â”œâ”€â”€ osiris-study.md
â”‚   â”œâ”€â”€ risk-assessment-methodology.md
â”‚   â”œâ”€â”€ study-area.md
â”‚   â”œâ”€â”€ weather-data.md
â”‚   â””â”€â”€ wildlife-data.md
â”‚
â”œâ”€â”€ frontend/
â”‚   â”œâ”€â”€ src/
â”‚   â””â”€â”€ package.json
â”‚
â”œâ”€â”€ models/
â”œâ”€â”€ notebooks/
â”œâ”€â”€ scripts/
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_api.py
â”‚
â”œâ”€â”€ .gitignore
â””â”€â”€ README.md
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/sanjanamonteiro/WildGuardAI.git
cd WildGuardAI
```

### 2. Set up the backend

From the project root:

```bash
python -m venv backend/venv
```

Activate the environment on Windows PowerShell:

```powershell
.\backend\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the backend:

```bash
uvicorn backend.app.main:app --reload
```

Backend base URL:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

### 3. Set up the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite in your browser.

**Note:** The dashboard requires the backend to be running and the expected processed datasets to be available in the project data directories.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Backend status |
| GET | `/api/health` | API health check |
| GET | `/api/risk-map` | Spatial risk map data |
| GET | `/api/wildlife-summary` | Wildlife observation summary |
| GET | `/api/weather-summary` | Weather summary |

## Testing

Run the backend API tests from the project root:

```powershell
.\backend\venv\Scripts\python.exe -m pytest tests\test_api.py -v
```

The current API test suite contains five endpoint tests.

## Important Data Limitations

- Satellite fire detections are thermal anomalies and are not necessarily confirmed fire incidents.
- Fire Radiative Power is not a measurement of burned area.
- Wildlife occurrence records are opportunistic observations, not estimates of animal populations.
- Wildlife record counts can vary due to reporting effort and source coverage.
- Roads and settlement proximity are indirect proxies for human access, not direct measurements of human activity or conflict.
- NASA POWER weather data represents a study-area reference point, not weather measurements for every grid cell.
- Land-cover classes alone do not establish habitat quality.
- Risk scores are relative, expert-weighted indicators and should not be interpreted as validated incident probabilities.

## Future Enhancements

- Integrate additional environmental and conservation datasets.
- Develop temporal monitoring and alerting capabilities.
- Explore machine-learning approaches when suitable labelled data becomes available.
- Improve spatial validation and field-based verification.
- Extend the dashboard with additional conservation monitoring indicators.

## Project Information

**Project:** WildGuard AI  
**Domain:** Data Science, Geospatial Analytics, Wildlife Conservation  
**Study Area:** Bandipur Tiger Reserve, Karnataka, India

**GitHub Repository:**  
https://github.com/sanjanamonteiro/WildGuardAI

---

*Developed as an academic project focused on geospatial analytics and technology-assisted wildlife conservation.*



