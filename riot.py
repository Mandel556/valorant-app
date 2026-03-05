import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

def get_player(name, tag):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    return response.json()

def get_match_history(puuid):
    url = f"https://americas.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}"
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    return response.json()

player = get_player("joker", "99888")
puuid = player["puuid"]

print(get_match_history(puuid))