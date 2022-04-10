import pygame


class Window:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BACKGROUND_COLOR = BLACK
    TEXT_COLOR = WHITE
    elements = []
    width_button = 80
    height_button = 50

    def __init__(self, width, height):
        self.width = width

        self.height = height

        self.window = None

        self.draw_window()

    def draw_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.BACKGROUND_COLOR)

    def redraw_window(self):
        self.window.fill(self.BACKGROUND_COLOR)
        for x in self.elements:
            x.draw()

    def click(self):
        pass

    def buttons_clicked_check(self, event, draw=None):
        pass
