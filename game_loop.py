'''
Arquivo com a função principal do jogo
'''

import pygame
import random
from parameters import *
from sprites import *
from functions import *
from players import *

''' Função principal do jogo, gerencia sprites, grupos, 
eventos do jogo, vida dos personagens, pontuação e 
outros aspectos do game.'''
def game_screen(screen,assets,player_type):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Cria lista que será usada para verificar condições usadas para criar o segundo boss
    boss_die = [False, -1, False]

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]

    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Carrega jogadores
    players = load_players(assets)

    # Cria grupos
    all_sprites = pygame.sprite.Group() # Grupo de todos os sprites
    all_blocks = pygame.sprite.Group()
    all_cactos = pygame.sprite.Group()
    all_puke = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    all_hearts = pygame.sprite.Group()
    foreground = pygame.sprite.Group()

    # Cria dicionário para adicionar todos os grupos
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_blocks'] = all_blocks
    groups['all_cactos'] = all_cactos
    groups['all_puke'] = all_puke
    groups['all_bullets'] = all_bullets
    groups['all_hearts'] = all_hearts
    
    # Cria Sprite do jogador e adiciona ao grupo
    player = Player(assets, groups, players[player_type])
    groups['player'] = player
    all_sprites.add(player)
    foreground.add(player)

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

    # Cria bonus de vida espalhados em posições aleatórias do mapa
    for i in range(INITIAL_HEARTS):
        heart_x = random.randint(4000, 5000)
        heart_y = random.choice([400,300,200,100])
        heart = Hearts(assets, heart_x, heart_y, world_speed)
        
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(heart)
        all_hearts.add(heart)

    score = 0
    pygame.mixer.music.load(os.path.join(snd_dir, 'mario_music.ogg'))
    pygame.mixer.music.play()
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
                    assets[JUMP_SOUND].play()
                if event.key == pygame.K_d and score >= boss_appears:
                    player.shoot()
                    assets[PEW_SOUND].play()

        # Atualiza a ação de todos os sprites
        all_sprites.update()

        # Adiciona pontos ao score
        score += 5

        # Verifica se houve colisão entre jogador e puke
        collisions_player_puke = pygame.sprite.spritecollide(player, all_puke, True, pygame.sprite.collide_mask)
        if len(collisions_player_puke) > 0:
            player.health -= 20
            collisions_player_puke = 0
        
        # Verifica se houve colisão entre jogador e cacto
        hits = pygame.sprite.spritecollide(player, all_cactos, True,  pygame.sprite.collide_mask)
        if len(hits) > 0:
            player.health -= 50
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

        # Verifica colisao entre jogador e vida extra
        collisions_player_heart = pygame.sprite.spritecollide(player, all_hearts, True, pygame.sprite.collide_mask)
        if len(collisions_player_heart) > 0:
            if player.health < 80: # Adiciona vida ao jogador se tiver menos que 80 de vida
                player.health += 20
                assets[COINSOUND_SOUND].play()
            collisions_player_heart = 0
            heart.kill()
            heart_x = random.randint(4000, 5000)
            heart_y = random.choice([400,300,200,100])
            new_heart = Hearts(assets, heart_x, heart_y, world_speed)
                
            # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
            all_sprites.add(new_heart)
            all_hearts.add(new_heart)

        # Verifica vida do personagem
        if player.health <= 0:
            final_score = str(score)
            with open('txt/score.txt', 'w') as arquivo:
                arquivo.write(final_score)
            assets[DIE_SOUND].play()
            pygame.mixer.music.stop()
            assets[BACKINBLACK_SOUND].stop()
            se_fodeu_screen(screen,assets)

            # Acessa o high score
            with open('txt/high_score.txt', 'r') as file:
                X = file.read()
                high_score = int(X)
            
            # Confere se o high score foi batido e apenas altera ele caso tenha sido
            if score > high_score:
                high_score = score
                with open('txt/high_score.txt', 'w') as arquivo:
                    arquivo.write(str(high_score))
            return 'endgame'

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
                        if abs(cacto.rect.centerx - cacto_x) < 150:
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

        # Verifica se algum heart saiu da janela
        for heart in all_hearts:
            if heart.rect.right < 0:
                # Destrói o heart e cria um novo no final da tela
                heart.kill()
                heart_x = random.randint(4000, 5000)
                heart_y = random.choice([400,300,200,100])
                new_heart = Hearts(assets, heart_x, heart_y, world_speed)
                    
                # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
                all_sprites.add(new_heart)
                all_hearts.add(new_heart)

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
        foreground.draw(screen)
        all_hearts.draw(screen)

        # Cria barra de vida
        player.life(screen)

         # Adiciona o primeiro boss após um certo score
        if score == boss_appears:
            boss = Boss(groups, assets, 1)
            all_sprites.add(boss)
            foreground.add(boss)
            assets[BACKINBLACK_SOUND].play()
            pygame.mixer.music.set_volume(0)
            assets[BACKINBLACK_SOUND].set_volume(0.03)

        # Junto com o boss inicia o disparo de puke
        if score >= boss_appears and boss.health > 0:
            boss.puke()
            boss.life(screen)
            
            # Verifica colisão do boss e bullet
            collisions_boss_bullets = pygame.sprite.spritecollide(boss, all_bullets, True, pygame.sprite.collide_mask)
            if len(collisions_boss_bullets) > 0:
                boss.health -= 30

                # Verifica vida do segundo boss
                if boss_die[0] == True and boss.health <= 0:
                    boss_die = [True, score+5000, True]
                    boss.kill()
                    assets[BACKINBLACK_SOUND].stop()
                    pygame.mixer.music.set_volume(0.1)
                    # Quando mata o segundo boss libera o personagem coronita
                    with open('txt/win.txt', 'w') as arquivo:
                        arquivo.write('ganhou!')

                # Verifica vida do primeiro boss
                if boss.health <= 0 and boss_die[0] == False:
                    boss_die = [True, score+5000, False]
                    boss.kill()
                    assets[BACKINBLACK_SOUND].stop()
                    pygame.mixer.music.set_volume(0.1)
                collisions_boss_bullets = 0
        
        # Adiciona o segundo boss
        if boss_die[0] == True and boss_die[1] == score and boss_die[2] == False:
            boss = Boss(groups, assets, 2)
            all_sprites.add(boss)
            foreground.add(boss)
            assets[BACKINBLACK_SOUND].play()
            assets[BACKINBLACK_SOUND].set_volume(0.03)
            pygame.mixer.music.set_volume(0)
    
        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()