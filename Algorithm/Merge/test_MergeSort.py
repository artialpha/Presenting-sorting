from unittest import TestCase
from Algorithm.Merge.MergeSort import MergeSort

first_tests = [
    [[8, 2], [2, 8]],
    [[1, 3, 2, 4], [1, 2, 3, 4]],
    [[1, 3, 5, 2, 4, 6], [1, 2, 3, 4, 5, 6]],
    [[1, 3, 5, 9, 10, 2, 4, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
]

seconds_tests = [
    [[[1], [2]], [1, 2]],
    [[[1, 3], [2, 4]], [1, 2, 3, 4]],
    [[[1, 3, 4, 5, 9], [2, 6, 7, 8, 10]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
]


class TestMergeSort(TestCase):
    def test_merge(self):

        for test in first_tests:
            i1 = 0
            j1 = round(len(test[0])/2)-1
            i2 = j1+1
            j2 = len(test[0])-1

            merge = MergeSort()
            merge.merge(i1, j1, i2, j2, test[0])
            print(test[0])

            self.assertEqual(test[0], test[1])

    def test_merge2(self):

        for test in seconds_tests:
            merge = MergeSort()
            lst = merge.merge2(test[0][0], test[0][1])
            print(lst)

            self.assertEqual(lst, test[1])

