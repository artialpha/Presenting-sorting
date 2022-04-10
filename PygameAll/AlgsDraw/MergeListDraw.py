import copy
import math
from PygameAll.Algs.MergeSort.MergeSortContainer import MergeSortContainer
from PygameAll.Algs.MergeSort.MergeList import MergeList
from PygameAll.AlgsDraw.QuickListDraw import QuickListDraw
from PygameAll.Elements.Text import Text
from PygameAll.AlgsDraw.ListDraw import ListDraw
from PygameAll.Elements.DrawObject import DrawObject


class MergeListDraw(MergeList, DrawObject):

    def __init__(self, lst, window, x, y):
        super().__init__(lst)
        self.window = window
        self.width_window = x
        self.height_window = y

        self.merge_sort_data = MergeSortContainer(MergeList(lst))
        self.merge_sort_data.merge_sort(self.merge_sort_data.lst)
        self.state_counter = 0

        self.padding = 20
        self.size_digit = None
        self.size_number = None
        self.space_for_number = None

        self.lists_merge = []

        self.data_for_list()
        self.state_display()

    def data_for_list(self):
        lst = MergeList.flat_list(self.lst)
        number_of_digits = int(math.log10(max(lst)))+1
        self.size_digit = self.FONT.size(str(number_of_digits))
        self.size_number = self.size_digit[0]*number_of_digits
        self.space_for_number = self.size_number + self.padding
        # print(self.size_digit, self.size_number, self.space_for_number)

    def draw(self):
        for lst in self.lists_merge:
            lst.draw()

    def prepare_list_display(self, lst, x, y):
        temp = MergeList.flat_list(lst)
        temp = ListDraw(temp, self.window, x=x, y=y)
        if temp not in self.lists_merge:
            self.lists_merge.append(temp)
        print(lst, 'wyswietlam liste')
        y_diff = 40
        x_ratio = 30
        if lst.a:
            x_diff = x_ratio * len(lst.a)
            self.prepare_list_display(lst.a, x - x_diff, y + y_diff)
        if lst.b:
            x_diff = x_ratio * len(lst.b)
            self.prepare_list_display(lst.b, x + x_diff, y + y_diff)

    def state_display(self):
        state = self.merge_sort_data.states[self.state_counter]
        lst = state.whole_list
        self.prepare_list_display(lst, 300, 100)




        #self.prepare_list_display(lst_flat)


