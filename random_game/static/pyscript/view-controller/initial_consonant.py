from common_view_controller import CommonGameViewController
from initial_consonant_quiz import InitialConsonantQuiz

game_instance = InitialConsonantQuiz()
controller = CommonGameViewController(game_instance, Element)

controller.element_initializing()
