from common_view_controller import CommonGameViewController
from timer_view_controller import TimerViewController
from korean_game import KoreanGame


timer_view_controller = TimerViewController(Element)
timer_view_controller.element_initializing()

game_instance = KoreanGame(
    on_timer_tick=timer_view_controller.timer_update,
    on_end_timer=timer_view_controller.timer_bomb,
)
controller = CommonGameViewController(game_instance, Element)

controller.element_initializing()
