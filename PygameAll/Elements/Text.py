from PygameAll.Elements.DrawObject import DrawObject


class Text(DrawObject):

    def __init__(self, window, x, y, text):
        super().__init__(window, x, y)
        self.text = text
        print(self.text)

    def __setattr__(self, att, value):
        if isinstance(value, str):
            self.__dict__[att] = self.FONT.render(value, True, self.TEXT_COLOR)
        elif isinstance(value, int):
            self.__dict__[att] = self.FONT.render(str(value), True, self.TEXT_COLOR)
        else:
            self.__dict__[att] = value

    def get_size_text(self):
        return self.FONT.size(self.text)

    def draw(self):
        self.window.blit(self.text, [self.x, self.y])
