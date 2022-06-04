from common_view_controller import CommonGameViewController
from hunch_game import HunchGame

game_instance = HunchGame()
controller = CommonGameViewController(game_instance, Element)

controller.handler_emit()
