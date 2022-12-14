from BearPhysics import BearPhysics

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