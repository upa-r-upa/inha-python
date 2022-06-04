from common_view_controller import CommonGameViewController
from bomb_game import BombGame

game_instance = BombGame()
controller = CommonGameViewController(game_instance, Element)

controller.handler_emit()
