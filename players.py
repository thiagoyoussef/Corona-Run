from parameters import *

''' 
Função que passa variados parâmetros utilizados para
criar os diversos tipos de personagens na classe Player.

Significados dos parâmetros:
O primeiro parâmetro relaciona a imagem do personagem.
O segundo parâmetro define o tamanho x do personagem.
O terceiro parâmetro define o tamanho y do personagem.
O quarto parâmetro define se será usada a animação do dino no personagem escolhido
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