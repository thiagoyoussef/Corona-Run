'''
Arquivo com a função principal do jogo
'''

import pygame
import random
from parameters import *
from assets import *
from sprites import *
from functions import *

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
    all_bullets = pygame.sprite.Group()

    # Cria dicionário para adicionar todos os grupos
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_blocks'] = all_blocks
    groups['all_cactos'] = all_cactos
    groups['all_puke'] = all_puke
    groups['all_bullets'] = all_bullets

    # Cria Sprite do jogador e adiciona ao grupo
    player = Player(assets, groups)
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
        block_x = random.randint(400, WIDTH)
        block_y = random.choice([375, 275, 175, 75])
        block = Tile(assets, block_x, block_y, world_speed)
        all_sprites.add(block)
        all_blocks.add(block)

    score = 0
    PLAYING = 0
    DONE = 1
    state = PLAYING
    pygame.mixer.music.play()

    game_state = 'start'

  # Mostra a tela inicial
    if game_state == 'start':
        start_screen(screen)

    game_state = 'playing'

    # While principal
    while game_state == 'playing':

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_state = 'done'
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_RIGHT and score >= boss_appears:
                    player.shoot()

        # Atualiza a ação de todos os sprites
        all_sprites.update()

        # Adiciona pontos ao score
        score += 5

        # Verifica se houve colisão entre jogador e cacto
        hits = pygame.sprite.spritecollide(player, all_cactos, True)
        if len(hits) > 0:
            player.health -= 10
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
            if player.health <= 0:
                game_state = game_over_screen(screen, assets)

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
                
                # Verifica se tem uma distancia minima para adicionar novos blocos
                OK = False
                while not OK:
                    block_x = random.randint(WIDTH, int(WIDTH * 1.5))
                    block_y = random.choice([375, 275, 175, 75])
                    new_block = Tile(assets, block_x, block_y, world_speed)
                    OK = True
                    for block in all_blocks:
                        if abs(block.rect.centerx - block_x) < 100:
                            OK = False   
 
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

        # Cria barra de vida
        player.life(screen)

         # Adiciona o boss após um certo score
        if score == boss_appears:
            boss = Boss(groups, assets)
            all_sprites.add(boss)
        
        # Junto com o boss inicia o disparo de puke
        if score >= boss_appears:
            boss.puke()
            boss.life(screen)
            
            # Verifica colisão do boss e bullet
            collisions_boss_bullets = pygame.sprite.spritecollide(player, all_puke, True)
            if len(collisions_boss_bullets) > 0:
                boss.health -= 10
                if boss.health <= 0:
                    boss.kill()
                collisions_boss_bullets = 0
        
        # Verifica se houve colisão entre jogador e puke
        collisions_player_puke = pygame.sprite.spritecollide(player, all_puke, True, pygame.sprite.collide_mask)
        if len(collisions_player_puke) > 0:
            player.health -= 10
            collisions_player_puke = 0
        
        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()