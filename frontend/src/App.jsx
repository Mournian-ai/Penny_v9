import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [text, setText] = useState('')
  const [response, setResponse] = useState(null)
  const [chat, setChat] = useState([])
  const [events, setEvents] = useState([])
  const [logs, setLogs] = useState([])

  const sendToPenny = async () => {
    const res = await axios.post('/api/speak', { text })
    setResponse(res.data.response || res.data.error)
    setText('')
  }

  useEffect(() => {
    const i = setInterval(async () => {
      const c = await axios.get('/api/chat')
      setChat(c.data.messages)
      const e = await axios.get('/api/events')
      setEvents(e.data.events)
      const l = await axios.get('/api/logs')
      setLogs(l.data.logs)
    }, 2000)
    return () => clearInterval(i)
  }, [])

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Penny Control Panel</h1>
      <div style={{ marginBottom: '1rem' }}>
        <input
          style={{ width: '300px', marginRight: '10px' }}
          value={text}
          onChange={e => setText(e.target.value)}
          placeholder='Tell Penny something'
        />
        <button onClick={sendToPenny}>Send</button>
        {response && <p>Penny said: <strong>{response}</strong></p>}
      </div>
      <div style={{ display: 'flex', gap: '1rem' }}>
        <div style={{ flex: 1 }}>
          <h2>Chat</h2>
          <div style={{ border: '1px solid #ccc', height: '200px', overflow: 'auto' }}>
            {chat.map((m, i) => <div key={i}>{m}</div>)}
          </div>
        </div>
        <div style={{ flex: 1 }}>
          <h2>Events</h2>
          <div style={{ border: '1px solid #ccc', height: '200px', overflow: 'auto' }}>
            {events.map((e, i) => <div key={i}>{e}</div>)}
          </div>
        </div>
        <div style={{ flex: 1 }}>
          <h2>Console</h2>
          <div style={{ border: '1px solid #ccc', height: '200px', overflow: 'auto' }}>
            {logs.map((l, i) => <div key={i}>{l}</div>)}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
