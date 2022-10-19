import json

def read_api_key(filename="credentials.json") -> str:
    """
    Read Ball Chasing API Key from a json file
    """
    api_key = ""
    with open(filename, "r") as fp:
        api_key = json.loads(fp.read())["API_KEY"]
    return api_key


def read_config(filename="config.json") -> dict:
    """
    Read Ball Chasing config file that should
    contain all your team mates
    """
    team = {}
    with open(filename, "r", encoding="utf8") as fp:
        team = json.loads(fp.read())["TEAM"]
    return team