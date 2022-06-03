class UserSettings:
    def __init__(self):
        self.people_range = None
        self.intimacy = None

    def set_people_range(self, people_range):
        self.people_range = people_range

    def set_intimacy(self, intimacy):
        self.intimacy = intimacy

    def validate_game_start(self):
        if self.people_range != None and self.intimacy != None:
            return True
        else:
            return False


user_settings = UserSettings()

game_start = Element("game-start")

range_minimum = Element("people-range-minimum")
range_middle = Element("people-range-middle")
range_maximum = Element("people-range-maximum")

range_minimum.element.onclick = lambda *args, **kwargs: user_settings.set_people_range(
    [1, 2]
)
range_middle.element.onclick = lambda *args, **kwargs: user_settings.set_people_range(
    [3, 10]
)
range_maximum.element.onclick = lambda *args, **kwargs: user_settings.set_people_range(
    [11, 50]
)


def handle_start_button_click(*args, **kwargs):
    if user_settings.validate_game_start():
        # link 변경
        pass
    else:
        pass


game_start.element.onclick = handle_start_button_click
