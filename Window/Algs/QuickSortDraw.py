from Algorithm.QuickSort import QuickSort


class QuickSortDraw(QuickSort):

    def __init__(self, data, draw=None):
        super().__init__()
        if draw:
            self.draw = draw
        self.data = data
        self.pivot_index = 0
        self.left_index = 0
        self.right_index = 0
        self.steps = []

    def __iadd__(self, other):
        self.steps.append(other)
        return self

    def __getitem__(self, index):
        return self.steps[index]

    def __str__(self):
        return f'{self.data}\nright: i{self.right_index}, v{self.data[self.right_index]}' \
               f'\nleft: i{self.left_index}, v{self.data[self.left_index]}' \
               f'\npivot: i{self.pivot_index}, v{self.data[self.pivot_index]}'

    def sort_data(self, left_index, right_index, data):
        if len(data) == 1:
            return data

        if left_index < right_index:
            # here i draw li, ri, pivot, edges
            pivot = self.partition(left_index, right_index, data)

            self.sort_data(left_index, pivot-1, data)
            self.sort_data(pivot+1, right_index, data)

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

    def perform_steps(self):
        print("i do steps")
        i = 0

        while i < len(self.steps):
            self.steps[i][0](*self.steps[i][1])
            i += 1

        '''
        print(self)
        while i < len(self.steps):

            x = input()
            if x == 'next':
                print(self.steps[i])

                self.steps[i][0](*self.steps[i][1])
                print('after step', i)
                print(self)
                i += 1
            elif x == 'prev' and i != 0:
                i -= 1
            print("nothing")
        '''

    def step_back(self, index):
        # print('in step back')
        method = self.steps[index][0]
        method_arguments = self.steps[index][1]
        if method_arguments[0] == 'left' or method_arguments[0] == 'right':
            index, value = method_arguments
            value *= -1
            method(*(index, value))
        elif method_arguments[0] == 'left-right' or method_arguments[0] == 'right-pivot':
            method(*method_arguments)
        else:
            print(method_arguments[1])
            method(method_arguments[1])

    def swap_index(self, *args):
        if args[0] == 'left-right':
            self.data[self.left_index], self.data[self.right_index] \
                = self.data[self.right_index], self.data[self.left_index]
        elif args[0] == 'right-pivot':
            self.data[self.pivot_index], self.data[self.right_index] \
                = self.data[self.right_index], self.data[self.pivot_index]
        else:
            print('i did not do anything', args)

    def swap_left_right(self):
        self.data[self.left_index], self.data[self.right_index] \
            = self.data[self.right_index], self.data[self.left_index]

    def swap_right_pivot(self):
        self.data[self.pivot_index], self.data[self.right_index] \
            = self.data[self.right_index], self.data[self.pivot_index]

    def move_index(self, *args):
        if args[0] == 'left':
            self.left_index += args[1]
        else:
            self.right_index += args[1]

    def place_pivot_indexes(self, *args):
        new_places = args[0]
        self.left_index = new_places[0]
        self.right_index = new_places[1]
        self.pivot_index = new_places[2]
