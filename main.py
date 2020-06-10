"""
Arquivo principal
Inicia a tela do jogo e inicializa o pygame
"""

import pygame
import random
import time
from parameters import WIDTH, HEIGHT, TITULO
from game_loop import game_screen 

pygame.init()
pygame.mixer.init()

# Gera tela principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITULO)

# Finalização 
# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
    