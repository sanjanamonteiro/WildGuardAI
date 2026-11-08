# Study Area Requirements

## 1. Purpose

WildGuard AI will be developed and evaluated using one selected wildlife reserve or protected area as the primary study area. The selected area must provide sufficient geographical, environmental, wildlife, fire-related, and historical information to support spatial analysis, machine-learning-based threat-risk prediction, GIS visualization, and conservation decision support.

## 2. Mandatory Requirements

The selected study area should provide, or have publicly accessible sources for, the following:

1. Protected-area boundary
2. Geographic coordinates and spatial information
3. Environmental data such as temperature and rainfall
4. Satellite-based fire or thermal-anomaly observations
5. Wildlife observation data
6. Roads and other relevant geographical infrastructure
7. Sufficient data for spatial analysis and machine-learning development

## 3. Strongly Preferred Requirements

The following information is desirable when available:

1. Historical conservation incidents
2. Settlement information
3. Vegetation or habitat indicators
4. Forest-cover or land-cover information
5. Water-body information
6. Multi-year historical data
7. Data that can be associated with geographical zones and time periods

## 4. Data Requirements

Potential data attributes may include:

* Latitude
* Longitude
* Date
* Temperature
* Rainfall
* Humidity
* Vegetation indicators
* Fire or thermal-anomaly observations
* Wildlife observations
* Historical incident information
* Distance to roads
* Distance to settlements
* Distance to water bodies
* Land-cover or habitat information

The exact features will be finalized after the available datasets are inspected.

## 5. Project Scope Limitations

WildGuard AI does not require live CCTV, IoT sensors, individual animal GPS tracking, private government databases, or guaranteed real-time illegal-activity detection.

The system will use available historical and/or near-real-time data sources to estimate potential threat risk for geographical zones.

Satellite fire detections will be treated as satellite-observed thermal anomalies or active-fire detections rather than automatic confirmation of ground fires or illegal activity.

## 6. Selection Principle

The final study area will be selected based on the availability, accessibility, quality, spatial coverage, and historical coverage of relevant datasets rather than simply selecting a reserve based on popularity.

The selected study area will be documented and used consistently throughout the data-processing, machine-learning, GIS, backend, and frontend stages of WildGuard AI.
# 7. Candidate Study Areas

The following protected areas have been shortlisted as potential study areas for WildGuard AI. The shortlist is based on their relevance to wildlife conservation, availability of documented geospatial and ecological information, suitability for spatial analysis, and potential availability of environmental, fire, wildlife and geographical datasets.

| Candidate                               | State     | Protected Area Type           | Current Status |
| --------------------------------------- | --------- | ----------------------------- | -------------- |
| Bandipur Tiger Reserve                  | Karnataka | Tiger Reserve                 | Candidate      |
| Nagarhole Tiger Reserve                 | Karnataka | Tiger Reserve                 | Candidate      |
| Kaziranga National Park / Tiger Reserve | Assam     | National Park / Tiger Reserve | Candidate      |
| Ranthambore Tiger Reserve               | Rajasthan | Tiger Reserve                 | Candidate      |
| Bhadra Tiger Reserve                    | Karnataka | Tiger Reserve                 | Candidate      |

No final study area has been selected at this stage.

The candidates will be evaluated in the next step based on the actual availability, accessibility, spatial coverage, temporal coverage, quality and suitability of the datasets required for WildGuard AI.

## 8. Data Availability Investigation

The shortlisted protected areas will be investigated based on the availability and accessibility of the datasets required for WildGuard AI. The investigation will focus on geographical, environmental, fire-related, wildlife, infrastructure, vegetation, historical and temporal data.

### 8.1 Data Availability Categories

| No. | Data Category                         | Priority  | What We Need                                                                                                                  |
| --- | ------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1   | Protected-area boundary               | Mandatory | Digital boundary of the reserve in a GIS-compatible format such as Shapefile, GeoJSON, KML or KMZ                             |
| 2   | Geographic coordinates                | Mandatory | Latitude, longitude and other spatial information required for mapping and spatial analysis                                   |
| 3   | Environmental data                    | Mandatory | Temperature, rainfall, humidity, precipitation and other relevant environmental variables                                     |
| 4   | Fire / thermal anomaly data           | Mandatory | Satellite-based active-fire or thermal-anomaly observations, including location and date                                      |
| 5   | Wildlife observations                 | Mandatory | Geographically referenced wildlife observations such as species, location, date and observation/count information             |
| 6   | Roads and geographical infrastructure | Mandatory | Roads, highways, tracks and other relevant infrastructure that can be used to calculate spatial features                      |
| 7   | Settlement data                       | Preferred | Villages, settlements, built-up areas and information that can support distance or density calculations                       |
| 8   | Vegetation / habitat data             | Preferred | NDVI, forest cover, land cover, habitat type, water bodies and other habitat-related information                              |
| 9   | Historical conservation incidents     | Preferred | Historical fire, human-wildlife conflict, wildlife mortality, habitat disturbance and other documented conservation incidents |
| 10  | Multi-year temporal data              | Preferred | Data covering multiple dates, months or years to support historical analysis and machine-learning development                 |

### 8.2 Candidate Data Availability Investigation Matrix

| Data Category                     | Bandipur Tiger Reserve | Nagarhole Tiger Reserve | Kaziranga National Park / Tiger Reserve | Ranthambore Tiger Reserve | Bhadra Tiger Reserve |
| --------------------------------- | ---------------------- | ----------------------- | --------------------------------------- | ------------------------- | -------------------- |
| Protected-area boundary           | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Geographic coordinates            | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Environmental data                | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Fire / thermal anomaly data       | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Wildlife observations             | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Roads / infrastructure            | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Settlement data                   | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Vegetation / habitat data         | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Historical conservation incidents | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |
| Multi-year temporal data          | To investigate         | To investigate          | To investigate                          | To investigate            | To investigate       |

### 8.3 Data Source Strategy

WildGuard AI will not depend on a single data source. Multiple publicly available and authoritative sources may be combined to construct the study-area dataset.

Potential sources include:

* Wildlife Institute of India (WII)
* Government of India and State Forest Department sources
* NASA FIRMS for satellite-based active-fire and thermal-anomaly observations
* Public GIS and geospatial datasets
* Satellite-derived environmental and vegetation datasets
* Scientific research publications and repositories
* Other publicly accessible conservation datasets where appropriate

### 8.4 Data Verification Principle

The existence of information about a protected area does not automatically mean that a usable dataset is available.

Each candidate will therefore be evaluated at three levels:

1. Whether relevant information exists.
2. Whether the required dataset can actually be accessed or downloaded.
3. Whether the dataset contains sufficient spatial, temporal and attribute information for WildGuard AI.

The final study area will be selected only after this investigation is completed.

### 8.5 Important Data Limitations

WildGuard AI does not require live CCTV feeds, IoT sensors, individual animal GPS tracking, private government databases or guaranteed real-time illegal-activity detection.

Satellite fire observations will be treated as satellite-observed active-fire or thermal-anomaly information rather than automatic confirmation of a ground fire or illegal activity.

The exact machine-learning features will be finalized only after the available datasets are inspected and their quality, spatial coverage and temporal coverage are determined.
## 8.6 Protected-Area Boundary Investigation

The availability of digital geographical boundaries was investigated for all five shortlisted candidate study areas. The primary boundary source identified is the National Tiger Conservation Authority (NTCA) Decision Support System, which provides a downloadable KML containing Protected Areas, Tiger Reserves and corridors. This provides a GIS-compatible source that can be used for mapping and spatial analysis after verification and conversion if required.

ISRO's Bhuvan–MoEF geoportal provides additional geospatial layers for National Parks, Sanctuaries, Protected Areas and Project Tiger areas and can be used as a secondary source for boundary verification.

| Candidate                 | Boundary Evidence                                                                       | GIS-Compatible Source                                       | Status    |
| ------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------- |
| Bandipur Tiger Reserve    | Official tiger-reserve documentation and GIS boundary mapping are available             | NTCA KML; ISRO Bhuvan Protected Area / Project Tiger layers | Available |
| Nagarhole Tiger Reserve   | Official tiger-reserve documentation and geographical extent are available              | NTCA KML; ISRO Bhuvan Protected Area / Project Tiger layers | Available |
| Kaziranga Tiger Reserve   | Official tiger-reserve documentation describes the protected-area extent and boundaries | NTCA KML; ISRO Bhuvan Protected Area / Project Tiger layers | Available |
| Ranthambore Tiger Reserve | Official tiger-reserve documentation and notified reserve information are available     | NTCA KML; ISRO Bhuvan Protected Area / Project Tiger layers | Available |
| Bhadra Tiger Reserve      | Official tiger-reserve documentation and GIS/geographical information are available     | NTCA KML; ISRO Bhuvan Protected Area / Project Tiger layers | Available |

### Boundary Source Verification

The NTCA Decision Support System provides a KML file containing Protected Areas, Tiger Reserves and corridors. The KML can be downloaded and visualized using Google Earth or another GIS-compatible application. NTCA states that the KML should be treated with appropriate caution because its accuracy, completeness and currency are not warranted.

The ISRO Bhuvan–MoEF geoportal provides additional protected-area and Project Tiger geospatial layers that can be used to cross-check the reserve boundary.

Historical Wildlife Institute of India GIS documentation also demonstrates the use of GIS-derived reserve boundaries. For example, WII's Bandipur GIS material identifies the boundary source as the Forest Survey of India (FSI), Dehradun.

### Step 3A Conclusion

All five shortlisted candidates have an identified source from which a GIS-compatible protected-area boundary can be obtained or verified.

Therefore, protected-area boundary availability does not currently eliminate any of the five candidates.

The final study-area selection will depend on the availability and quality of the remaining required datasets, including environmental, fire/thermal anomaly, wildlife, infrastructure, vegetation and historical incident data.

### Boundary Data Handling Plan

Once the final study area is selected, the boundary will be obtained from an appropriate authoritative source and stored in the WildGuard AI project as a GIS-compatible file.

The boundary will then be:

1. Verified against the official protected-area name and location.
2. Checked for coordinate reference system information.
3. Loaded using GeoPandas.
4. Converted to a suitable format such as GeoJSON if required.
5. Visualized on the WildGuard AI GIS map.
6. Used to restrict or define the spatial analysis area.

The project will retain the source information and attribution for the selected boundary dataset.
## 8.7 Environmental Data Investigation

Environmental data availability was investigated for the five shortlisted protected areas. The investigation focused on temperature, precipitation/rainfall, humidity-related variables and other environmental variables that can be used as machine-learning features.

WildGuard AI can use gridded environmental datasets rather than depending exclusively on weather stations located inside the protected area. Geographic coordinates from the protected-area boundary can be used to extract the environmental grid cells covering the study area.

### Environmental Data Sources

| Source                                | Main Variables                                                                                         | Spatial Coverage                       | Temporal Coverage | Potential Use                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------- | ----------------- | -------------------------------------------- |
| Copernicus ERA5-Land                  | Temperature, precipitation, soil water, pressure, radiation and other land variables                   | Global                                 | 1950–present      | Primary environmental dataset                |
| Copernicus ERA5                       | Temperature, humidity-related variables, precipitation, pressure, wind and other atmospheric variables | Global                                 | 1940–present      | Additional environmental variables           |
| India Meteorological Department (IMD) | Daily rainfall                                                                                         | India                                  | 1901–2024         | India-specific rainfall validation / feature |
| Other satellite-derived datasets      | Environmental and land-surface indicators                                                              | Global / regional depending on dataset | Varies            | Additional features if required              |

ERA5-Land provides global gridded land-surface data from 1950 to the present, with approximately 9 km native spatial resolution and hourly temporal resolution. Available variables include 2-metre temperature, total precipitation, soil water and other land-surface variables.

ERA5 provides additional atmospheric variables and extends from 1940 to the present.

The India Meteorological Department provides a 0.25° × 0.25° daily gridded rainfall dataset covering India for 1901–2024.

### 8.7.1 Candidate Environmental Data Availability

| Environmental Requirement      | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ------------------------------ | --------- | --------- | --------- | ----------- | --------- |
| Temperature                    | Available | Available | Available | Available   | Available |
| Rainfall / precipitation       | Available | Available | Available | Available   | Available |
| Humidity-related variables     | Available | Available | Available | Available   | Available |
| Soil moisture / soil water     | Available | Available | Available | Available   | Available |
| Solar radiation                | Available | Available | Available | Available   | Available |
| Wind / atmospheric variables   | Available | Available | Available | Available   | Available |
| Multi-year historical coverage | Available | Available | Available | Available   | Available |
| Spatial coverage of reserve    | Available | Available | Available | Available   | Available |

### 8.7.2 Environmental Data Strategy

The environmental data will not necessarily be downloaded as one complete dataset for the entire country.

After the final study area is selected, the reserve boundary will be used to determine the relevant geographical extent. Environmental grid cells covering the study area will then be extracted.

The data can subsequently be aggregated into appropriate temporal units such as:

* daily
* weekly
* monthly
* seasonal

The final temporal resolution will be selected after examining the other datasets and determining the most appropriate common time period for machine-learning analysis.

### 8.7.3 Potential Environmental Features

Potential features for WildGuard AI include:

* mean temperature
* minimum temperature
* maximum temperature
* rainfall / precipitation
* cumulative rainfall
* humidity-related variables
* soil moisture
* solar radiation
* wind speed
* seasonal indicators
* rainfall anomaly
* temperature anomaly

Not all listed variables will necessarily be included in the final model. Feature selection will be performed after the actual datasets are downloaded and inspected.

### 8.7.4 Environmental Data Limitations

ERA5 and ERA5-Land are reanalysis products and therefore represent model-based estimates constrained by observations rather than direct measurements at every location.

The spatial resolution of gridded environmental data is also coarser than the scale of individual roads, villages or specific wildlife locations.

Therefore, environmental variables will be treated as spatially referenced environmental indicators rather than exact measurements at every point inside the reserve.

### Step 3B Conclusion

All five shortlisted protected areas have sufficient geographical coverage from publicly accessible gridded environmental datasets.

Environmental-data availability therefore does not currently eliminate any candidate from the shortlist.

The final environmental dataset will be selected after the study area is finalized and the required variables, temporal resolution and spatial resolution are determined.
## 8.8 Fire / Thermal Anomaly Data Investigation

NASA's Fire Information for Resource Management System (FIRMS) was investigated as the primary source for satellite-derived active-fire and thermal-anomaly observations.

FIRMS distributes global active-fire data from NASA satellite instruments including MODIS and VIIRS. The data can be viewed spatially and downloaded in formats including Shapefile, CSV/TXT, KML and JSON. Historical active-fire data are also available through the FIRMS archive.

### 8.8.1 FIRMS Data Coverage

| Dataset              | Approximate Temporal Coverage | Spatial Resolution  | Potential Use                                      |
| -------------------- | ----------------------------- | ------------------- | -------------------------------------------------- |
| MODIS Collection 6.1 | 2000–present                  | Approximately 1 km  | Long-term historical fire/thermal-anomaly features |
| VIIRS S-NPP          | 2012–present                  | Approximately 375 m | Higher-resolution active-fire features             |
| VIIRS NOAA-20        | 2018–present                  | Approximately 375 m | Higher-resolution active-fire features             |
| VIIRS NOAA-21        | 2024–present                  | Approximately 375 m | Recent active-fire features                        |

### 8.8.2 Candidate Fire Data Availability

| Fire / Thermal Requirement      | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ------------------------------- | --------- | --------- | --------- | ----------- | --------- |
| Satellite active-fire data      | Available | Available | Available | Available   | Available |
| MODIS historical coverage       | Available | Available | Available | Available   | Available |
| VIIRS coverage                  | Available | Available | Available | Available   | Available |
| Historical fire observations    | Available | Available | Available | Available   | Available |
| Geographic coordinates          | Available | Available | Available | Available   | Available |
| Detection date/time             | Available | Available | Available | Available   | Available |
| Detection confidence attributes | Available | Available | Available | Available   | Available |
| GIS-compatible formats          | Available | Available | Available | Available   | Available |

### 8.8.3 Potential FIRMS Features

After the final study area is selected, FIRMS observations can be spatially joined with the protected-area boundary and divided into geographical analysis zones.

Potential features include:

* number of active-fire detections
* number of detections per zone
* fire detections within a specified distance of a zone
* monthly fire-detection count
* seasonal fire-detection count
* recent fire-detection count
* historical fire frequency
* detection confidence
* distance from detected thermal anomalies to roads or settlements
* fire-density indicators

The final features will be determined after inspecting the actual FIRMS dataset.

### 8.8.4 Important Interpretation Limitation

FIRMS observations represent satellite-derived active fires or thermal anomalies. A detected point does not automatically prove that the entire surrounding area is burning or that an illegal activity has occurred.

Thermal anomalies may be associated with fire, hot smoke, agricultural activity or other heat sources. Cloud cover and satellite observation conditions can also affect detection.

Therefore, WildGuard AI will use FIRMS observations as one environmental/fire-risk indicator rather than treating them as confirmed incidents.

### 8.8.5 Historical Data Strategy

For historical machine-learning analysis, archived FIRMS data will be preferred over near-real-time data where appropriate.

The final historical period will be selected after investigating the availability of wildlife observations, incidents and other datasets so that the datasets can be aligned to a common temporal period.

### Step 3C Conclusion

NASA FIRMS provides sufficient spatial and historical coverage for all five shortlisted protected areas.

Fire and thermal-anomaly data availability therefore does not currently eliminate any candidate.

FIRMS will be considered a major potential data source for WildGuard AI's environmental and fire-related risk features.
## 8.9 Wildlife Observation Data Investigation

Wildlife observation data were investigated as a major requirement for WildGuard AI. The investigation considered camera-trap records, wildlife sightings, species occurrence records, survey observations and other geographically referenced wildlife information.

The Wildlife Institute of India (WII), including its Tiger Cell, conducts and manages large-scale wildlife monitoring using camera traps, line transects, habitat assessments, occupancy modelling, GIS and spatial analysis. WII documentation confirms long-term wildlife monitoring and research in several of the shortlisted tiger reserves.

### 8.9.1 Potential Wildlife Data Sources

| Source                                         | Type of Information                                                                        | Potential Use                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Wildlife Institute of India (WII)              | Camera-trap surveys, wildlife monitoring, species presence, population and habitat studies | Primary authoritative source / research evidence     |
| NTCA / Tiger Cell                              | Tiger presence, distribution, prey and habitat monitoring                                  | Tiger-related conservation information               |
| India Biodiversity Portal                      | Species observations and biodiversity records                                              | Supplementary occurrence data                        |
| GBIF                                           | Public biodiversity occurrence datasets from contributing institutions                     | Supplementary geographically referenced observations |
| Scientific research publications / WII reports | Wildlife sightings, camera-trap surveys, species distributions and spatial studies         | Historical/contextual information                    |

### 8.9.2 Candidate Wildlife Data Availability

| Wildlife Data Requirement                         | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ------------------------------------------------- | --------- | --------- | --------- | ----------- | --------- |
| Wildlife monitoring documented                    | Available | Available | Available | Available   | Available |
| Camera-trap / field survey evidence               | Available | Available | Available | Available   | Available |
| Wildlife species information                      | Available | Available | Available | Available   | Available |
| Spatial wildlife research                         | Available | Available | Available | Available   | Available |
| Public occurrence dataset identified              | To verify | To verify | To verify | To verify   | To verify |
| Exact observation coordinates publicly accessible | To verify | To verify | To verify | To verify   | To verify |
| Multi-year wildlife information                   | Available | Available | Available | Available   | Available |

### 8.9.3 Important Wildlife Data Accessibility Issue

The existence of wildlife monitoring data does not necessarily mean that the underlying observations can be downloaded with exact coordinates.

Wildlife locations, particularly locations of endangered species such as tigers, may be spatially generalized or protected for conservation and security reasons. Public biodiversity databases may therefore contain observations with reduced spatial precision.

Consequently, WildGuard AI will not assume that exact camera-trap coordinates or individual-animal locations are publicly available.

The project will use only legally accessible and appropriately licensed wildlife observations.

### 8.9.4 Wildlife Features Potentially Used by WildGuard AI

Depending on the dataset ultimately obtained, potential wildlife-related features may include:

* wildlife observation count
* species count
* species presence/absence
* prey-species observation count
* predator observation count
* wildlife observation density
* observation frequency by zone
* seasonal wildlife activity
* historical wildlife presence
* distance from observation zones to roads
* distance from observation zones to settlements
* changes in observation frequency over time

The final features will depend on the spatial precision, temporal coverage and attributes of the actual dataset obtained.

### 8.9.5 Wildlife Data Strategy

WildGuard AI will not attempt to identify or track individual animals.

Where sensitive wildlife coordinates are unavailable, spatially aggregated observations or zone-level observations may be used instead.

Wildlife observations will therefore be converted into geographical features appropriate for the selected study area and available data resolution.

### Step 3D Conclusion

All five shortlisted protected areas have documented wildlife monitoring and research activities.

However, public accessibility of exact geographically referenced wildlife observations must be investigated separately for each candidate.

Therefore, wildlife-data accessibility remains an important selection criterion and may influence the final choice of study area.

The candidate comparison will not treat documented research data as equivalent to a directly downloadable dataset.

The final study area will be selected only after the accessibility, spatial precision, temporal coverage and licensing of the wildlife observations are verified.
## 8.10 Roads and Settlement Data Investigation

Road and settlement data were investigated because geographical accessibility and human presence are important potential factors in wildlife habitat threat analysis.

Roads can be used to calculate features such as distance to roads, road density and proximity to major infrastructure. Settlement data can similarly be used to estimate the relationship between geographical zones and human habitation.

### 8.10.1 Potential Road and Settlement Data Sources

| Source                           | Data Available                                                    | Potential Use                               |
| -------------------------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| ISRO Bhuvan                      | Infrastructure (Road & Rail)                                      | Road and infrastructure mapping             |
| ISRO Bhuvan                      | Settlement Locations                                              | Settlement proximity and density            |
| OpenStreetMap                    | Roads, tracks, settlements, buildings and other mapped features   | Detailed geographical features              |
| Geofabrik OpenStreetMap extracts | Downloadable OSM regional datasets                                | Local GIS processing and feature extraction |
| Government / State GIS sources   | Roads and administrative/geographical information where available | Validation and supplementary data           |

### 8.10.2 Candidate Road and Settlement Data Availability

| Requirement                         | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ----------------------------------- | --------- | --------- | --------- | ----------- | --------- |
| Road data                           | Available | Available | Available | Available   | Available |
| Major road / highway information    | Available | Available | Available | Available   | Available |
| Tracks / smaller roads where mapped | Available | Available | Available | Available   | Available |
| Settlement locations                | Available | Available | Available | Available   | Available |
| Village / habitation information    | Available | Available | Available | Available   | Available |
| GIS-compatible geographical data    | Available | Available | Available | Available   | Available |
| Potential for distance calculations | Available | Available | Available | Available   | Available |

### 8.10.3 Potential Road Features

After the final study area is selected, the following features may be derived:

* distance to nearest road
* distance to major road
* road density
* road length within a geographical zone
* road proximity category
* distance to highways
* density of roads around a zone

### 8.10.4 Potential Settlement Features

Potential settlement-related features include:

* distance to nearest settlement
* number of settlements within a specified radius
* settlement density
* distance to village
* built-up-area proximity
* human habitation proximity category

The exact radius and spatial aggregation method will be determined after the final study area and analysis-zone design are established.

### 8.10.5 Data Combination Strategy

Road and settlement datasets will be spatially joined with the selected protected-area boundary.

The project will use GIS operations to calculate spatial relationships between geographical analysis zones and human infrastructure.

For example:

Protected-area boundary
→ divide into analysis zones
→ load road layer
→ calculate distance to roads
→ load settlement layer
→ calculate distance to settlements
→ generate ML features.

### 8.10.6 Data Limitations

OpenStreetMap coverage is dependent on mapping activity and may vary between locations. Missing roads or settlements therefore cannot automatically be interpreted as evidence that the feature does not exist.

Bhuvan datasets may also have specific scale, accuracy and usage limitations. The selected dataset will therefore be inspected and documented before being used in the final model.

Where practical, multiple sources can be cross-checked.

### Step 3E Conclusion

Road and settlement data can be obtained or accessed for all five shortlisted protected areas through publicly available geospatial sources.

Road and settlement data therefore do not currently eliminate any candidate.

These datasets are considered important potential inputs for WildGuard AI because they allow human-accessibility and human-presence indicators to be derived from geographical information.
## 8.11 Vegetation / Habitat Data Investigation

Vegetation and habitat data were investigated because changes in vegetation condition, land cover and habitat composition can provide important environmental indicators for WildGuard AI.

Potential vegetation-related variables include NDVI, vegetation fraction, forest/vegetation cover, land-cover class, water bodies and other habitat indicators.

### 8.11.1 Potential Vegetation and Habitat Data Sources

| Source                                 | Data                                  | Resolution / Coverage                | Potential Use                            |
| -------------------------------------- | ------------------------------------- | ------------------------------------ | ---------------------------------------- |
| ISRO Bhuvan                            | OCM2 NDVI                             | 1 km, India, fortnightly, 2011–2021  | Historical vegetation-condition feature  |
| ISRO Bhuvan                            | OCM2 vegetation fraction              | 1 km, India, fortnightly, 2011–2021  | Vegetation-density feature               |
| ISRO Bhuvan                            | Land Use / Land Cover                 | Multiple Indian mapping years        | Land-cover and habitat classification    |
| ESA WorldCover                         | Global land-cover map                 | 10 m, 2020 and 2021                  | High-resolution land-cover feature       |
| Copernicus / Sentinel-derived products | Vegetation and land-cover information | Regional/global depending on product | Additional or updated habitat indicators |

### 8.11.2 Candidate Vegetation / Habitat Data Availability

| Requirement                              | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ---------------------------------------- | --------- | --------- | --------- | ----------- | --------- |
| NDVI                                     | Available | Available | Available | Available   | Available |
| Vegetation fraction                      | Available | Available | Available | Available   | Available |
| Land-use / land-cover data               | Available | Available | Available | Available   | Available |
| Forest / vegetation information          | Available | Available | Available | Available   | Available |
| Water-body information                   | Available | Available | Available | Available   | Available |
| High-resolution land-cover data          | Available | Available | Available | Available   | Available |
| Historical vegetation information        | Available | Available | Available | Available   | Available |
| Potential multi-year vegetation analysis | Available | Available | Available | Available   | Available |

### 8.11.3 Potential Vegetation Features

After the final study area is selected, potential vegetation-related machine-learning features may include:

* mean NDVI
* minimum NDVI
* maximum NDVI
* NDVI anomaly
* seasonal NDVI
* vegetation fraction
* forest-cover proportion
* land-cover class
* percentage of vegetation within a zone
* percentage of water bodies
* habitat/land-cover diversity
* vegetation change over time

The final list will be determined after the actual datasets are inspected.

### 8.11.4 Land-Cover and Habitat Classification

High-resolution land-cover information can be used to identify different geographical classes within the study area.

Potential classes may include:

* tree / forest cover
* shrubland
* grassland
* cropland
* wetlands
* water bodies
* built-up areas
* bare land

The actual classes available will depend on the selected land-cover dataset.

Land-cover information can be converted into zone-level features for the WildGuard AI model.

### 8.11.5 Vegetation Time-Series Strategy

Vegetation information may be aggregated temporally to match the other datasets.

For example:

Satellite vegetation observations
→ calculate NDVI statistics
→ aggregate by geographical zone
→ aggregate by month or season
→ combine with environmental and fire features
→ create machine-learning input features.

The temporal period will be selected only after the wildlife and incident datasets are investigated so that the datasets can be aligned.

### 8.11.6 Important Data Limitations

Different vegetation datasets have different spatial resolutions and processing methods.

For example, a 1 km NDVI product should not be interpreted as providing 1 km-level measurements of every individual tree.

Similarly, land-cover classifications represent mapped classes and may contain classification errors.

ESA WorldCover 2020 and 2021 were produced using different algorithm versions. Therefore, differences between those two products should not automatically be interpreted as actual land-cover change.

The final analysis will document the selected dataset, resolution, year and processing method.

### Step 3F Conclusion

Publicly accessible vegetation and habitat datasets are available for all five shortlisted protected areas.

The combination of ISRO Bhuvan, satellite-derived vegetation products and high-resolution land-cover datasets provides sufficient information to construct potential vegetation and habitat features.

Vegetation and habitat data availability therefore does not currently eliminate any candidate.

The final vegetation dataset will be selected after the study area and common analysis period are finalized.
## 8.12 Historical Conservation Incident Data Investigation

Historical conservation incident data were investigated because historical incidents can provide important information for identifying geographical areas that have experienced previous conservation-related threats.

The investigation considered human-wildlife conflict, wildlife mortality, road kills, crop and livestock damage, habitat disturbance, fire-related incidents and other documented conservation events.

### 8.12.1 Potential Historical Incident Sources

| Source                            | Type of Information                                                              | Potential Use                         |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------- |
| Wildlife Institute of India (WII) | Conservation reports, conflict studies, wildlife mortality and spatial research  | Primary authoritative source          |
| Project Elephant / MoEFCC         | Human-elephant conflict trends, mortality, human casualties and spatial hotspots | Conflict-related features             |
| NTCA / Tiger Cell                 | Tiger-related monitoring and conservation information                            | Tiger and habitat-related information |
| State Forest Departments          | Management plans, conflict records and incident information                      | Local validation / supplementary data |
| WII Digital Repository            | Research reports, technical reports and historical studies                       | Historical incident information       |
| Scientific publications           | Documented incidents, hotspots and spatial analyses                              | Supplementary historical evidence     |

### 8.12.2 Candidate Historical Incident Data Availability

| Requirement                                       | Bandipur  | Nagarhole | Kaziranga | Ranthambore | Bhadra    |
| ------------------------------------------------- | --------- | --------- | --------- | ----------- | --------- |
| Historical conservation information               | Available | Available | Available | Available   | Available |
| Human-wildlife conflict information               | Available | Available | Available | Available   | Available |
| Wildlife mortality information                    | Available | Available | Available | Available   | Available |
| Wildlife road-kill information                    | Available | Available | Available | Available   | Available |
| Habitat / human-pressure information              | Available | Available | Available | Available   | Available |
| Spatial incident studies                          | Available | Available | Available | Available   | Available |
| Multi-year historical information                 | Available | Available | Available | Available   | Available |
| Directly downloadable structured incident dataset | To verify | To verify | To verify | To verify   | To verify |

### 8.12.3 Examples of Documented Historical Information

WII documentation for Bandipur describes substantial human-wildlife conflict around the reserve and identifies surrounding villages, roads and changing land-use patterns as important pressures.

For Karnataka, WII and Project Elephant have published a 2026 report covering human-elephant conflict from 2000–2025, including elephant mortality, human casualties, spatial hotspots, seasonal patterns and major causes of conflict.

For Ranthambore, WII research and technical documentation provide evidence of human-wildlife conflict studies and spatial investigation. A WII technical report for Ranthambore also identifies human-wildlife conflict data as a required dataset containing information such as incident coordinates, village, wildlife and human death/injury, road kills, livestock losses and crop/property damage.

For Kaziranga, WII research has investigated wildlife mortality and road-related disturbance associated with National Highway 715 and the Kaziranga–Karbi Anglong landscape.

These examples demonstrate that historical conservation information exists for the shortlisted areas, but the availability of the underlying structured records must be verified before they are used directly for machine learning.

### 8.12.4 Potential Incident Features

If sufficiently structured data are obtained, potential features include:

* number of historical incidents
* incidents per geographical zone
* human-wildlife conflict frequency
* wildlife mortality count
* wildlife road-kill count
* crop-damage incidents
* livestock-loss incidents
* human casualty incidents
* seasonal incident frequency
* recent incident count
* historical incident density
* distance from incidents to roads
* distance from incidents to settlements
* distance from incidents to water bodies
* change in incident frequency over time

### 8.12.5 Spatial and Temporal Requirements

For direct use in the machine-learning model, an incident record should ideally contain:

* incident date or year
* incident type
* geographical coordinates or sufficiently precise location
* affected species or category
* relevant severity information
* source or reference

Records without spatial information may still be useful for background analysis but may not be suitable for zone-level spatial modelling.

Similarly, incidents without reliable dates may not be suitable for temporal prediction.

### 8.12.6 Important Data Limitation

Historical conservation information published in reports is not equivalent to a directly downloadable machine-learning dataset.

News reports and narrative documents may confirm that incidents occurred but may not contain sufficiently precise coordinates, dates or standardized attributes.

WildGuard AI will therefore distinguish between:

1. documented historical incidents,
2. structured incident records,
3. geographically referenced incident records, and
4. directly downloadable datasets.

Only appropriately structured and legally accessible records will be used as direct machine-learning inputs.

### Step 3G Conclusion

Historical conservation information is documented for all five shortlisted protected areas.

However, the accessibility and structure of the underlying incident records vary.

Therefore, historical incident data remain an important candidate-selection criterion.

The final study area should preferably have accessible historical records containing sufficient spatial and temporal information to support zone-level analysis and construction of a defensible machine-learning target.

No claim will be made that historical incident data are fully open or directly downloadable until the actual source files are verified.
## 8.13 Multi-Year Temporal Coverage Investigation

The temporal coverage of the major datasets was investigated to determine whether the data can be aligned into a common historical period for WildGuard AI.

The investigation distinguishes between the maximum historical period of an individual dataset and the common period that can actually be used for integrated machine-learning analysis.

### 8.13.1 Major Dataset Temporal Coverage

| Dataset                  | Approximate Available Period | Temporal Characteristics                                     |
| ------------------------ | ---------------------------- | ------------------------------------------------------------ |
| ERA5-Land                | 1950–present                 | Hourly and monthly options                                   |
| NASA FIRMS MODIS         | November 2000–present        | Satellite active-fire observations                           |
| NASA FIRMS VIIRS S-NPP   | January 2012–present         | Higher-resolution active-fire observations                   |
| NASA FIRMS VIIRS NOAA-20 | April 2018–present           | Higher-resolution active-fire observations                   |
| NASA FIRMS VIIRS NOAA-21 | January 2024–present         | Higher-resolution active-fire observations                   |
| ISRO Bhuvan OCM2 NDVI    | January 2011–December 2021   | Fortnightly, 1 km                                            |
| ESA WorldCover           | 2020 and 2021                | 10 m land-cover maps                                         |
| Wildlife observations    | Candidate-dependent          | Must be verified for accessible spatial and temporal records |
| Historical incidents     | Candidate-dependent          | Must be verified for structured dates and locations          |

### 8.13.2 Temporal Coverage Requirement

WildGuard AI requires sufficient temporal overlap between the datasets used for machine-learning development.

The final modelling period should therefore be determined after the wildlife and historical incident datasets are verified.

A dataset with a long historical record cannot by itself establish that the complete WildGuard AI dataset has equivalent historical coverage.

For example, environmental data may be available for several decades while geographically referenced wildlife observations may cover only a smaller period.

### 8.13.3 Potential Common Modelling Period

Based on the currently identified data sources, a common modelling period beginning around **2012 or later** is potentially practical because:

* NASA FIRMS VIIRS S-NPP begins in January 2012.
* ERA5-Land provides continuous hi
## 8.14 Final Candidate Data Availability Matrix

The findings from Steps 3A–3H were consolidated into a final candidate data-availability matrix.

The matrix distinguishes between datasets that are broadly accessible from public geospatial or environmental sources and datasets for which the underlying records require additional verification.

### 8.14.1 Overall Data Availability

| Data Category                          | Bandipur        | Nagarhole       | Kaziranga       | Ranthambore     | Bhadra          |
| -------------------------------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| Protected-area boundary                | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Environmental data                     | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Fire / thermal anomaly data            | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Wildlife monitoring evidence           | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Public wildlife occurrence records     | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       |
| Road data                              | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Settlement data                        | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Vegetation / habitat data              | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Historical conservation information    | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Structured historical incident records | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       | 🟡 Verify       |
| Multi-year environmental coverage      | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       | 🟢 Strong       |
| Common ML modelling period             | 🟡 To determine | 🟡 To determine | 🟡 To determine | 🟡 To determine | 🟡 To determine |

### 8.14.2 Interpretation of Status

**🟢 Strong**
A suitable public or authoritative source has been identified and the dataset category is broadly accessible for the candidate's geographical area.

**🟡 Verify**
Relevant information or research exists, but the exact dataset required by WildGuard AI must still be checked for spatial precision, temporal coverage, downloadable format, licensing and accessibility.

**🔴 Insufficient**
The available evidence would not currently provide enough information for the intended WildGuard AI analysis.

No candidate is currently classified as insufficient.

### 8.14.3 Important Candidate Differences

Although environmental, fire, boundary, road, settlement and vegetation datasets are broadly available for all five candidates, the availability of geographically useful historical conservation information differs in strength.

Bandipur and Nagarhole have particularly strong documented human-wildlife-conflict evidence. Long-term monitoring around these landscapes has generated large numbers of reported conflict incidents, including geographically referenced information collected through conservation programs and research.

WII research published in 2026 reports more than 20,000 verified farmer-reported human-elephant-conflict incidents from 2015–2023 around Bandipur and Nagarahole.

The Wild Seve program also documented more than 13,000 human-wildlife-conflict cases around the two protected areas and collected incident information through a structured reporting and compensation-support system.

These records demonstrate strong historical conservation-monitoring activity. However, the underlying raw dataset is not automatically assumed to be publicly downloadable. Accessibility and licensing must still be verified before using such records directly in WildGuard AI.

### 8.14.4 Data Selection Principle

The final study area will not be selected solely because it has the largest amount of publicly available information.

The selected area should provide a practical combination of:

1. Reliable protected-area boundary.
2. Environmental time-series data.
3. Satellite fire/thermal-anomaly data.
4. Wildlife observation information.
5. Roads and settlement data.
6. Vegetation/habitat information.
7. Historical conservation information.
8. Sufficient spatial precision.
9. Sufficient temporal overlap.
10. Data that can legally and practically be used in the academic project.

### 8.14.5 Current Candidate Assessment

| Candidate                 | Overall Data Situation | Main Strength                                                          | Main Remaining Verification                                |
| ------------------------- | ---------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------- |
| Bandipur Tiger Reserve    | Strong                 | Extensive wildlife and human-wildlife-conflict research and monitoring | Obtain/verify usable wildlife and incident records         |
| Nagarhole Tiger Reserve   | Strong                 | Extensive wildlife and human-wildlife-conflict research and monitoring | Obtain/verify usable wildlife and incident records         |
| Kaziranga Tiger Reserve   | Strong                 | Extensive ecological and wildlife research                             | Obtain/verify usable spatial wildlife and incident records |
| Ranthambore Tiger Reserve | Strong                 | Extensive tiger, conflict and conservation research                    | Obtain/verify usable structured wildlife/incident records  |
| Bhadra Tiger Reserve      | Strong                 | Wildlife monitoring and Western Ghats conflict research                | Obtain/verify usable wildlife and incident records         |

### Step 3I Conclusion

All five candidates satisfy the broad data requirements identified at the beginning of the study-area investigation.

No candidate can be eliminated solely because environmental, fire, boundary, road, settlement or vegetation data are unavailable.

The main differentiating factor is the accessibility and spatial/temporal usefulness of wildlife observations and historical conservation incidents.

The final selection will therefore be based on evidence collected during the complete investigation rather than on geographic preference alone.

Step 3J will document the evidence supporting the candidate comparison before the final study area is selected.
## 8.15 Evidence Summary

The investigation shows that all five shortlisted protected areas have sufficient publicly documented information to remain candidates for the WildGuard AI study area.

### Bandipur Tiger Reserve

Bandipur has extensive documented wildlife monitoring, human-wildlife conflict research, environmental studies, road and settlement information, and protected-area GIS information. Long-term monitoring and conflict studies provide evidence that spatial and temporal conservation data exist for the region.

**Current assessment:** Strong candidate.

**Main remaining verification:** Determine whether suitable wildlife observation records and structured historical incident records can be obtained in a usable format for machine-learning and spatial analysis.

### Nagarhole Tiger Reserve

Nagarhole has extensive ecological and wildlife monitoring studies, human-wildlife conflict documentation, environmental information, GIS-based research, and geographical infrastructure data. Research has documented spatial patterns of wildlife occurrence and human-wildlife conflict around the reserve.

**Current assessment:** Strong candidate.

**Main remaining verification:** Determine the accessibility, spatial precision and temporal coverage of usable wildlife observation and historical incident datasets.

### Kaziranga National Park / Tiger Reserve

Kaziranga has extensive wildlife, habitat, fire, environmental and conservation research. GIS-based studies and protected-area information provide sufficient evidence that the area can support spatial conservation analysis.

**Current assessment:** Strong candidate.

**Main remaining verification:** Verify whether wildlife observations and historical conservation incidents are available with sufficient spatial and temporal detail for ML modelling.

### Ranthambore Tiger Reserve

Ranthambore has extensive research related to tiger ecology, human-wildlife conflict, wildlife mortality, habitat and geographical factors. Published research has also documented conflict information and spatial locations around the reserve.

**Current assessment:** Strong candidate.

**Main remaining verification:** Verify access to structured incident records and suitable wildlife occurrence data that can be converted into model features.

### Bhadra Tiger Reserve

Bhadra has documented wildlife monitoring, human-wildlife conflict research, habitat studies, environmental information and GIS-based conservation research. Its location within the Western Ghats also provides opportunities for analysing environmental and habitat-related factors.

**Current assessment:** Strong candidate.

**Main remaining verification:** Verify the availability of sufficiently detailed wildlife observations and historical incident records.

### Overall Evidence Assessment

The investigation does not currently eliminate any candidate based on the major data categories required by WildGuard AI.

The strongest common data categories are:

* Protected-area boundaries
* Environmental variables
* Fire and thermal-anomaly observations
* Roads and geographical infrastructure
* Settlement information
* Vegetation and habitat indicators
* Multi-year environmental observations
* Published wildlife and conservation research

The main uncertainty across all candidates is the availability of **directly usable, structured and spatially precise wildlife observation and historical incident datasets**.

Therefore, the final study area will not be selected only because a protected area has extensive published research. The final selection will be based on the candidate for which the required datasets can actually be obtained, processed and combined into a reliable spatial machine-learning dataset.

**Decision rule:** Select the study area only after verifying the practical accessibility and usability of the required datasets.
## 8.16 Wildlife and Incident Dataset Verification

The availability of wildlife observations and historical conservation incidents is the most important remaining factor in selecting the final WildGuard AI study area.

### Wildlife Observation Data

Potential sources include:

* India Biodiversity Portal
* GBIF occurrence records
* Wildlife Institute of India research datasets and publications
* Published ecological and wildlife-monitoring studies

The India Biodiversity Portal provides publicly accessible biodiversity observations and spatial map information. Its observation system supports filtering and downloading observation data. GBIF also provides occurrence records through its occurrence database and downloadable formats.

However, wildlife observations must be filtered carefully before use because publicly available records may vary in:

* Geographic precision
* Observation date
* Species identification
* Number of individuals
* Observation source
* Spatial coverage
* Temporal coverage

Sensitive wildlife locations may also be generalized or unavailable at exact coordinates.

### Historical Conservation and Human-Wildlife Conflict Data

The strongest identified source is the Wild Seve program around Bandipur and Nagarahole.

The Wild Seve program operated for 48 months and recorded 13,808 human-wildlife conflict claims in 19 forest ranges around Bandipur and Nagarahole. The records included crop loss, property damage, livestock predation, human injuries and human fatalities.

This demonstrates that substantial structured conflict information exists for the Bandipur-Nagarahole landscape.

However, the published research does not establish that the complete raw incident-level dataset is publicly downloadable. Therefore, the existence of the dataset must not be treated as equivalent to unrestricted raw-data access.

### Dataset Verification Requirements

Before selecting the final study area, the following must be verified:

| Requirement                                       | Required |
| ------------------------------------------------- | -------- |
| Wildlife observation records                      | Yes      |
| Observation date                                  | Yes      |
| Species information                               | Yes      |
| Geographic coordinates or usable spatial location | Yes      |
| Historical incident records                       | Yes      |
| Incident date                                     | Yes      |
| Incident type/category                            | Yes      |
| Geographic location                               | Yes      |
| Sufficient records for modelling                  | Yes      |
| Public/legal access to the data                   | Yes      |
| Suitable temporal coverage                        | Yes      |

### Selection Principle

The final study area will be selected based on the practical availability of datasets rather than simply the amount of published research.

A candidate will be considered suitable if its data can be:

1. Obtained legally from an accessible source.
2. Stored in a machine-readable format.
3. Connected to geographic locations.
4. Combined with environmental and geographical features.
5. Used to construct a meaningful machine-learning dataset.

The final study-area decision will therefore be made only after the actual availability of the required wildlife and incident records has been checked.
## 8.17 Public Wildlife Dataset Verification

A publicly accessible wildlife-occurrence source has been identified through the Global Biodiversity Information Facility (GBIF).

The India Biodiversity Portal has a registered occurrence dataset hosted through GBIF. The dataset provides a downloadable Darwin Core Archive and can therefore be considered a potential machine-readable source for wildlife observations.

GBIF also provides an occurrence-download system that allows records to be filtered and downloaded for further analysis.

### Potential Use in WildGuard AI

Wildlife occurrence records may provide features such as:

* Species observed
* Observation date
* Geographic coordinates
* Number of observations
* Species diversity
* Seasonal wildlife occurrence
* Spatial wildlife density
* Historical presence of selected species

These records can potentially be spatially joined with the selected protected-area boundary and environmental/geographical datasets.

### Important Data-Quality Checks

Before using GBIF/India Biodiversity Portal records for modelling, the following must be checked:

| Check                                        | Required |
| -------------------------------------------- | -------- |
| Records located inside/around the study area | Yes      |
| Geographic coordinates available             | Yes      |
| Observation dates available                  | Yes      |
| Species information available                | Yes      |
| Sufficient number of records                 | Yes      |
| Duplicate records identified                 | Yes      |
| Records with unusable coordinates removed    | Yes      |
| Sensitive/generalized records identified     | Yes      |
| Appropriate time period                      | Yes      |

### Current Status

**Potential wildlife dataset source identified:** Yes.

**Dataset usable for WildGuard AI:** Not confirmed yet.

The dataset must be downloaded or queried and inspected before it can be accepted as the project's wildlife-observation dataset.

### Historical Incident Data

Bandipur and Nagarahole have an additional advantage because the Wild Seve program documented a large number of human-wildlife conflict incidents.

The published Wild Seve study recorded 13,808 registered conflict cases between July 2015 and June 2019. The incidents included crop loss, property damage, livestock predation, human injuries and human fatalities. The study also states that incident locations and spatio-temporal information were recorded.

However, the complete raw Wild Seve incident database is not currently treated as an automatically downloadable public dataset. Therefore, it will not be assumed to be directly available until access is verified.

### Decision

The existence of a published dataset or research program is not sufficient by itself.

A dataset will be accepted for WildGuard AI only after confirming:

1. Actual access.
2. Machine-readable format.
3. Spatial information.
4. Temporal information.
5. Sufficient number of records.
6. Appropriate licensing or permitted research use.

This verification will be performed before the final study area is selected.
## 8.18 Actual Wildlife Data Verification

The wildlife-data investigation identified multiple potential machine-readable sources that can be considered for WildGuard AI.

### Source 1 — India Biodiversity Portal Publication-Grade Dataset

The India Biodiversity Portal has a publication-grade occurrence dataset registered with GBIF.

The dataset:

* Is published by the India Biodiversity Portal.
* Is available through GBIF.
* Provides occurrence records.
* Is distributed as a Darwin Core Archive.
* Has a CC BY 4.0 licence.

This makes it a potentially usable public wildlife-observation source.

However, the dataset must still be filtered geographically to determine how many relevant records occur inside or around each candidate protected area.

### Source 2 — Nature Conservation Foundation Mammal Dataset

A GBIF dataset published by the Nature Conservation Foundation contains mammal occurrence records collected through line-transect surveys in the Western Ghats.

The dataset contains 335 occurrence records from 34 localities across the Western Ghats and includes Karnataka locations.

This dataset may provide supplementary wildlife observations for Karnataka candidates such as Bandipur, Nagarhole and Bhadra.

However, its actual spatial overlap with each candidate protected area must be checked before accepting it as a project dataset.

### Source 3 — Wild Seve

Wild Seve provides strong evidence of detailed human-wildlife conflict information around Bandipur and Nagarahole.

The program recorded 13,808 human-wildlife conflict cases between July 2015 and June 2019.

The records included:

* Incident location
* Date/time information
* Animal responsible
* Type of loss
* Quantity of loss
* Spatial information
* Photographs
* Crop-damage information

However, the complete Wild Seve dataset is not publicly downloadable because it contains sensitive information relating to endangered wildlife and affected villages and households.

Therefore, Wild Seve will be treated as a potential research/reference source rather than an automatically available raw dataset.

### Current Wildlife Data Status

| Source                           | Machine-readable          | Spatial information | Publicly accessible | WildGuard use                         |
| -------------------------------- | ------------------------- | ------------------- | ------------------- | ------------------------------------- |
| India Biodiversity Portal / GBIF | Yes                       | To verify           | Yes                 | Potential primary source              |
| NCF Western Ghats mammal dataset | Yes                       | Yes                 | Yes                 | Potential supplementary source        |
| Wild Seve                        | Yes, internally collected | Yes                 | No                  | Reference / possible requested access |

### Important Conclusion

WildGuard AI does not require the complete Wild Seve dataset to proceed.

If a suitable public wildlife-occurrence dataset can provide sufficient observations for the selected study area, it can be combined with:

* Environmental data
* Fire/thermal anomalies
* Vegetation indicators
* Roads
* Settlements
* Protected-area boundaries
* Other publicly accessible conservation information

Historical incident information can then be incorporated using publicly available structured records if available, or through a carefully documented alternative target-variable construction.

### Next Verification

The next step is to determine which candidate protected area has a sufficient number of usable public wildlife records.

The candidates will therefore be checked for:

1. Number of occurrence records.
2. Geographic coverage.
3. Date coverage.
4. Species diversity.
5. Coordinate availability.
6. Relevance to the protected-area boundary.
7. Compatibility with the other WildGuard AI datasets.

No final study area will be selected until this verification is completed.
## 8.19 Wildlife Data Candidate Comparison

The investigation of publicly accessible wildlife occurrence datasets shows that wildlife data availability differs between the shortlisted protected areas.

| Candidate   | Public wildlife-data evidence                                                                                                         | Spatial relevance | Current status                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------ |
| Bandipur    | GBIF/India Biodiversity Portal and Western Ghats datasets may provide records                                                         | To verify         | 🟡 Verify                      |
| Nagarhole   | GBIF/India Biodiversity Portal and Western Ghats datasets may provide records                                                         | To verify         | 🟡 Verify                      |
| Kaziranga   | GBIF dataset explicitly includes Kaziranga National Park and surrounding areas                                                        | Strong evidence   | 🟢 Available source identified |
| Ranthambore | Public biodiversity occurrence sources may provide records                                                                            | To verify         | 🟡 Verify                      |
| Bhadra      | GBIF dataset contains sampling sites within Muthodi forests of Bhadra Tiger Reserve; additional Western Ghats datasets include Bhadra | Strong evidence   | 🟢 Available source identified |

### Bhadra Evidence

A GBIF-registered dataset published by the Nature Conservation Foundation contains tree occurrence records from two sites within the Muthodi forests of Bhadra Tiger Reserve.

The dataset contains geographic coordinates and records collected during January–May 2006. It is available under a CC BY 4.0 licence.

Additional GBIF datasets from Western Ghats surveys also identify Bhadra as one of their survey localities.

This provides direct evidence that machine-readable biodiversity records exist for Bhadra.

However, tree occurrence records alone are not sufficient for WildGuard AI. Mammal, bird or other wildlife observations would be more useful for the wildlife-threat component.

### Kaziranga Evidence

A GBIF-registered occurrence dataset explicitly covers Kaziranga National Park and surrounding areas of Assam.

The dataset contains observations of birds, mammals, insects, amphibians and reptiles and is available under a CC BY 4.0 licence.

This provides direct evidence that publicly accessible biodiversity observations exist for the Kaziranga landscape.

The exact number of usable records inside the protected-area boundary must still be determined.

### Bandipur and Nagarhole

Bandipur and Nagarhole have extensive published wildlife-monitoring and human-wildlife-conflict research.

However, the current investigation has not yet confirmed a single public GBIF dataset containing a sufficiently large number of directly usable wildlife records specifically inside either reserve.

Therefore, they remain candidates but require further geographic filtering and dataset verification.

### Ranthambore

Ranthambore has extensive wildlife and conservation research.

However, a directly usable public occurrence dataset specifically covering the reserve has not yet been confirmed during this stage.

Additional GBIF and biodiversity-source filtering is required before its wildlife-data availability can be classified as strong.

### Important Interpretation

The current evidence does **not** mean that Bhadra or Kaziranga should automatically become the final study area.

The wildlife dataset must satisfy the complete WildGuard AI requirements:

1. Sufficient number of observations.
2. Useful geographic coordinates.
3. Observation dates.
4. Relevant species information.
5. Appropriate temporal coverage.
6. Spatial coverage across the study area.
7. Compatibility with environmental, fire, road, settlement and vegetation datasets.

### Current Status

No final study area has been selected.

The next verification will focus on the **actual number and geographic distribution of records** available for each candidate.

This is necessary because a dataset can mention a protected area while still containing too few observations inside the actual boundary for reliable spatial machine-learning analysis.
## 8.20 Geographic Wildlife Record Verification

The next stage of study-area selection requires checking whether publicly available wildlife observations actually fall within the boundaries of the shortlisted protected areas.

A dataset mentioning a protected area is not sufficient. The records must be spatially filtered against the official protected-area boundary.

### Verification Method

For each candidate protected area:

1. Obtain the official protected-area boundary.
2. Obtain the relevant GBIF wildlife occurrence records.
3. Check whether geographic coordinates are available.
4. Convert the occurrence records into spatial point data.
5. Ensure that the occurrence coordinates and protected-area boundary use compatible coordinate reference systems.
6. Perform a point-in-polygon spatial join.
7. Count the observations located inside the protected-area boundary.
8. Examine the geographic distribution of the observations.
9. Check the observation dates.
10. Check the species represented by the records.

### Required Output

For every candidate, the following information should eventually be recorded:

| Candidate   | Records inside boundary | Species represented | Date range   | Coordinate quality | Status     |
| ----------- | ----------------------: | ------------------: | ------------ | ------------------ | ---------- |
| Bandipur    |            To calculate |        To calculate | To calculate | To verify          | 🟡 Pending |
| Nagarhole   |            To calculate |        To calculate | To calculate | To verify          | 🟡 Pending |
| Kaziranga   |            To calculate |        To calculate | To calculate | To verify          | 🟡 Pending |
| Ranthambore |            To calculate |        To calculate | To calculate | To verify          | 🟡 Pending |
| Bhadra      |            To calculate |        To calculate | To calculate | To verify          | 🟡 Pending |

### Why Geographic Filtering Is Necessary

A GBIF dataset may contain observations from an entire state, ecological region or collection of survey locations.

Therefore:

**Dataset exists ≠ sufficient observations inside the reserve.**

The actual number of observations inside the protected-area boundary is what matters for WildGuard AI.

### Wildlife Data Requirements for WildGuard AI

The selected reserve should ideally have:

* Multiple wildlife observations.
* More than one species.
* Geographic coordinates.
* Observation dates.
* Spatial coverage across multiple parts of the reserve.
* Sufficient records for aggregation into geographic zones.
* Records that can be legally reused for academic research.

### Important Modelling Consideration

Wildlife observations will not necessarily be used as the prediction target.

They may instead be converted into spatial features such as:

* Wildlife observation count
* Species richness
* Species-specific observation count
* Wildlife observation density
* Seasonal observation frequency
* Distance from wildlife observation locations to roads
* Distance from wildlife observation locations to settlements

The final target variable will be defined separately after the historical incident and threat-label data have been verified.

### Current Status

The geographic coverage of wildlife observations has **not yet been confirmed for any candidate**.

Therefore, no candidate will be selected solely because a relevant GBIF dataset exists.

The final study area will be selected only after combining:

1. Wildlife-data coverage.
2. Historical incident-data availability.
3. Environmental-data availability.
4. Fire-data availability.
5. Geographic-data availability.
6. Temporal compatibility.
7. Suitability for spatial machine-learning analysis.
## 8.21 GBIF Occurrence Verification Plan

GBIF will be used as one of the potential public sources for wildlife occurrence data.

The GBIF Occurrence API supports searching occurrence records using geographic, taxonomic, temporal and other filters. Occurrence records can contain geographic coordinates and observation dates, which are required for the spatial analysis planned for WildGuard AI.

### Verification Procedure

For each shortlisted protected area:

1. Search GBIF occurrence records relevant to the candidate.
2. Identify records with geographic coordinates.
3. Identify records with observation dates.
4. Identify the taxonomic groups represented.
5. Determine whether the records occur inside or sufficiently close to the protected-area boundary.
6. Estimate the number of potentially usable records.
7. Check whether the temporal coverage is useful for the project.
8. Record the source dataset and licence information.

### Candidate Verification

| Candidate   | GBIF wildlife source | Geographic records | Temporal records | Current status |
| ----------- | -------------------- | ------------------ | ---------------- | -------------- |
| Bandipur    | To verify            | To verify          | To verify        | 🟡 Pending     |
| Nagarhole   | To verify            | To verify          | To verify        | 🟡 Pending     |
| Kaziranga   | Identified           | To verify          | To verify        | 🟡 Pending     |
| Ranthambore | To verify            | To verify          | To verify        | 🟡 Pending     |
| Bhadra      | Identified           | To verify          | To verify        | 🟡 Pending     |

### Acceptance Criteria

A wildlife dataset will be considered useful for WildGuard AI when it provides:

* A meaningful number of records.
* Geographic coordinates or sufficiently precise locations.
* Observation dates.
* Relevant species information.
* Spatial coverage useful for zone-based analysis.
* A time period that can be aligned with the other project datasets.
* A licence or access condition compatible with academic project use.

### Important Limitation

The number of GBIF records returned by a search does not automatically represent the number of records suitable for machine learning.

Records may contain:

* Duplicate observations.
* Records outside the protected-area boundary.
* Generalized coordinates.
* Missing dates.
* Taxonomic uncertainty.
* Poor spatial coverage.
* Observations from only a small number of locations.

Therefore, raw occurrence counts will be treated as an initial screening measure rather than final evidence of dataset quality.

### Current Decision

Final Study Area Selected: Bandipur Tiger Reserve, Karnataka

# 9. Final Study Area Selection

## 9.1 Selected Study Area

**Bandipur Tiger Reserve, Karnataka, India**

Bandipur Tiger Reserve has been selected as the final study area for WildGuard AI.

The selection is based on the availability of documented information relevant to the project's required data categories, including wildlife monitoring, human-wildlife conflict, environmental conditions, fire-related threats, vegetation, roads, settlements and protected-area GIS information.

## 9.2 Why Bandipur Was Selected

Bandipur provides a suitable combination of:

* Protected-area GIS information
* Wildlife monitoring information
* Human-wildlife conflict information
* Environmental data availability
* Satellite-based fire/thermal-anomaly data
* Vegetation and habitat information
* Road and settlement information
* Multi-year data sources
* Existing conservation research

The Bandipur landscape also provides documented examples of environmental and human-related conservation threats, making it suitable for developing and demonstrating the WildGuard AI threat-risk workflow.

## 9.3 Official Protected-Area Information

Bandipur is a tiger reserve in Karnataka.

According to the National Tiger Conservation Authority, the Bandipur Tiger Reserve has:

* Core area: 872.24 km²
* Buffer area: 584.06 km²
* Total tiger-reserve area: 1,456.30 km²

The official boundary data will be obtained from the National Tiger Conservation Authority's protected-area/tiger-reserve GIS resources.

## 9.4 WildGuard AI Study Scope

The project will analyse Bandipur Tiger Reserve using geographical zones rather than individual animals.

The system will combine available:

* Environmental observations
* Fire/thermal-anomaly observations
* Wildlife observations
* Historical conservation information
* Vegetation/habitat indicators
* Roads
* Settlements
* Other relevant geographical features

These features will be processed to estimate potential threat probability for geographical zones.

The resulting risk will be represented using:

**Threat Probability → Risk Score → Risk Level**

The risk levels will be:

* Low
* Medium
* High

The exact thresholds will be determined during the modelling stage based on the available target data and model results.

## 9.5 Important Data Limitation

The Wild Seve program provides strong evidence of historical human-wildlife-conflict monitoring around Bandipur and Nagarahole.

However, the complete Wild Seve incident-level dataset is not treated as a publicly downloadable dataset because it contains sensitive spatial and wildlife information.

Therefore, WildGuard AI will not claim to use the complete Wild Seve database unless appropriate access is obtained.

Instead, publicly accessible and legally reusable datasets will be used wherever possible.

## 9.6 Project Boundary

The final project study area is:

**Bandipur Tiger Reserve, Karnataka, India**

The project will not attempt to model all Indian protected areas.

It will focus on developing and demonstrating the WildGuard AI methodology within this selected reserve.

## 9.7 Study-Area Selection Status

**FINAL STUDY AREA SELECTED**

Bandipur Tiger Reserve has been selected as the study area for the remaining development of WildGuard AI.

Future data collection, preprocessing, feature engineering, machine-learning modelling and GIS development will use Bandipur as the primary geographical reference area.

