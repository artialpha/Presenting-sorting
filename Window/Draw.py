import pygame
import random
from Window.AlgsDraw.QuickListDraw import QuickListDraw
from Window.Button import Button
from Window.Text import Text


class Draw:
    WHITE = (255, 255, 255)
    elements = []

    def __init__(self, width, height, fps, velocity):
        self.width = width
        self.height = height
        self.fps = fps
        self.velocity = velocity

        self.window = None
        self.draw_window()

        # list of random numbers
        lst = random.sample(range(10, 100), 9)
        # lst = [3, 1, 9, 7, 8, 2, 6, 4, 5]
        print(lst)
        self.list_draw = QuickListDraw(lst, self.window, self.width / 2, self.height / 4)
        self.elements.append(self.list_draw)

        # Buttons
        width = 80
        height = 50
        x = self.width/2
        y = self.height*(3/4)
        padding = 10
        self.button_prev = Button(self.window, x-width-padding, y, width, height, "prev")
        self.button_next = Button(self.window, x+padding, y, width, height, "next")
        self.elements.append(self.button_next)
        self.elements.append(self.button_prev)

        # Counter of steps
        x = (self.width/2)
        y = self.height*(3/4)-50
        padding = 10
        self.max_steps = Text(self.window, x + padding, y, str(len(self.list_draw.quick_sort_data.steps)))
        max_steps_width = self.max_steps.text.get_size()[0]
        self.current_number = Text(self.window, x - max_steps_width - padding, y, '0')

        self.elements.append(self.current_number)
        self.elements.append(self.max_steps)

    def draw_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.WHITE)

    def redraw_window(self):
        for x in self.elements:
            x.draw()

    def click(self, prev=False):
        self.list_draw.button_clicked(prev)
        self.current_number.text = self.list_draw.step_counter


'''
    def move(self, dt, fps, velocity):
        distance = self.size_of_digit_y
        for x in range(int(fps/velocity)):
            #print(round(dt, 2), fps, self.size_of_digit_y*round(dt, 2)*velocity, fps/velocity)
            self.list_display[0][1][1] += distance*round(dt, 2)*velocity
            self.redraw_window()
            pygame.display.update()
        self.list_display[0][1][1] = round(self.list_display[0][1][1], 2)
'''
