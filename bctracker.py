import json
from os import remove
import time
import pprint

import requests

from utils import read_api_key, read_config

BASE_URI = "https://ballchasing.com/api"
PLAYLIST = "private"
USEFUL_KEYS = [
    "id", "date", "duration", "map_code", "map_name",
    "orange", "blue", "overtime", "playlist_id",
    "replay_title", "rocket_league_id", "visibility"
]


def get_replays(api_key: str, player_id: str, playlist: str) -> dict:
    response = requests.get(f"{BASE_URI}/replays", headers={
        "Authorization": api_key
    }, params={
        "player-id": player_id,
        "playlist": playlist
    })
    return response.json()


def follow_next(api_key: str, next_url: str) -> dict:
    response = requests.get(next_url, headers={
        "Authorization": api_key
    })
    return response.json()


def filter_useful_keys(keys, replays):
    tmp_replays = []
    for r in replays:
        tmp_replay = {}
        for key in keys:
            tmp_replay[key] = r[key]
        tmp_replays.append(tmp_replay)

    return tmp_replays


def remove_duplicates(replays):
    ids = set((r["id"] for r in replays))
    replays_clean = []
    for i in ids:
        replay = [r for r in replays if r["id"] == i][0]
        replays_clean.append(replay)

    return replays_clean


def filter_standard_games(replays):
    def is_standard(replay):
        try:
            return (len(replay["orange"]["players"]) == 3
                    and len(replay["blue"]["players"]) == 3)
        except:
            return False

    return [r for r in replays if is_standard(r)]


if __name__ == "__main__":

    api_key = read_api_key()
    team = read_config()

    team_replays = []

    for player in team:
        print(f"Fetching replays for {player['name']}...")
        player_replays = get_replays(api_key, player["id"], PLAYLIST)
        # Append the current page player replays to the team replays
        page_replays = player_replays.get("list")
        if page_replays:
            # Preserve useful keys
            page_replays = filter_useful_keys(USEFUL_KEYS, page_replays)
            team_replays = [*team_replays, *page_replays]

        pages_read = 0
        while "next" in player_replays:
            print(f"Following page #{pages_read+1}...")
            print(f"> {player_replays['next']}")
            next_page = player_replays["next"]
            player_replays = follow_next(api_key, next_page)
            # Append the current page player replays to the team replays
            page_replays = player_replays.get("list")
            if page_replays:
                team_replays = [*team_replays, *page_replays]

            pages_read += 1
            time.sleep(2)

        time.sleep(2)

    # Remove replay duplicates
    team_replays = remove_duplicates(team_replays)

    # Preserve only standard 3v3 replays
    team_replays = filter_standard_games(team_replays)

    # Order replays by date
    team_replays = sorted(team_replays, key=lambda r: r["date"], reverse=True)

    print(f"Found {len(team_replays)} replays")

    print(f"Storing replays...")
    # Store results
    with open("saved_data/team_replays.json", "w") as fp:
        fp.write(json.dumps(team_replays))
