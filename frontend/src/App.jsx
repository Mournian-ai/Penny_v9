import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [text, setText] = useState("")
  const [response, setResponse] = useState(null)

  const sendToPenny = async () => {
  const res = await axios.post("/api/speak", { text })
  setResponse(res.data.response || res.data.error)
  setText("")
}

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Penny V9 Control Panel</h1>
      <input
        style={{ width: "300px", marginRight: "10px" }}
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Tell Penny something"
      />
      <button onClick={sendToPenny}>Send</button>
      {response && <p>Penny got: <strong>{response}</strong></p>}
    </div>
  )
}

export default App
