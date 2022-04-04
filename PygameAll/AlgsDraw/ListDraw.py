import math
from PygameAll.Elements.DrawObject import DrawObject


class ListDraw(DrawObject):

    def __init__(self, lst, window, x, y):
        super().__init__(x=x, y=y, window=window)
        self.lst = lst
        self.list_display = None
        self.step_counter = 0

        number_of_digits = int(math.log10(max(lst)))+1
        self.size_of_digit_x, self.size_of_digit_y = self.FONT.size(str(number_of_digits))

        self.size_of_number = self.size_of_digit_x*number_of_digits
        self.padding = 20
        # print(self.size_of_number, 'self.size_of_number') 2 digits size x = 30 for FONT=30
        self.space_for_number = self.size_of_number + self.padding
        # print(self.space_for_number, 'self.space_for_number')
        self.prepare_list_display()
        print(self.list_display)

    def __getitem__(self, item):
        return self.list_display[item]

    def draw(self):
        self.window.fill(self.BACKGROUND_COLOR)
        for number, cords in self.list_display:
            number_display = self.FONT.render(str(number), True, self.TEXT_COLOR)
            self.window.blit(number_display, cords)

    def prepare_list_display(self):
        length_lst_half = (len(self.lst) / 2)
        y = self.y / 4

        if length_lst_half.is_integer():
            length_lst_half = int(length_lst_half)
            x = (self.x + self.padding) / 2

            list_cords = [[x + element*self.space_for_number, y] for element in
                          range(-length_lst_half, length_lst_half)]
        else:
            length_lst_half = int(length_lst_half)
            x = (self.x - self.size_of_number) / 2

            list_cords = [[x + element*self.space_for_number, y] for element in
                          range(-length_lst_half, length_lst_half+1)]
        self.list_display = list((list(i) for i in zip(self.lst, list_cords)))

