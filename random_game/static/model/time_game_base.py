from random import randrange
from game_base import GameBase
from threading import Timer


class TimeGameBase(GameBase):
    def __init__(self, *, game_id, game_limit_time=randrange(30, 50), on_tick_time):
        super().__init__(
            game_id=game_id,
        )
        self.timer = Timer()
        self.game_limit_time = game_limit_time

    def _end_time(self):

        self.end_game()

    def _start_time(self):
        self.timer.start()

    def start_game(self):
        super().start_game()

    def end_game(self):
        super().end_game()
