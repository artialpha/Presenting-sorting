import math
import pygame
pygame.init()


class Draw:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.SysFont("Times New Roman", 40)

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.lst = lst
        self.window = None
        self.list_display = None

        number_of_digits = int(math.log10(max(lst)))+1
        size_of_digit = self.FONT.size(str(number_of_digits))[0]

        self.size_of_number = size_of_digit*number_of_digits
        self.padding = 20
        print(self.size_of_number, 'self.size_of_number')
        self.space_for_number = self.size_of_number + self.padding
        print(self.space_for_number, 'self.space_for_number')

        self.draw_window()
        self.prepare_list_display()

    def draw_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.WHITE)

    def prepare_list_display(self):
        x = (self.width - self.space_for_number + self.padding) / 2
        y = self.height / 4

        length_lst_half = int(len(self.lst) / 2)

        #print(self.lst, x, y)
        #print(self.FONT.size('5'))
        list_cords = [(x + element*self.space_for_number, y) for element in range(-length_lst_half, length_lst_half+1)]
        self.list_display = list(zip(self.lst, list_cords))

    '''
            display_list
            i want to display the list horizontally in the middle 
            so i need to take into consideration how much space the list takes
            i use self.FONT.size(...) to determine it 
            it returns a tuple (width, height)
            https://www.pygame.org/docs/ref/font.html#pygame.font.Font.size
    '''
    def display_list(self):
        for number, cords in self.list_display:
            number_display = self.FONT.render(str(number), True, self.BLACK)
            self.window.blit(number_display, cords)

    def swap(self):
        pass
