'''
Arquivo com todas as funções que
serão utilizadas no pygame
'''

import pygame
from parameters import *
import time
from game_loop import*
from players import load_players
from assets import*

''' Função que retorna sprites das diferentes animações de um sprite'''
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

''' Função que adiciona a tela de start'''
def start_screen(screen, assets):
    
    # Carrega a imagem e desenha ela
    home_screen_img = pygame.transform.scale(assets[HOME_SCREEN], (int(WIDTH) , int(HEIGHT)))
    background_rect = home_screen_img.get_rect()
    screen.blit(home_screen_img, background_rect)
    font = assets[SCORE_FONT]
    
    # Realiza animações ao passar mouse nos botões START/QUIT
    while True:
        START = font.render('START', True, BLACK)
        START_rect = START.get_rect()
        START_rect.x = WIDTH//8 + 295
        START_rect.y = HEIGHT * 2/4
        screen.blit(START, [START_rect.x, START_rect.y])
        QUIT = font.render('QUIT', True, BLACK)
        QUIT_rect = QUIT.get_rect()
        QUIT_rect.x = WIDTH//8 + 310
        QUIT_rect.y = HEIGHT*3/4 - 100
        screen.blit(QUIT, [QUIT_rect.x, QUIT_rect.y])
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
                
            # Acrescenta o click nos botões START/QUIT
            click = pygame.mouse.get_pos()
            if START_rect.left < click[0] < START_rect.right and START_rect.top < click[1]  < START_rect.bottom:
                START = font.render('START', True, GREEN)
                screen.blit(START, [START_rect.x, START_rect.y])
                pygame.display.flip()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 'start'           
            if QUIT_rect.left < click[0] < QUIT_rect.right and QUIT_rect.top < click[1] < QUIT_rect.bottom:
                QUIT = font.render('QUIT', True, GREEN)
                screen.blit(QUIT, [QUIT_rect.x, QUIT_rect.y])
                pygame.display.flip()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 'quit'
            # Verifica se jogador desejas finalizar o jogo
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return 'quit'

''' Função que adiciona o inicio com seleção de personagens'''
def player_screen(screen, assets):
    
    # Carrega os players
    players = load_players(assets)
    
    # Carrega a imagem de fundo 
    background_img = pygame.transform.scale(assets[BACKGROUND_IMG], (int(WIDTH) , int(HEIGHT)))
    
    # Carrega a fonte e escolhe o que será escrito na tela
    font = assets[SCORE_FONT]
    choose = font.render('Choose your caracter', True, BLACK)
    
    # Ajusta a escala e as coordenadas dos personagens
    kratos = pygame.transform.scale(players[KRATOS][0], (int(players[KRATOS][1]) , int(players[KRATOS][2])))
    kratos_rect = kratos.get_rect()
    kratos_rect.x = 251
    kratos_rect.y = 88
    sonic = pygame.transform.scale(players[SONIC][0], (int(players[SONIC][1]) , int(players[SONIC][2])))
    sonic_rect = sonic.get_rect()
    sonic_rect.x = 417
    sonic_rect.y = 88
    dino = pygame.transform.scale(assets['dino_play.png'], (int(100) , int(70)))
    dino_rect = dino.get_rect()
    dino_rect.x = 567
    dino_rect.y = 88
    mario = pygame.transform.scale(players[MARIO][0], (int(players[MARIO][1]) , int(players[MARIO][2])))
    mario_rect = mario.get_rect()
    mario_rect.x = 296
    mario_rect.y = 247
    yoshi = pygame.transform.scale(players[YOSHI][0], (int(players[YOSHI][1]) , int(players[YOSHI][2])))
    yoshi_rect = yoshi.get_rect()
    yoshi_rect.x = 417
    yoshi_rect.y = 400
    ash = pygame.transform.scale(players[ASH][0], (int(players[ASH][1]) , int(players[ASH][2])))
    ash_rect = ash.get_rect()
    ash_rect.x = 587
    ash_rect.y = 238
    deadpool = pygame.transform.scale(players[DEADPOOL][0], (int(players[DEADPOOL][1]) , int(players[DEADPOOL][2])))
    deadpool_rect = deadpool.get_rect()
    deadpool_rect.x = 267
    deadpool_rect.y = 368
    flappy = pygame.transform.scale(players[FLAPPY][0], (int(players[FLAPPY][1]) , int(players[FLAPPY][2])))
    flappy_rect = flappy.get_rect()
    flappy_rect.x = 567
    flappy_rect.y = 388
    # Verifica se o jogador ja ganhou o jogo alguma vez
    filesize = os.path.getsize("txt/win.txt")
    if filesize == 0: # Se nao, aparece mysterious box
        mysterious_box = pygame.transform.scale(assets[MYSTERIOUS_BOX], (int(MYSTERIOUS_BOX_SIZE) , int(MYSTERIOUS_BOX_SIZE)))
    else: # Se sim, aparece coronita
        coronita = pygame.transform.scale(players[CORONITA][0], (int(players[CORONITA][1]) , int(players[CORONITA][2])))
        coronita_rect = coronita.get_rect()
        coronita_rect.x = 417
        coronita_rect.y = 208
    background_rect = background_img.get_rect()

    # Desenha na tela a imagem de fundo, personagens e texto
    screen.blit(background_img, background_rect)
    screen.blit(choose, [210, 30])
    screen.blit(kratos, [251, 88])
    screen.blit(sonic, [417, 88])
    screen.blit(dino, [567, 88])
    screen.blit(mario, [296, 247])
    screen.blit(yoshi, [417, 400])
    screen.blit(ash, [587, 238])
    screen.blit(deadpool, [267, 368])
    # Desenha mysterious box ou coronita
    if filesize == 0:
        screen.blit(mysterious_box, [395, 195])
    else:
        screen.blit(coronita, [417, 208])
    screen.blit(flappy, [567, 388])

    # Verifica se o jogador clicou em algum personagem
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return 'quit'
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
                if filesize != 0:
                    if click[0] > coronita_rect.left and click[0] < coronita_rect.right and click[1] > coronita_rect.top and click[1] < coronita_rect.bottom:
                        return CORONITA
                if click[0] > flappy_rect.left and click[0] < flappy_rect.right and click[1] > flappy_rect.top and click[1] < flappy_rect.bottom:
                    return FLAPPY
        pygame.display.update()

''' Função que adiciona a tela de game over'''
def game_over_screen(screen, assets):

    # Redimensiona o tamanho da imagem
    replay = pygame.transform.scale(assets[REPLAY], (int(WIDTH/8) , int(HEIGHT/8)))
    background_rect = replay.get_rect()
    
    # Localização da imagem
    background_rect.centerx = WIDTH / 2
    background_rect.bottom = int(HEIGHT * 7/8)

    # Loop do game over
    while True:
        
        # Desenha a tela
        screen.fill(BLACK)
        
        # Busca os valores de score e high_score nos respectivos arquivos
        with open('txt/high_score.txt', 'r') as file:
            X = file.read()
            high_score = int(X)
        with open('txt/score.txt', 'r') as file:
            Y = file.read()
            final_score = int(Y)

        # Desenha o score
        text_surface = assets[SCORE_FONT].render("Score: {:08d}".format(final_score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  50)
        screen.blit(text_surface, text_rect)

        # Desenha o high score
        text_surface = assets[SCORE_FONT].render("High Score: {:08d}".format(high_score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  100)
        screen.blit(text_surface, text_rect)

        # Escreve nossos nomes
        font = assets[SCORE_FONT]    
        text = font.render('By: Luca, Thiago and Vitor', True, RED) 
        screen.blit(text, [WIDTH//8 + 20, HEIGHT//4 + 100])

        # Escreve a opção de  play again
        font = assets[SCORE_FONT]    
        text = font.render('To play again, press the button', True, RED) 
        screen.blit(text, [WIDTH//10 - 20, HEIGHT//4 + 200])
        
        # Adiciona o botão de replay
        screen.blit(replay, background_rect)
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                press = pygame.mouse.get_pressed()
                if press and background_rect.left < pos[0] < background_rect.right and background_rect.top < pos[1] < background_rect.bottom:
                    return 'replay'
    
def se_fodeu_screen(screen, assets):

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
