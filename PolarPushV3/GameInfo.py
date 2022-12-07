from PlayerBear import PlayerBear
class GameInfo:
    
    
    def __init__(self,round=1):
        self.round = round 
        self.started = False
        self.round_start_time = 60
        self.score_total = 0
        self.max_rounds = 7

        
        
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
        self.game_end = True
    def start_round(self):
        self.started =True
        self.total_window_run_time = int(pygame.time.get_ticks()/1000)
    def get_round_time(self):
        if not self.started:
            return self.round_start_time
        self.round_time_left = self.round_start_time + self.total_window_run_time - int(pygame.time.get_ticks()/1000)
        # if not self.round_time_left<=0:
        return self.round_time_left