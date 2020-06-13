"""
Arquivo principal
Inicia a tela do jogo e inicializa o pygame
"""

import pygame
import random
import time
from parameters import WIDTH, HEIGHT, TITULO, img_dir
from game_loop import game_screen 
from functions import *
from assets import load_assets
from game_loop import*

pygame.init()
pygame.mixer.init()

# Gera tela principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITULO)

# Carrega assets
assets = load_assets(img_dir)

# Finalização 
# Comando para evitar travamentos.
try:
    if start_screen(screen, assets) != 'quit': # Mostra tela de start
        player_type = player_screen(screen, assets) # Mostra tela de seleção de jogadores
        #game_screen(screen, assets, player_type) # Tela do jogo
        if game_screen(screen, assets, player_type) == 'endgame':
            while True:
                if game_over_screen(screen, assets) == False:
                    player_type = player_screen(screen, assets)
                    game_screen(screen, assets, player_type)

finally:
    pygame.quit()


    