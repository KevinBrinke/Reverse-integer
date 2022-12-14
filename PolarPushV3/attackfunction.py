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