# OSIRIS Study for WildGuard AI

## 1. What is OSIRIS?

OSIRIS stands for Open Source Intelligence & Reconnaissance Integrated System.

It is an open-source global intelligence platform that combines information from multiple data sources and presents the information through an interactive intelligence dashboard.

## 2. What does OSIRIS do?

OSIRIS collects and displays information from different intelligence domains such as:

- Aviation
- Maritime
- CCTV
- Seismic activity
- Fires
- Weather
- News
- Cyber threats
- Conflict zones

## 3. Main Idea We Are Taking From OSIRIS

WildGuard AI will use a similar intelligence-dashboard concept.

Instead of monitoring many global intelligence domains, WildGuard AI will specialize in wildlife conservation.

## 4. OSIRIS → WildGuard AI

OSIRIS:

Multiple global intelligence sources
        ↓
Data processing
        ↓
Interactive intelligence map
        ↓
Situational awareness

WildGuard AI:

Wildlife + environmental + geographical + historical data
        ↓
Data processing
        ↓
AI threat prediction
        ↓
Wildlife risk map
        ↓
Conservation decision support

## 5. What We Will Reuse Conceptually

We will take inspiration from:

- Interactive map-based intelligence
- Multiple data layers
- Real-time/updated information
- Geographic visualization
- Situational awareness
- Dashboard-based decision support

## 6. What Will Be Different

WildGuard AI will be specifically designed for wildlife conservation.

It will focus on:

- Habitat threats
- Environmental/fire risk
- Human-activity-related risk
- Wildlife/habitat risk
- AI-based threat prediction
- Risk zones
- Conservation alerts

## 7. Important Project Principle

WildGuard AI will provide decision support to conservation personnel.

It will predict potential risk.

It will NOT claim that a crime or poaching event is definitely happening.

## 8. OSIRIS Architecture and WildGuard AI Integration

### Components We Will Reuse

WildGuard AI will reuse relevant OSIRIS components for:

- Interactive geographic map
- MapLibre-based map visualization
- Geographic data layers
- GeoJSON-based visualization
- Map controls and map interactions
- Visualization of points, lines, and zones

### Components We Will Develop

WildGuard AI will develop its own components for:

- Wildlife and habitat threat data
- Environmental and fire-risk data
- Human-activity-related risk data
- AI-based threat prediction
- Threat risk scoring
- Wildlife/habitat risk zones
- Conservation alerts
- Conservation-specific dashboard information
- WildGuard AI database and data pipeline

### Integration Principle

OSIRIS will provide the geospatial visualization foundation.

WildGuard AI will add the wildlife-conservation intelligence layer on top of this foundation.

The final system will be designed specifically for wildlife conservation and decision support.

## 9. Verified OSIRIS Architecture

The OSIRIS application uses a main page-level component that loads and provides data to the OsirisMap component.

The map receives:
- Data
- Active layer configuration
- Map projection and terrain settings
- Map interaction callbacks
- Other visualization-related properties

The LayerPanel controls the active map layers and passes the selected layer configuration to the map.

For WildGuard AI, this architecture will allow us to reuse the existing geospatial visualization structure while connecting it to wildlife-specific data and AI-generated threat information.

## 10. WildGuard AI Data Flow

WildGuard AI will follow the data flow:

Data Sources
→ Data Processing
→ AI Threat Prediction
→ Threat Risk Scoring
→ Risk Zone Generation
→ Conservation Alerts
→ Map and Dashboard

The system will collect and process information related to:
- Environmental conditions
- Fire risk
- Habitat conditions
- Human activity
- Wildlife-related observations

The processed information will be provided to the AI threat prediction system.

The AI system will generate a predicted threat level and risk score.

The predicted risks will be represented geographically as risk zones on the map.

Conservation alerts will be generated to support conservation personnel in identifying areas that may require attention.

## 11. WildGuard AI Core Data Categories

WildGuard AI will use the following major data categories:

1. Environmental Data
   - Temperature
   - Rainfall
   - Vegetation conditions
   - Drought indicators

2. Fire and Disaster Data
   - Active fires
   - Burned areas
   - Fire intensity
   - Nearby environmental hazards

3. Human Activity Data
   - Roads
   - Settlements
   - Human activity near protected areas
   - Infrastructure

4. Wildlife and Habitat Data
   - Wildlife observations
   - Protected areas
   - Habitat locations
   - Species information

5. Historical Threat Data
   - Previous incidents
   - Historical environmental threats
   - Historical risk levels


## 12. AI Threat Prediction

The AI component will analyse environmental, human-activity, wildlife and historical data to estimate the potential threat level of a geographical area.

The prediction output will include:
- Threat category
- Risk score
- Risk level
- Geographic location

The system will use the prediction as decision support for conservation personnel.


## 13. WildGuard AI Risk Levels

WildGuard AI will classify areas into:

- Low Risk
- Moderate Risk
- High Risk
- Critical Risk

These risk levels will be visualized geographically on the map.


## 14. WildGuard AI Final Architecture

Data Sources
→ Data Collection
→ Data Processing
→ Feature Engineering
→ AI Threat Prediction
→ Risk Scoring
→ Geographic Risk Zones
→ Conservation Alerts
→ WildGuard AI Dashboard

OSIRIS will provide the geospatial visualization foundation.

WildGuard AI will provide the wildlife-conservation intelligence, prediction and alerting functionality.

## 15. WildGuard AI Data Sources

WildGuard AI will use the following data sources:

### Environmental Data
- Temperature
- Rainfall
- Vegetation
- Drought conditions

### Fire Data
- Active fire locations
- Fire intensity
- Burned areas

### Geographic Data
- Protected areas
- Forest/habitat boundaries
- Roads
- Settlements
- Infrastructure

### Wildlife Data
- Wildlife observations
- Species information
- Wildlife locations

### Historical Data
- Previous threats
- Previous fire incidents
- Historical risk information

## 16. Initial Dataset Strategy

The project will initially use publicly available datasets and APIs.

The datasets will be cleaned, transformed and combined into a common geographic format before being provided to the AI prediction system.

The system will be designed so additional real-time data sources can be integrated later.

## 17. Selected Data Sources

WildGuard AI will initially use:

- NASA FIRMS — active fire data
- NASA Earth observation data — environmental information
- Protected-area and habitat datasets — geographic conservation information
- Wildlife/species datasets — wildlife information
- OpenStreetMap — roads, settlements and infrastructure
- Historical/project-generated data — training and testing the AI model

These sources will provide the initial data required for threat prediction and geographic visualization.

Additional real-time sources may be integrated in future versions.

## 18. AI Threat Categories

WildGuard AI will initially predict three major threat categories:

### 1. Environmental Threat
Risks caused by environmental conditions such as:
- Drought
- Extreme temperature
- Vegetation stress
- Water scarcity

### 2. Fire Threat
Risks related to:
- Active fires
- High fire intensity
- Fire-prone conditions
- Fire spread near habitats

### 3. Human Activity Threat
Risks caused by human activity near wildlife habitats, such as:
- Roads
- Settlements
- Infrastructure
- Human activity near protected areas

The AI model will combine relevant features from these categories to calculate an overall threat risk for a geographic area.

## 19. AI Model Inputs

The AI model will use features such as:
- Temperature
- Rainfall
- Vegetation condition
- Drought indicators
- Fire activity
- Distance to roads
- Distance to settlements
- Habitat/protected-area information
- Historical threat information

## 20. AI Model Outputs

The AI model will produce:
- Threat category
- Risk score
- Risk level
- Geographic location

The risk level will be classified as:
- Low
- Moderate
- High
- Critical

These outputs will be used to generate geographic risk zones and conservation alerts.

## 21. AI/ML Approach

WildGuard AI will use a supervised machine learning approach for initial threat-risk prediction.

The model will learn relationships between environmental conditions, fire activity, human activity, habitat information and historical threat data.

### Initial Model

The initial implementation will use Random Forest because it:
- Works well with structured tabular data
- Can handle multiple input features
- Can model non-linear relationships
- Provides feature importance
- Is suitable for an initial project implementation

### Prediction

The trained model will predict the threat level for a geographic area.

The prediction will be converted into a risk score and classified as:
- Low Risk
- Moderate Risk
- High Risk
- Critical Risk

The model will be evaluated using appropriate classification metrics such as:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The AI prediction will be used as decision support and will not be treated as confirmation that a threat or crime is occurring.

## 22. WildGuard AI Database

WildGuard AI will use MongoDB to store wildlife, habitat, environmental, threat and prediction data.

### Main Collections

1. wildlife
   - Species and wildlife observations

2. habitats
   - Habitat and protected-area information

3. environmental_data
   - Temperature, rainfall, vegetation and drought data

4. fire_events
   - Active fire and historical fire information

5. human_activity
   - Roads, settlements and infrastructure information

6. threat_predictions
   - AI-generated threat predictions and risk scores

7. conservation_alerts
   - Alerts generated for high-risk areas

8. historical_threats
   - Historical threat information used for analysis and model training

### Database Flow

Data Sources
→ MongoDB
→ Data Processing
→ AI Model
→ Threat Predictions
→ Risk Zones
→ Conservation Alerts
→ Map/Dashboard

## 23. WildGuard AI System Architecture

### 1. Data Layer
Collect data from:
- NASA FIRMS
- Environmental/earth observation sources
- Protected-area and habitat datasets
- Wildlife datasets
- OpenStreetMap
- Historical/project-generated data

### 2. Data Processing Layer
- Data collection
- Cleaning
- Transformation
- Geographic processing
- Feature engineering

### 3. AI Layer
- Machine learning model
- Threat prediction
- Risk scoring
- Threat classification

### 4. Backend Layer
- FastAPI
- MongoDB
- Data and prediction APIs
- Conservation alert management

### 5. Visualization Layer
- OSIRIS/MapLibre map foundation
- Wildlife and habitat layers
- Fire and environmental layers
- Human-activity layers
- AI-generated risk zones

### 6. User Interface
The dashboard will provide:
- Interactive conservation map
- Threat information
- Risk levels
- AI predictions
- Conservation alerts
- Wildlife/habitat information

### Overall Architecture

External Data Sources
        ↓
Data Processing
        ↓
MongoDB
        ↓
Feature Engineering
        ↓
AI Threat Prediction
        ↓
Risk Scoring
        ↓
FastAPI Backend
        ↓
WildGuard AI Dashboard
        ↓
OSIRIS/MapLibre Geographic Visualization
        ↓
Risk Zones + Conservation Alerts

## 24. WildGuard AI Modules

WildGuard AI will contain the following main modules:

1. Interactive Conservation Map
2. Wildlife and Habitat Monitoring
3. Environmental Risk Monitoring
4. Fire Threat Monitoring
5. Human Activity Risk Monitoring
6. AI Threat Prediction
7. Risk Zone Visualization
8. Conservation Alert System
9. Conservation Dashboard
10. Data Management and Processing

## 25. WildGuard AI Technology Stack

### Frontend
- React
- TypeScript
- MapLibre
- OSIRIS map components

### Backend
- Python
- FastAPI

### Database
- MongoDB

### AI/ML
- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest

### Data Visualization
- MapLibre
- GeoJSON
- Interactive geographic layers

### Development Tools
- Git
- GitHub
- VS Code

## 26. Frontend and Backend Structure

### Frontend

The frontend will provide:
- Interactive map
- Threat risk zones
- Wildlife and habitat information
- Environmental information
- Fire information
- Risk scores
- Conservation alerts
- Dashboard controls

The existing OSIRIS map visualization structure will be reused and adapted for WildGuard AI.

### Backend

The backend will provide:
- Data collection APIs
- Database APIs
- Data processing
- AI prediction APIs
- Risk scoring
- Conservation alert generation

FastAPI will act as the communication layer between the frontend, database and AI components.

## 27. AI/ML Development Plan

The AI development process will follow:

1. Collect datasets
2. Clean and combine the data
3. Select relevant features
4. Perform exploratory data analysis
5. Create training and testing datasets
6. Train the Random Forest model
7. Evaluate model performance
8. Improve the model if required
9. Save the trained model
10. Connect the model to the FastAPI backend
11. Generate threat predictions
12. Display predictions on the map

The model will predict the potential threat level of geographic areas using the selected environmental, fire, habitat and human-activity features.

## 28. OSIRIS to WildGuard AI Integration

The integration will follow this approach:

OSIRIS Map Foundation
        ↓
WildGuard Data Layers
        ↓
WildGuard AI Predictions
        ↓
Risk Zones
        ↓
Conservation Alerts

OSIRIS components will primarily support geographic visualization and map interaction.

WildGuard AI will add its own:
- Wildlife data
- Habitat data
- Environmental data
- Fire data
- Human activity data
- AI predictions
- Risk zones
- Conservation alerts

Existing OSIRIS functionality will not be unnecessarily removed. Components will be adapted or extended only where required for WildGuard AI.

## 29. Final WildGuard AI Development Roadmap

### Phase 1 — Foundation
- Study OSIRIS architecture
- Define WildGuard AI requirements
- Set up project structure
- Set up database

### Phase 2 — Data
- Collect datasets
- Clean data
- Store data in MongoDB
- Create data-processing pipeline

### Phase 3 — AI
- Prepare features
- Train Random Forest model
- Evaluate model
- Save trained model
- Create prediction API

### Phase 4 — Backend
- Build FastAPI endpoints
- Connect MongoDB
- Connect AI model
- Generate risk scores
- Generate conservation alerts

### Phase 5 — Map Integration
- Connect WildGuard data to the OSIRIS map
- Add wildlife layers
- Add habitat layers
- Add environmental layers
- Add fire layers
- Add human-activity layers
- Add AI risk zones

### Phase 6 — Dashboard
- Build conservation dashboard
- Display predictions
- Display risk levels
- Display alerts
- Add filtering and map controls

### Phase 7 — Testing
- Test data pipeline
- Test database
- Test APIs
- Test AI predictions
- Test map layers
- Test alerts
- Test complete system

### Phase 8 — Finalization
- Improve UI
- Optimize performance
- Document the system
- Prepare screenshots
- Prepare project report
- Prepare presentation
- Prepare project demonstration

### Final System

WildGuard AI will combine:

OSIRIS Geospatial Visualization
+
Wildlife & Environmental Data
+
Machine Learning
+
MongoDB
+
FastAPI
+
Conservation Risk Analysis
+
Real-Time/Updated Monitoring

to provide an AI-powered decision-support system for wildlife habitat threat monitoring and conservation.

