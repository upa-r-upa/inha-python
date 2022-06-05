import random
from game_base import GameBase


class InitialConsonantQuiz(GameBase):
    def __init__(self):
        super().__init__(
            game_id="initial-consonant-quiz",
        )

        self.__initial_consonant_list = [
            "ㄱ",
            "ㄲ",
            "ㄴ",
            "ㄷ",
            "ㄹ",
            "ㅁ",
            "ㅂ",
            "ㅅ",
            "ㅇ",
            "ㅈ",
            "ㅊ",
            "ㅋ",
            "ㅌ",
            "ㅍ",
            "ㅎ",
        ]

    def get_random_consonant_str(self):
        consonant_list = self.__get_random_consonants()
        result_consonant = "".join(consonant_list)

        return result_consonant

    def __get_random_consonants(self):
        consonant_length = random.randrange(2, 4)
        consonant_list = []

        for _ in range(consonant_length):
            consonant_list.append(self.__get_random_consonant())

        return consonant_list

    def __get_random_consonant(self):
        initial_consonant = random.choice(self.__initial_consonant_list)

        return initial_consonant
