from utils import UIUtils
from urllib.parse import urlencode


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
ui_utils = UIUtils()

range_minimum = Element("people-range-minimum")
range_middle = Element("people-range-middle")
range_maximum = Element("people-range-maximum")

range_button_list = [range_minimum, range_middle, range_maximum]


def handle_range_click(element, range):
    ui_utils.buttons_toggle(element, "selected", range_button_list)
    user_settings.set_people_range(range)


range_minimum.element.onclick = lambda *args, **kwargs: handle_range_click(
    range_minimum, [1, 2]
)
range_middle.element.onclick = lambda *args, **kwargs: handle_range_click(
    range_middle, [3, 10]
)
range_maximum.element.onclick = lambda *args, **kwargs: handle_range_click(
    range_maximum, [11, 50]
)

intimacy_low = Element("intimacy-low")
intimacy_high = Element("intimacy-high")

intimacy_button_list = [intimacy_low, intimacy_high]


def handle_intimacy_click(element, intimacy):
    ui_utils.buttons_toggle(element, "selected", intimacy_button_list)
    user_settings.set_intimacy(intimacy)


intimacy_low.element.onclick = lambda *args, **kwargs: handle_intimacy_click(
    intimacy_low, 0
)
intimacy_high.element.onclick = lambda *args, **kwargs: handle_intimacy_click(
    intimacy_high, 1
)

game_start = Element("game-start")
hidden_move_a_tag = Element("hidden-move-a")


def handle_start_button_click(*args, **kwargs):
    if user_settings.validate_game_start():
        # link 변경
        hidden_move_a_tag.element.href = "/api/redirect-game?" + urlencode(
            {
                "people_min": user_settings.people_range[0],
                "people_max": user_settings.people_range[1],
                "intimacy": user_settings.intimacy,
            }
        )
        hidden_move_a_tag.element.click()
    else:
        pass


game_start.element.onclick = handle_start_button_click
