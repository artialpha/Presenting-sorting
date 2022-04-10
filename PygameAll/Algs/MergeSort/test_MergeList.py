import copy
from unittest import TestCase
from PygameAll.Algs.MergeSort.MergeList import MergeList

first_test = [1, 2, 3, 4, 5, 6]
second_test = [11, 4, 5, 10, 1, 7, 6, 12, 3, 9, 2, 8]


class TestMergeList(TestCase):

    def test_merge(self):
        merge = MergeList(first_test)
        print(merge, 'print merge kiedy składa się z liczb')

        self.assertEqual(merge[0], 1)
        self.assertEqual(merge[1], 2)
        self.assertEqual(merge[:2], MergeList([1, 2]))
        self.assertEqual(merge[0:2], MergeList([1, 2]))
        self.assertEqual(merge[1:4], MergeList([2, 3, 4]))
        half = half = int(len(merge)/2)

        self.assertEqual(merge[:half], MergeList([1, 2, 3]))
        self.assertEqual(merge[half:], MergeList([4, 5, 6]))

        merge.cut_in_half()
        print(merge, 'merge after cutting in half for the first time')
        self.assertEqual(merge.a, MergeList([1, 2, 3]))
        self.assertEqual(merge.b, MergeList([4, 5, 6]))

        self.assertTrue(merge.a.out is merge)
        self.assertTrue(merge.b.out is merge)

        print(id(merge), 'id merge before [:]')
        merge_before = merge
        merge[:] = merge.a + merge.b
        print(merge, 'merge after merge[:] = [merge.a, merge.b] ')
        print(id(merge), 'id merge')
        self.assertEqual(merge, MergeList([1, 2, 3, 4, 5, 6]))
        self.assertTrue(merge is merge_before)
        merge.cut_in_half()
        print(merge)
        merge.a.cut_in_half()
        merge.b.cut_in_half()
        print(merge)

    def test_cut(self):
        merge = MergeList(second_test)
        print('merge before cut')
        print(merge)

        merge.cut_in_half()
        print('\nmerge after 1st cut')
        print(merge)

        merge.a.cut_in_half()
        merge.b.cut_in_half()
        print('\nmerge after 2nd cut on both a and b')
        print(merge)

        self.assertEqual(merge.a.a.index, '00')
        self.assertEqual(merge.a.b.index, '01')
        self.assertEqual(merge.b.a.index, '10')
        self.assertEqual(merge.b.b.index, '11')

        self.assertEqual(merge.a.a, merge[merge.a.a.index])
        self.assertEqual(merge.a.b, merge[merge.a.b.index])
        self.assertEqual(merge.b.a, merge[merge.b.a.index])
        self.assertEqual(merge.b.b, merge[merge.b.b.index])

        self.assertEqual(merge.a.a, merge['00'])
        self.assertEqual(merge.a.b, merge['01'])
        self.assertEqual(merge.b.a, merge['10'])
        self.assertEqual(merge.b.b, merge['11'])

        merge.a.a.cut_in_half()
        merge.b.b.cut_in_half()
        print('\nmerge after 3rd cut on a.a and b.b')
        print(merge)

        self.assertEqual(merge.a.a.a, merge['000'])
        self.assertEqual(merge.b.b.b, merge['111'])

        self.assertEqual(MergeList([11]), merge['000'])
        self.assertEqual(MergeList([2, 8]), merge['111'])

    def test_flat(self):
        data_flat = [
            ([0, 1, 2, 3, 4, 5, 6], list(range(7))),
            ([1, 2, 3], [1, 2, 3]),
            ([[0, 1, 2], [3, 4, 5]], [0, 1, 2, 3, 4, 5]),
            ([0, 1, 2, [3, 4, 5], 6, 7], list(range(8))),
            ([[0, 1, 2, 3], [4, 5, 6, 7]], list(range(8))),
            ([0, 1, 2, [3, [4, 5]], 6, 7], list(range(8))),
            ([[0, 1, 2], [3, [4, 5]], 6, 7], list(range(8))),
            ([[0, [1, 2]], [3, [4, 5]], [6, 7]], list(range(8))),
            ([0, 1, 2, [3, 4, [5, [6, 7]]], 8, 9, 10, 11, 12], list(range(13))),
            ([[0, 1, 2], [3, 4, [5, [6, 7]]], [8, 9, 10, 11, 12]], list(range(13))),
            ([0, [1, 2], [3, 4, [5, [6, 7]]], 8, 9, 10, 11, 12], list(range(13))),
            ([[[0], [1]], [2], [3, 4, [5, [6, 7]]], [[8, 9], [10, 11, 12]]], list(range(13))),
        ]

        # print(data_flat)
        for x in data_flat:
            merge = MergeList(x)
            to_flat = MergeList(x[0])
            flattened = merge.flat_list(to_flat)
            padding = 50
            print(f'{str(x[0]):{padding}} before flat, type of it', type(to_flat))
            print(f'{str(merge.flat_list(x[0])):{padding}} after flat\n')

            self.assertEqual(flattened, x[1])

    def test_repr(self):
        data_repr = [
            ([[0, 1, 2], [3, 4, 5]], [list(range(6)), [list(range(3)), list(range(3, 6))]]),
            ([[0, 1, 2, 4], [4, 5, 6, 7]], [list(range(8)), [list(range(4)), list(range(4, 8))]]),
            ([[[0, 1], [2, 3]], [[4, 5], [6, 7]]], [list(range(8)), [list(range(4)), list(range(4, 8))]]),
        ]

        for x in data_repr:
            merge = MergeList(x[0])
            print('start function create repr')
            merge.create_representation()
            print(merge.lst, 'merge lst')
            print(merge.representation, 'merge repr')

            for r in merge.representation:
                print(r)
            print('\n')



