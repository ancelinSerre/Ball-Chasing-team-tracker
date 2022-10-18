# Ball chasing tracker

Track your scrims and improve by taking advantage of the [Ball Chasing](https://ballchasing.com) in-game statisticts 📈 🚀

## Step 1: Authentification

Add your Ball chasing API token in a file following that structure:

```json
{
    "API_KEY": "YOUR_API_KEY"
}
```

> Rename the file `ex_credentials.json` to `credentials.json` and replace the dummy API key by yours.

You can (re)generate your API key [right there](https://ballchasing.com/upload).


## Step 2: Team config

Add all the players composing your team in a config file following that structure:

```json
{
    "TEAM": [
        {
            "name": "Kaydop",
            "id": "BALL_CHASING_USER_ID"
        },
        {
            "name": "Fairy Peak",
            "id": "BALL_CHASING_USER_ID"
        },
        {
            "name": "Alpha54",
            "id": "BALL_CHASING_USER_ID"
        }
    ]
}
```

> Rename the file `ex_config.json` to `config.json` and replace the players by yours.

In order to find the Ball Chasing user id, what you can do is :

1. Check on their website by first searching your replays (just type your IG name in the search bar).
2. Then, click on your name on the first replay that appears.
3. Finally, check in the page url, it should be written there like that:

```bash
                                   this is your id
                               <---------------------->
https://ballchasing.com/player/steam/76561198960189434
```

Just replace the `/` by a `:` and you should be fine.