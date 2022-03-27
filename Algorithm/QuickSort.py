from Sort import Sort
import random


class QuickSort(Sort):

    def __init__(self, data, draw):
        super().__init__(data)
        self.pivot_index = len(data) - 1
        self.draw = draw

    @classmethod
    def sort_data(cls, left_index, right_index, data):
        if len(data) == 1:
            return data

        if left_index < right_index:
            pivot = cls.partition(left_index, right_index, data)
            # here i draw li, ri, pivot, edges
            cls.sort_data(left_index, pivot-1, data)
            cls.sort_data(pivot+1, right_index, data)

    @staticmethod
    def partition(left_index, right_index, data):
        pivot_index = right_index

        while left_index < right_index:
            if data[left_index] >= data[pivot_index]:
                if data[right_index] < data[pivot_index]:
                    # swap values
                    data[left_index], data[right_index] = data[right_index], data[left_index]
                else:
                    right_index -= 1
            else:
                left_index += 1

        pivot_index, right_index = right_index, pivot_index
        data[pivot_index], data[right_index] = data[right_index], data[pivot_index]
        return pivot_index
