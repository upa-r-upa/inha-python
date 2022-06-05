from common_view_controller import CommonGameViewController
from baskin_robbins import BaskinRobbins


class BaskinRobbinsViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing()

        keyword = self._game_model.get_random_keyword()
        Element("match-keyword-title").write(keyword)


game_instance = BaskinRobbins()
controller = BaskinRobbinsViewController(game_instance, Element)

controller.element_initializing()
