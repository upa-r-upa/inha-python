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
    
    def __init__(intimacy):
        __intimacy = intimacy
    
    def _get_filtered_penalty_list(self): 
        # [구현부] 친밀도에 따른 벌칙을 return 해야 함.
        pass;

    def _get_random_penalty(self, penalty_list):
        # [구현부] penalty_list를 사용해 랜덤한 패널티를 return 해야 함
        pass
        
    def play_random_penalty(self):
        # 참고: 친밀도 값은 __intimacy
        # [구현부] _get_filtered_penalty_list, _get_random_penalty를 사용해 최종적으로 친밀도에 맞는 벌칙 한개를 return 해야함.
        pass
    