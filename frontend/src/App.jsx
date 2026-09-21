import { useEffect, useState } from 'react'

function App() {
  const [backendMessage, setBackendMessage] = useState('Connecting to backend...')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then((response) => response.json())
      .then((data) => {
        setBackendMessage(data.message)
      })
      .catch(() => {
        setBackendMessage('Backend connection failed')
      })
  }, [])

  return (
    <div className="app">
      <header className="header">
        <h1>WildGuard AI</h1>
        <p>
          AI-Powered Wildlife Habitat Threat Prediction and
          Real-Time Conservation Monitoring System
        </p>
      </header>

      <main className="dashboard">
        <div className="status-card">
          <h2>System Status</h2>
          <p>Wildlife conservation risk monitoring dashboard</p>

          <p className="status">
            Backend: {backendMessage}
          </p>
        </div>
      </main>
    </div>
  )
}

export default App