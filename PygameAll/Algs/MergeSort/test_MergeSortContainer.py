import random
from unittest import TestCase
from MergeSortContainer import MergeSortContainer
from MergeList import MergeList

first_test = (
    #[93, 5, 56, 34, 29, 82, 14, 24, 39, 45],
    #[5, 1, 2, 4, 3],
    #[1, 3, 5, 4, 2],
    MergeList([9, 6, 10, 3, 2, 1, 7, 5, 4, 8]),
)

data_test = [MergeList(random.sample(range(100), 10)) for y in range(20)]


class TestMergeSortContainer(TestCase):
    def test_merge_sort(self):
        for test in first_test:
            merge = MergeSortContainer(test)
            test = merge.merge_sort(test)
            print('+++++++++++++++++++')
            #print(test)
            indexes = []
            for index, x in enumerate(merge.steps):
                if 'add_to_final_list' in str(x[0]):
                    indexes.append(index)
                    print(x[1], index, '\n')

            for index in indexes:
                args = merge.steps[index][1]
                merge.steps[index][0](args)
                print(merge.final_lst)

    # i want to know if MergeList can be sorted with merge_sort (and it should be)
    def test_data(self):
        for unsorted in data_test:
            merge = MergeSortContainer(unsorted)
            after_sorting = merge.merge_sort(unsorted)
            print(unsorted, 'before sorting, there sorted ->', type(sorted(unsorted)))
            print(after_sorting, 'after sorting\n')
            self.assertTrue(isinstance(unsorted, MergeList))
            self.assertTrue(isinstance(after_sorting, MergeList))
            self.assertEqual(sorted(unsorted), after_sorting)

