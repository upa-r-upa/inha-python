from model.PenaltyCard import PenaltyCard

static_penalty_list = [
    # 예시 벌칙 리스트, 이미지와 함께 함.
    PenaltyCard('술 1잔 마시기'),
    PenaltyCard('술 2잔 마시기'),
    PenaltyCard('술 3잔 마시기'),
]


class Penalty:
    # 가급적 Convention 지킬 것.
    penalty_list = static_penalty_list
    
    def __init__(number_of_people):
        __number_of_people = number_of_people
    
    def play_random_penalty(self):
        pass
    
    def _get_random_penalty(self):
        pass
    
    def _get_filtered_penalty_list(self): 
        pass;
    
    