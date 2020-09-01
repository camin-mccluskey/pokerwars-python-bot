#!/usr/bin/env python

from threading import Thread
from bottle import get, post, run, request, response
from time import sleep
from dotenv import load_dotenv
from sys import exit, argv
from src.game_master import GameMaster

import requests
import os

load_dotenv()

port = 3000
username = os.getenv('USERNAME')
api_token = os.getenv('API_TOKEN')

# pass botendpoint in a cmd line arg from ngrok
bot_endpoint = argv[1]
notifications = True

# initialise GameMaster
game_master = GameMaster()


@post('/pokerwars.io/play')
def play():
    # This endpoint is called by pokerwars.io to request the bot's next move on a tournament.
    game_state = request.json
    return game_master.play(game_state)


@get('/pokerwars.io/ping')
def ping():
    # This is used by pokerwars.io when the bot subscribes, to verify that is alive and responding
    print('Received ping from pokerwars.io, responding with a pong')
    response.content_type = 'application/json'
    return {"pong": True}


@post('/pokerwars.io/notifications')
def notifications():
    print('Received notification')
    print(request.json)
    response.content_type = 'application/json'
    return


def subscribe():
    down = True

    while down:
        try:
            print('Trying to subscribe to pokerwars.io ...')
            r = requests.get(bot_endpoint + '/pokerwars.io/ping')

            if r.status_code == 200:
                down = False

                r = requests.post('https://play.pokerwars.io/v1/pokerwars/subscribe',
                                  json={'username': username,
                                        'token': api_token,
                                        'botEndpoint': bot_endpoint,
                                        'notifications': bool(notifications)})

                print('Subscription --> Status code: ' + str(r.status_code))
                print('Subscription --> Body: ' + str(r.json()))

                if r.status_code != 202:
                    print('Failed to subscribe, aborting ...')
                    exit()
        except requests.RequestException:
            exit()

        sleep(2)


if __name__ == '__main__':
    s = Thread(target=subscribe)
    s.daemon = True
    s.start()

    run(port=port)
