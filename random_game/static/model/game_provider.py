import random


class GameProvider:
    def __init__(
        self,
        game_list,
    ):
        self.game_list = game_list

    def __filtered_function(self, game, prev_game, intimacy, people_range):
        non_same_prev_game = game["game_id"] != prev_game
        intimacy_matched = game["intimacy"] <= intimacy
        range_matched = game["recommended_people_range"][0] <= people_range[0]

        return non_same_prev_game and intimacy_matched and range_matched

    def _get_random_game(self, prev_game, intimacy, people_range):
        filtered_origin_list = filter(
            lambda x: self.__filtered_function(x, prev_game, intimacy, people_range),
            self.game_list,
        )
        filtered_list = list(filtered_origin_list)
        return random.choice(filtered_list)

    def get_random_game(self, people_range, intimacy, prev_game):
        random_game = self._get_random_game(prev_game, intimacy, people_range)

        return random_game
