import copy
import math
import pygame
from PygameAll.Algs.MergeSort.MergeSortContainer import MergeSortContainer
from PygameAll.Algs.MergeSort.MergeList import MergeList
from PygameAll.AlgsDraw.QuickListDraw import QuickListDraw
from PygameAll.Elements.Text import Text
from PygameAll.AlgsDraw.ListDraw import ListDraw
from PygameAll.Elements.DrawObject import DrawObject


class MergeListDraw(MergeList, DrawObject):
    x, y = 300, 25
    cords_replace = (300, 300)
    letter_move_y = 30

    def __init__(self, lst, window, x, y):
        super().__init__(lst)
        self.window = window
        self.width_window = x
        self.height_window = y

        self.merge_sort_data = MergeSortContainer(MergeList(lst))
        self.merge_sort_data.get_states(self.merge_sort_data.lst)
        self.state_counter = 0

        self.padding = 20
        self.size_digit = None
        self.size_number = None
        self.space_for_number = None

        self.lists_merge = []
        self.letters = []
        self.list_merged = None

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
        self.window.fill(self.BACKGROUND_COLOR)
        for lst in self.lists_merge:
            lst.draw()
        for letter in self.letters:
            letter.draw()

    def prepare_list_display(self, lst, x, y, ind=None):
        temp = MergeList.flat_list(lst)
        temp = ListDraw(temp, self.window, x=x, y=y, index=lst.index)
        if temp not in self.lists_merge:
            self.lists_merge.append(temp)

    @staticmethod
    def calculate_position_from_index(index):
        if index:
            x_start = 120
            x_pos = 0
            index = index[1:len(index)]
            for digit in index:
                if digit == '1':
                    x_pos += x_start
                else:
                    x_pos -= x_start
                x_start /= 2
            y_pos = len(index) * 60
            return x_pos, y_pos
        return 0, 0

    def state_display(self):
        state = self.merge_sort_data.states[self.state_counter]
        print(state)
        if lists := state.lists_created:
            for lst in lists:
                x_diff, y_dif = self.calculate_position_from_index(lst.index)
                self.prepare_list_display(lst, self.x + x_diff, self.y + y_dif, lst.index)

        if replace_list := state.replace_list:
            self.letters.clear()
            if self.cords_replace in self.lists_merge:
                self.lists_merge.remove(self.cords_replace)
            self.prepare_list_display(replace_list, *self.cords_replace, None)

        if index_replace := state.index_replace:
            replace_list = state.replace_list
            replace_list.index = state.index_replace

            diff_out = self.calculate_position_from_index(index_replace)
            diff_a = self.calculate_position_from_index(index_replace + '0')
            diff_b = self.calculate_position_from_index(index_replace + '1')
            to_remove = (diff_out, diff_a, diff_b)

            if (self.x, self.y) in self.lists_merge:
                for rem in to_remove:
                    self.lists_merge.remove((self.x + rem[0], self.y + rem[1]))
            self.lists_merge.remove(self.cords_replace)
            self.prepare_list_display(replace_list, self.x + diff_out[0], self.y + diff_out[1])

        if index_list := state.index_list:
            self.letters.clear()
            ia = self.lists_merge.index(index_list + '0')
            # why j is under 7 in replace list? in 13 79 replace 79
            ib = self.lists_merge.index(index_list + '1')
            list_a = self.lists_merge[ia]
            list_b = self.lists_merge[ib]

            i = Text(self.window, list_a[state.index_a][1][0], list_a[state.index_a][1][1] + self.letter_move_y, 'i')
            j = Text(self.window, list_b[state.index_b][1][0], list_b[state.index_b][1][1] + self.letter_move_y, 'j')
            if i not in self.letters:
                self.letters.append(i)
                self.letters.append(j)

    def reverse_state(self):
        state = self.merge_sort_data.states[self.state_counter]

        # i remove lists from the step that have been created
        if lists := state.lists_created:
            for lst in lists:
                self.lists_merge.remove(lst)

        if index_list := state.index_list:
            self.letters.clear()
            if state.index_a != 0 and state.index_b != 0 or state.replace_list:
                self.draw_indexes(state, index_list)

        if replace_list := state.replace_list:
            if len(replace_list) == 1 and state.index_a == 0 and state.index_b == 0:
                self.lists_merge.remove(self.cords_replace)
            elif self.merge_sort_data.states[self.state_counter-1].replace_list != replace_list:
                replace_list = replace_list[:-1]
                if self.cords_replace in self.lists_merge:
                    self.lists_merge.remove(self.cords_replace)
                self.prepare_list_display(replace_list, *self.cords_replace, None)
            else:
                self.prepare_list_display(replace_list, *self.cords_replace, None)

        if index_replace := state.index_replace:
            prev_state = self.merge_sort_data.states[self.state_counter-2]

            prev_list = MergeList(state.whole_list[index_replace[1:]].original_list)
            half = int(len(prev_list)/2)
            prev_list_a = prev_list[:half]
            prev_list_a.index = index_replace + '0'
            prev_list_b = prev_list[half:]
            prev_list_b.index = index_replace + '1'

            diff_out = self.calculate_position_from_index(index_replace)
            # it shouldn't remove the last but the list with index_replace
            self.lists_merge.remove((self.x + diff_out[0], self.y + diff_out[1]))

            x_diff, y_dif = self.calculate_position_from_index(index_replace)
            self.prepare_list_display(prev_list, self.x + x_diff, self.y + y_dif, index_replace)

            x_diff, y_dif = self.calculate_position_from_index(index_replace + '0')
            self.prepare_list_display(prev_list_a, self.x + x_diff, self.y + y_dif, index_replace + '0')

            x_diff, y_dif = self.calculate_position_from_index(index_replace + '1')
            self.prepare_list_display(prev_list_b, self.x + x_diff, self.y + y_dif, index_replace + '1')

            self.draw_indexes(prev_state, index_replace)
        self.state_counter -= 1

    def draw_indexes(self, state, index_list):
        ia = self.lists_merge.index(index_list + '0')
        ib = self.lists_merge.index(index_list + '1')
        print(index_list, 'index_list')
        for lst in self.lists_merge:
            print(lst, lst.index)
        list_a = self.lists_merge[ia]
        list_b = self.lists_merge[ib]

        i = Text(self.window, list_a[state.index_a][1][0], list_a[state.index_a][1][1] + self.letter_move_y, 'i')
        j = Text(self.window, list_b[state.index_b][1][0], list_b[state.index_b][1][1] + self.letter_move_y, 'j')
        if i not in self.letters:
            self.letters.append(i)
            self.letters.append(j)