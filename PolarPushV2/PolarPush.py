import pygame
import time
import math
from random import randint, choice
from utils import scale_image, blit_rotate_center
#pygame screen
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Polar Push')


#pygame variables
run = True
fps = 60
clock = pygame.time.Clock()
#game states
game_active = True
game_pause =  False
game_end = False
game_button_end = False
game_time_start = 200
game_time_restart = 0
game_start_button = False
game_round_button_start = False
game_round_count = 1


test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
def display_time_left():
    current_time =  int(pygame.time.get_ticks()/1000) - game_time_restart
    time_left = 200- current_time
    time_left_surf = test_font.render(f'Time: {time_left}',False,(64,64,64))
    time_left_rect = time_left_surf.get_rect(center = (400,50))
    screen.blit(time_left_surf,time_left_rect)


#game running map images
water_surf = pygame.image.load('graphics/backgroundwater.png').convert()
iceberg_surf = scale_image(pygame.image.load('graphics/icebergisolated.png'),.8).convert_alpha()
boundary_surf = scale_image(pygame.image.load('graphics/barrier.png'),.8).convert_alpha()
invis_surf = scale_image(boundary_surf, 1.2)#not drawn is invis
#needs mask of invis surf or in general a circle'd line bigger than the image slightly
boundary_surf_mask= pygame.mask.from_surface(boundary_surf)
x_bounds,y_bounds = 300,100
#drawn map images
map_images = [(water_surf,(0,0)),(water_surf,(1000,0)),(iceberg_surf,(300,100)),(boundary_surf,(300,100))]
#bear selection images
invert_bear_surf = scale_image(pygame.image.load('graphics/player/invertbearpixel.png'),.4).convert_alpha()
white_bear_surf = scale_image(pygame.image.load('graphics/player/regularbearpixel.png'),.4).convert_alpha()
#round images
#game start images
#game end images
#game pause images

#classes for bear characters
class BearPhysics:
    def __init__(self,max_vel, rot_vel, start_coordinates, start_angle):
        #initialized
        self.max_vel = max_vel
        self.rotation_vel = rot_vel
        #dependents
        self.x, self.y = start_coordinates
        self.angle = start_angle
        self.vel = 0
        #constants
        self.acceleration = 0.3
        



    #physics
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

    #button commands
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
   
    #animation
    def draw(self, screen):
        blit_rotate_center(screen, self.bear_img, (self.x,self.y),self.angle)
    


class PlayerBear(BearPhysics):
    def __init__(self, max_vel, rot_vel, bear_choice, player_number,start_coordinates,start_angle):
        super().__init__(max_vel, rot_vel, start_coordinates,start_angle)
        self.bear_choice = bear_choice
        self.player_number = player_number
        self.bear_mask = None
        

    def get_player_number(self):
        return self.player_number
    def choose_bear(self):
        if self.bear_choice == 1:
            self.bear_img = invert_bear_surf     
        if self.bear_choice == 2:
            self.bear_img = white_bear_surf
        self.bear_mask = pygame.mask.from_surface(self.bear_img)

    def collide(self, mask, x_bounds, y_bounds):
        boundary= (int(self.x - x_bounds), int(self.y - y_bounds ))
        poi = mask.overlap(self.bear_mask, boundary)
        return poi #point of intersection
    
    def bounce_to_center(self):
        bounce_center_vel = 0
        bounce_center_vel -= self.vel#turn tangent tangent to all center and bounce
        
        self.reduce_speed()
    def bounce(self):
        print("bounce")

#player objects
player_one = PlayerBear(4,6,1,1,(466,350),270)
player_two = PlayerBear(4,6,2,2,(650,350),90)

def move_bear_keys(p_one,p_two):
    keys = pygame.key.get_pressed()
    #player one basic movement
    move_key_pressed_p_one = False
    if keys[pygame.K_a]:
        p_one.rotate(left=True)
    if keys[pygame.K_d]:
        p_one.rotate(right=True)
    if keys[pygame.K_w]:
        move_key_pressed_p_one = True
        p_one.move_forward()
    if keys[pygame.K_s]:
        move_key_pressed_p_one = True
        p_one.move_backward()
    #deaccelerate if keys s or w are not pressed
    if not move_key_pressed_p_one:
        p_one.reduce_speed()
    
    #player two basic movement
    move_key_pressed_p_two = False
    if keys[pygame.K_LEFT]:
        p_two.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        p_two.rotate(right=True)
    if keys[pygame.K_UP]:
        move_key_pressed_p_two = True
        p_two.move_forward()
    if keys[pygame.K_DOWN]:
        move_key_pressed_p_two = True
        p_two.move_backward()
    #deaccelerate if keys up or down are not pressed
    if not move_key_pressed_p_two:
        p_two.reduce_speed()

# class Player(PlayerBear):
def draw(screen,map_images,player_one,player_two):
    for img, pos in map_images:
        screen.blit(img,pos)
    player_one.draw(screen)
    player_two.draw(screen)
    
while run == True:
    player_one.choose_bear()
    player_two.choose_bear()
    draw(screen,map_images,player_one,player_two)
            # if event.type == pygame.KEYDOWN:
            #     if event.type ==pygame.K_m:
            #         game_active=False
    move_bear_keys(player_one, player_two)
     
    pygame.draw.rect(screen,'Black', pygame.Rect(286,21,228,48))
    pygame.draw.rect(screen,'#00e8ec', pygame.Rect(290,25,220,40))
    display_time_left()
    if player_one.collide(boundary_surf_mask,x_bounds,y_bounds) !=None:
                player_one.bounce_to_center()
    if player_two.collide(boundary_surf_mask,x_bounds,y_bounds) !=None:
                player_two.bounce_to_center()
    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            pygame.quit 
            exit()
        if game_active:
            a=0
            #player controls-forward/back/left/right
            #others soon


            
  

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                game_time_restart = int(pygame.time.get_ticks() / 1000)
        
    clock.tick(fps)
    pygame.display.update()
        # screen.blit(name_surf,name_rect)
                
