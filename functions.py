'''
Arquivo com todas as funções que
serão utilizadas no pygame
'''

import pygame
from parameters import *
import time

# Animações de quando o personagem anda
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
def start_screen(screen):
    screen.fill(BLACK)
    screen.draw_text("CORONA RUN", screen.title_font, 100, RED,
                    WIDTH / 2, HEIGHT / 4, align="center")
    screen.draw_text("PRESS SPACE TO JUMP AND DOUBLE SPACE TO MEGAJUMP", screen.title_font, 75, WHITE,
                    WIDTH / 2, HEIGHT * 2, align="center")
    screen.draw_text("Press any key to start", screen.title_font, 75, WHITE,
                    WIDTH / 2, HEIGHT * 3 / 4, align="center")
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
    # Verifica se o jogo foi fechado.
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state = DONE
            running = False
            return running
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            state = PLAYING
            running = False
            return running

# Função que adiciona tela de game over
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
    
    return 1