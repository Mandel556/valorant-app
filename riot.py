import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

def get_match_history(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v3/matches/na/{name}/{tag}"
    response = requests.get(url, headers={"Authorization": API_KEY})
    return response.json()

def parse_match_stats(matches_data, player_name, player_tag):
    stats = []

    for match in matches_data["data"]:
        for player in match["players"]["all_players"]:
            if player["name"].lower() == player_name.lower() and player["tag"].lower() == player_tag.lower():
                team = player["team"].lower()

                if team not in ["red", "blue"]:
                    continue

                stats.append({
                    "map": match["metadata"]["map"],
                    "agent": player["character"],
                    "kills": player["stats"]["kills"],
                    "deaths": player["stats"]["deaths"],
                    "assists": player["stats"]["assists"],
                    "headshots": player["stats"]["headshots"],
                    "bodyshots": player["stats"]["bodyshots"],
                    "rank": player["currenttier_patched"],
                    "won": match["teams"][team]["has_won"]
                })

    return stats

def get_overall_stats(stats):
    total_kills = sum(m["kills"] for m in stats)
    total_deaths = sum(m["deaths"] for m in stats)
    total_assists = sum(m["assists"] for m in stats)
    total_headshots = sum(m["headshots"] for m in stats)
    total_bodyshots = sum(m["bodyshots"] for m in stats)
    total_wins = sum(1 for m in stats if m["won"])
    total_matches = len(stats)
    total_shots = total_headshots + total_bodyshots

    return {
        "matches_played": total_matches,
        "wins": total_wins,
        "losses": total_matches - total_wins,
        "win_rate": round((total_wins / total_matches) * 100, 1),
        "kills": total_kills,
        "deaths": total_deaths,
        "assists": total_assists,
        "kda": round((total_kills + total_assists) / max(total_deaths, 1), 2),
        "headshot_%": round((total_headshots / max(total_shots, 1)) * 100, 1),
        "most_played_agent": max(set(m["agent"] for m in stats), key=lambda a: sum(1 for m in stats if m["agent"] == a)),
        "rank": stats[0]["rank"]
    }

matches = get_match_history("joker", "99888")
stats = parse_match_stats(matches, "joker", "99888")
overall = get_overall_stats(stats)

print(overall)

def get_match_history(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v3/matches/na/{name}/{tag}?mode=competitive&size=10"
    response = requests.get(url, headers={"Authorization": API_KEY})
    return response.json()