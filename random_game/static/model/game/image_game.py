import random
from game_base import GameBase

static_keyword_list = [
    "잘 안 씻을 것 같은 사람은?",
    "자뻑이 심할 것 같은 사람은?",
    "바바리맨이 잘 어울릴 것 같은 사람은?",
    "학교에서 공부 제일 안할 것 같은 사람은?",
    "죽어도 이성적인 감정이 안 느껴질 것 같은 사람은?",
    "첫인상과 완전 반대인 것 같은 사람은?",
    "자판기 밑에 떨어진 500원 목숨 걸고 주울 것 같은 사람은?",
    "같이 있으면 어색할 것 같은 사람은?",
    "가오가 육체를 완전히 지배할 것 같은 사람은?",
    "첫사랑을 아직도 못 잊고 있을 것 같은 사람은?",
    "상견례 프로패스 각일 것 같은 사람은?",
    "자리에 없으면 가장 많이 언급될 것 같은 사람은?",
    "긁지 않은 복권일 것 같은 사람은?",
    "아직도 산타클로스 존재를 믿을 것 같은 사람은?",
    "최근까지 이불에 지도 그렸을 것 같은 사람은?",
]


class ImageGame(GameBase):
    def __init__(self):
        super().__init__(
            game_id="image-game",
        )

        self.__keyword_list = static_keyword_list

    def get_random_keyword(self):
        random_keyword = random.choice(self.__keyword_list)

        return random_keyword
