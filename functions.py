'''
Arquivo com todas as funções que
serão utilizadas no pygame
'''

import pygame
from parameters import *
import time

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
    font1 = pygame.font.SysFont("comicsansms", 48)
    font2 = pygame.font.SysFont("comicsansms", 24)
    text = font2.render('START', True, GREEN)  
    screen.blit(text, [WIDTH//8 + 220, HEIGHT*3/4])
    text = font2.render('QUIT', True, GREEN)
    screen.blit(text, [WIDTH//8 + 220, HEIGHT*3/4])
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
        # Verifica se o jogo foi fechado.
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYUP:
                return False

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