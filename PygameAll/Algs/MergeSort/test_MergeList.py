from unittest import TestCase
from PygameAll.Algs.MergeSort.MergeList import MergeList

first_test = [1, 2, 3, 4, 5, 6]


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
