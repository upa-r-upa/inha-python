import random
from game_base import GameBase

static_keyword_list = [
    "과일 이름",
    "연예인 이름",
    "자기소개",
    "좋아하는 음식",
    "나라 이름",
    "동물 이름",
    "생선 이름",
    "색깔",
]


class IAMGround(GameBase):
    def __init__(self):
        super().__init__(
            game_id="iam-ground",
        )

        self.__keyword_list = static_keyword_list

    def get_random_keyword(self):
        random_keyword = random.choice(self.__keyword_list)

        return random_keyword
