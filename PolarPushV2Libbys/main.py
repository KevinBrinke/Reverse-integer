import pygame
import math
import time
from utils import scale_image,blit_rotate_center
import sys



WATER = scale_image(pygame.image.load("graphics/backgroundwater.png"), 1)

#map coordinates pixels spawns
x_,y_map=213,210
x_offeset,y_offset = 155,145
ICEBERG = scale_image(pygame.image.load("graphics/icebergisolated.png"), .85)
BOUNDARY = scale_image(pygame.image.load("graphics/barrier.png"), .85)
BOUNDARY_BORDER = scale_image(pygame.image.load("graphics/barrier.png"), 1.02)
BOUNDARY_MASK = pygame.mask.from_surface(BOUNDARY_BORDER)



INVERT_BEAR = scale_image(pygame.image.load("graphics/invertbearpixel.png"), .5)
CUTE_BEAR = scale_image(pygame.image.load("graphics/regularbearpixel.png"), .5)
# INVERT_BEAR_MASK = pygame.mask.from_surface(INVERT_BEAR)
# CUTE_BEAR_MASK = pygame.mask.from_surface(CUTE_BEAR)


WIDTHBACK, HEIGHTBACK= WATER.get_width(), WATER.get_height()
WIDTH, HEIGHT= BOUNDARY.get_width(), BOUNDARY.get_height()
print(WIDTH,HEIGHT,WIDTHBACK,HEIGHTBACK,BOUNDARY_BORDER.get_width(),BOUNDARY_BORDER.get_height())
WINDOW = pygame.display.set_mode((WIDTHBACK, HEIGHTBACK))
pygame.display.set_caption("Polar Push")

FPS = 60

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
    
    def collide(self, mask, x= x_offeset, y= y_offset):
       
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
    IMG = INVERT_BEAR
    START_POS = (320,475)
    START_ANGLE = 270
    BEAR_MASK = pygame.mask.from_surface(IMG)

    def bounce(self):
        self.vel = -self.vel
        self.move()

class PlayerBear2(AbstractBear):
    IMG = CUTE_BEAR
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
images=[(WATER, (0, 0)), (ICEBERG, (x_, y_map)), (BOUNDARY, (x_, y_map))]

player1_bear = PlayerBear(6,6)
player2_bear = PlayerBear2(6,6)

#run window
while run:
    clock.tick(FPS)
    
#draw animations
    draw(WINDOW, images, player1_bear, player2_bear)
    
#any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    #keys player controls character
    keys=pygame.key.get_pressed()


    move_player(player1_bear,player2_bear)

    if player1_bear.collide (BOUNDARY_MASK) != None:
        player1_bear.bounce()
    if player2_bear.collide (BOUNDARY_MASK) != None:
        player2_bear.bounce()
    if player1_bear.bumper1(player2_bear.BEAR_MASK) != None:
        player2_bear.hit(1)



pygame.quit()