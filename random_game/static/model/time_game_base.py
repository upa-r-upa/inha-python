from random import randrange
from game_base import GameBase
from timer import Timer
from js import console


class TimeGameBase(GameBase):
    def __init__(
        self,
        *,
        game_id,
        game_limit_time=randrange(5, 10),
        on_end_timer=lambda: None,
        on_timer_tick=lambda x, y: None,
    ):
        super().__init__(
            game_id=game_id,
        )
        self.__timer = None
        self.game_limit_time = game_limit_time

        self.__on_timer_tick = on_timer_tick
        self.__on_end_timer = on_end_timer

    def emit_handler(self, on_timer_tick=None, on_end_timer=None):
        if on_timer_tick:
            self.__on_timer_tick = on_timer_tick

        if on_end_timer:
            self.__on_end_timer = on_end_timer

    def __set_timer(self, timer):
        self.__timer = timer

    def _end_time(self):
        self.__on_end_timer()

    def _start_time(self):
        self.__set_timer(
            Timer(self.game_limit_time, self.__on_timer_tick, self.end_game)
        )
        self.__timer.start()

    def start_game(self):
        super().start_game()
        self._start_time()

    def end_game(self):
        super().end_game()
        self._end_time()
