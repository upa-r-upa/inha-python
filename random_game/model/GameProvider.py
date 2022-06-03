import random


game_list = ["bomb-game", "hunch-game"]


class GameProvider:
    def __init__(self):
        self.game_list = game_list

    def _get_random_game(self, prev_game):
        filtered_origin_list = filter(lambda x: x != prev_game, self.game_list)
        filtered_list = list(filtered_origin_list)
        return random.choice(filtered_list)

    def play_random_game(self, people_range, intimacy, prev_game):
        random_game = self._get_random_game(prev_game)

        return random_game
