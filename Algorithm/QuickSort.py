from Sort import Sort


class QuickSort(Sort):

    def __init__(self, data):
        super().__init__(data)
        self.pivot_index = len(data) - 1

    @classmethod
    def sort_data(cls, left_index, right_index, pivot_index, data):
        pass

    @staticmethod
    def partition(left_index, right_index, pivot_index, data):

        while left_index < right_index:
            if data[left_index] > data[pivot_index]:
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
