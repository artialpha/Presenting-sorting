import pygame
pygame.init()


class DrawObject:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.SysFont("Times New Roman", 30)

    def __init__(self, window, x, y, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

    def draw(self):
        pass
