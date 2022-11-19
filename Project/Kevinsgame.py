import pygame
import math
pygame.init()


area_width=900
area_height=600
window= pygame.display.set_mode((area_width,area_height))
clock =pygame.time.Clock()

board_surf = pygame.Surface((area_width, area_height))

run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        






pygame.quit()
exit()