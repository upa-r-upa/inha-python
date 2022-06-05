from common_view_controller import CommonGameViewController
from finger_game import FingerGame

game_instance = FingerGame()
controller = CommonGameViewController(game_instance, Element)

controller.element_initializing(direction_show=True)
