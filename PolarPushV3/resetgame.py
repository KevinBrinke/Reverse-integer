import pygame
import time
import math
from utils import scale_image, blit_rotate_center, blit_text_center, blit_text_top
pygame.init()
WIDTH,HEIGHT = 1200,800
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Polar Push')
center_map = (583,369)
#game running map images
water_surf = pygame.image.load('graphics/backgroundwater.png').convert()
iceberg_surf = scale_image(pygame.image.load('graphics/icebergisolated.png'),.8).convert_alpha()
boundary_surf = scale_image(pygame.image.load('graphics/barrier.png'),.8).convert_alpha()
boundary_invis_surf = scale_image(pygame.image.load('graphics/barriercircle.png'), .65).convert_alpha()#not drawn is invis
boundary_surf_mask= pygame.mask.from_surface(boundary_invis_surf)
x_bounds,y_bounds = 288,76
#drawn map images
map_images = [(water_surf,(0,0)),(water_surf,(1000,0)),(iceberg_surf,(300,100))]
#bear selection images
invert_bear_surf = scale_image(pygame.image.load('graphics/player/invertbearpixel.png'),.4).convert_alpha()
white_bear_surf = scale_image(pygame.image.load('graphics/player/regularbearpixel.png'),.4).convert_alpha()
front_hit_surf = pygame.image.load('graphics/hitboxfront.png').convert_alpha()
back_hit_surf = pygame.image.load('graphics/hitboxback.png').convert_alpha()


pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)
pixel_font_bigger = pygame.font.Font('font/Pixeltype.ttf', 90)
pixel_font_title = pygame.font.Font('font/Pixeltype.ttf', 140)
pixel_font_biggest = pygame.font.Font('font/Pixeltype.ttf', 200)

run = True
fps = 60
clock = pygame.time.Clock()

def draw_map(screen,map_terrain):
    for img,pos in map_terrain:
        screen.blit(img,pos)

while run == True:
    draw_map(screen,map_images)
    # draw_characters()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run =  False
            break

    move_bear_keys()