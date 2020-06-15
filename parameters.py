'''
Arquivo com todos os parâmetros fixos que
serão utilizados no código.
'''

from os import path
import pygame

# Estabelece a pasta que contem as figuras, sons e fontes.
img_dir = path.join(path.dirname(__file__), 'assets', 'img')
snd_dir = path.join(path.dirname(__file__),  'assets', 'snd')
font_dir = path.join(path.dirname(__file__),  'assets', 'font')

# Dados gerais do jogo.
TITULO = 'Corona Run'
WIDTH = 1000 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo
BOSS_IMG = 'boss.png'
BOSS_1_IMG = 'boss_1_1.png'
BOSS_2_IMG = 'boss_1_2.png'
BOSS_3_IMG = 'boss_1_3.png'
BOSS_4_IMG = 'boss_1_4.png'
FINAL_BOSS = 'final_boss.png'
FINAL_1_BOSS = 'boss_2_1.png'
FINAL_2_BOSS = 'boss_2_2.png'
FINAL_3_BOSS = 'boss_2_3.png'
FINAL_4_BOSS = 'boss_2_4.png'
BACKGROUND_IMG = 'background.png'
CACTOS_IMG = 'cactos.png'
SCORE_FONT = 'PressStart2P.ttf'
GAME_OVER_IMG = 'game_over.png'
PUKE_IMG = 'puke.png'
BLOCK_IMG = 'block_img.png'
BULLET_IMG = 'balinha.png'
HOME_SCREEN = 'home_screen.png'
REPLAY = 'replay_button.png'
HEART_IMG = 'heart.png'
MYSTERIOUS_BOX = 'mysterious_box.png'

# Parametros relacionados aos sons
JUMP_SOUND = 'jump.ogg'
DIE_SOUND = 'die.wav'
BACKINBLACK_SOUND = 'backinblack.ogg'
COINSOUND_SOUND = 'coinsound.wav'
PEW_SOUND = 'pew.wav'

# Parametros relacionados aos jogadores
DINO = 'dino.png'
SONIC = 'sonic.png'
KRATOS = 'kratos.png'
MARIO = 'mario.png'
YOSHI = 'yoshi.png'
CORONITA = 'coronita.png'
DEADPOOL = 'deadpool.png'
ASH = 'ash.png'
FLAPPY = 'flappy.png'
DINO_PLAY = 'dino_play.png'

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

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
DEATH = 3

# Define a velocidade inicial do mundo
world_speed = -8

# Define a quantidade inicial de:
INITIAL_CACTOS = 3 # Cactos
INITIAL_BLOCKS = 4 # Blocks
INITIAL_HEARTS = 1

# Tamanho de alguns sprites
TILE_SIZE = 50
BOSS_SIZE = 175
BULLET_SIZE = 60
HEART_SIZE = 45
MYSTERIOUS_BOX_SIZE = 150

# Score que o boss entra na tela
boss_appears = 5000