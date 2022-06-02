from abc import *
from Penalty import Penalty

# py-script는 핸들러와 연결만 할 예정.
# 웬만하면 모든 작업은 여기에서 이뤄질 수 있도록 함.
class GameBase(metaclass=ABCMeta):
    def __init__(self, intimacy, recommendedPeopleRange, direction, description, name):
        # 친밀도 
            # 0~N까지, 높을수록 친밀한 값
        self.intimacy = intimacy
        # 권장 인원
        self.recommendedPeopleRange = recommendedPeopleRange
        # 방향
        self.direction = direction
        
        # 설명
        self.description = description
        # 게임 이름
        self.name = name
        
    @abstractmethod
    def start_game(self):
        pass
    
    def end_game(self):
        pass
    
    def play_random_penalty(self):
        penalty = Penalty()
    
        return penalty.play_random_penalty()

    