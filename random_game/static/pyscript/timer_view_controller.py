from utils import UIUtils


class TimerViewController:
    def __init__(self, element):
        self._ui_utils = UIUtils()
        self.Element = element

    def time_format(self, second):
        minute = int(second / 60)
        count = second - minute * 60

        if minute < 10:
            str_minute = f"0{minute}"
        else:
            str_minute = str(minute)
        if count < 10:
            str_count = f"0{count}"
        else:
            str_count = str(count)

        return f"{str_minute} : {str_count}"

    def timer_bomb(self):
        notice_container = self.Element("game-end-notice-container")
        container = self.Element("bomb-image")
        self._ui_utils.view_toggle(notice_container, True)
        self._ui_utils.view_toggle(container, True)

    def timer_update(self, time, remaining_time):
        rest_time_element = self.Element("rest-time")
        rest_time_element.write(self.time_format(remaining_time))

    def element_initializing(self):
        container = self.Element("timer-container")
        self._ui_utils.view_toggle(container, True)
