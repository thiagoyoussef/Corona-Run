from parameters import *

''' 
Função que passa variados parametros que sera usado para
criar os diversos tipos de personagens na classe Player
Primeiro parametro relaciona a imagem do personagem
Segundo parametro define tamanho x do personagem
Terceiro parametro define tamanho y do personagem
Quarto parametro define se será usado a animacao do dino no personagem escolhido
'''

def load_players(assets):
    players = {}
    players[KRATOS] = [assets[KRATOS], 130, 90, False]
    players[DINO] = [assets[DINO], 250, 100, True]
    players[SONIC] = [assets[SONIC], 125, 80, False]
    players[MARIO] = [assets[MARIO], 55, 55, False]
    players[YOSHI] = [assets[YOSHI], 100, 60, False]
    players[DEADPOOL] = [assets[DEADPOOL], 110, 110, False]
    players[CORONITA] = [assets[CORONITA], 100, 120, False]
    players[ASH] = [assets[ASH], 50, 70, False]
    players[FLAPPY] = [assets[FLAPPY], 100, 70, False]
    return players