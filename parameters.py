'''
Arquivo com todos os parâmetros que
será utilizado nas classes e funções
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
FINAL_BOSS = 'final_boss.png'
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
CHECKPOINT_SOUND = 'checkPoint.wav'
COINSOUND_SOUND = 'coinsound.wav'
COUNTDOWN_SOUND = 'countdown.wav'
EXPL3_SOUND = 'expl3.wav'
EXPL6_SOUND = 'expl6.wav'
FINALE_SOUND = 'finale.mp3'
PEW_SOUND = 'pew.wav'
WIND_SOUND = 'windsfx3.ogg'

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
world_speed = -7

# Define a quantidade inicial de:
INITIAL_CACTOS = 2 # Cactos
INITIAL_BLOCKS = 5 # Blocks
INITIAL_HEARTS = 1

# Tamanho de alguns sprites
TILE_SIZE = 50
BOSS_SIZE = 175
BULLET_SIZE = 60
HEART_SIZE = 45
MYSTERIOUS_BOX_SIZE = 150

# Score que o boss entra na tela
boss_appears = 1500 # a definir, deixei baixo para rodar os testes