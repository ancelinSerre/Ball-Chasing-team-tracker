import json
import pprint

import requests

BASE_URI = "https://ballchasing.com/api"

TEAM = {
    "Ancelin": "steam:76561198060189434",
    "Anthony": "steam:76561198008382438",
    "Noé": "steam:76561198094258435",
    "Tom": "steam:76561198136333163"
}


def get_api_key(credentials_file):
    with open(credentials_file, "r") as fp:
        return json.loads(fp.read())["API_KEY"]


def get_replays(api_key, player_id, playlist):
    response = requests.get(f"{BASE_URI}/replays", headers={
        "Authorization": api_key
    }, params={
        "player-id": player_id,
        "playlist": playlist
    })
    return response.json()


if __name__ == "__main__":

    api_key = get_api_key("credentials.json")
    player_id = "steam:76561198060189434"
    playlist = "private"

    # replays = get_replays(api_key, player_id, "private")
    # with open("replays.json", "w") as fp:
    #     fp.write(json.dumps(replays))


    replays = None
    with open("replays.json", "r") as fp:
        replays = json.loads(fp.read())

    pp = pprint.PrettyPrinter()
    for replay in replays["list"]:
        replay_link = replay["link"]

        game = {
            "date": replay["date"],
            "playlist": replay.get("playlist_id", "unknown"),
            "blue": [{
                "name": p["name"],
                "score": p["score"]
            } for p in replay["blue"].get("players", [])],
            "orange": [{
                "name": p["name"],
                "score": p["score"]
            } for p in replay["orange"].get("players", [])],
        }
        pp.pprint(game)

    # Next url, follow this url when all replays are read
    # print(replays["next"])
