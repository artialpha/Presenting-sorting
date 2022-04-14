from PygameAll.Elements.DrawObject import DrawObject


class Text(DrawObject):

    def __init__(self, window, x, y, text):
        super().__init__(window=window, x=x, y=y)
        self.text = text

    def __setattr__(self, att, value):
        if isinstance(value, str):
            self.__dict__[att] = self.FONT.render(value, True, self.TEXT_COLOR)
        elif isinstance(value, int) and (att != 'x' and att != 'y'):
            self.__dict__[att] = self.FONT.render(str(value), True, self.TEXT_COLOR)
        else:
            self.__dict__[att] = value

    def __eq__(self, other):
        return self.text == other.text

    def get_size_text(self):
        return self.FONT.size(self.text)

    def draw(self):
        self.window.blit(self.text, [self.x, self.y])
