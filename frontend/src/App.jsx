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
    <div>
      <h1>WildGuard AI</h1>

      <p>
        AI-Powered Wildlife Habitat Threat Prediction
        and Real-Time Conservation Monitoring System
      </p>

      <p>Wildlife conservation risk monitoring dashboard</p>

      <hr />

      <h2>Backend Status</h2>
      <p>{backendMessage}</p>
    </div>
  )
}

export default App