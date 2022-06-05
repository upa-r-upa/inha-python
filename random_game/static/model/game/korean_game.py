from time_game_base import TimeGameBase


class KoreanGame(TimeGameBase):
    def __init__(self, *, on_end_timer, on_timer_tick):

        super().__init__(
            game_id="korean-game",
            on_timer_tick=on_timer_tick,
            on_end_timer=on_end_timer,
            game_limit_time=50,
        )
