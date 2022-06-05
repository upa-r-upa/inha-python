class UIUtils:
    def buttons_toggle(self, element, toggle_classname, buttons_list):
        element.element.classList.add(toggle_classname)

        for button in buttons_list:
            if element != button:
                button.element.classList.remove(toggle_classname)

    def view_toggle(self, element, toggle):
        if toggle:
            element.element.classList.remove("hidden-area")
        else:
            element.element.classList.add("hidden-area")
