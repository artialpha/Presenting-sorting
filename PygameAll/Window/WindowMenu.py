from PygameAll.Elements.TextArea import TextArea
from PygameAll.Window.Window import Window


class WindowMenu(Window):

    def __init__(self, width, height, fps, velocity):
        super().__init__(width, height, fps, velocity)

        x = (self.width-self.width_button)/2
        y = self.height*(1/4)
        padding = 10
        self.button_prev = TextArea(self.window, x, y, self.width_button, self.height_button, "quick")
        self.button_next = TextArea(self.window, x, y + padding + self.height_button, self.width_button,
                                    self.height_button, "merge")
        self.elements.append(self.button_next)
        self.elements.append(self.button_prev)

