from common_view_controller import CommonGameViewController
from timer_view_controller import TimerViewController
from bomb_game import BombGame


class BombTimerViewController(TimerViewController):
    def __init__(self, element):
        super().__init__(element)

    def element_initializing(self):
        super().element_initializing()
        self.Element("rest-time").write("?? : ??")


bomb_timer_view_controller = BombTimerViewController(Element)
bomb_timer_view_controller.element_initializing()

game_instance = BombGame(on_end_timer=bomb_timer_view_controller.timer_bomb)
controller = CommonGameViewController(game_instance, Element)

controller.element_initializing(direction_show=True)
