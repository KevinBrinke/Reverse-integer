import pygame
import math
import time
from utils import scale_image,blit_rotate_center



WATER = scale_image(pygame.image.load("imgs/backgroundwater.png"), 1)
ICEBERG = scale_image(pygame.image.load("imgs/icebergisolated.png"), .85)
BOUNDARY = scale_image(pygame.image.load("imgs/barrier.png"), .85)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 1)
FINISH = scale_image(pygame.image.load("imgs/finish.png"), 1)

POLAR_BEAR = scale_image(pygame.image.load("imgs/character models/wolfbear.jpg"), .07)
CUTE_BEAR = scale_image(pygame.image.load("imgs/character models/cutebear.jpg"), .045)


WIDTHBACK, HEIGHTBACK= WATER.get_width(), WATER.get_height()
WIDTH, HEIGHT= BOUNDARY.get_width(), BOUNDARY.get_height()
print(WIDTH,HEIGHT,WIDTHBACK,HEIGHTBACK)
WINDOW = pygame.display.set_mode((WIDTHBACK, HEIGHTBACK))
pygame.display.set_caption("Polar Push")
#WIN= pygame.display.set_mode((WIDTH, HEIGHT))


FPS = 60


class AbstractBear:

    def __init__(self, max_vel,rotation_vel):
        self.img=self.IMG

        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 90
        self.x, self.y = self.START_POS

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x,self.y),self.angle)

class PlayerBear(AbstractBear):
    IMG = POLAR_BEAR
    START_POS = (400,450)

def draw(win,images, player_bear):
    for img, pos in images:
        win.blit(img, pos)

    player_bear.draw(win)
    pygame.display.update()




run = True
clock=pygame.time.Clock()
images=[(WATER,(0,0)), (ICEBERG,(213,200)),(BOUNDARY,(213,200))]

player_bear = PlayerBear(4,4)

#run window
while run:
    clock.tick(FPS)
    
    #draw animations
    draw(WINDOW, images, player_bear)
    
    # WINDOW.blit(WATER,(0,0))
    # WINDOW.blit(ICEBERG,(0,0))
    # WINDOW.blit(BOUNDARY,(0,0))
    # WINDOW.blit(POLAR_BEAR,(WIDTH/2-70,HEIGHT/2-110))
    # WINDOW.blit(CUTE_BEAR,(WIDTH/2+30,HEIGHT/2-110))

    
    


    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
            break

pygame.quit()