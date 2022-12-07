from utils import *
import math
from PlayerBear import PlayerBear

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

    def collide_other_bear(self, mask, x_bounds, y_bounds):
        boundary_offset= (int(self.x - x_bounds ), int(self.y - y_bounds ))
        poi = self.bear_mask.overlap(mask, (1,0))
        return poi #point of intersection

    def bounce_to_center_trigger(self):
        self.bounce_center_vel = 8        #turn tangent tangent to all center and bounce    
        self.reduce_speed()
    def bounce_trigger(self):
        print("bounce")

    def reset(self):
        self.x,self.y = self.start_pos
        self.angle = self.start_angle
        self.vel = 0
       
