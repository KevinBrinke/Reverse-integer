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
    
    
    def __init__(self,round=1):
        self.round = round 
        self.started = False
        self.round_start_time = 60
        self.score_total = 0
        self.max_rounds = 5
        self.game_end = False
        
        
    # def next_round(self):
    #     self.round +=1
    #     self.start = False
    def reset_game_to_round_start(self):
        self.round += 1
        self.started =  False
        if player_one.get_score() > self.score_total/2:
            player_one.increase_score()
        elif player_one.get_score() < self.score_total/2:
            player_two.increase_score()
        else:
            self.round -= 1
        if self.round > self.max_rounds:
            self.game_finished()

        self.score_total = 0
        player_one.reset()
        player_two.reset()
        player_one.reset_score()
        player_two.reset_score()
        
    
    # def plus_game_win(self):

    def game_finished(self):
        return self.game_end == True
    def start_round(self):
        self.started =True
        self.total_window_run_time = int(pygame.time.get_ticks()/1000)
    def get_round_time(self):
        if not self.started:
            return self.round_start_time
        self.round_time_left = self.round_start_time + self.total_window_run_time - int(pygame.time.get_ticks()/1000)
        # if not self.round_time_left<=0:
        return self.round_time_left
        # game_info.reset_game_to_round_start()
    # def start_round_countdown(self):
    #     self.count_started = True
    #     self.total_window_run_time = int(pygame.time.get_ticks()/1000)

    # def get_round_countdown(self):
        
    #     if not self.count_started:
    #         return self.countdown_start_time
    #     self.count_down_action = self.countdown_start_time + self.total_window_run_time - int(pygame.time.get_ticks()/2000)

    #     return self.count_down_action
    # def round_end(self):
        
            
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
front_hit_surf = pygame.image.load('graphics/hitboxfront.png').convert_alpha()
back_hit_surf = pygame.image.load('graphics/hitboxback.png').convert_alpha()
boundary_surf_mask= pygame.mask.from_surface(boundary_invis_surf)
x_bounds,y_bounds = 288,76
#drawn map images
map_images = [(water_surf,(0,0)),(water_surf,(1000,0)),(iceberg_surf,(300,100))]
#bear selection images
invert_bear_surf = scale_image(pygame.image.load('graphics/player/invertbearpixel.png'),.4).convert_alpha()
white_bear_surf = scale_image(pygame.image.load('graphics/player/regularbearpixel.png'),.4).convert_alpha()

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
        self.vel_bounce = 0
        self.bounce_acceleration = .1
        self.bounce_direction = 0
        



    #physics
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        if self.vel_bounce  >-1: 
            self.y -= vertical
            self.x -= horizontal
    def bounce_center_move(self):
        radians = math.radians(85)#self.sprite_angle(walls)j;
        vertical = math.cos(radians) * self.bounce_center_vel
        horizontal = math.sin(radians) * self.bounce_center_vel
        
        
        self.y -= vertical
        self.x -= horizontal
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_angle(self):
        return self.angle
    def fall_off(self):
        
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
        # if self.vel_bounce < 0 :
        #     self.vel_bounce = min((self.vel_bounce + self.bounce_acceleration/3 , 0))
        #     self.bounce_move()
        # if self.vel_bounce > 0 :
        #     self.vel_bounce = max((self.vel_bounce - self.bounce_acceleration/3 , 0))
        #     self.bounce_move()
        
            
        # if self.bounce_center_vel >= 0 :
        #     self.bounce_center_vel = max(self.bounce_center_vel - self.acceleration / 2, 0)
        #     if self.bounce_center_vel > 0 :
        #         self.bounce_center_move()
        #     else:
        #         self.bounce_center_vel = 0
       

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
        if self.angle <0: self.angle = 359
        if self.angle>360: self.angle = 1
    #animation
    def draw(self, screen):
        self.bear_mask = pygame.mask.from_surface(blit_rotate_center(screen, self.bear_img, (self.x,self.y),self.angle))

    
   
   #triggers
    def collide_fall(self, mask, x_bounds, y_bounds):
        boundary_offset= (int(self.x - x_bounds), int(self.y - y_bounds ))
        poi = mask.overlap(self.bear_mask, boundary_offset)
        return poi #point of intersection
    

    def collide_other_bear(self, mask, x_bounds, y_bounds):
        offset= (int(self.x - x_bounds ), int(self.y - y_bounds ))
        poi = self.bear_mask.overlap(mask, offset)
        return poi #point of intersection
    


    def collide_wall(self):
        print("collide wall")#sprite walls
    
    
    
    # def attack(self):
    #     extra_x,extra_y= 0,0
    #     radians = math.radians(self.angle)
    #     width = 30*math.cos(radians) #+ 14* math.cos(radians)
    #     height = 30*math.sin(radians) #+ 14*math.sin(radians)
    #     if height< 0:
    #         height *= -1

    #     if width <0:
    #         width *= (-1)
    #     if self.angle>=45 and self.angle < 135: extra_x = 9*math.sin(radians)
    #     if self.angle>=135 and self.angle < 225: 
    #         extra_y = -15*math.cos(radians)
    #         if height< 0 :
    #             height *= -1
    #         height+=10
    #     if self.angle>=225 and self.angle < 315: extra_x = -12*math.sin(radians)
    #     if self.angle>=315 and self.angle < 45: extra_y = 9*math.cos(radians)
    #     width +=4
        
        

    #     height +=4 
    #     print(height)
    #     front_displacement_x = math.sin(radians)* (-20)+3*math.sin(radians)
    #     front_displacement_y =  math.cos(radians)*(-20)+3*math.cos(radians) 
    #     attacking_rect = pygame.Rect(self.x+front_displacement_x+extra_x+12,self.y+extra_y+8+front_displacement_y,width,height)
    #     self.got_hit_rect = pygame.Rect(self.x+17,self.y+12,20,20)
    #     self.hit_box=pygame.draw.rect(self.screen, "#990099", attacking_rect)
    #     self.hit_back=pygame.draw.rect(self.screen, "#990099", self.got_hit_rect)
    #     if self.player_number ==1:
    #         if attacking_rect.colliderect(player_two.get_target()):
    #             print("hit 1")
    #     if self.player_number == 2:
    #         if attacking_rect.colliderect(player_one.get_target()):
    #             print("hit 2")


    #     # if self.bear_mask.overlap(attacking_rect_mask,(self.x+front_displacement_x+extra_x+12,self.y+extra_y+4+front_displacement_y))!= None:
    #     #     print("hit")
    #     pygame.display.update()
    # def set_target(self,target):w
    #     self.target = target
    # def get_target(self):
    #     return self.got_hit_rect
    #collision physics
    def bounce_to_center_trigger(self):
        self.bounce_center_vel = 8        #turn tangent tangent to all center and bounce    
        self.reduce_speed()
    def bounce_trigger(self,other_bear_info):
        self.other_x = other_bear_info[0]
        self.other_y = other_bear_info[1]
        self.other_angle = other_bear_info[2]
        # print(self.other_x,self.other_y,self.other_angle, self.player_number)
        abs_value_x = abs(self.x - self.other_x)
        abs_value_y = abs(self.y - self.other_y)
        if abs_value_x < abs_value_y:
            # print("up or down")
            if self.y > self.other_y:
                # print("down")
                self.bounce_direction = 0 #hits the other down
            if self.y < self.other_y:
                # print("hitting the others up")
                self.bounce_direction = 2 #hits the other up
        if abs_value_x > abs_value_y:
            # print("left or right")
            if self.x>self.other_x:
                # print("im on the left")
                self.bounce_direction = 3 #hits the other right
            if self.x< self.other_x:
                # print("im on the right") 
                self.bounce_direction = 1 #hits the other left
        total_angle = 360
        angle_diff = abs(abs(self.angle - self.other_angle ) -180)
        print(angle_diff,self.angle,self.other_angle)
        if angle_diff  >60:
            self.bounce()
        else:
            self.negate()

    def bounce(self):
        if self.bounce_direction ==0:
            if self.other_angle >145 and self.other_angle < 215:
                self.vel_bounce = 4
                # self.bounce_move()
        if self.bounce_direction ==2:
            if self.other_angle <80 and self.other_angle > 290:
                self.vel_bounce = 4
                # self.bounce_move()
        if self.bounce_direction ==3:
            if self.other_angle >100 and self.other_angle < 170:
                self.vel_bounce = 4
                # self.bounce_move()
        if self.bounce_direction ==1:
            if self.other_angle <280 and self.other_angle > 190:
                self.vel_bounce = 4
                # self.bounce_move()
        
                # print("hit down")    
    # def bounce_move(self):
    #     other_radians = math.radians(self.other_angle)
    #     self.horizontal_bounce = math.sin(other_radians)*self.vel_bounce
    #     self.vertical_bounce =  math.cos(other_radians)*self.vel_bounce
    #     self.x +=self.horizontal_bounce
    #     self.y +=self.vertical_bounce
    #     print(self.horizontal_bounce,self.vertical_bounce,self.bounce_direction)
    #     player_two.negate()
    #     player_one.negate()


    def negate(self):
        other_radians = math.radians(self.other_angle)
        self.vel_bounce = 3
        self.vel_bounce = max(self.vel_bounce -1 - self.bounce_acceleration , 0)
        self.horizontal_bounce = math.sin(other_radians)*self.vel_bounce
        self.vertical_bounce =  math.cos(other_radians)*self.vel_bounce
        self.x -= self.horizontal_bounce
        self.y -= self.vertical_bounce

    def reset(self):
        self.x,self.y = self.start_pos
        self.angle = self.start_angle
        self.vel = 0
        self.vel_bounce = 0
       


class PlayerBear(BearPhysics):
    def __init__(self, max_vel, rot_vel, bear_choice, player_number,start_coordinates,start_angle,screen):
        super().__init__(max_vel, rot_vel, start_coordinates,start_angle)
        self.bear_choice = bear_choice
        self.player_number = player_number
        self.bear_mask = None
        self.score = 0
        self.round_wins = 0
        self.screen = screen
        
        

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
        game_info.score_total += 1
    def reset_score(self):
        self.score = 0
    def get_score(self):
        return self.score
    def increase_score(self):
        self.round_wins += 1
    def get_wins(self):
        return self.round_wins

#player objects
player_one = PlayerBear(5,5,1,1,(466,350),270,screen)
player_two = PlayerBear(5,5,2,2,(650,350),90,screen)
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
    pygame.draw.line(screen,"#000000",(14,590),(315,590),6)
    pygame.draw.line(screen,"#66aaee",(100,622),(220,622),3)
    pygame.draw.line(screen,"#aaaaee",(40,700),(280,700),3)

    

    game_name_text = pixel_font_bigger.render(f"Polar Push",0,"#55aaff")
    screen.blit(game_name_text,(20,HEIGHT - game_name_text.get_height() - 200))
    score_side_text = pixel_font.render(f"Score",0,"#ddaaff")
    screen.blit(score_side_text,(115,HEIGHT - score_side_text.get_height() - 170))
    score_vs_text = pixel_font_bigger.render(f"{player_one.get_score()}  to  {player_two.get_score()}",0,"#ddaaff")
    screen.blit(score_vs_text,(80,HEIGHT - score_vs_text.get_height() - 100))
    score_round_text = pixel_font.render(f"{player_one.get_wins()}     to     {player_two.get_wins()}",0,"#ddaaff")
    screen.blit(score_round_text,(100,HEIGHT-score_round_text.get_height() -30))
    score_round_text = pixel_font.render(f"wins",0,"#9955bb")
    screen.blit(score_round_text,(130,HEIGHT-score_round_text.get_height() -60))
    pygame.draw.rect(screen,'#000000', pygame.Rect(280,21,628,48))
    pygame.draw.rect(screen,'#00e8ec', pygame.Rect(284,25,620,40))
    blit_text_top(screen,pixel_font,f"Time = {game_info.get_round_time()}                         round:  {game_info.round}")

    screen.blit(player_one.get_bear(),(20,643))
    screen.blit(player_two.get_bear(),(250,643))

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
        pygame.draw.rect(screen,'#000000', pygame.Rect(280,21,628,48))
        pygame.draw.rect(screen,'#00e8ec', pygame.Rect(284,25,620,40))
        blit_text_top(screen,pixel_font,f"Press any key to start round:  {game_info.round}")
        # blit_text_center(screen,pixel_font_bigger,f"{game_info.get_round_countdown}")
        while game_info.game_finished():
            screen.fill('#4499ee')
            score_round_text = pixel_font.render(f"{player_one.get_wins()}     to     {player_two.get_wins()}",0,"#ddaaff")
            screen.blit(score_round_text,(100,HEIGHT-score_round_text.get_height() -30))
            score_round_text = pixel_font.render(f"wins",0,"#9955bb")
            screen.blit(score_round_text,(130,HEIGHT-score_round_text.get_height() -60))
            pygame.display.update()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                pygame.time.wait(100)
                pygame.draw.rect(screen,'#000000', pygame.Rect(545,335,80,80))                
                pygame.draw.rect(screen,'#00e8ec', pygame.Rect(550,340,70,70))
                # screen.blit(iceberg_surf,(300,100))
                countdown_3 = pixel_font_title.render(f"3",0,"#9955bb")
                screen.blit(countdown_3,(563,345))
                pygame.display.update()
                pygame.time.wait(1000)
                pygame.draw.rect(screen,'#000000', pygame.Rect(545,335,80,80))                
                pygame.draw.rect(screen,'#00e8ec', pygame.Rect(550,340,70,70))
                # screen.blit(iceberg_surf,(300,100))
                countdown_2 = pixel_font_title.render(f"2",0,"#9955bb")
                screen.blit(countdown_2,(563,345))
                pygame.display.update()
                pygame.time.wait(1000)
                pygame.draw.rect(screen,'#000000', pygame.Rect(545,335,80,80))                
                pygame.draw.rect(screen,'#00e8ec', pygame.Rect(550,340,70,70))
                # screen.blit(iceberg_surf,(300,100))
                countdown_1 = pixel_font_title.render(f"1",0,"#9955bb")
                screen.blit(countdown_1,(574,345))
                pygame.display.update()
                pygame.time.wait(1000)
                pygame.draw.rect(screen,'#000000', pygame.Rect(545,335,80,80))                
                pygame.draw.rect(screen,'#00e8ec', pygame.Rect(550,340,70,70))
                # screen.blit(iceberg_surf,(300,100))
                countdown_Go = pixel_font_bigger.render(f"Go",0,"#9955bb")
                screen.blit(countdown_Go,(553,352))
                pygame.display.update()
                pygame.time.wait(500)
                game_info.start_round()
                

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run =  False
            break
        
    # pygame.draw.circle(screen, "red",(583,369),263,1) #red circle


    #player controls-forward/back/left/right
    move_bear_keys(player_one, player_two)
   
    
    
    
    # player_one_hit_other = player_one.collide_other_bear(player_one.bear_mask,1,1)
    # player_two_hit_other = player_two.collide_other_bear(player_two.bear_mask,1,1)
    # if player_one_hit_other != None:
    #     print(player_one_hit_other)
    player_one_offset = (player_one.get_x(),player_one.get_y(),player_one.get_angle())
    player_two_offset = (player_two.get_x(),player_two.get_y(),player_two.get_angle())
    player_one_fall = player_one.collide_fall(boundary_surf_mask,x_bounds,y_bounds)
    player_one_hit = player_one.collide_other_bear(player_two.bear_mask,player_two.get_x(),player_two.get_y()) 
    player_two_hit = player_two.collide_other_bear(player_one.bear_mask,player_one.get_x(),player_one.get_y()) 
    if player_one_hit:
        player_two.bounce_trigger(player_one_offset)
    if player_two_hit:
        player_one.bounce_trigger(player_two_offset)
    # print(player_one_hit,player_two_hit)
    
    if player_one_fall != None:
        print(player_one_fall)
        player_two.set_score()
        player_one.fall_off()

    player_two_fall = player_two.collide_fall(boundary_surf_mask,x_bounds,y_bounds)

    if player_two_fall!= None:
        player_one.set_score() 
        player_two.fall_off()
    
    

    if game_info.get_round_time() == 0:
        game_info.reset_game_to_round_start()

    
    


            

        
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
