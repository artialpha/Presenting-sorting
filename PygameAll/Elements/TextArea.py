import pygame
from PygameAll.Elements.DrawObject import DrawObject


class TextArea(DrawObject):

    def __init__(self, window, x, y, width, height, text='', bg_color=(100, 100, 100)):
        super().__init__(window, x, y, width, height)
        self.text = self.FONT.render(str(text), True, self.TEXT_COLOR)
        self.window = window
        self.rect = None
        self.bg_color = bg_color

    def draw(self):
        self.rect = pygame.draw.rect(self.window, self.bg_color, (self.x, self.y, self.width, self.height), 0)
        self.window.blit(self.text, (self.x + (self.width/2 - self.text.get_width()/2), self.y
                                            + (self.height/2 - self.text.get_height()/2)))
