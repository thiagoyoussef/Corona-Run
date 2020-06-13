'''
Arquivo com todas as funções que
serão utilizadas no pygame
'''

import pygame
from parameters import *
import time
from players import load_players

# Animacoes quando o personagem anda
def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height),pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

# Função que adiciona a tela de start
def start_screen(screen, assets):
    home_screen_img = pygame.transform.scale(assets[HOME_SCREEN], (int(WIDTH) , int(HEIGHT)))
    background_rect = home_screen_img.get_rect()
    screen.blit(home_screen_img, background_rect)
    font = pygame.font.SysFont("comicsansms", 48)
    while True:
        START = font.render('START', True, BLACK)
        START_rect = START.get_rect()
        START_rect.x = WIDTH//8 + 250
        START_rect.y = HEIGHT*2/4
        screen.blit(START, [WIDTH//8 + 250, HEIGHT*2/4])
        QUIT = font.render('QUIT', True, BLACK)
        QUIT_rect = QUIT.get_rect()
        QUIT_rect.x = WIDTH//8 + 320
        QUIT_rect.y = HEIGHT*3/4 - 100
        screen.blit(QUIT, [WIDTH//8 + 320, HEIGHT*3/4 - 100])
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            click = pygame.mouse.get_pos()
            if click[0] > START_rect.left and click[0] < START_rect.right and click[1] > START_rect.top and click[1] < START_rect.bottom:
                START = font.render('START', True, GREEN)
                START_rect = START.get_rect()
                START_rect.x = WIDTH//8 + 250
                START_rect.y = HEIGHT*2/4
                screen.blit(START, [WIDTH//8 + 250, HEIGHT*2/4])
                pygame.display.flip()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return False
                
        for event in pygame.event.get():
            click = pygame.mouse.get_pos()
            if click[0] > QUIT_rect.left and click[0] < QUIT_rect.right and click[1] > QUIT_rect.top and click[1] < QUIT_rect.bottom:
                QUIT = font.render('QUIT', True, GREEN)
                QUIT_rect = QUIT.get_rect()
                QUIT_rect.x = WIDTH//8 + 320
                QUIT_rect.y = HEIGHT*3/4 - 100
                screen.blit(QUIT, [WIDTH//8 + 320, HEIGHT*3/4 - 100])
                pygame.display.flip()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 'quit'

# Função que adiciona a inicio com seleção de personagens
def player_screen(screen, assets):
    players = load_players(assets)
    background_img = pygame.transform.scale(assets[BACKGROUND_IMG], (int(WIDTH) , int(HEIGHT)))
    kratos = pygame.transform.scale(players[KRATOS][0], (int(players[KRATOS][1]) , int(players[KRATOS][2])))
    kratos_rect = kratos.get_rect()
    kratos_rect.x = 267
    kratos_rect.y = 88
    sonic = pygame.transform.scale(players[SONIC][0], (int(players[SONIC][1]) , int(players[SONIC][2])))
    sonic_rect = sonic.get_rect()
    sonic_rect.x = 417
    sonic_rect.y = 88
    dino = pygame.transform.scale(players[DINO][0], (int(players[DINO][1]) , int(players[DINO][2])))
    dino_rect = dino.get_rect()
    dino_rect.x = 567
    dino_rect.y = 88
    mario = pygame.transform.scale(players[MARIO][0], (int(players[MARIO][1]) , int(players[MARIO][2])))
    mario_rect = mario.get_rect()
    mario_rect.x = 267
    mario_rect.y = 238
    yoshi = pygame.transform.scale(players[YOSHI][0], (int(players[YOSHI][1]) , int(players[YOSHI][2])))
    yoshi_rect = yoshi.get_rect()
    yoshi_rect.x = 417
    yoshi_rect.y = 238
    ash = pygame.transform.scale(players[ASH][0], (int(players[ASH][1]) , int(players[ASH][2])))
    ash_rect = ash.get_rect()
    ash_rect.x = 567
    ash_rect.y = 238
    deadpool = pygame.transform.scale(players[DEADPOOL][0], (int(players[DEADPOOL][1]) , int(players[DEADPOOL][2])))
    deadpool_rect = deadpool.get_rect()
    deadpool_rect.x = 267
    deadpool_rect.y = 388
    coronita = pygame.transform.scale(players[CORONITA][0], (int(players[CORONITA][1]) , int(players[CORONITA][2])))
    coronita_rect = coronita.get_rect()
    coronita_rect.x = 417
    coronita_rect.y = 388
    flappy = pygame.transform.scale(players[FLAPPY][0], (int(players[FLAPPY][1]) , int(players[FLAPPY][2])))
    flappy_rect = flappy.get_rect()
    flappy_rect.x = 567
    flappy_rect.y = 388
    background_rect = background_img.get_rect()
    screen.blit(background_img, background_rect)
    screen.blit(kratos, [267, 88])
    screen.blit(sonic, [417, 88])
    screen.blit(dino, [567, 88])
    screen.blit(mario, [267, 238])
    screen.blit(yoshi, [417, 238])
    screen.blit(ash, [567, 238])
    screen.blit(deadpool, [267, 388])
    screen.blit(coronita, [417, 388])
    screen.blit(flappy, [567, 388])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if click[0] > kratos_rect.left and click[0] < kratos_rect.right and click[1] > kratos_rect.top and click[1] < kratos_rect.bottom:
                    return KRATOS
                if click[0] > sonic_rect.left and click[0] < sonic_rect.right and click[1] > sonic_rect.top and click[1] < sonic_rect.bottom:
                    return SONIC
                if click[0] > dino_rect.left and click[0] < dino_rect.right and click[1] > dino_rect.top and click[1] < dino_rect.bottom:
                    return DINO
                if click[0] > mario_rect.left and click[0] < mario_rect.right and click[1] > mario_rect.top and click[1] < mario_rect.bottom:
                    return MARIO
                if click[0] > yoshi_rect.left and click[0] < yoshi_rect.right and click[1] > yoshi_rect.top and click[1] < yoshi_rect.bottom:
                    return YOSHI
                if click[0] > ash_rect.left and click[0] < ash_rect.right and click[1] > ash_rect.top and click[1] < ash_rect.bottom:
                    return ASH
                if click[0] > deadpool_rect.left and click[0] < deadpool_rect.right and click[1] > deadpool_rect.top and click[1] < deadpool_rect.bottom:
                    return DEADPOOL
                if click[0] > coronita_rect.left and click[0] < coronita_rect.right and click[1] > coronita_rect.top and click[1] < coronita_rect.bottom:
                    return CORONITA
                if click[0] > flappy_rect.left and click[0] < flappy_rect.right and click[1] > flappy_rect.top and click[1] < flappy_rect.bottom:
                    return FLAPPY
        pygame.display.update()

# Função que adiciona a tela de game over
def game_over_screen(screen, assets):

    # Redimensiona o tamanho da imagem
    game_over_img = pygame.transform.scale(assets[GAME_OVER_IMG], (int(WIDTH/2.114) , int(HEIGHT/2.4)))
    background_rect = game_over_img.get_rect()

    # Centraliza a imagem
    background_rect.centerx = WIDTH / 2
    background_rect.bottom = int(HEIGHT / 1.5)
    
    # Desenha a imagem
    screen.fill(BLACK)
    screen.blit(game_over_img, background_rect)
    pygame.display.flip()

    # Pausa o jogo na tela de game over
    time.sleep(1)
    
    return 'endgame'