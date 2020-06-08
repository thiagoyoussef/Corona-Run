import pygame
from os import path
from Parameters import SCORE_FONT, FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, GREEN, BLUE, GRAVITY, JUMP, MEGA_JUMP_1, MEGA_JUMP_2, GROUND, STILL, JUMPING, FALLING, DEATH, world_speed, INITIAL_CACTOS, INITIAL_BLOCKS, TILE_SIZE, BOSS_SIZE

PLAYER_IMG = 'dino.png'
BOSS_IMG = 'boss.png'
BACKGROUND_IMG = 'background.png'
CACTOS_IMG = 'cactos.png'
SCORE_FONT = 'PressStart2P.ttf'
GAME_OVER_IMG = 'game_over.png'
PUKE_IMG = 'puke.png'
BLOCK_IMG = 'block_img.png'

# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, PLAYER_IMG)).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.image.load(path.join(img_dir, BACKGROUND_IMG)).convert_alpha()
    assets[CACTOS_IMG] = pygame.image.load(path.join(img_dir, CACTOS_IMG)).convert_alpha()
    assets[SCORE_FONT] = pygame.font.Font(SCORE_FONT, 28)
    assets[GAME_OVER_IMG] = pygame.image.load(path.join(img_dir, GAME_OVER_IMG)).convert_alpha()
    assets[BOSS_IMG] = pygame.image.load(path.join(img_dir, BOSS_IMG)).convert_alpha()
    assets[PUKE_IMG] = pygame.image.load(path.join(img_dir, PUKE_IMG)).convert_alpha()
    assets[BLOCK_IMG] = pygame.image.load(path.join(img_dir, BLOCK_IMG)).convert_alpha()
    return assets

# Carrega som do jogo
pygame.mixer.music.load('sounds/mario_music.ogg')
pygame.mixer.music.set_volume(0.2)

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

# Funcao que adiciona tela de game over
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
    time.sleep(5)
    
    return 1

