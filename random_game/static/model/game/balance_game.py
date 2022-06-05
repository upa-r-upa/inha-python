import random
from time_game_base import TimeGameBase

static_keyword_list = [
    ["친구 전 애인과 연애하기", "전 애인 친구랑 연애하기"],
    ["100% 확률로 1억 받기", "25% 확률로 100억 받기"],
    ["애인에게 추근대는 베프", "베프에게 대시하는 애인"],
    ["한 달 내내 치킨 무 없이 치킨 먹기", "한 달 내내 콜라 없이 빅맥 먹기"],
    ["10억 받고 스마트폰 없이 살기", "10만원 받고 스마트폰하며 살기"],
    ["한파 속 아아 마시기", "폭염 속 불닭볶음면 먹기"],
    ["남사친과 1박 2일 여행가는 애인", "전남친과 밤새 술 마시는 애인"],
    ["입에서 발냄새 나는 애인", "발에서 입냄새 나는 애인"],
    ["7시 출근~ 4시 퇴근", "10시 출근 ~ 7시 퇴근"],
    ["10살 연상 후임", "10살 연하 상사"],
    ["월요일에 연차쓰기", "금요일에 연차쓰기"],
    ["1년 동안 핸드폰 없이 살기", "1년 동안 친구없이 살기"],
    ["평생 두통", "평생 치통"],
    ["365일폭염", "365일장마"],
]


class BalanceGame(TimeGameBase):
    def __init__(self, on_end_timer, on_timer_tick):
        super().__init__(
            game_id="image-game", on_end_timer=on_end_timer, on_timer_tick=on_timer_tick
        )

        self.__keyword_list = static_keyword_list

    def get_random_keyword(self):
        random_keyword = random.choice(self.__keyword_list)

        return random_keyword
