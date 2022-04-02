import pygame
import random
from Window.ListToDraw import ListToDraw
from Window.Button import Button
from Window.Letter import Letter
from Window.Edge import Edge


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
        #lst = random.sample(range(10, 100), 9)
        lst = [3, 1, 9, 7, 8, 2, 6, 4, 5]
        print(lst)
        self.list_draw = ListToDraw(lst, self.window, self.width / 2, self.height / 4)
        self.elements.append(self.list_draw)

        # Buttons
        self.padding_button = 10
        self.button_next = Button(width=80, height=50, x=self.width/2 + self.padding_button, y=self.height*(3/4),
                                  text="next", window=self.window)
        self.button_prev = Button(width=80, height=50, x=self.width/2-80 - self.padding_button, y=self.height*(3/4),
                                  text="prev", window=self.window)
        self.elements.append(self.button_next)
        self.elements.append(self.button_prev)

        self.left_index = None
        self.right_index = None
        self.pivot_index = None

    def draw_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.WHITE)

    def redraw_window(self):
        for x in self.elements:
            x.draw()

    def next_clicked(self):
        qs_data = self.list_draw.quick_sort_data
        if self.list_draw.step_counter < len(qs_data.steps):
            step = qs_data[self.list_draw.step_counter]
            method = step[0]
            arguments = step[1]
            method(self.list_draw.step_counter)

            if arguments[0] == 'left' or arguments[0] == 'right':
                self.move_index(self.list_draw.step_counter)
            elif arguments[0] == 'left-right' or arguments[0] == 'right-pivot':
                self.swap_values(self.list_draw.step_counter)
            else:
                self.draw_indexes(self.list_draw.step_counter)
            self.list_draw.step_counter += 1

    def prev_clicked(self):
        pass

    def move_index(self, i):
        digit_x_size = self.list_draw.size_of_number
        padding = self.list_draw.padding

        steps = self.list_draw.quick_sort_data
        arguments = steps[self.list_draw.step_counter][1]
        index, movement = arguments

        if index == 'left':
            self.left_index.x += (digit_x_size+padding) * movement
        else:
            self.right_index.x += (digit_x_size+padding) * movement

    def swap_values(self, i):
        step = self.list_draw.quick_sort_data[i]
        left_index = self.list_draw.quick_sort_data.left_index
        right_index = self.list_draw.quick_sort_data.right_index
        pivot_index = self.list_draw.quick_sort_data.pivot_index

        lst = self.list_draw.list_display

        if step[1][0] == 'left-right':
            lst[left_index][0], lst[right_index][0] = lst[right_index][0], lst[left_index][0]
        else:
            lst[pivot_index][0], lst[right_index][0] = lst[right_index][0], lst[pivot_index][0]

    def draw_indexes(self, i):
        digit_y_size = self.list_draw.size_of_digit_y

        step = self.list_draw.quick_sort_data[i]

        # indexes
        left, right, pivot = step[1][0]

        # take tuple which consists of information value + position
        left_number = self.list_draw[left]
        right_number = self.list_draw[right]
        pivot_number = self.list_draw[pivot]

        left_x, left_y = left_number[1]
        right_x, right_y = right_number[1]
        pivot_x, pivot_y = pivot_number[1]

        if self.left_index:
            self.left_index.x, self.left_index.y = left_x, left_y + digit_y_size
            self.right_index.x, self.right_index.y = right_x, right_y + digit_y_size
            self.pivot_index.x, self.pivot_index.y = pivot_x, pivot_y - digit_y_size
        else:
            self.left_index = Letter(self.window, left_x, left_y + digit_y_size, 'i')
            self.right_index = Letter(self.window, right_x, right_y + digit_y_size, 'j')
            self.pivot_index = Letter(self.window, pivot_x, pivot_y - digit_y_size, 'p')
            self.elements.append(self.left_index)
            self.elements.append(self.right_index)
            self.elements.append(self.pivot_index)

    def move(self, dt, fps, velocity):
        distance = self.size_of_digit_y
        for x in range(int(fps/velocity)):
            #print(round(dt, 2), fps, self.size_of_digit_y*round(dt, 2)*velocity, fps/velocity)
            self.list_display[0][1][1] += distance*round(dt, 2)*velocity
            self.redraw_window()
            pygame.display.update()
        self.list_display[0][1][1] = round(self.list_display[0][1][1], 2)


