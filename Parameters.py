'''
Arquivo com todos os parâmetros que
será utilizado nas classes e funções
'''

from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sounds')

# Dados gerais do jogo.
TITULO = 'Corona Run'
WIDTH = 1000 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo
PLAYER_IMG = 'dino.png'
BOSS_IMG = 'boss.png'
BACKGROUND_IMG = 'background.png'
CACTOS_IMG = 'cactos.png'
SCORE_FONT = 'PressStart2P.ttf'
GAME_OVER_IMG = 'game_over.png'
PUKE_IMG = 'puke.png'
BLOCK_IMG = 'block_img.png'

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 2

# Define dois tipos de pulo
JUMP = 26
MEGA_JUMP_1 = 5
MEGA_JUMP_2 = 10

# Define a altura do chão
GROUND = HEIGHT / 1.183

# Define estados possíveis do jogo
START = 5
PLAYING = 6
ENDGAME = 7
DONE = 8

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
DEATH = 3

# Define a velocidade inicial do mundo
world_speed = -7

# Define a quantidade inicial de:
INITIAL_CACTOS = 2 # Cactos
INITIAL_BLOCKS = 4 # Blocks

# Outras constantes
TILE_SIZE = 50
BOSS_SIZE = 175