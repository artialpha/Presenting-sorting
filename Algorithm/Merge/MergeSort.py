from Algorithm.Sort import Sort


class MergeSort(Sort):

    def __init__(self):
        super().__init__()

    @staticmethod
    def sort_data(data):
        if len(data) == 1:
            return data

        half = int(len(data)/2)
        lst1 = MergeSort.sort_data(data[:half])
        lst2 = MergeSort.sort_data(data[half:])
        print(lst1, lst2)
        return MergeSort.merge(lst1, lst2)

    @staticmethod
    def merge(lst1, lst2):
        i = 0
        j = 0
        replace_lst = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                replace_lst.append(lst1[i])
                i += 1
            else:
                replace_lst.append(lst2[j])
                j += 1

        if i == len(lst1):
            replace_lst.extend(lst2[j:])
        else:
            replace_lst.extend(lst1[i:])

        return replace_lst

    @staticmethod
    def merge2(i1, j1, i2, j2, data):
        replace_lst = []
        keep_i1 = i1
        while i1 <= j1 and i2 <= j2:
            if data[i1] < data[i2]:
                replace_lst.append(data[i1])
                i1 += 1
            else:
                replace_lst.append(data[i2])
                i2 += 1

        if i1 > j1:
            replace_lst.extend(data[i2:j2+1])
        else:
            replace_lst.extend(data[i1:j1+1])
        data[keep_i1:j2+1] = replace_lst
