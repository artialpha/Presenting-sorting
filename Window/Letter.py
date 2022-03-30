from Window.DrawObject import DrawObject


class Letter(DrawObject):

    def __init__(self, window, x, y, letter):
        super().__init__(window, x, y)
        self.letter = self.FONT.render(letter, True, self.BLACK)

    def draw(self):
        self.window.blit(self.letter, [self.x, self.y])
