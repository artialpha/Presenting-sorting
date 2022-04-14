import math

from PygameAll.Algs.MergeSort.MergeList import MergeList
from PygameAll.Elements.DrawObject import DrawObject


class ListDraw(DrawObject):

    def __init__(self, lst, window, x=None, y=None, width=None, height=None, index=None):
        super().__init__(x=x, y=y, window=window)
        self.lst = lst
        self.list_display = None
        self.step_counter = 0
        self.width = width
        self.height = height
        self.index = index

        number_of_digits = int(math.log10(max(lst)))+1
        self.size_of_digit_x, self.size_of_digit_y = self.FONT.size(str(number_of_digits))

        self.size_of_number = self.size_of_digit_x*number_of_digits
        self.padding = 20
        # print(self.size_of_number, 'self.size_of_number') 2 digits size x = 30 for FONT=30
        self.space_for_number = self.size_of_number + self.padding
        # print(self.space_for_number, 'self.space_for_number')
        self.prepare_list_display()

    def __getitem__(self, item):
        return self.list_display[item]

    def __eq__(self, other):
        if isinstance(other, ListDraw):
            return self.list_display == other.list_display
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        elif isinstance(other, str):
            return self.index == other
        elif isinstance(other, MergeList):
            print(self.lst)
            return self.lst == other

    def __str__(self):
        return str(self.list_display)

    def __repr__(self):
        return str(self.list_display)

    def draw(self):
        for number, cords in self.list_display:
            number_display = self.FONT.render(str(number), True, self.TEXT_COLOR)
            self.window.blit(number_display, cords)

    def prepare_list_display(self):
        length_lst_half = (len(self.lst) / 2)
        if self.height:
            y = self.height / 4
        else:
            y = self.y

        if length_lst_half.is_integer():
            length_lst_half = int(length_lst_half)
            if self.width:
                x = (self.width + self.padding) / 2
            else:
                x = self.x + self.padding/2

            list_cords = [[x + element*self.space_for_number, y] for element in
                          range(-length_lst_half, length_lst_half)]
        else:
            length_lst_half = int(length_lst_half)
            if self.width:
                x = (self.width - self.size_of_number) / 2
            else:
                x = self.x - self.size_of_number/2

            list_cords = [[x + element*self.space_for_number, y] for element in
                          range(-length_lst_half, length_lst_half+1)]
        self.list_display = list((list(i) for i in zip(self.lst, list_cords)))
