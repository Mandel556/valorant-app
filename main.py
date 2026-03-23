from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from riot import get_match_history, parse_match_stats, get_overall_stats

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/player/{name}/{tag}")
def get_player_stats(name: str, tag: str):
    matches = get_match_history(name, tag)
    stats = parse_match_stats(matches, name, tag)
    if not stats:
        return {"error": "Player not found or no competitive matches"}
    return get_overall_stats(stats)

@app.get("/compare/{name1}/{tag1}/{name2}/{tag2}")
def compare_players(name1: str, tag1: str, name2: str, tag2: str):
    matches1 = get_match_history(name1, tag1)
    stats1 = parse_match_stats(matches1, name1, tag1)
    matches2 = get_match_history(name2, tag2)
    stats2 = parse_match_stats(matches2, name2, tag2)

    if not stats1:
        return {"error": f"Player {name1}#{tag1} not found"}
    if not stats2:
        return {"error": f"Player {name2}#{tag2} not found"}

    return {
        "player1": {"name": f"{name1}#{tag1}", **get_overall_stats(stats1)},
        "player2": {"name": f"{name2}#{tag2}", **get_overall_stats(stats2)}
    }