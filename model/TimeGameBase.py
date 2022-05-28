from GameBase import GameBase
from threading import Timer
from abc import *
        

class TimeGameBase(GameBase):
    # 초 단위로 시간을 입력 받습니다.
    def __init__(self, intimacy, recommendedPeopleRange, direction, description, name, game_limit_time):
        super().__init__(intimacy, recommendedPeopleRange, direction, description, name)
        
        game_limit_time = game_limit_time
        
        
    @abstractmethod
    def _end_time(self):
        pass
    
    def _start_time(self):
        pass
    
    def start_game(self):
        super().start_game()
        
        timer = Timer(self.game_limit_time, self.time_end)
        timer.start()
    
    def end_game(self):
        super().end_game()
        self._end_time()