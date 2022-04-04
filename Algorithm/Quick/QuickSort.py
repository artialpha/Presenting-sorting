from Algorithm.Sort import Sort


class QuickSort(Sort):

    def __init__(self):
        super().__init__()

    @classmethod
    def sort_data(cls, left_index, right_index, data):
        if len(data) == 1:
            return data

        if left_index < right_index:
            # here i draw li, ri, pivot, edges
            pivot = cls.partition(left_index, right_index, data)

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

        data[pivot_index], data[right_index] = data[right_index], data[pivot_index]
        # right_index is the place of a new pivot
        return right_index
