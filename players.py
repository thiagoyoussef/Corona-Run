from parameters import *

def load_players(assets):
    players = {}
    players[KRATOS] = [assets[KRATOS], 125,50, False]
    players[DINO] = [assets[DINO], 250, 100, True]
    players[SONIC] = [assets[SONIC], 125, 50, False]
    players[MARIO] = [assets[MARIO], 125, 50, False]
    players[YOSHI] = [assets[YOSHI], 125, 50, False]
    return players