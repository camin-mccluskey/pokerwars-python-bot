def checkOrBetStrat(game_info):
    # always check
    return {"action": "check"}

def callOrRaiseStrat(game_info):
    # always raise 3BB if possible otherwise bot checks
    bb = game_info['bigBlindValue']
    minBet = game_info['minBet']
    bet = bb*3
    
    if minBet:
        bet = max(minBet, bet)
    
    return {"action": "raise", "chips": bet}

