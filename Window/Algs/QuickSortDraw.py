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
        self.steps.append((self.place_pivot_indexes, (left_index, right_index, pivot_index)))

        while left_index < right_index:
            if data[left_index] >= data[pivot_index]:
                if data[right_index] < data[pivot_index]:
                    # swap values
                    data[left_index], data[right_index] = data[right_index], data[left_index]
                    self.steps.append(self.swap_left_right)
                else:
                    right_index -= 1
                    self.steps.append(self.decrease_right)
            else:
                left_index += 1
                self.steps.append(self.increase_left)

        data[pivot_index], data[right_index] = data[right_index], data[pivot_index]
        self.steps.append(self.swap_right_pivot)
        # right_index is the place of a new pivot
        return right_index

    def perform_steps(self):
        print("i do steps")
        for step in self.steps:
            # print(step)
            if callable(step):
                step()
            else:
                step[0](*step[1])

    def swap_left_right(self):
        self.data[self.left_index], self.data[self.right_index] \
            = self.data[self.right_index], self.data[self.left_index]

    def swap_right_pivot(self):
        self.data[self.pivot_index], self.data[self.right_index] \
            = self.data[self.right_index], self.data[self.pivot_index]

    def decrease_right(self):
        self.right_index -= 1

    def increase_left(self):
        self.left_index += 1

    def place_pivot_indexes(self, *args):
        self.left_index = args[0]
        self.right_index = args[1]
        self.pivot_index = args[2]
