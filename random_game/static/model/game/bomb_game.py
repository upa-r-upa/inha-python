from time_game_base import TimeGameBase


class BombGame(TimeGameBase):
    def __init__(self, *, on_end_timer):

        super().__init__(game_id="bomb-game", on_end_timer=on_end_timer)
