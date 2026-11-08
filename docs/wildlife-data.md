
# Wildlife Observation Dataset – Bandipur

## 1. Overview

WildGuard AI uses wildlife occurrence observations from the Global Biodiversity Information Facility (GBIF) to provide biodiversity context for the Bandipur study area in Karnataka, India.

The dataset contains animal observations recorded between 2020 and 2025 and spatially filtered using the Bandipur study-area boundary.

These observations are used as a supporting biodiversity layer. They do not represent a complete wildlife census or actual animal population estimates.

## 2. Data Source

- Platform: Global Biodiversity Information Facility (GBIF)
- Dataset download: GBIF occurrence download
- Primary contributing dataset: eBird Observation Dataset
- Primary publisher: Cornell Lab of Ornithology
- Other contributing sources: NCF-India and iNaturalist
- Study area: Bandipur Tiger Reserve, Karnataka
- Observation period: 2020–2025

The dominant eBird dataset is primarily composed of bird observations. The dataset also contains a small number of mammal observations from other contributing sources.

## 3. Data Processing Methodology

The original GBIF download was processed using Python, Pandas and GeoPandas-compatible spatial operations.

The following filtering steps were applied:

1. Retained records belonging to Kingdom Animalia.
2. Retained records with occurrence status PRESENT.
3. Retained records with basis of record HUMAN_OBSERVATION.
4. Retained observations dated between 2020 and 2025.
5. Checked observation coordinates against the Bandipur boundary.
6. Retained records whose coordinates fall within or on the study-area boundary.
7. Exported the filtered observations into CSV and GeoJSON formats.

The spatial filtering used the exact Bandipur boundary polygon and the Shapely `covers` operation.

## 4. Processed Dataset

Output files:

- `data/processed/wildlife/bandipur_wildlife_observations.csv`
- `data/processed/wildlife/bandipur_wildlife_observations.geojson`

Dataset characteristics:

| Metric | Value |
|---|---:|
| Total filtered observations | 28,759 |
| Unique scientific species names | 311 |
| Bird observations (Aves) | 28,727 |
| Mammal observations (Mammalia) | 32 |
| Missing scientific names | 0 |
| Duplicate GBIF IDs | 0 |
| Duplicate occurrence IDs | 0 |
| Coordinate reference system | EPSG:4326 |

## 5. Taxonomic Composition

The processed dataset is dominated by bird observations.

- Aves: 28,727 observations (approximately 99.89%).
- Mammalia: 32 observations (approximately 0.11%).

Therefore, this dataset is treated primarily as a bird-observation dataset with supplementary mammal records.

### 5.1 Frequently Recorded Bird Orders

The most frequently recorded bird orders include:

| Bird order | Observations |
|---|---:|
| Passeriformes | 13,304 |
| Accipitriformes | 2,203 |
| Piciformes | 1,689 |
| Galliformes | 1,533 |
| Coraciiformes | 1,525 |
| Columbiformes | 1,477 |
| Psittaciformes | 1,408 |
| Pelecaniformes | 1,112 |

Passeriformes accounts for the largest number of observations in the dataset.

### 5.2 Frequently Recorded Bird Families

| Bird family | Observations |
|---|---:|
| Accipitridae | 2,199 |
| Sturnidae | 1,937 |
| Phasianidae | 1,533 |
| Columbidae | 1,477 |
| Psittaculidae | 1,408 |
| Muscicapidae | 1,341 |
| Dicruridae | 1,236 |
| Pycnonotidae | 1,212 |

These values represent observation frequency and must not be interpreted as population abundance.

## 6. Mammal Observations

Only 32 mammal observations were present in the filtered dataset.

Recorded mammals include:

- Chital (*Axis axis*)
- Bonnet macaque (*Macaca radiata*)
- Asian elephant (*Elephas maximus*)
- Gaur (*Bos gaurus*)
- Dhole (*Cuon alpinus*)
- Bengal tiger (*Panthera tigris tigris*)
- Indian leopard (*Panthera pardus fusca*)
- Sloth bear (*Melursus ursinus*)

The small number of mammal records is insufficient for training a reliable mammal-specific prediction model.

Some records have closely related or potentially synonymous taxonomic names. Taxonomic harmonization is required before treating all names as separate species.

## 7. Temporal Distribution and Data Source Variation

The observation counts by year are:

| Year | Observations |
|---|---:|
| 2020 | 1,626 |
| 2021 | 6,728 |
| 2022 | 4,255 |
| 2023 | 7,614 |
| 2024 | 8,510 |
| 2025 | 26 |

Most observations from 2020–2024 were contributed by eBird.

The 2025 observations came from:
- NCF-India: 18 records
- iNaturalist: 7 records
- Other unidentified source: 1 record

No eBird observations were present for 2025 in this particular download.

Consequently, the low 2025 count reflects a substantial change in source coverage. It must not be interpreted as a decline in wildlife populations.

For temporal comparisons, 2020–2024 should be treated as the primary analysis period, while 2025 should be retained as supplementary data.

## 8. Data Quality Assessment

The following checks were performed:

- Missing scientific names: 0
- Duplicate GBIF identifiers: 0
- Duplicate occurrence identifiers: 0
- Invalid output geometries: 0
- Coordinate reference system: EPSG:4326

### Coordinate Uncertainty

Coordinate uncertainty was unavailable for 28,721 of the 28,759 observations.

This represents approximately 99.87% of the dataset.

As a result, the exact positional accuracy of most wildlife observations cannot be independently established from this field.

This limitation should be considered when using observations for fine-scale spatial analysis.

## 9. Generated Visualizations

The following charts were generated using Matplotlib at 300 DPI:

1. `wildlife_yearly_observations.png`
2. `wildlife_top_bird_orders.png`
3. `wildlife_top_bird_families.png`
4. `wildlife_mammal_species.png`

Location:

`data/processed/wildlife/charts/`

## 10. Role in WildGuard AI

The wildlife observation dataset will be used as a supporting biodiversity layer in the WildGuard AI system.

Potential applications include:

- Displaying recorded biodiversity observations within the study area.
- Visualizing the spatial distribution of recorded wildlife observations.
- Identifying locations with documented wildlife observations.
- Providing biodiversity context alongside vegetation, fire and environmental information.
- Supporting conservation-oriented spatial analysis.

The dataset will not be treated as direct evidence of wildlife population density, confirmed animal absence, poaching incidents or habitat-threat labels.

## 11. Limitations

1. The dataset is heavily dominated by bird observations.
2. Mammal records are too limited for reliable mammal-specific machine learning.
3. Citizen-science observations can contain spatial and temporal sampling bias.
4. Observer activity and species detectability influence recorded observation frequency.
5. Coordinate uncertainty is missing for most records.
6. The 2025 source composition differs substantially from previous years.
7. Observation records do not establish population abundance or species absence.

## 12. Conclusion

The processed GBIF dataset provides 28,759 wildlife observations across 311 unique scientific species names within the Bandipur study area.

It provides useful biodiversity context for WildGuard AI, particularly for visualizing recorded bird observations and supporting conservation-oriented spatial analysis.

However, source variation, observation bias and coordinate uncertainty must be considered when interpreting the results. The dataset is therefore used as supporting evidence rather than as a complete representation of wildlife populations.
