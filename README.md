# pokerwars.io-starterbot-python
Implementation of poker bot in Python.


## Quick start
A few requirements to play:
- have [python](https://www.python.org/) installed
- make sure that the computer where your bot runs is visible from the internet, so we can communicate with it. [This is a useful service](http://canyouseeme.org/) to double check this. Bot default port is `3000`, but you can change this on the `bot.py` file. If you need help to open a port on your router [check this guide](https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/) or [contact us](mailto:contact@pokerwars.io). We are always willing to help you.
- [Register with Pokerwars](https://www.pokerwars.io/) and retrieve your [API token](https://www.pokerwars.io/token) and [username](https://www.pokerwars.io/profile).
- check out this repo with git or download it from [this link](https://github.com/pokerwars/pokerwars.io-starterbot-python/archive/master.zip).

```
USERNAME=insert here your bot username, find it at https://www.pokerwars.io/profile
API_TOKEN=insert here your api token, find it at https://www.pokerwars.io/token
BOT_ENDPOINT=insert here your bot ip address. i.e.: http://1.2.3.4:3000
```

## Play!
Now you are ready to run the bot!

Install dependencies:
```
$ pip install -r requirements.txt
```

Run the bot:
```
$ python starterbot.py
```

The bot will try to subscribe to pokerwars.io when it starts up. If no errors happens, it will start playing straightaway, otherwise you should see an error. The most common is that we cannot see your bot, please double check [your bot is visible from the internet](http://canyouseeme.org/) and [you have configured your router correctly](https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/). If you do not have access to your router or your bot is behind a firewall, try [ngrok](https://ngrok.com/).
## Bot subscription to pokerwars
When the bot starts up, the ```subscribe()``` method waits for its ```/pokerwars.io/ping``` endpoint to become available before subscribing the bot with pokerwars.io. This lets us know that your bot is ready to play and if we can ping your bot then it will be added to the next available tournament.

If the subscription request is not accepted or fails, for whatever reason, the bot will exit.
