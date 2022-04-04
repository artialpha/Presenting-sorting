from unittest import TestCase
from QuickSortStepContainer import QuickSortStepContainer
import copy
import random

first_test = (
    [5, 1, 2, 4, 3],
    #[1, 3, 5, 4, 2],
    #[9, 6, 3, 2, 1, 7, 5, 4, 8]
)

data_test = [random.sample(range(100), 10) for y in range(20)]


class TestQuickSortDraw(TestCase):

    def test_step_back_1(self):
        """
        list of steps for test: [5, 1, 2, 4, 3]
        ((0, 4, 4), (0, 0, 0)) counter 0
        ('right', -1) counter 1             r3
        ('right', -1) counter 2             r2
        ('left-right',) counter 3           [2, 1, 5, 4, 3]
        ('left', 1) counter 4               l1
        ('left', 1) counter 5               l2
        ('right-pivot',) counter 6          [2, 1, 3, 4, 5]
        ((0, 1, 1), (2, 2, 4)) counter 7    l0 r1 p1 PREV: 2, 2, 4
        ('right', -1) counter 8             r0
        ('right-pivot',) counter 9          [1, 2, 3, 4, 5]
        ((3, 4, 4), (0, 0, 1)) counter 10   l3 r4 p4
        ('left', 1) counter 11              l4
        ('right-pivot',) counter 12

        :return:
        """

        draw_list = []

        for unsorted in first_test:
            print(unsorted, 'unsorted')
            draw = QuickSortStepContainer(unsorted)
            draw.quick_sort(0, len(unsorted) - 1, copy.copy(unsorted))
            draw_list.append(draw)

        for draw in draw_list:
            for count, step in enumerate(draw.steps):
                print(step[1], f'counter {count}')

        draw_to_test = draw_list[0]
        step = 0

        # 0 step = place pivot, right and left
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.right_index, 4)

        # 1 step = right--
        step += 1
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.right_index, 3)

        # 2 step = right --
        step += 1
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.right_index, 2)

        # 3 step = swap left nad right value
        # before swap:  left = 5, right = 2
        # after:        right = 2, left = 5
        step += 1
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 2)
        self.assertEqual(draw_to_test.lst[draw_to_test.left_index], 5)
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 5)
        self.assertEqual(draw_to_test.lst[draw_to_test.left_index], 2)
        print(draw_to_test, '')

        # Now i go back
        # performing a "step back" should swap back values at left and right index
        # I don't change the value of the step because I want to undo step at this index
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 2)
        self.assertEqual(draw_to_test.lst[draw_to_test.left_index], 5)

        # Undo 2 step - it means that right index should be increased by one
        step -= 1
        self.assertEqual(draw_to_test.right_index, 2)
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.right_index, 3)

        # Undo 1 step - it means that right index should be increased by one
        step -= 1
        self.assertEqual(draw_to_test.right_index, 3)
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.right_index, 4)

        # undo 0 step - place indexes back to the starting position
        self.assertEqual(draw_to_test.left_index, 0)
        self.assertEqual(draw_to_test.right_index, 4)
        self.assertEqual(draw_to_test.pivot_index, 4)
        step -= 1
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.left_index, None)
        self.assertEqual(draw_to_test.right_index, None)
        self.assertEqual(draw_to_test.pivot_index, None)

        print(step, 'step 0')
        # move to 4th step
        for s in range(5):
            draw_to_test.steps[s][0](s)
            print(s, 's')
            step = s
        self.assertEqual(draw_to_test.left_index, 1)

        # 5 step
        step += 1
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.left_index, 2)

        # 6 step swap values of right and pivot
        step += 1
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 5)
        self.assertEqual(draw_to_test.lst[draw_to_test.pivot_index], 3)
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 3)
        self.assertEqual(draw_to_test.lst[draw_to_test.pivot_index], 5)

        # 7 step new place for indexes
        step += 1
        self.assertEqual(draw_to_test.left_index, 2)
        self.assertEqual(draw_to_test.right_index, 2)
        self.assertEqual(draw_to_test.pivot_index, 4)
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.left_index, 0)
        self.assertEqual(draw_to_test.right_index, 1)
        self.assertEqual(draw_to_test.pivot_index, 1)

        # 8 step
        step += 1
        self.assertEqual(draw_to_test.right_index, 1)
        draw_to_test.steps[step][0](step)
        self.assertEqual(draw_to_test.right_index, 0)

        # undo 8step
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.right_index, 1)

        # undo 7step
        step -= 1
        self.assertEqual(draw_to_test.left_index, 0)
        self.assertEqual(draw_to_test.right_index, 1)
        self.assertEqual(draw_to_test.pivot_index, 1)
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.left_index, 2)
        self.assertEqual(draw_to_test.right_index, 2)
        self.assertEqual(draw_to_test.pivot_index, 4)

        # undo 7step
        step -= 1
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 3)
        self.assertEqual(draw_to_test.lst[draw_to_test.pivot_index], 5)
        draw_to_test.step_back(step)
        self.assertEqual(draw_to_test.lst[draw_to_test.right_index], 5)
        self.assertEqual(draw_to_test.lst[draw_to_test.pivot_index], 3)

    def test_first_test(self):
        draw_list = []

        for unsorted in first_test:
            draw = QuickSortStepContainer(copy.copy(unsorted))
            draw.quick_sort(0, len(unsorted) - 1, copy.copy(unsorted))
            draw.reset_indexes()
            draw_list.append(draw)

        for draw in draw_list:
            print(draw.lst, 'before')
            draw.execute_steps()
            print(draw.lst, 'after\n')

        for draw in draw_list:
            self.assertTrue(all(draw.lst[i] <= draw.lst[i + 1] for i in range(len(draw.lst) - 1)))

    def test_data_test(self):
        draw_list = []

        for unsorted in data_test:
            draw = QuickSortStepContainer(copy.copy(unsorted))
            draw.quick_sort(0, len(unsorted) - 1, unsorted)
            draw_list.append(draw)

        for draw in draw_list:
            print(draw.lst, 'before')
            draw.execute_steps()
            print(draw.lst, 'after\n')

        for draw in draw_list:
            self.assertTrue(all(draw.lst[i] <= draw.lst[i + 1] for i in range(len(draw.lst) - 1)))