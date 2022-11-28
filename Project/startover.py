import pygame
import math
import time
from utils import scale_image,blit_rotate_center
import sys



WATER = scale_image(pygame.image.load("imgs/backgroundwater.png"), 1)

#map coordinates pixels spawns
x_,y_map=213,210
x_offeset,y_offset = 155,145
ICEBERG = scale_image(pygame.image.load("imgs/icebergisolated.png"), .85)
BOUNDARY = scale_image(pygame.image.load("imgs/barrier.png"), .85)
BOUNDARY_BORDER = scale_image(pygame.image.load("imgs/barrier.png"), 1.02)
BOUNDARY_MASK = pygame.mask.from_surface(BOUNDARY_BORDER)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 1)
FINISH = scale_image(pygame.image.load("imgs/finish.png"), 1)

INVERT_BEAR = scale_image(pygame.image.load("imgs/invertbearpixel.png"), .5)
REGULAR_BEAR = scale_image(pygame.image.load("imgs/regularbearpixel.png"), .5)
INVERT_BEAR_MASK = pygame.mask.from_surface(INVERT_BEAR)
REGULAR_BEAR_MASK = pygame.mask.from_surface(REGULAR_BEAR)


WIDTHBACK, HEIGHTBACK= WATER.get_width(), WATER.get_height()
WIDTH, HEIGHT= BOUNDARY.get_width(), BOUNDARY.get_height()
#print(WIDTH,HEIGHT,WIDTHBACK,HEIGHTBACK,BOUNDARY_BORDER.get_width(),BOUNDARY_BORDER.get_height())
WINDOW = pygame.display.set_mode((WIDTHBACK, HEIGHTBACK))
pygame.display.set_caption("Polar Push")

FPS = 60



class AbstractBear:

    def __init__(self, max_vel,rotation_vel):
        self.img = self.IMG
        self.bear_mask = pygame.mask.from_surface(self.img)
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
        offset_boundary = (int(self.x - x), int(self.y - y ))
        poi = mask.overlap(self.bear_mask, offset_boundary)#point of interesction = poi 
        return poi

    def hit_other(self,mask):
        
        
        poi= mask.overlap()


    def hit(self,direction):
        self.x-=3
        self.y-=0
 
class Square(AbstractBear):
    IMG = REGULAR_BEAR
    START_POS = (400,475)
    START_ANGLE = 0
    pygame.mask.from_surface(IMG)

class Player(AbstractBear):
    IMG = INVERT_BEAR
    START_POS = (320,475)
    START_ANGLE = 270
    BEAR_MASK = pygame.mask.from_surface(IMG)

    # def start_angle(self):
    #     if player_num is 1:
    #         START_ANGLE=270
    #     if player_num is 2:
    #         START_ANGLE= 90

    def bounce(self):
        self.vel = -self.vel
        self.move()



def draw(win,images, player_one, player_two):
    for img, pos in images:
        win.blit(img, pos)

    player_two.draw(win)
    player_one.draw(win)

    pygame.display.update()


def move_player(player_one):
    keys=pygame.key.get_pressed()

    #player1movemnet
    moved_player1 = False
    if keys[pygame.K_a]:
        player_one.rotate(left=True)
    if keys[pygame.K_d]:
        player_one.rotate(right=True)
    if keys[pygame.K_w]:
        moved_player1 = True
        player_one.move_forward()
    if keys[pygame.K_s]:
        moved_player1 = True
        player_one.move_backward()

    if not moved_player1:
        player_one.reduce_speed()






run = True
clock=pygame.time.Clock()
images=[(WATER, (0, 0)), (ICEBERG, (x_, y_map)), (BOUNDARY, (x_, y_map))]

player_one = Player(4,4)
player_two = Square(0,0)


#run window
while run:
    clock.tick(FPS)
    
#draw animations
    draw(WINDOW, images, player_one, player_two)
    
#any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    #keys player controls character
    keys=pygame.key.get_pressed()


    move_player(player_one)

    if player_one.collide (BOUNDARY_MASK) != None:
        player_one.bounce()
    if player_one.hit_other(INVERT_BEAR_MASK):
        player_two.hit()




pygame.quit()