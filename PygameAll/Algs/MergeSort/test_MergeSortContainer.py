import random
import copy
from unittest import TestCase
from MergeSortContainer import MergeSortContainer
from MergeList import MergeList

first_test = (
    #[93, 5, 56, 34, 29, 82, 14, 24, 39, 45],
    #[5, 1, 2, 4, 3],
    #[1, 3, 5, 4, 2],
    MergeList([9, 6, 10, 3, 2, 1, 7, 5, 4, 8]),
)

data_test = [MergeList(random.sample(range(100), 10)) for y in range(40)]


class TestMergeSortContainer(TestCase):

    def test_execute_steps(self):
        for test in first_test:
            merge = MergeSortContainer(test)
            #merge.merge_sort(copy.deepcopy(test))

            print('at the start merge.lst', merge.lst)
            merge.merge_sort(merge.lst)
            print('after mergesort', merge.lst)
            merge.show_states()

    # i want to know if MergeList can be sorted with merge_sort (and it should be)
    def test_data(self):
        for unsorted, for_merge in zip(data_test, copy.deepcopy(data_test)):
            merge = MergeSortContainer(for_merge)
            after_sorting = merge.merge_sort(for_merge)
            print(unsorted, 'before sorting, there sorted ->', sorted(unsorted))
            print(after_sorting, 'after sorting\n')
            self.assertTrue(isinstance(unsorted, MergeList))
            self.assertTrue(isinstance(after_sorting, MergeList))
            self.assertEqual(sorted(unsorted), after_sorting)

    def test_cut(self):
        data = [3, 5, 8, 2, 10, 1, 4, 7, 9, 6]
        data_cut1_a = [3, 5, 8, 2, 10]
        data_cut1_b = [1, 4, 7, 9, 6]
        data_cut1 = [[3, 5, 8, 2, 10], [1, 4, 7, 9, 6]]

        merge = MergeSortContainer(data)
        self.assertEqual(merge.lst, MergeList([3, 5, 8, 2, 10, 1, 4, 7, 9, 6]))
        merge.cut_in_half()

        print('merge first cut in half')
        self.assertEqual(merge.lst, MergeList(data_cut1))
        self.assertEqual(merge.lst.a, MergeList(data_cut1_a))
        self.assertEqual(merge.lst.b, MergeList(data_cut1_b))
        self.assertTrue(merge.lst.a.out == merge.lst)
        self.assertTrue(merge.lst.b.out == merge.lst)
        print(merge.lst, 'merge.lst')
        print(merge.lst.a, 'merge.lst.a')
        print(merge.lst.b, 'merge.lst.a')

        # second cut on merge.lst.a
        data_cut2 = [[[3, 5], [8, 2, 10]], [1, 4, 7, 9, 6]]
        data_cut2_aa = [3, 5]
        data_cut2_ab = [8, 2, 10]
        data_cut2_a = [[3, 5], [8, 2, 10]]
        merge.lst.a.cut_in_half()
        self.assertEqual(merge.lst, MergeList(data_cut2))
        self.assertEqual(merge.lst.b, MergeList(data_cut1_b))   # it should remain untouched
        self.assertEqual(merge.lst.a, MergeList(data_cut2_a))
        self.assertEqual(merge.lst.a.a, MergeList(data_cut2_aa))
        self.assertEqual(merge.lst.a.b, MergeList(data_cut2_ab))
        self.assertTrue(merge.lst.a == merge.lst.a.a.out)
        self.assertTrue(merge.lst.a == merge.lst.a.b.out)

        print('\nmerge second cut')
        print(merge.lst, 'merge.lst')
        print(merge.lst.a, 'merge.lst.a')
        print(merge.lst.b, 'merge.lst.a')

        # third cut on merge.lst.a
        data_cut3 = [[[3, 5], [8, 2, 10]], [[1, 4], [7, 9, 6]]]
        data_cut3_ba = [1, 4]
        data_cut3_bb = [7, 9, 6]
        data_cut3_b = [[1, 4], [7, 9, 6]]
        merge.lst.b.cut_in_half()
        self.assertEqual(merge.lst, MergeList(data_cut3))
        self.assertEqual(merge.lst.a, MergeList(data_cut2_a))   # it shouldn't change
        self.assertEqual(merge.lst.b.a, MergeList(data_cut3_ba))
        self.assertEqual(merge.lst.b.b, MergeList(data_cut3_bb))
        self.assertEqual(merge.lst.b, MergeList(data_cut3_b))
        self.assertTrue(merge.lst.b == merge.lst.b.a.out)
        self.assertTrue(merge.lst.b == merge.lst.b.b.out)

        print('\nmerge third cut')
        print(merge.lst, 'merge.lst')
        print(merge.lst.a, 'merge.lst.a')
        print(merge.lst.b, 'merge.lst.a')

        # when a mergelist is already cut - i shouldn't do it and return None
        self.assertEqual(None, merge.cut_in_half())

