# WildGuard AI – Risk Assessment Methodology

## 1. Overview

WildGuard AI uses a geospatial, indicator-based assessment to examine environmental threats and habitat conditions within Bandipur Tiger Reserve, Karnataka.

The study area is divided into 1 km grid cells to support spatial analysis and conservation prioritization.

The methodology combines historical satellite fire detections, road accessibility, settlement proximity, land-cover characteristics and wildlife observations.

The assessment is designed as a transparent, evidence-based decision-support system. It is not presented as a trained machine-learning prediction model.

## 2. Assessment Dimensions

### 2.1 Fire Threat

Fire-related indicators include:

- Historical satellite fire detection count.
- Fire detection frequency.
- Fire Radiative Power (FRP), used as an indicator of fire intensity.
- Satellite detection confidence for descriptive interpretation.

**Purpose:** Identify grid cells with recorded satellite fire activity.

**Limitation:** Satellite detections are not confirmed fire incidents. Absence of a detection does not prove absence of fire.

### 2.2 Human-Access Pressure

Human-access indicators include:

- Road length within each grid cell.
- Road density per square kilometre.
- Distance to the nearest mapped settlement.

**Purpose:** Examine potential accessibility and human-pressure patterns.

**Limitation:** Road and settlement proximity are indirect indicators. They do not establish actual human activity, poaching or wildlife conflict.

### 2.3 Habitat Condition

Habitat indicators include:

- Tree-cover percentage.
- Shrubland percentage.
- Grassland percentage.
- Cropland percentage.
- Built-up percentage.
- Bare or sparse vegetation percentage.
- Water percentage.

**Purpose:** Describe the land-cover composition of each grid cell.

**Limitation:** Land-cover categories alone do not establish habitat quality. Their ecological interpretation depends on species requirements, habitat connectivity and local conditions.

Habitat indicators are retained as a separate ecological dimension and are not automatically interpreted as positive or negative threat indicators.

## 3. Wildlife Observation Data

Wildlife observations and distinct species counts are used as ecological context.

The processed dataset contains 28,759 recorded wildlife observations and 309 distinct recorded species for the study period 2020–2025.

These observations are not automatically treated as threat indicators because the dataset contains opportunistic observations and is affected by observer effort, detection probability and spatial sampling bias.

The small number of mammal observations does not support reliable mammal-specific machine-learning modelling.

Observation counts are not population estimates or complete wildlife census results. The substantially lower number of observations in 2025 must not be interpreted as a wildlife population decline.

## 4. Weather Context

NASA POWER daily weather data for 2020–2025 provides study-area-wide environmental context.

Variables include:

- Mean temperature (T2M).
- Maximum temperature (T2M_MAX).
- Minimum temperature (T2M_MIN).
- Relative humidity (RH2M).
- Corrected precipitation (PRECTOTCORR).

The weather dataset represents one reference coordinate (latitude 11.7, longitude 76.6). It is not interpreted as independent weather measurements for individual grid cells.

Monthly and annual summaries are used to communicate broader environmental patterns.

## 5. Historical Human–Wildlife Conflict Context

Historical human–wildlife conflict records are available as administrative-circle and year-level aggregates.

They are used for broader contextual interpretation rather than assigned to individual 1 km grid cells as precise incident labels.

These aggregated records are not suitable as precise grid-level supervised training labels.

## 6. Spatial Analysis Unit

- Study area: Bandipur Tiger Reserve, Karnataka.
- Grid resolution: 1 km.
- Total clipped grid cells: 1,084.
- Coordinate reference system: EPSG:32643.
- Spatial unit: Grid cell clipped to the reserve boundary.

The grid cells are clipped to the reserve boundary. Consequently, cells along the boundary may have smaller areas than complete 1 km² cells.

The common projected coordinate reference system supports consistent spatial measurements and integration of the input datasets.

## 7. Risk Assessment Approach

The project assesses fire threat and human-access pressure separately.

Habitat characteristics, wildlife observations and weather conditions are retained as additional ecological and environmental context.

The assessment workflow includes:

1. Examine indicator distributions.
2. Identify missing values and zero values.
3. Apply appropriate transformations and normalization.
4. Establish and justify indicator weights.
5. Calculate separate assessment scores.
6. Define relative risk categories.
7. Examine sensitivity to alternative weights.
8. Visualize the results spatially.

The resulting scores represent relative spatial assessments within the study area. They are not probabilities of future events.

### 7.1 Fire Threat Score

The fire threat score combines two components:

- Historical fire detection count: 50%.
- Fire intensity represented by mean Fire Radiative Power (FRP): 50%.

The fire detection count is transformed using the natural logarithm transformation `log1p`, followed by Min-Max normalization across all grid cells.

Mean FRP is transformed using `log1p` and normalized separately among grid cells with recorded fire detections.

Grid cells without recorded fire detections receive a fire intensity component of zero.

Both components are scaled from 0 to 100 before combining them.

The combined score is calculated as:

**Fire Threat Score =**

`(0.50 × Normalized Fire Detection Count) + (0.50 × Normalized Mean FRP)`

The resulting score ranges from 0 to 100 and is used to compare relative fire threat across grid cells.

### 7.2 Human-Access Pressure Score

The human-access pressure score combines:

- Road density: 50%.
- Proximity to the nearest mapped settlement: 50%.

Road density is transformed using `log1p` and Min-Max normalized across all grid cells.

Nearest-settlement distance is Min-Max normalized and reverse-scaled so that cells closer to mapped settlements receive higher proximity scores.

Both components are scaled from 0 to 100 before combining them.

The combined score is calculated as:

**Human-Access Pressure Score =**

`(0.50 × Normalized Road Density) + (0.50 × Normalized Settlement Proximity)`

The resulting score ranges from 0 to 100 and represents relative human-access pressure based on the selected spatial indicators.
The thresholds are specific to the baseline scoring configuration. Alternative weighting scenarios are evaluated separately during sensitivity analysis.
