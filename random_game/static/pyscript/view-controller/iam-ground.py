from common_view_controller import CommonGameViewController
from iam_ground import IAMGround


class IAMGroundViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing(direction_show=True)

        keyword = self._game_model.get_random_keyword()
        Element("match-keyword-title").write(keyword)


game_instance = IAMGround()
controller = IAMGroundViewController(game_instance, Element)

controller.element_initializing()
