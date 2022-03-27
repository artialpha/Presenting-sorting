import pygame
import random
from Window.ListToDraw import ListToDraw
from Window.Button import Button
from Window.Letter import Letter
from Window.Edge import Edge


class Draw:
    WHITE = (255, 255, 255)

    def __init__(self, width, height, fps, velocity):
        self.width = width
        self.height = height
        self.fps = fps
        self.velocity = velocity

        self.window = None
        self.draw_window()

        lst = random.sample(range(9, 100), 8)
        self.list_to_display = ListToDraw(lst, self.window, self.width/2, self.height/4)

        # Buttons
        self.padding_button = 10
        self.button_next = Button(width=80, height=50, x=self.width/2 + self.padding_button, y=self.height*(3/4),
                                  text="next", window=self.window)
        self.button_prev = Button(width=80, height=50, x=self.width/2-80 - self.padding_button, y=self.height*(3/4),
                                  text="prev", window=self.window)

        # letter
        x, y = self.list_to_display[0][1]
        self.letter = Letter(self.window, x, y, 'b')

        #edge
        self.edge = Edge(self.window, x, y, 2)

    def draw_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.WHITE)

    def redraw_window(self):
        self.list_to_display.display_list()
        self.button_next.draw_button()
        self.button_prev.draw_button()
        self.letter.draw_letter()
        self.edge.draw_edge(-20)





    '''
            display_list
            i want to display the list horizontally in the middle 
            so i need to take into consideration how much space the list takes
            i use self.FONT.size(...) to determine it 
            it returns a tuple (width, height)
            https://www.pygame.org/docs/ref/font.html#pygame.font.Font.size
    '''

    def move(self, dt, fps, velocity):
        distance = self.size_of_digit_y
        for x in range(int(fps/velocity)):
            #print(round(dt, 2), fps, self.size_of_digit_y*round(dt, 2)*velocity, fps/velocity)
            self.list_display[0][1][1] += distance*round(dt, 2)*velocity
            self.redraw_window()
            pygame.display.update()
        self.list_display[0][1][1] = round(self.list_display[0][1][1], 2)


