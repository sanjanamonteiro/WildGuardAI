
import { useEffect, useMemo, useState } from 'react'
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import './App.css'

const API_URL = 'http://127.0.0.1:8000'

function formatNumber(value) {
  return Number(value || 0).toLocaleString('en-IN')
}

function formatMonth(value) {
  if (!value) return ''
  const date = new Date(value)
  return date.toLocaleDateString('en-IN', {
    month: 'short',
    year: 'numeric',
    timeZone: 'UTC',
  })
}

function MonthlyTrendChart({ records, dataKey, title, unit, color }) {
  const values = records
    .map((record) => Number(record[dataKey]))
    .filter((value) => Number.isFinite(value))

  if (!values.length) {
    return <div className="chart-empty">No monthly data available.</div>
  }

  const min = Math.min(...values)
  const max = Math.max(...values)
  const range = max - min || 1

  const points = records
    .map((record, index) => {
      const value = Number(record[dataKey])
      if (!Number.isFinite(value)) return null

      const x = 48 + (index / Math.max(records.length - 1, 1)) * 640
      const y = 18 + ((max - value) / range) * 145

      return { x, y, value }
    })
    .filter(Boolean)

  const line = points.map((point) => `${point.x},${point.y}`).join(' ')
  const firstMonth = formatMonth(records[0]?.MONTH_START)
  const lastMonth = formatMonth(records[records.length - 1]?.MONTH_START)

  return (
    <div className="chart-card">
      <div className="chart-title-row">
        <div>
          <h3>{title}</h3>
          <span className="chart-subtitle">
            Monthly trend · {unit}
          </span>
        </div>
        <span className="chart-range">
          {min.toFixed(1)} – {max.toFixed(1)}
        </span>
      </div>

      <div className="chart-area">
        <svg
          viewBox="0 0 720 205"
          role="img"
          aria-label={`${title} monthly trend chart`}
          className="trend-chart"
        >
          {[20, 65, 110, 165].map((y) => (
            <line
              key={y}
              x1="48"
              y1={y}
              x2="688"
              y2={y}
              className="chart-grid-line"
            />
          ))}

          <polyline
            points={line}
            fill="none"
            stroke={color}
            strokeWidth="3"
            strokeLinejoin="round"
            strokeLinecap="round"
          />

          {points.map((point, index) => (
            <circle
              key={index}
              cx={point.x}
              cy={point.y}
              r="2.5"
              fill={color}
            >
              <title>{point.value.toFixed(2)}</title>
            </circle>
          ))}
        </svg>

        <div className="chart-axis-labels">
          <span>{firstMonth}</span>
          <span>{lastMonth}</span>
        </div>
      </div>
    </div>
  )
}

function AnnualWildlifeChart({ records }) {
  const maximum = Math.max(
    ...records.map((record) => record.observations),
    1
  )

  return (
    <div className="chart-card">
      <div className="chart-title-row">
        <div>
          <h3>Annual Wildlife Observations</h3>
          <span className="chart-subtitle">
            Recorded observations by year
          </span>
        </div>
      </div>

      {records.length === 0 ? (
        <div className="chart-empty">No annual data available.</div>
      ) : (
        <div className="annual-chart">
          {records.map((record) => (
            <div className="annual-bar-item" key={record.year}>
              <span className="annual-value">
                {formatNumber(record.observations)}
              </span>
              <div className="annual-bar-track">
                <div
                  className="annual-bar"
                  style={{
                    height: `${Math.max(
                      (record.observations / maximum) * 100,
                      2
                    )}%`,
                  }}
                />
              </div>
              <span className="annual-year">{record.year}</span>
            </div>
          ))}
        </div>
      )}

      <p className="chart-footnote">
        Observation counts depend on recording and reporting coverage.
        They are not wildlife population estimates.
      </p>
    </div>
  )
}

function App() {
  const [geoData, setGeoData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [mapMode, setMapMode] = useState('fire')

  const [wildlife, setWildlife] = useState(null)
  const [wildlifeError, setWildlifeError] = useState('')

  const [weather, setWeather] = useState(null)
  const [weatherError, setWeatherError] = useState('')

  useEffect(() => {
    fetch(`${API_URL}/api/risk-map`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Unable to load risk map data')
        }
        return response.json()
      })
      .then((result) => {
        setGeoData(result.data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })

    fetch(`${API_URL}/api/wildlife-summary`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Unable to load wildlife summary')
        }
        return response.json()
      })
      .then(setWildlife)
      .catch((err) => setWildlifeError(err.message))

    fetch(`${API_URL}/api/weather-summary`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Unable to load weather summary')
        }
        return response.json()
      })
      .then(setWeather)
      .catch((err) => setWeatherError(err.message))
  }, [])

  const features = geoData?.features || []

  const stats = useMemo(() => {
    const fireCounts = {
      High: 0,
      Moderate: 0,
      Low: 0,
      'No recorded fire detection': 0,
    }

    const accessCounts = {
      High: 0,
      Moderate: 0,
      Low: 0,
    }

    features.forEach((feature) => {
      const properties = feature.properties
      const fire = properties.fire_risk_category
      const access = properties.human_access_category

      if (fire in fireCounts) fireCounts[fire]++
      if (access in accessCounts) accessCounts[access]++
    })

    return {
      total: features.length,
      fireDetections: features.reduce(
        (sum, feature) =>
          sum + (Number(feature.properties.fire_count) || 0),
        0
      ),
      fireCells: features.filter(
        (feature) => feature.properties.fire_detected
      ).length,
      fireCounts,
      accessCounts,
    }
  }, [features])

  const getRiskColor = (feature) => {
    const category =
      mapMode === 'fire'
        ? feature.properties.fire_risk_category
        : feature.properties.human_access_category

    const colors = {
      High: '#dc5555',
      Moderate: '#e8a33d',
      Low: '#4c9b72',
      'No recorded fire detection': '#cbd2cc',
    }

    return colors[category] || '#cbd2cc'
  }

  const mapStyle = (feature) => ({
    fillColor: getRiskColor(feature),
    fillOpacity: 0.72,
    color: '#46574b',
    weight: 0.6,
    opacity: 0.7,
  })

  const onEachFeature = (feature, layer) => {
    const p = feature.properties

    layer.bindPopup(`
      <div>
        <strong>Grid Cell: ${p.cell_id}</strong>
        <hr />
        <b>Fire risk:</b> ${p.fire_risk_category}<br />
        <b>Fire detections:</b> ${p.fire_count}<br />
        <b>Fire threat score:</b> ${Number(p.fire_threat_score).toFixed(2)}<br />
        <hr />
        <b>Human access:</b> ${p.human_access_category}<br />
        <b>Access pressure score:</b> ${Number(p.human_access_pressure_score).toFixed(2)}<br />
        <b>Road length:</b> ${Number(p.road_length_km).toFixed(2)} km<br />
        <b>Nearest settlement:</b> ${Number(p.nearest_settlement_km).toFixed(2)} km
      </div>
    `)
  }

  const currentCounts =
    mapMode === 'fire' ? stats.fireCounts : stats.accessCounts

  const weatherRecords = weather?.monthly_records || []
  const wildlifeRecords = wildlife?.annual_observations || []
  const classDistribution = wildlife?.class_distribution || []

  if (loading) {
    return <div className="loading">Loading WildGuard AI dashboard...</div>
  }

  if (error) {
    return <div className="error">Dashboard error: {error}</div>
  }

  return (
    <div className="app">
      <header className="header">
        <div>
          <div className="brand-label">
            WILDLIFE CONSERVATION INTELLIGENCE
          </div>
          <h1>WildGuard AI</h1>
          <p>
            AI-Powered Wildlife Habitat Threat Assessment
            and Conservation Monitoring System
          </p>
        </div>

        <div className="header-location">
          <span className="status-dot"></span>
          Bandipur Tiger Reserve, Karnataka
        </div>
      </header>

      <main className="dashboard">
        <section className="section-heading">
          <div>
            <h2>Conservation Overview</h2>
            <p>Spatial risk assessment across the Bandipur study area</p>
          </div>
          <span className="data-label">2020–2025 DATA</span>
        </section>

        <section className="stats-grid">
          <div className="stat-card">
            <span className="stat-label">GRID CELLS</span>
            <strong>{stats.total.toLocaleString('en-IN')}</strong>
            <span className="stat-description">
              Spatial analysis units
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">FIRE DETECTIONS</span>
            <strong>{stats.fireDetections}</strong>
            <span className="stat-description">
              Satellite detections
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">CELLS WITH FIRE</span>
            <strong>{stats.fireCells}</strong>
            <span className="stat-description">
              Cells with detections
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">HIGH ACCESS PRESSURE</span>
            <strong>{stats.accessCounts.High}</strong>
            <span className="stat-description">
              Relative high category
            </span>
          </div>
        </section>

        <section className="map-section">
          <div className="map-heading">
            <div>
              <h2>Bandipur Spatial Risk Map</h2>
              <p>Select a risk layer and explore individual grid cells.</p>
            </div>

            <div className="map-switch">
              <button
                className={mapMode === 'fire' ? 'active' : ''}
                onClick={() => setMapMode('fire')}
              >
                Fire Threat
              </button>
              <button
                className={mapMode === 'access' ? 'active' : ''}
                onClick={() => setMapMode('access')}
              >
                Human Access
              </button>
            </div>
          </div>

          <div className="map-container">
            <MapContainer
              center={[11.77, 76.54]}
              zoom={10}
              scrollWheelZoom={true}
              className="risk-map"
            >
              <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />

              {geoData && (
                <GeoJSON
                  key={mapMode}
                  data={geoData}
                  style={mapStyle}
                  onEachFeature={onEachFeature}
                />
              )}
            </MapContainer>
          </div>

          <div className="legend">
            <strong>
              {mapMode === 'fire'
                ? 'Fire Threat'
                : 'Human Access Pressure'}
            </strong>

            {Object.entries(currentCounts).map(([category, count]) => (
              <div className="legend-item" key={category}>
                <span
                  className="legend-color"
                  style={{
                    backgroundColor:
                      category === 'No recorded fire detection'
                        ? '#cbd2cc'
                        : category === 'High'
                          ? '#dc5555'
                          : category === 'Moderate'
                            ? '#e8a33d'
                            : '#4c9b72',
                  }}
                ></span>
                <span>{category}</span>
                <strong>{count}</strong>
              </div>
            ))}
          </div>
        </section>

        <section className="analytics-section">
          <div className="section-heading">
            <div>
              <h2>Wildlife Observation Intelligence</h2>
              <p>
                Recorded wildlife observations within the study area
              </p>
            </div>
            <span className="data-label">GBIF · 2020–2025</span>
          </div>

          {wildlifeError ? (
            <div className="section-error">
              Wildlife data unavailable: {wildlifeError}
            </div>
          ) : !wildlife ? (
            <div className="section-loading">
              Loading wildlife information...
            </div>
          ) : (
            <>
              <div className="stats-grid wildlife-stats">
                <div className="stat-card">
                  <span className="stat-label">
                    TOTAL OBSERVATIONS
                  </span>
                  <strong>
                    {formatNumber(wildlife.total_observations)}
                  </strong>
                  <span className="stat-description">
                    Recorded wildlife observations
                  </span>
                </div>

                <div className="stat-card">
                  <span className="stat-label">RECORDED SPECIES</span>
                  <strong>
                    {formatNumber(wildlife.unique_species)}
                  </strong>
                  <span className="stat-description">
                    Unique species in the dataset
                  </span>
                </div>
              </div>

              <div className="analytics-grid">
                <div className="chart-card">
                  <div className="chart-title-row">
                    <div>
                      <h3>Observation Class Distribution</h3>
                      <span className="chart-subtitle">
                        Recorded observations by animal class
                      </span>
                    </div>
                  </div>

                  {classDistribution.map((item) => {
                    const percentage =
                      wildlife.total_observations > 0
                        ? (item.observations /
                            wildlife.total_observations) *
                          100
                        : 0

                    return (
                      <div className="class-row" key={item.animal_class}>
                        <div className="class-label-row">
                          <strong>{item.animal_class}</strong>
                          <span>
                            {formatNumber(item.observations)} ·{' '}
                            {percentage.toFixed(2)}%
                          </span>
                        </div>
                        <div className="class-bar-track">
                          <div
                            className="class-bar"
                            style={{ width: `${percentage}%` }}
                          />
                        </div>
                      </div>
                    )
                  })}
                </div>

                <AnnualWildlifeChart records={wildlifeRecords} />
              </div>

              <div className="data-warning">
                <strong>Wildlife data interpretation</strong>
                <p>
                  {wildlife.data_warning}
                </p>
              </div>
            </>
          )}
        </section>

        <section className="analytics-section">
          <div className="section-heading">
            <div>
              <h2>Weather Intelligence</h2>
              <p>
                Temperature, humidity and rainfall trends for the study area
              </p>
            </div>
            <span className="data-label">NASA POWER · 2020–2025</span>
          </div>

          {weatherError ? (
            <div className="section-error">
              Weather data unavailable: {weatherError}
            </div>
          ) : !weather ? (
            <div className="section-loading">
              Loading weather information...
            </div>
          ) : (
            <>
              <div className="weather-latest">
                <div className="stat-card">
                  <span className="stat-label">
                    LATEST MEAN TEMPERATURE
                  </span>
                  <strong>
                    {Number(
                      weather.latest_temperature_mean
                    ).toFixed(1)}°C
                  </strong>
                  <span className="stat-description">
                    Monthly mean temperature
                  </span>
                </div>

                <div className="stat-card">
                  <span className="stat-label">LATEST MEAN HUMIDITY</span>
                  <strong>
                    {Number(
                      weather.latest_humidity_mean
                    ).toFixed(1)}%
                  </strong>
                  <span className="stat-description">
                    Monthly mean relative humidity
                  </span>
                </div>

                <div className="stat-card">
                  <span className="stat-label">
                    LATEST MONTHLY RAINFALL
                  </span>
                  <strong>
                    {Number(
                      weather.latest_rainfall_total_mm
                    ).toFixed(1)} mm
                  </strong>
                  <span className="stat-description">
                    Total monthly rainfall
                  </span>
                </div>
              </div>

              <div className="analytics-grid weather-charts">
                <MonthlyTrendChart
                  records={weatherRecords}
                  dataKey="temperature_mean"
                  title="Mean Temperature"
                  unit="°C"
                  color="#d58a3c"
                />

                <MonthlyTrendChart
                  records={weatherRecords}
                  dataKey="rainfall_total_mm"
                  title="Monthly Rainfall"
                  unit="mm"
                  color="#478cae"
                />

                <MonthlyTrendChart
                  records={weatherRecords}
                  dataKey="humidity_mean"
                  title="Mean Relative Humidity"
                  unit="%"
                  color="#568c70"
                />
              </div>

              <div className="data-warning">
                <strong>Weather data interpretation</strong>
                <p>{weather.data_note}</p>
                <p>
                  Latest available month: {weather.latest_available_month}
                </p>
              </div>
            </>
          )}
        </section>

        <section className="note">
          <strong>Overall data interpretation</strong>
          <p>
            Risk categories are relative classifications based on
            expert-defined scoring weights. Satellite fire detections
            are not confirmed fire incidents. Human-access pressure
            uses road density and settlement proximity as indirect
            indicators, not direct evidence of human activity or conflict.
            Wildlife observations are not population estimates.
          </p>
        </section>

        <footer>
          WildGuard AI | Bandipur Tiger Reserve | Research Prototype
        </footer>
      </main>
    </div>
  )
}

export default App
