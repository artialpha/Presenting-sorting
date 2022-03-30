import pygame
from Window.DrawObject import DrawObject


class Button(DrawObject):

    def __init__(self, width, height, x, y, text, window):
        super().__init__(window, x, y, width, height)
        self.text = self.FONT.render(str(text), True, self.BLACK)
        self.window = window
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.rect(self.window, (100, 100, 100), (self.x, self.y, self.width, self.height), 0)
        self.window.blit(self.text, (self.x + (self.width/2 - self.text.get_width()/2), self.y
                                            + (self.height/2 - self.text.get_height()/2)))
