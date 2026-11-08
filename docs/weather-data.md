# NASA POWER Weather Data – Bandipur Wildlife Habitat Analysis

## 1. Data Source

Weather data was collected from NASA POWER (Prediction Of Worldwide Energy Resources).

- **Source:** NASA POWER Daily API
- **Study area:** Bandipur Tiger Reserve, Karnataka, India
- **Coordinate:** Latitude 11.7°N, Longitude 76.6°E
- **Temporal coverage:** 1 January 2020 – 31 December 2025
- **Temporal resolution:** Daily
- **Original file:** `data/raw/weather/POWER_Point_Daily_20200101_20251231_011d70N_076d60E_LST.csv`

## 2. Weather Parameters

The dataset contains five environmental variables:

| Parameter | Description | Unit |
|---|---|---|
| T2M | Daily mean temperature at 2 metres | °C |
| T2M_MAX | Daily maximum temperature | °C |
| T2M_MIN | Daily minimum temperature | °C |
| RH2M | Relative humidity at 2 metres | % |
| PRECTOTCORR | Corrected precipitation | mm/day |

## 3. Data Processing

The original NASA POWER file contains descriptive metadata before its actual CSV header. The processing script identifies the row beginning with `YEAR,` before loading the data.

The following processing operations were performed:

1. Loaded the original weather dataset.
2. Converted the `YEAR` and `DOY` fields into calendar dates.
3. Converted weather measurements into numeric values.
4. Treated the NASA POWER missing-value code (-999) as missing data.
5. Checked for invalid dates and duplicate records.
6. Generated cleaned daily weather records.
7. Aggregated daily records into monthly and annual summaries.
8. Calculated rainfall totals, average rainfall, and wet-day counts.

The original raw dataset was preserved.

## 4. Data Quality Validation

| Validation | Result |
|---|---:|
| Total daily records | 2,192 |
| Invalid dates | 0 |
| Duplicate dates | 0 |
| Missing weather values | 0 |
| First date | 2020-01-01 |
| Last date | 2025-12-31 |
| Monthly summary records | 72 |
| Annual summary records | 6 |

The dataset contains complete daily coverage for all six calendar years, including 366 records in the leap years 2020 and 2024.

## 5. Annual Weather Summary

| Year | Mean temperature (°C) | Mean humidity (%) | Total rainfall (mm) | Wet days |
|---|---:|---:|---:|---:|
| 2020 | 23.77 | 74.02 | 957.78 | 176 |
| 2021 | 22.99 | 78.70 | 1,392.52 | 222 |
| 2022 | 23.03 | 78.26 | 1,291.63 | 197 |
| 2023 | 23.86 | 71.73 | 886.71 | 168 |
| 2024 | 24.11 | 74.51 | 1,165.16 | 171 |
| 2025 | 23.49 | 74.79 | 896.75 | 176 |

## 6. Processed Output Files

The processed weather files are stored in:

`data/processed/weather/`

- `daily_weather.csv` – cleaned daily weather observations.
- `monthly_weather_summary.csv` – monthly aggregated weather measurements.
- `annual_weather_summary.csv` – annual aggregated weather measurements.

## 7. Relevance to Wildlife Habitat Threat Assessment

Weather information provides environmental context for understanding habitat conditions and potential environmental stress.

Potential applications include:

- Examining rainfall patterns and seasonal variation.
- Understanding temperature and humidity conditions.
- Providing contextual information when interpreting satellite fire detections.
- Supporting temporal comparisons of environmental conditions.

Weather variables should be interpreted alongside vegetation, fire, wildlife observations, roads, settlements and historical human–wildlife conflict information.

## 8. Limitations

1. Weather data represents one NASA POWER coordinate and does not provide independent measurements for every 1 km grid cell.
2. NASA POWER data is gridded or model-derived environmental information and should not be treated as direct measurements from a weather station inside every location.
3. Weather patterns alone cannot establish the cause of wildlife movement, habitat degradation or fire occurrence.
4. The six-year dataset provides historical environmental context, not a validated future weather forecast.
5. Weather variables should not be replicated across spatial grid cells and interpreted as spatially varying measurements.

## 9. Conclusion

The NASA POWER weather dataset was successfully processed and validated, producing 2,192 daily records, 72 monthly summaries and 6 annual summaries covering 2020–2025. It provides a consistent environmental context dataset for the WildGuard AI wildlife habitat threat assessment.
