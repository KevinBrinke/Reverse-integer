import pygame
import time
import math
from utils import scale_image, blit_rotate_center, blit_text_center, blit_text_top
#pygame screen
pygame.font.init()
WIDTH,HEIGHT = 1200,800
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Polar Push')
center_map = (583,369)


#pygame variables
run = True
fps = 60
clock = pygame.time.Clock()
#game states
# game_active = True
# game_pause =  False
# game_round_end = False
# game_end = False
# game_button_end = False
# game_time_start = 1000
# game_time_restart = 0
# game_start_button = False
# game_round_button_start = False
# game_round_count = 0

pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)
pixel_font_bigger = pygame.font.Font('font/Pixeltype.ttf', 90)
pixel_font_title = pygame.font.Font('font/Pixeltype.ttf', 140)
pixel_font_biggest = pygame.font.Font('font/Pixeltype.ttf', 200)

# def display_time_left():
#     current_time =  int(pygame.time.get_ticks()/1000) - game_time_restart
#     time_left = game_time_start - current_time
#     time_left_surf = test_font.render(f'Time: {time_left}',False,(64,64,64))
#     time_left_rect = time_left_surf.get_rect(center = (400,50))
#     screen.blit(time_left_surf,time_left_rect)
#     if time_left <= 0:
#         return False
# def pause():
#     if game_pause == True:
#         return False
#     else:
#         return True


class GameInfo:
    round = 5
    
    def __init__(self,round=1):
        self.round = round 
        self.started = False
        self.round_start_time = 60
        

        
        
    def next_round(self):
        self.round +=1
        self.start = False
    def reset(self):
        self.round = 1
        self.started =  False
        self.round_start_time = 30
    def game_finished(self):
        return self.round>self.roundS
    def start_round(self):
        self.started =True
        self.total_window_run_time = int(pygame.time.get_ticks()/1000)
    def get_round_time(self):
        if not self.started:
            return self.round_start_time
        self.round_time_left = self.round_start_time + self.total_window_run_time - int(pygame.time.get_ticks()/1000)
        return self.round_time_left
        
# def pause():
#     if game_pause == True:
#         return False
#     else:
#         return True

#
#
# 
# 
# 
#game running map images
water_surf = pygame.image.load('graphics/backgroundwater.png').convert()
iceberg_surf = scale_image(pygame.image.load('graphics/icebergisolated.png'),.8).convert_alpha()
boundary_surf = scale_image(pygame.image.load('graphics/barrier.png'),.8).convert_alpha()
boundary_invis_surf = scale_image(pygame.image.load('graphics/barriercircle.png'), .65).convert_alpha()#not drawn is invis
#needs mask of invis surf or in general a circle'd line bigger than the image slightly

boundary_surf_mask= pygame.mask.from_surface(boundary_invis_surf)
x_bounds,y_bounds = 288,76
#drawn map images
map_images = [(water_surf,(0,0)),(water_surf,(1000,0)),(iceberg_surf,(300,100))]
#bear selection images
invert_bear_surf = scale_image(pygame.image.load('graphics/player/invertbearpixel.png'),.4).convert_alpha()
white_bear_surf = scale_image(pygame.image.load('graphics/player/regularbearpixel.png'),.4).convert_alpha()
#round images
#game start images
#game end images
#game pause images
# 
# 
# 
# 
# 

#classes for bear characters
class BearPhysics:
    def __init__(self,max_vel, rot_vel, start_coordinates, start_angle):
        #initialized
        self.max_vel = max_vel
        self.rotation_vel = rot_vel
        #dependents
        self.start_pos = start_coordinates
        self.start_angle = start_angle
        self.x, self.y = start_coordinates
        self.angle = start_angle
        self.vel = 0
        #constants
        self.acceleration = 0.3
        self.bounce_center_vel = 0
        



    #physics
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        if self.bounce_center_vel == 0: 
            self.y -= vertical
            self.x -= horizontal
    def bounce_center_move(self):
        radians = math.radians(85)#self.sprite_angle(walls)j;
        vertical = math.cos(radians) * self.bounce_center_vel
        horizontal = math.sin(radians) * self.bounce_center_vel
        
        
        self.y -= vertical
        self.x -= horizontal

    def fall_off(self):
        print("fall off")
        player_one.reset()
        player_two.reset()
        # game_active == False 

    
    def reduce_speed(self):
        if self.vel >= 0 :
            self.vel = max(self.vel - self.acceleration / 5, 0)
            self.move()
        if self.vel < 0 :
            self.vel = min(self.vel + self.acceleration / 5, 0)
            self.move()
        if self.bounce_center_vel >= 0 :
            self.bounce_center_vel = max(self.bounce_center_vel - self.acceleration / 2, 0)
            if self.bounce_center_vel > 0 :
                self.bounce_center_move()
            else:
                self.bounce_center_vel = 0
       

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
    
   
   #triggers
    def collide_fall(self, mask, x_bounds, y_bounds):
        boundary_offset= (int(self.x - x_bounds), int(self.y - y_bounds ))
        poi = mask.overlap(self.bear_mask, boundary_offset)
        return poi #point of intersection
    def collide_wall(self):
        print("collide wall")#sprite walls
    
    def collide_other_bear(self):
        print("collide with bear")
    
    
    #collision physics
    def bounce_to_center_trigger(self):
        self.bounce_center_vel = 8        #turn tangent tangent to all center and bounce    
        self.reduce_speed()
    def bounce_trigger(self):
        print("bounce")

    def reset(self):
        self.x,self.y = self.start_pos
        self.angle = self.start_angle
        self.vel = 0


class PlayerBear(BearPhysics):
    def __init__(self, max_vel, rot_vel, bear_choice, player_number,start_coordinates,start_angle):
        super().__init__(max_vel, rot_vel, start_coordinates,start_angle)
        self.bear_choice = bear_choice
        self.player_number = player_number
        self.bear_mask = None
        self.score = 0
        
        

    def get_player_number(self):
        return self.player_number
    def choose_bear(self):
        if self.bear_choice == 1:
            self.bear_img = invert_bear_surf     
        elif self.bear_choice == 2:
            self.bear_img = white_bear_surf
        self.bear_mask = pygame.mask.from_surface(self.bear_img)
    def get_bear(self):
        return self.bear_img
    def set_score(self):
        self.score += 1
    def get_score(self):
        return self.score

#player objects
player_one = PlayerBear(5,5,1,1,(466,350),270)
player_two = PlayerBear(5,5,2,2,(650,350),90)
game_info = GameInfo()



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




# def other_keys(game_active):
#     keys_other = pygame.key.get_pressed()
#     while game_active == True:
        
#         



def draw(screen,map_images,player_one,player_two,game_info):
    for img, pos in map_images:
        screen.blit(img,pos)
    #score board
    pygame.draw.rect(screen,'#55aaff', pygame.Rect(8,526,314,260))#background
    pygame.draw.rect(screen,'#eeffff', pygame.Rect(14,532,302,248))#top half
    pygame.draw.rect(screen,'#3344dd', pygame.Rect(14,590,302,190))#bottom half

    pygame.draw.line(screen,"#000000",(14,590),(316,590),6)
    game_name_text = pixel_font_bigger.render(f"Polar Push",0,"#55aaff")
    screen.blit(game_name_text,(20,HEIGHT - game_name_text.get_height() - 200))
    score_side_text = pixel_font.render(f"Score",0,"#ddaaff")
    screen.blit(score_side_text,(115,HEIGHT - score_side_text.get_height() - 160))
    score_vs_text = pixel_font_bigger.render(f"{player_one.get_score()}  to  {player_two.get_score()}",0,"#ddaaff")
    
    screen.blit(score_vs_text,(80,HEIGHT - score_vs_text.get_height() - 80))
    pygame.draw.rect(screen,'Black', pygame.Rect(280,21,628,48))
    pygame.draw.rect(screen,'#00e8ec', pygame.Rect(284,25,620,40))
    blit_text_top(screen,pixel_font,f"Time = {game_info.get_round_time()}                         round:  {game_info.round}")

    screen.blit(player_one.get_bear(),(20,663))
    screen.blit(player_two.get_bear(),(250,663))

    player_one.draw(screen)
    player_two.draw(screen)
    pygame.display.update()



player_one.choose_bear()
player_two.choose_bear()





pygame.init()



while run == True:



    clock.tick(fps)
    draw(screen,map_images,player_one,player_two,game_info)
    while not game_info.started:
        pygame.draw.rect(screen,'Black', pygame.Rect(280,21,628,48))
        pygame.draw.rect(screen,'#00e8ec', pygame.Rect(284,25,620,40))
        blit_text_top(screen,pixel_font,f"Press any key to start round:  {game_info.round}")
        game_info.get_round_time()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                game_info.start_round()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run =  False
            break
        
    # pygame.draw.circle(screen, "red",(583,369),263,1) #red circle


    #player controls-forward/back/left/right
    move_bear_keys(player_one, player_two)
    
    player_one_fall = player_one.collide_fall(boundary_surf_mask,x_bounds,y_bounds)
    if player_one_fall != None:
        print(player_one_fall)
        player_two.set_score()
        player_one.fall_off()

    player_two_fall = player_two.collide_fall(boundary_surf_mask,x_bounds,y_bounds)

    if player_two_fall!= None:
        player_one.set_score() 
        player_two.fall_off()
        
    


            

        
        # game end scenarios
        # display_time_left()
        # if display_time_left() is False:
        #     game_dead = False
        #     print(game_dead)


        
           
                
        
    
                
pygame.quit()
exit()




# if game_active:
#             if event.type ==pygame.K_m:
#                 game_active=False       
#         elif game_active == False:
#             if event.type ==pygame.K_p:
#                 game_active=True
# game_time_restart = int(pygame.time.get_ticks() / 1000)


#///
        # screen.blit(name_surf,name_rect)

#...
