def checkOrBetStrat(game_info):
    # always check
    return {"action": "check"}

def callOrRaiseStrat(game_info):
    # always raise 3BB if possible otherwise bot checks 
    return {"action": "raise", "chips": game_info["bigBlindValue"]*3}

