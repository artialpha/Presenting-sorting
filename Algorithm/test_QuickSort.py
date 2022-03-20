import random
import numpy as np
from unittest import TestCase
from QuickSort import QuickSort


data_test = [random.sample(range(100), 10) for y in range(20)]


class TestQuickSortPartition(TestCase):

    def test_partition(self):
        for unsorted in data_test:
            pivot_index = len(unsorted) - 1

            print(pivot_index, 'pivot index')
            print(unsorted[pivot_index], 'pivot value')
            print(unsorted, '\n')
            pivot_index = QuickSort.partition(0, len(unsorted) - 1, unsorted)
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

    def test_sort_data(self):
        for unsorted in data_test:
            pivot_index = len(unsorted) - 1
            print(unsorted, "before quick")
            QuickSort.sort_data(0, len(unsorted) - 1, unsorted)
            print(unsorted, "after quick")
            print("RUNDA NASTEPNA")
            self.assertTrue(all(unsorted[i] <= unsorted[i+1] for i in range(len(unsorted) - 1)))
