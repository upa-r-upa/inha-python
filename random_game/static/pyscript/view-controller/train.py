from common_view_controller import CommonGameViewController
from train_game import TrainGame


class TrainGameViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing()

        train_card = self._game_model.get_random_train()
        Element("train-image").element.src = train_card.img_url
        Element("train-title").write(train_card.label)


game_instance = TrainGame()
controller = TrainGameViewController(game_instance, Element)

controller.element_initializing()
