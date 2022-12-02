import pygame
from sys import exit
from utils import scale_image,blit_rotate_center
import math

def display_time():
    current_time =  int(pygame.time.get_ticks()/1000) - start_time
    time_left = 200- current_time
    time_surf = test_font.render(f'Time: {time_left}',False,(64,64,64))
    time_rect = time_surf.get_rect(center = (400,50))
    screen.blit(time_surf,time_rect)


pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Polar Push')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active= False
start_time = 0

sky_surf  =pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

water_surf = pygame.image.load("imgs/backgroundwater.png").convert()
x_,y_map=213,210
x_offset,y_offset = 155,145
iceberg_surf = scale_image(pygame.image.load("imgs/icebergisolated.png"), .85)
bounds_surf = scale_image(pygame.image.load("imgs/barrier.png"), .85)

invert_bear_surf = scale_image(pygame.image.load("imgs/invertbearpixel.png"), .5).convert_alpha()
invert_bear_rect = invert_bear_surf.get_rect(center= (500,380))
white_bear_surf = scale_image(pygame.image.load("imgs/regularbearpixel.png"), .5).convert_alpha()
white_bear_rect = white_bear_surf.get_rect(center= (700,380))


print(water_surf.get_width(),water_surf.get_height())
# name_surf = test_font.render('Polar Push', True, (64,64,64))
# name_rect = name_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(600,300))


player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,200,2)
player_stand_rect = player_stand.get_rect(center = (400,200))



class AbstractBear:

    def __init__(self, max_vel,rotation_vel):
        self.img = self.IMG
        self.bear_mask = self.BEAR_MASK
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = self.START_ANGLE
        self.x, self.y = self.START_POS
        self.acceleration= 0.2

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x,self.y),self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    
    #velocity player move
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        if self.vel >= 0 :
            self.vel = max(self.vel - self.acceleration / 2, 0)
            self.move()
        elif self.vel < 0 :
            self.vel = min(self.vel + self.acceleration / 2, 0)
            self.move()
    def ice_slide(self):
        print("not ready yet")
    
    def collide(self, mask, x= x_offset, y= y_offset):
       
        # bear2_mask = pygame.mask.from_surface(self.img)
        offset_boundary = (int(self.x - x), int(self.y - y ))
        poi = mask.overlap(self.bear_mask, offset_boundary)#point of interesction = poi 
        return poi


    def bumper1(self, mask):
        self.bear_mask
        poi_bears = self.bear_mask.overlap(mask,(2,0))
        return poi_bears
    def bumper2(self,mask):
        bear_mask = pygame.mask.from_surface(bear_mask)
    def hit(self,direction):
        self.x-=1
        self.y-=0
 

class PlayerBear(AbstractBear):
    IMG = invert_bear_surf
    START_POS = (320,475)
    START_ANGLE = 270
    BEAR_MASK = pygame.mask.from_surface(IMG)

    def bounce(self):
        self.vel = -self.vel
        self.move()

class PlayerBear2(AbstractBear):
    IMG = white_bear_surf
    START_POS = (650,475)
    START_ANGLE = 90
    BEAR_MASK = pygame.mask.from_surface(IMG)
    def bounce(self):
        self.vel = -self.vel
        self.move()

def draw(win,images, player1_bear, player2_bear):
    for img, pos in images:
        win.blit(img, pos)

    player1_bear.draw(win)
    player2_bear.draw(win)
    pygame.display.update()


def move_player(player1_bear,player2_bear):
    keys=pygame.key.get_pressed()

    #player1movemnet
    moved_player1 = False
    if keys[pygame.K_a]:
        player1_bear.rotate(left=True)
    if keys[pygame.K_d]:
        player1_bear.rotate(right=True)
    if keys[pygame.K_w]:
        moved_player1 = True
        player1_bear.move_forward()
    if keys[pygame.K_s]:
        moved_player1 = True
        player1_bear.move_backward()

    if not moved_player1:
        player1_bear.reduce_speed()


    #player2movement
    moved_player2 = False
    if keys[pygame.K_LEFT]:
        player2_bear.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player2_bear.rotate(right=True)
    if keys[pygame.K_UP]:
        moved_player2 = True
        player2_bear.move_forward()
    if keys[pygame.K_DOWN]:
        moved_player2 = True
        player2_bear.move_backward()

    if not moved_player2:
        player2_bear.reduce_speed()



run = True
clock=pygame.time.Clock()
images=[(water_surf, (0, 0)), (iceberg_surf, (x_, y_map)), (bounds_surf, (x_, y_map))]

player1_bear = PlayerBear(6,6)
player2_bear = PlayerBear2(6,6)

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
    #game active spawns characters and background should pause game hit button to start on countdown of 3
    #game_pause with counter everytime it pauses including start, with button p to start
    if game_active:       
        screen.blit(sky_surf,(0,0))
        pygame.draw.line(screen,'#ffffff', (0,0),(800,400),50)
        screen.blit(ground_surf,(0,300))
        #game background
        screen.blit(water_surf,(0,0))
        screen.blit(water_surf,(1024,0))
        screen.blit(iceberg_surf,(300,100))
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
        
        screen.blit(white_bear_surf, white_bear_rect)

        move_player(player1_bear,player2_bear)
        
        #collision
        if snail_rect.colliderect(player_rect): game_active = True
    else:
        screen.fill("#4400ee")
        screen.blit(player_stand,player_stand_rect)


    #draw all elements
    #update everything
    pygame.display.update()
    clock.tick(60)    