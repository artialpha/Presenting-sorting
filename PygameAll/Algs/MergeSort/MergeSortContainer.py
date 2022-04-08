from PygameAll.Algs.StepContainer import StepContainer
from MergeList import MergeList


class MergeSortContainer(StepContainer):

    # Step container copies the list so that i won't change the original
    def __init__(self, lst):
        super().__init__(lst)

        self.stack_for_cutting = []
        self.i = None
        self.j = None

        self.final_lst = []

    def merge_sort(self, data):
        if len(data) == 1:
            return data

        half = int(len(data)/2)
        self.steps.append(
            (
                self.cut_in_half,
                (data, [data[:half], data[half:]])
            )
        )
        lst1 = self.merge_sort(data[:half])
        lst2 = self.merge_sort(data[half:])
        return self.merge(lst1, lst2)

    def merge(self, lst1, lst2):
        i = 0
        j = 0
        replace_lst = MergeList([])

        self.steps.append((self.place_indexes, (lst1, lst2)))
        while i < len(lst1) and j < len(lst2):
            self.steps.append((self.compare_values, (lst1[i], lst2[j])))
            if lst1[i] < lst2[j]:
                self.steps.append((self.add_one_value, lst1[i]))
                replace_lst.append(lst1[i])

                if i+1 < len(lst1):
                    self.steps.append((self.move_index, i))
                i += 1
            else:
                self.steps.append((self.add_one_value, lst2[j]))
                replace_lst.append(lst2[j])

                if j+1 < len(lst2):
                    self.steps.append((self.move_index, j))
                j += 1

        if i == len(lst1):
            replace_lst.extend(lst2[j:])
            self.steps.append((self.add_rest, lst2[j:]))
            self.steps.append((self.add_to_final_list, replace_lst))
        else:
            replace_lst.extend(lst1[i:])
            self.steps.append((self.add_rest, lst1[i:]))
            self.steps.append((self.add_to_final_list, replace_lst))
        # [:]
        return replace_lst

    def cut_in_half(self):
        half = int(len(self.lst)/2)
        a = self.lst[:half]
        b = self.lst[half:]
        self.lst[:] = [a, b]

    def place_indexes(self):
        pass

    def compare_values(self):
        pass

    def add_one_value(self):
        pass

    def move_index(self):
        pass

    def add_rest(self):
        pass

    def add_to_final_list(self, replace_lst):
        self.final_lst = [lst for lst in self.final_lst if not len(set(lst) & set(replace_lst)) > 0]
        self.final_lst.append(replace_lst)

    def show_steps(self):
        for counter, step in enumerate(self.steps):
            print(step, counter)
