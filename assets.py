'''
Arquivo que carrega todos os assets
'''

import pygame
from os import path
from parameters import *
import time
import os

# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    # Carrega imagens do jogo
    assets[SONIC] = pygame.image.load(path.join(img_dir, SONIC)).convert_alpha()
    assets[KRATOS] = pygame.image.load(path.join(img_dir, KRATOS)).convert_alpha()
    assets[MARIO] = pygame.image.load(path.join(img_dir, MARIO)).convert_alpha()
    assets[YOSHI] = pygame.image.load(path.join(img_dir, YOSHI)).convert_alpha()
    assets[DEADPOOL] = pygame.image.load(path.join(img_dir, DEADPOOL)).convert_alpha()
    assets[DINO] = pygame.image.load(path.join(img_dir, DINO)).convert_alpha()
    assets[ASH] = pygame.image.load(path.join(img_dir, ASH)).convert_alpha()
    assets[CORONITA] = pygame.image.load(path.join(img_dir, CORONITA)).convert_alpha()
    assets[FLAPPY] = pygame.image.load(path.join(img_dir, FLAPPY)).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, BACKGROUND_IMG)).convert_alpha()
    assets[CACTOS_IMG] = pygame.image.load(path.join(img_dir, CACTOS_IMG)).convert_alpha()
    assets[GAME_OVER_IMG] = pygame.image.load(path.join(img_dir, GAME_OVER_IMG)).convert_alpha()
    assets[BOSS_IMG] = pygame.image.load(path.join(img_dir, BOSS_IMG)).convert_alpha()
    assets[BOSS_SMILE] = pygame.image.load(path.join(img_dir, BOSS_SMILE)).convert_alpha()
    assets[PUKE_IMG] = pygame.image.load(path.join(img_dir, PUKE_IMG)).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, BLOCK_IMG)).convert_alpha()
    assets[BULLET_IMG] = pygame.image.load(path.join(img_dir, BULLET_IMG)).convert_alpha()
    assets[HOME_SCREEN] = pygame.image.load(path.join(img_dir, HOME_SCREEN)).convert_alpha()
    # Carrega fontes do jogo
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(font_dir, SCORE_FONT), 28)
    # Carrega som do jogo
    pygame.mixer.music.load(os.path.join(snd_dir, 'mario_music.ogg'))
    pygame.mixer.music.set_volume(0.1)
    assets[JUMP_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, JUMP_SOUND))
    assets[DIE_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, DIE_SOUND))
    assets[BACKINBLACK_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, BACKINBLACK_SOUND))
    assets[CHECKPOINT_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, CHECKPOINT_SOUND))
    assets[COINSOUND_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, COINSOUND_SOUND))
    assets[COUNTDOWN_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, COUNTDOWN_SOUND))
    assets[EXPL3_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, EXPL3_SOUND))
    assets[EXPL6_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, EXPL6_SOUND))
    #assets[FINALE_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, FINALE_SOUND))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, PEW_SOUND))
    #assets[WIND_SOUND] = pygame.mixer.Sound(os.path.join(snd_dir, WIND_SOUND))

    return assets