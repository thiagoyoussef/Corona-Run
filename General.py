"""Inicialização 
Importa e inicia pacotes"""
import pygame
import random
from Parameters import WIDTH, HEIGHT, TITULO
from GameLoop import game_screen
import time

pygame.init()
pygame.mixer.init()

# Gera tela principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITULO)

game_screen(screen)

# Finalização 
# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()