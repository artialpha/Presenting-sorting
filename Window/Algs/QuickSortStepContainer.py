from Algorithm.QuickSort import QuickSort
import copy


class QuickSortStepContainer(QuickSort):

    def __init__(self, lst, draw=None):
        super().__init__()
        if draw:
            self.draw = draw
        self.lst = lst
        self.pivot_index = None
        self.left_index = None
        self.right_index = None
        self.steps = []

    def __iadd__(self, other):
        self.steps.append(other)
        return self

    def __getitem__(self, index):
        return self.steps[index]

    def __str__(self):
        return f'\nleft: i{self.left_index}, v{self.lst[self.left_index]}' \
               f'{self.lst}\nright: i{self.right_index}, v{self.lst[self.right_index]}' \
               f'\npivot: i{self.pivot_index}, v{self.lst[self.pivot_index]}'

    def prepare_steps(self):
        copy_list = copy.copy(self.lst)
        self.quick_sort(0, len(copy_list) - 1, copy_list)

    def quick_sort(self, left_index, right_index, data):
        if len(data) == 1:
            return data

        if left_index < right_index:
            # here i draw li, ri, pivot, edges
            pivot = self.partition(left_index, right_index, data)

            self.quick_sort(left_index, pivot - 1, data)
            self.quick_sort(pivot + 1, right_index, data)

    def partition(self, left_index, right_index, data):
        pivot_index = right_index
        self.steps.append((self.place_pivot_indexes,
                           (
                               (left_index, right_index, pivot_index),
                               (self.left_index, self.right_index, self.pivot_index)
                           )))

        while left_index < right_index:
            if data[left_index] >= data[pivot_index]:
                if data[right_index] < data[pivot_index]:
                    # swap values
                    data[left_index], data[right_index] = data[right_index], data[left_index]
                    self.steps.append((self.swap_index, ('left-right', )))
                else:
                    right_index -= 1
                    self.steps.append((self.move_index, ('right', -1)))
            else:
                left_index += 1
                self.steps.append((self.move_index, ('left', 1)))

        data[pivot_index], data[right_index] = data[right_index], data[pivot_index]
        self.steps.append((self.swap_index, ('right-pivot', )))
        self.left_index, self.right_index, self.pivot_index = left_index, right_index, pivot_index
        # right_index is the place of a new pivot
        return right_index

    def execute_steps(self):
        print("i do steps")
        i = 0

        print(self)
        while i < len(self.steps):
            self.steps[i][0](i)
            i += 1

    def step_back(self, index):
        # print('in step back')
        method = self.steps[index][0]
        method_arguments = self.steps[index][1]
        if method_arguments[0] == 'left' or method_arguments[0] == 'right':
            print(method_arguments)
            method(index, True)
        elif method_arguments[0] == 'left-right' or method_arguments[0] == 'right-pivot':
            method(index)
        else:
            print(method_arguments[1])
            method(index, True)

    def swap_index(self, i):
        method_arguments = self.steps[i][1]
        if method_arguments[0] == 'left-right':
            self.lst[self.left_index], self.lst[self.right_index] \
                = self.lst[self.right_index], self.lst[self.left_index]
        elif method_arguments[0] == 'right-pivot':
            self.lst[self.pivot_index], self.lst[self.right_index] \
                = self.lst[self.right_index], self.lst[self.pivot_index]
        else:
            print('i did not do anything', method_arguments)

    def move_index(self, i, step_back=False):
        direction, value = self.steps[i][1]
        if step_back:
            value *= (-1)
        if direction == 'left':
            self.left_index += value
        else:
            self.right_index += value

    def place_pivot_indexes(self, i, step_back=False):
        method_arguments = self.steps[i][1]
        new_places = method_arguments[1] if step_back else method_arguments[0]
        self.left_index = new_places[0]
        self.right_index = new_places[1]
        self.pivot_index = new_places[2]

    def reset_indexes(self):
        self.right_index, self.left_index, self.pivot_index = 0, 0, 0
