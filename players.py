from parameters import *

''' 
Função que passa variados parametros que sera usado para
criar os diversos tipos de personagens na classe Player
Primeiro parametro relaciona a imagem do personagem
Segundo parametro define tamanho x do personagem
Terceiro parametro define tamanho y do personagem
Quarto parametro define se será usado a animacao do dino no personagem escolhido
Quinto parametro ajusta a altura do chão para cada personagem
'''

def load_players(assets):
    players = {}
    players[KRATOS] = [assets[KRATOS], 130,115, False, 0]
    players[DINO] = [assets[DINO], 250, 100, True, 0]
    players[SONIC] = [assets[SONIC], 125, 80, False, 0]
    players[MARIO] = [assets[MARIO], 55, 55, False, 0]
    players[YOSHI] = [assets[YOSHI], 100, 60, False, 3]
    players[DEADPOOL] = [assets[DEADPOOL], 110, 110, False, 0]
    players[CORONITA] = [assets[CORONITA], 100, 120, False, 0]
    players[ASH] = [assets[ASH], 50, 70, False, 1]
    players[FLAPPY] = [assets[FLAPPY], 110, 80, False, 0]
    return players