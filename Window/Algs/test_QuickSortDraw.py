from unittest import TestCase
from QuickSortDraw import QuickSortDraw
import copy
import random

first_test = (
    [5, 1, 2, 4, 3],
    [1, 3, 5, 4, 2],
    [9, 6, 3, 2, 1, 7, 5, 4, 8]
)

data_test = [random.sample(range(100), 10) for y in range(20)]


class TestQuickSortDraw(TestCase):

    def test_first_test(self):
        draw_list = []

        for unsorted in first_test:
            draw = QuickSortDraw(copy.copy(unsorted))
            draw.sort_data(0, len(unsorted)-1, unsorted)
            draw_list.append(draw)

        for draw in draw_list:
            print(draw.data, 'before')
            draw.perform_steps()
            print(draw.data, 'after')

        for draw in draw_list:
            self.assertTrue(all(draw.data[i] <= draw.data[i+1] for i in range(len(draw.data) - 1)))

    def test_data_test(self):
        draw_list = []

        for unsorted in data_test:
            draw = QuickSortDraw(copy.copy(unsorted))
            draw.sort_data(0, len(unsorted)-1, unsorted)
            draw_list.append(draw)

        for draw in draw_list:
            print(draw.data, 'before')
            draw.perform_steps()
            print(draw.data, 'after\n')

        for draw in draw_list:
            self.assertTrue(all(draw.data[i] <= draw.data[i+1] for i in range(len(draw.data) - 1)))