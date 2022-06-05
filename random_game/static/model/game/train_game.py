import random
from game_base import GameBase
from image_card import ImageCard

static_train_card = [
    ImageCard(label="1호선", img_url="game/train-game/number-1.png"),
    ImageCard(label="2호선", img_url="game/train-game/number-2.png"),
    ImageCard(label="3호선", img_url="game/train-game/number-3.png"),
    ImageCard(label="4호선", img_url="game/train-game/number-4.png"),
    ImageCard(label="5호선", img_url="game/train-game/number-5.png"),
    ImageCard(label="6호선", img_url="game/train-game/number-6.png"),
    ImageCard(label="7호선", img_url="game/train-game/number-7.png"),
    ImageCard(label="8호선", img_url="game/train-game/number-8.png"),
    ImageCard(label="경의중앙선", img_url="game/train-game/number-9.png"),
    ImageCard(label="수인분당선", img_url="game/train-game/number-10.png"),
]


class TrainGame(GameBase):
    def __init__(self):
        super().__init__(
            game_id="train-game",
        )

        self.__train_card_list = static_train_card

    def get_random_train(self):
        random_train = random.choice(self.__train_card_list)

        return random_train
