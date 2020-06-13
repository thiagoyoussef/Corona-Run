from parameters import *

def load_players(assets):
    players = {}
    players[KRATOS] = [assets[KRATOS], 125,100, False, WIDTH / 10, HEIGHT ]
    players[DINO] = [assets[DINO], 250, 100, True, WIDTH / 10, HEIGHT * 7 / 8]
    players[SONIC] = [assets[SONIC], 125, 80, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[MARIO] = [assets[MARIO], 70, 50, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[YOSHI] = [assets[YOSHI], 100, 60, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[DEADPOOL] = [assets[DEADPOOL], 100, 60, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[CORONITA] = [assets[CORONITA], 100, 60, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[ASH] = [assets[ASH], 100, 60, False, WIDTH / 10, HEIGHT * 7 / 8]
    players[FLAPPY] = [assets[FLAPPY], 100, 60, False, WIDTH / 10, HEIGHT * 7 / 8]
    return players