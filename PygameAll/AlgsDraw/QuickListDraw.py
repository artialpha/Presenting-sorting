from PygameAll.Algs.QuickSort.QuickSortStepContainer import QuickSortStepContainer
from PygameAll.Elements.Text import Text
from PygameAll.AlgsDraw.ListDraw import ListDraw
import copy


class QuickListDraw(ListDraw):
    def __init__(self, lst, window, x=None, y=None, width=None, height=None):
        super().__init__(lst=lst, x=x, y=y, window=window, width=width, height=height)

        self.quick_sort_data = QuickSortStepContainer(copy.copy(lst))
        self.quick_sort_data.prepare_steps()
        self.left_index = None
        self.right_index = None
        self.pivot_index = None

    def draw(self):
        super(QuickListDraw, self).draw()
        if self.left_index:
            self.left_index.draw()
            self.right_index.draw()
            self.pivot_index.draw()

    def button_clicked(self, prev=False):
        qs_data = self.quick_sort_data
        if 0 <= self.step_counter <= len(qs_data.steps):
            if prev:
                self.step_counter -= 1
                qs_data.step_back(self.step_counter)
            step = qs_data[self.step_counter]
            method = step[0]
            arguments = step[1]
            # make this step in a container
            if not prev:
                method(self.step_counter)

            if arguments[0] == 'left':
                self.move_index(self.left_index, prev)
            elif arguments[0] == 'right':
                self.move_index(self.right_index, prev)
            elif arguments[0] == 'left-right' or arguments[0] == 'right-pivot':
                self.swap_values()
            else:
                if self.left_index:
                    self.draw_indexes(self.left_index, self.right_index, self.pivot_index, prev)
                else:
                    self.left_index, self.right_index, self.pivot_index = self.draw_indexes(prev)
                    print(self.left_index, self.right_index, self.pivot_index)
            if not prev:
                self.step_counter += 1

    def move_index(self, index_to_move, prev=False):
        digit_x_size = self.size_of_number
        padding = self.padding

        steps = self.quick_sort_data
        arguments = steps[self.step_counter][1]
        index, movement = arguments

        movement = -movement if prev else movement

        index_to_move.x += (digit_x_size+padding) * movement

    def swap_values(self):
        step = self.quick_sort_data[self.step_counter]
        left_index = self.quick_sort_data.left_index
        right_index = self.quick_sort_data.right_index
        pivot_index = self.quick_sort_data.pivot_index

        lst = self.list_display

        if step[1][0] == 'left-right':
            lst[left_index][0], lst[right_index][0] = lst[right_index][0], lst[left_index][0]
        else:
            lst[pivot_index][0], lst[right_index][0] = lst[right_index][0], lst[pivot_index][0]

    def draw_indexes(self,  left_index=None, right_index=None, pivot_index=None, prev=False):
        digit_y_size = self.size_of_digit_y

        step = self.quick_sort_data[self.step_counter]

        print(step[1][0], 'next')
        print(step[1][1], 'prev')
        # indexes
        if prev:
            left, right, pivot = step[1][1]
        else:
            left, right, pivot = step[1][0]

        # take tuple which consists of information value + position
        left_number = self[left]
        right_number = self[right]
        pivot_number = self[pivot]

        left_x, left_y = left_number[1]
        right_x, right_y = right_number[1]
        pivot_x, pivot_y = pivot_number[1]

        if left_index:
            left_index.x, left_index.y = left_x, left_y + digit_y_size
            right_index.x, right_index.y = right_x, right_y + digit_y_size
            pivot_index.x, pivot_index.y = pivot_x, pivot_y - digit_y_size
        else:
            left_index = Text(self.window, left_x, left_y + digit_y_size, 'i')
            right_index = Text(self.window, right_x, right_y + digit_y_size, 'j')
            pivot_index = Text(self.window, pivot_x, pivot_y - digit_y_size, 'p')
            return left_index, right_index, pivot_index
