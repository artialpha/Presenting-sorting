from unittest import TestCase

import numpy as np

from QuickSort import QuickSort


class TestQuickSortPartition(TestCase):
    data_test = [
        [np.array([10, 2, 5, 1, 9, 4, 7, 3, 8, 6]), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
        [np.array([4, 1, 2, 10, 8, 3, 5, 6, 9, 7]), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
    ]

    def test_partition(self):
        for unsorted, after_sort in self.data_test:
            pivot_index = len(unsorted) - 1

            print(pivot_index, 'pivot index')
            print(unsorted[pivot_index], 'pivot value')
            print(unsorted, '\n')
            pivot_index = QuickSort.partition(0, len(unsorted) - 1, pivot_index, unsorted)
            print(pivot_index, 'pivot index')
            print(unsorted[pivot_index], 'pivot value')
            print(unsorted, '\n')
            msg_less = "elements before the pivot are smaller"
            msg_greater = "elements after the pivot are greater"

            for x in range(len(unsorted)):
                if x < pivot_index:
                    self.assertLess(unsorted[x], unsorted[pivot_index], msg_less)
                elif x > pivot_index:
                    self.assertGreater(unsorted[x], unsorted[pivot_index], msg_greater)


class TestQuickSortSortData(TestCase):
    data_test = [
        #[[10, 2, 5, 1, 9, 4, 7, 3, 8, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        [[4, 1, 2, 10, 8, 3, 5, 6, 9, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    ]

    def test_sort_data(self):
        for unsorted, after_sort in self.data_test:
            pivot_index = len(unsorted) - 1
            print(unsorted, "before quick")
            QuickSort.sort_data(0, len(unsorted) - 1, pivot_index, unsorted)
            print(unsorted, "after quick")
            print("RUNDA NASTEPNA")
