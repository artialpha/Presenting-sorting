from unittest import TestCase

from PygameAll.Window.WindowMerge import WindowMerge

first_test = [
    [3, 1, 9, 4, 2, 5, 6, 7, 0, 8]
]


class TestMergeListDraw(TestCase):
    def test_state_display(self):

        def show_lists(lists):
            for x in lists:
                print(x)

        width = 600
        height = 400

        for test in first_test:
            window = WindowMerge(width, height, test)
            counter = window.list_draw.state_counter
            states = window.list_draw.merge_sort_data.states
            lists = window.list_draw.lists_merge

            show_lists(lists)
            print(counter)
            print(states[counter])

            window.list_draw.state_counter += 10
            print(window.list_draw.state_counter, ' counter')
            window.list_draw.state_display()
            show_lists(lists)
