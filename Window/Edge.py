import pygame
from Window.DrawObject import DrawObject


class Edge(DrawObject):
    RED = (255, 0, 0)

    def __init__(self, window, x, y, width):
        super().__init__(window, x, y, width)

    # positive direction goes right, negative left
    def draw_edge(self, direction):
        pygame.draw.line(self.window, self.RED, (self.x, self.y), (self.x+direction, self.y), self.width)
        pygame.draw.line(self.window, self.RED, (self.x, self.y), (self.x, self.y+20), self.width)
