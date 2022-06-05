from common_view_controller import CommonGameViewController
from timer_view_controller import TimerViewController
from balance_game import BalanceGame


class BalanceGameViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing()

        keyword = self._game_model.get_random_keyword()
        Element("match-keyword-title-1").write(keyword[0])
        Element("match-keyword-title-2").write(keyword[1])


timer_view_controller = TimerViewController(Element)
timer_view_controller.element_initializing()

game_instance = BalanceGame(
    on_timer_tick=timer_view_controller.timer_update,
    on_end_timer=timer_view_controller.timer_bomb,
)
controller = BalanceGameViewController(game_instance, Element)

controller.element_initializing()
