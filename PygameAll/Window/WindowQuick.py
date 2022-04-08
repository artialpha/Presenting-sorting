import pygame
import random
from PygameAll.AlgsDraw.QuickListDraw import QuickListDraw
from PygameAll.Elements.TextArea import TextArea
from PygameAll.Elements.Text import Text
from PygameAll.Window.Window import Window


class WindowQuick(Window):

    def __init__(self, width, height, fps, velocity, lst):
        super().__init__(width, height, fps, velocity)



        print(lst)
        self.list_draw = QuickListDraw(lst, self.window, self.width-self.width_for_scroll, self.height)
        self.elements.append(self.list_draw)

        # Buttons
        x = (self.width-self.width_for_scroll)/2
        y = self.height*(3/4)
        padding = 10
        self.button_prev = TextArea(self.window, x - self.width_button - padding, y, self.width_button,
                                    self.height_button, "prev")
        self.button_next = TextArea(self.window, x + padding, y, self.width_button, self.height_button, "next")
        self.elements.append(self.button_next)
        self.elements.append(self.button_prev)

        # Counter of steps
        x = (self.width-self.width_for_scroll)/2
        y = self.height*(3/4)-50
        padding = 10
        self.max_steps = Text(self.window, x + padding, y, str(len(self.list_draw.quick_sort_data.steps)))
        max_steps_width = self.max_steps.text.get_size()[0]
        self.current_number = Text(self.window, x - max_steps_width - padding, y, '0')

        self.elements.append(self.current_number)
        self.elements.append(self.max_steps)

    def click(self, prev=False):
        self.list_draw.button_clicked(prev)
        self.current_number.text = self.list_draw.step_counter

    def buttons_clicked_check(self, event):
        if self.button_next.rect.collidepoint(event.pos):
            if self.list_draw.step_counter < len(self.list_draw.quick_sort_data.steps):
                self.click()

        if self.button_prev.rect.collidepoint(event.pos):
            if 1 < self.list_draw.step_counter:
                self.click(True)


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
