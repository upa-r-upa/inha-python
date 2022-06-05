from common_view_controller import CommonGameViewController
from initial_consonant_quiz import InitialConsonantQuiz


class InitialConsonantViewController(CommonGameViewController):
    def element_initializing(self):
        super().element_initializing()

        random_keyword = self._game_model.get_random_consonant_str()
        Element("consonant-label").write(random_keyword)


game_instance = InitialConsonantQuiz()
controller = InitialConsonantViewController(game_instance, Element)

controller.element_initializing()
