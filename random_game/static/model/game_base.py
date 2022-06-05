import random
from urllib.parse import urlparse, parse_qsl
from penalty import Penalty
from js import window
from game_data_set import game_data_set
from image_card import ImageCard

static_direction_list = [
    ImageCard(label="시계 방향으로 진행하기", img_url="common/direction-left.png"),
    ImageCard(label="반시계 방향으로 진행하기", img_url="common/direction-right.png"),
]


class GameBase:
    def __init__(
        self,
        *,
        game_id,
    ):
        game_set = game_data_set[game_id]

        # 게임의 unique id, route로 사용
        self.game_id = game_id
        # 권장 인원
        self.recommended_people_range = game_set["recommended_people_range"]
        # 방향
        self.direction = random.choice(static_direction_list)

        # 게임 메인 이미지
        self.main_image_url = game_set["main_image_url"]
        # 설명
        self.description = game_set["description"]
        # 게임 이름
        self.name = game_set["name"]

        parsed_url = urlparse(window.location.href)
        params_dict = dict(parse_qsl(parsed_url.query))

        intimacy = int(params_dict["intimacy"])

        self.__penalty = Penalty(intimacy)

    def start_game(self):
        pass

    def end_game(self):
        pass

    def play_random_penalty(self):

        return self.__penalty.play_random_penalty()
