import pygame
from sys import exit

def display_time():
    current_time =  int(pygame.time.get_ticks()/1000) - start_time
    time_left = 200- current_time
    time_surf = test_font.render(f'Time: {time_left}',False,(64,64,64))
    time_rect = time_surf.get_rect(center = (400,50))
    screen.blit(time_surf,time_rect)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Polar Push')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active= False
start_time = 0

sky_surf  =pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# name_surf = test_font.render('Polar Push', True, (64,64,64))
# name_rect = name_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(600,300))
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:       
        screen.blit(sky_surf,(0,0))
        pygame.draw.line(screen,'#ffffff', (0,0),(800,400),50)
        screen.blit(ground_surf,(0,300))
        #time background
        pygame.draw.rect(screen,'Black', pygame.Rect(286,21,228,48))
        pygame.draw.rect(screen,'#00e8ec', pygame.Rect(290,25,220,40))
        display_time()
        # screen.blit(name_surf,name_rect)

        snail_rect.x -= 6
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)
        
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        #collision
        if snail_rect.colliderect(player_rect): game_active = False

    else:
        screen.fill('blue')


    #draw all elements
    #update everything
    pygame.display.update()
    clock.tick(60)    








    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")
