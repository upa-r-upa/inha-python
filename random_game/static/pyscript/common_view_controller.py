from urllib.parse import urlparse, parse_qsl, unquote, urlencode
from js import window
from utils import UIUtils


class CommonGameViewController:
    def __init__(self, model, Element):
        self.__game_model = model
        self.__ui_utils = UIUtils()

        self.Element = Element

    def next_game_start(self, *args):
        hidden_move_a_tag = self.Element("hidden-move-a")
        parsed_url = urlparse(window.location.href)

        params_dict = dict(parse_qsl(parsed_url.query))

        params_dict["prev_game"] = self.__game_model.game_id

        hidden_move_a_tag.element.href = "/api/redirect-game?" + unquote(
            urlencode(params_dict)
        )
        hidden_move_a_tag.element.click()

    def penalty_start(self, *args):
        penalty_container = self.Element("penalty-container")
        penalty_container.element.classList.remove("hidden-area")

        img_element = penalty_container.select("img")
        title_element = penalty_container.select("p")

        random_penalty_card = self.__game_model.play_random_penalty()

        title_element.element.innerText = random_penalty_card.name
        img_element.element.src = "/static/" + random_penalty_card.img_src

    def close_description(self, *args):
        description_container = self.Element("description-container")
        description_container.element.classList.add("hidden-area")

        self.__game_model.start_game()

    def element_initializing(self, *, direction_show=False):
        next_game_button = self.Element("next-game-button")
        penalty_play_button = self.Element("extra-penalty-button")
        description_close_button = self.Element("game-description-close")

        description_close_button.element.onclick = self.close_description
        next_game_button.element.onclick = self.next_game_start
        penalty_play_button.element.onclick = self.penalty_start

        if direction_show:
            direction_container = self.Element("direction-container")
            direction_img = direction_container.select("img")
            direction_label = self.Element("direction-label")

            self.__ui_utils.view_toggle(direction_container, True)

            direction_img.element.src = "/static/" + self.__game_model.direction.img_url
            direction_label.write(self.__game_model.direction.label)
