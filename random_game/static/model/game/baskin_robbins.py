import random
from game_base import GameBase

static_keyword_list = ["귀엽게", "사랑스럽게", "터프하게", "섹시하게", "웃기게", "슬프게", "앙큼하게", "평범하게"]


class BaskinRobbins(GameBase):
    def __init__(self):
        super().__init__(
            game_id="baskin-robbins",
        )

        self.__keyword_list = static_keyword_list

    def get_random_keyword(self):
        random_keyword = random.choice(self.__keyword_list)

        return random_keyword
