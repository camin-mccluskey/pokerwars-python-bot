"""
Controls bot play by generating many bots and controlling a tournament between then
"""
from bottle import response
from src.strategy import checkOrBetStrat, callOrRaiseStrat


class GameMaster:
    def __init__(self):
        pass

    def play(self, game_state):
        """
        Plays bot next move
        :param game_state:
        :return:
        """

        # default action is fold
        action = {"action": "fold"}

        if game_state["canCheckOrBet"]:
            # bot can check or bet only if, in the current turn, no bot has bet already
            # if a bot bet already, bot must call or raise.
            action = checkOrBetStrat(game_state)

        if game_state["canCallOrRaise"]:
            # bot can call or raise only if there has been a bet before
            action = callOrRaiseStrat(game_state)

        response.content_type = 'application/json'
        return action

    def update_bot(self):
        """
        Updates the bot state. e.g. from last hand played or the result of a tounament
        :return:
        """
        pass

    def save_best_known_bot_state(self):
        """
        Saves the best known bot state to memory
        :return:
        """
        pass
