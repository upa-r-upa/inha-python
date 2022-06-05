import random
from penalty_card import PenaltyCard

static_penalty_list = [
    # 예시 벌칙 리스트, 이미지와 함께 함.
    PenaltyCard(name="소주 원샷!", img_src="images/penalty/soju-cup.png"),
    PenaltyCard(name="맥주 원샷!", img_src="images/penalty/one-beer.png"),
    PenaltyCard(name="소맥 원샷!", img_src="images/penalty/beer-with-cup.png"),
    PenaltyCard(name="벌칙 PASS!", img_src="images/penalty/pass.png"),
    PenaltyCard(
        name="술 한잔 원샷, 흑기사 찬스!", intimacy=1, img_src="images/penalty/highfive.png"
    ),
    PenaltyCard(name="러브샷!", intimacy=1, img_src="images/penalty/love.png"),
]


class Penalty:
    def __init__(self, intimacy):
        self.penalty_list = static_penalty_list
        self.__prev_penalty = None
        self.__intimacy = intimacy

    def __set_prev_intimacy(self, penalty_card):
        self.__prev_penalty = penalty_card

    def __get_non_overlap_penalty_list(self, penalty_list):
        return list(
            filter(
                lambda x: self.__prev_penalty == None
                or x.name != self.__prev_penalty.name,
                penalty_list,
            )
        )

    def __get_intimacy_filtered_list(self, penalty_list):
        return list(filter(lambda x: x.intimacy <= self.__intimacy, penalty_list))

    def __get_random_penalty(self):
        non_overlap_penalty_list = self.__get_non_overlap_penalty_list(
            self.penalty_list
        )
        filtered_list = self.__get_intimacy_filtered_list(non_overlap_penalty_list)

        return random.choice(filtered_list)

    def play_random_penalty(self):
        random_penalty = self.__get_random_penalty()

        self.__set_prev_intimacy(random_penalty)

        return random_penalty
