import random
import pygame
from Parameters import SCORE_FONT, FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, GREEN, BLUE, GRAVITY, JUMP, MEGA_JUMP_1, MEGA_JUMP_2, GROUND, STILL, JUMPING, FALLING, DEATH, world_speed, INITIAL_CACTOS, INITIAL_BLOCKS, TILE_SIZE, BOSS_SIZE
from Assets import game_over_screen, PLAYER_IMG, BOSS_IMG, CACTOS_IMG, PUKE_IMG, BLOCK_IMG, load_assets, load_spritesheet


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
            MEGA_JUMP_1: spritesheet[2:3],
            MEGA_JUMP_2: spritesheet[2:3],
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
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP
            self.state = JUMPING
        # tipos de MEGA JUMP;
        elif self.state == JUMPING: 
            self.speedy -= JUMP
            self.state = MEGA_JUMP_1 
        elif self.state == FALLING:
            self.speedy -= JUMP
            self.state = MEGA_JUMP_2



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

        # Se já está na hora de  mudar de imagem...
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