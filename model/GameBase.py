from abc import *
from Penalty import Penalty

# py-script는 핸들러와 연결만 할 예정.
# 웬만하면 모든 작업은 여기에서 이뤄질 수 있도록 함.
class GameBase(metaclass=ABCMeta):
    def __init__(self, intimacy, recommendedPeopleRange, direction, description, name):
        # 친밀도
        intimacy = intimacy
        # 권장 인원
        recommendedPeopleRange = recommendedPeopleRange
        # 방향
        direction = direction
        
        # 설명
        description = description
        # 게임 이름
        name = name
        
    @abstractmethod
    def start_game(self):
        pass
    
    @abstractmethod
    def end_game(self):
        pass
    
    @abstractmethod
    def play_penalty(self):
        penalty = Penalty()
    
        return penalty.play_random_penalty()
    
    @abstractmethod
    def penalty_end(self):
        pass
    