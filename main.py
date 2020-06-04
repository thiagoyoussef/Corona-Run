import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

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

# Carrega som do jogo
pygame.mixer.music.load('sounds/mario_music.ogg')
pygame.mixer.music.set_volume(0.2)

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
NORMAL_JUMP = 30
MEGA_JUMP = 45

# Define a altura do chão
GROUND = HEIGHT / 1.183

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
DEATH = 3

# Define a velocidade inicial do mundo
world_speed = -10

# Define a quantidade inicial de:
INITIAL_CACTOS = 2 # Cactos
INITIAL_BLOCKS = 6 # Blocks

# Outras constantes
TILE_SIZE = 70
BOSS_SIZE = 175

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

# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, assets, x, y, speedx):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        block_img = pygame.transform.scale(assets[BLOCK_IMG], (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = block_img
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, assets):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho da imagem
        player_img = pygame.transform.scale(assets[PLAYER_IMG], (250, 100))

        # Define sequências de sprites de cada animação
        spritesheet = load_spritesheet(player_img, 1, 5)
        self.animations = {
            STILL: spritesheet[2:4],
            JUMPING: spritesheet[2:3],
            FALLING: spritesheet[3:4],
        }
        
        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Define animação atual
        self.animation = self.animations[self.state]

        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Começa no centro da janela
        self.rect.centerx = WIDTH / 10
        self.rect.bottom = int(HEIGHT * 7 / 8)
        self.rect.top = 0
        self.speedy = 0
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75

    # Método que faz o personagem pular
    def jump(self, JUMP_TYPE):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_TYPE
            self.state = JUMPING

    # Metodo que atualiza a posição do personagem
    def update(self):
        self.speedy += GRAVITY

        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy

        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = STILL

        # Update de movimentacao 
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

# Classe que representa o boss
class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        boss_img = pygame.transform.scale(assets[BOSS_IMG], (BOSS_SIZE, BOSS_SIZE))
        self.image = boss_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 100
        self.rect.bottom = HEIGHT - 400
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        
        # Atualização da posição do boss, manter comentado a linha abaixo para ficar estático
        #self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def puke(self):
        # Verifica se pode disparar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último disparo.
        elapsed_ticks = now - self.last_shot

        # Se já pode disparar novamente...
        if elapsed_ticks > self.shoot_ticks:

            # Marca o tick da nova imagem.
            self.last_shot = now
            
            # O novo puke vai ser criada logo a esquerda e no centro vertical do boss
            new_puke = Puke(self.assets, self.rect.left, self.rect.centery)
            self.groups['all_sprites'].add(new_puke)
            self.groups['all_puke'].add(new_puke)

# Classe Puke que representa os disparos do boss
class Puke(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, assets, left, centery):
        
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        puke_img = pygame.transform.scale(assets[PUKE_IMG], (70, 100))
        self.image = puke_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = centery
        self.rect.left = left
        self.speedx = -10  # Velocidade fixa para esquerda
        self.speedy = random.randint(0,5) # Velocidade aleatória para baixo

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o puke passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

# Classe que reprenta os cactos
class Cactos(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, speedx):
        
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminui o tamanho da imagem
        cactos_img = pygame.transform.scale(assets[CACTOS_IMG], (70, 100))
        self.image = cactos_img
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Posiciona o cacto
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        
    def update(self):
        self.rect.x += self.speedx

# Função principal do jogo
def game_screen(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Cria grupos
    all_sprites = pygame.sprite.Group() # Grupo de todos os sprites
    all_blocks = pygame.sprite.Group()
    all_cactos = pygame.sprite.Group()
    all_puke = pygame.sprite.Group()

    # Cria dicionário para adicionar todos os grupos
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_blocks'] = all_blocks
    groups['all_cactos'] = all_cactos
    groups['all_puke'] = all_puke

    # Cria Sprite do jogador e adiciona ao grupo
    player = Player(assets)
    all_sprites.add(player) 
  
    # Cria cactos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_CACTOS):
        cacto_x = random.randint(800, 1400)
        cacto_y = HEIGHT / 1.47
        cacto = Cactos(assets, cacto_x, cacto_y, world_speed)
        
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(cacto)
        all_cactos.add(cacto)
    
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = random.randint(0, WIDTH)
        block_y = random.randint(0, int(HEIGHT * 0.5))
        block = Tile(assets, block_x, block_y, world_speed)
        
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(block)
        all_blocks.add(block)
    
    score = 0
    PLAYING = 0
    DONE = 1
    state = PLAYING
    pygame.mixer.music.play()

    # While principal
    while state != DONE or state != 1:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Adiciona o boss após um certo score
        if score == 2500:
            boss = Boss(groups, assets)
            all_sprites.add(boss)
        
        # Junto com o boss inicia o disparo de puke
        if score >= 2500:
            boss.puke()
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                state = DONE
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE:
                    player.jump(NORMAL_JUMP)
                if event.key == pygame.K_UP:
                    player.jump(MEGA_JUMP)

        # Atualiza a ação de todos os sprites
        all_sprites.update()

        # Adiciona pontos ao score
        score += 10

        # Verifica se houve colisão entre jogador e cacto
        hits = pygame.sprite.spritecollide(player, all_cactos, True)
        if len(hits) > 0:
            state = game_over_screen(screen, assets)

        # Verifica se algum cacto saiu da janela
        for cacto in all_cactos:
            if cacto.rect.right < 0:
                
                # Destrói o cacto e cria um novo no final da tela
                cacto.kill()
                
                # Verifica se tem uma distancia minima para adicionar novos cactos
                OK = False
                while not OK:
                    cacto_x = random.randint (1000, 2000) 
                    cacto_y = HEIGHT / 1.47
                    new_cacto = Cactos(assets, cacto_x, cacto_y, world_speed)
                    OK = True
                    for cacto in all_cactos:
                        if abs(cacto.rect.centerx - cacto_x) < 100:
                            OK = False   
                
                # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados              
                all_sprites.add(new_cacto)
                all_cactos.add(new_cacto)
        
        # Verifica se algum bloco saiu da janela
        for block in all_blocks:
            if block.rect.right < 0:
                
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(WIDTH, int(WIDTH * 1.5))
                block_y = random.randint(0, int(HEIGHT * 0.5))
                new_block = Tile(assets, block_x, block_y, world_speed)

                # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
                all_sprites.add(new_block)
                all_blocks.add(new_block)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Atualiza a posição da imagem de fundo.
        background_rect.x += world_speed
        
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        # Desenha todos os sprites na tela
        all_sprites.draw(screen)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()