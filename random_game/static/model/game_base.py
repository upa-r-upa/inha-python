import random
from penalty import Penalty
from game_data_set import game_data_set

static_direction_list = ["시계 방향으로", "시계 반대 방향으로"]


class GameBase:
    def __init__(
        self,
        *,
        game_id,
    ):
        game_set = game_data_set[game_id]

        # 게임의 unique id, route로 사용
        self.game_id = game_id
        # 친밀도. 0~N까지, 높을수록 친밀한 값
        self.intimacy = game_set["intimacy"]
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

        self.__penalty = Penalty(self.intimacy)

    def start_game(self):
        pass

    def end_game(self):
        pass

    def play_random_penalty(self):

        return self.__penalty.play_random_penalty()
