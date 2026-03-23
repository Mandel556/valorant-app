import { useState } from "react"
import axios from "axios"

function App() {
  const [name1, setName1] = useState("")
  const [tag1, setTag1] = useState("")
  const [name2, setName2] = useState("")
  const [tag2, setTag2] = useState("")
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const compare = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/compare/${name1}/${tag1}/${name2}/${tag2}`
      )
      setData(response.data)
    } catch (err) {
      setError("Could not fetch player data. Check the names and try again.")
    }
    setLoading(false)
  }

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif", maxWidth: "800px", margin: "0 auto" }}>
      <h1>Valorant Player Comparison</h1>

      <div style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
        <input placeholder="Player 1 name" value={name1} onChange={e => setName1(e.target.value)} />
        <input placeholder="Tag (e.g. NA1)" value={tag1} onChange={e => setTag1(e.target.value)} />
        <input placeholder="Player 2 name" value={name2} onChange={e => setName2(e.target.value)} />
        <input placeholder="Tag (e.g. NA1)" value={tag2} onChange={e => setTag2(e.target.value)} />
        <button onClick={compare}>Compare</button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <div style={{ display: "flex", gap: "40px" }}>
          {[data.player1, data.player2].map((player, i) => (
            <div key={i} style={{ flex: 1, background: "#f5f5f5", padding: "20px", borderRadius: "8px" }}>
              <h2>{player.name}</h2>
              <p><b>Rank:</b> {player.rank}</p>
              <p><b>KDA:</b> {player.kda}</p>
              <p><b>Win Rate:</b> {player.win_rate}%</p>
              <p><b>Headshot %:</b> {player["headshot_%"]}</p>
              <p><b>Most Played:</b> {player.most_played_agent}</p>
              <p><b>Matches:</b> {player.matches_played}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App