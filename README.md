# pokerwars.io-starterbot-python
Implementation of poker bot in Python.


## Quick start
A few requirements to play:
- have [python](https://www.python.org/) installed
- [ngrok](https://ngrok.com/) installed in the project directory
- [Register with Pokerwars](https://www.pokerwars.io/) and retrieve your [API token](https://www.pokerwars.io/token) and [username](https://www.pokerwars.io/profile).
- check out this repo with git
- Add a `.env` file with the following

```
USERNAME=insert here your bot username, find it at https://www.pokerwars.io/profile
API_TOKEN=insert here your api token, find it at https://www.pokerwars.io/token
```

## Play!
Now you are ready to run the bot!

Install dependencies:
```
$ pip install -r requirements.txt
```

Run Tunnel and bot:

> [ngrok](https://ngrok.com/) must be installed in your project directory to open a tunnel.

```
$ make start
```


The bot will try to subscribe to pokerwars.io when it starts up, using the tunnel. If no errors occur, it will start playing straightaway, otherwise you should see an error. The most common is Pokerwars cannot see your bot, please double check your bot is visible.


## Bot subscription to pokerwars
When the bot starts up, the ```subscribe()``` method waits for its ```/pokerwars.io/ping``` endpoint to become available before subscribing the bot with pokerwars.io.

If the subscription request is not accepted or fails, for whatever reason, the bot will exit.

## Developing

- [ ] Add a strategy runner to dynamically evolve strategy over time
- [ ] Add tests
