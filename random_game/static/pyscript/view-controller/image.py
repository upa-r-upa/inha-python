from common_view_controller import CommonGameViewController
from image_game import ImageGame


class ImageViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing()

        keyword = self._game_model.get_random_keyword()
        Element("match-keyword-title").write(keyword)


game_instance = ImageGame()
controller = ImageViewController(game_instance, Element)

controller.element_initializing()
