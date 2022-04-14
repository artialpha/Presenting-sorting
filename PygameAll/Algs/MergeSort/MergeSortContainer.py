import copy

from PygameAll.Algs.StepContainer import StepContainer
from PygameAll.Algs.MergeSort.MergeList import MergeList


class MergeSortContainer(StepContainer):

    class State:
        def __init__(self, whole_list, index_list, index_a, index_b, replace_list, lists_created=None,
                     index_replace=None, message=None):
            self.whole_list = copy.deepcopy(whole_list)
            self.index_list = index_list
            self.index_a = index_a
            self.index_b = index_b
            self.replace_list = copy.deepcopy(replace_list)
            self.lists_created = copy.deepcopy(lists_created)
            self.index_replace = index_replace
            self.message = message

        def __str__(self):
            print('whole list:', self.whole_list, 'index_list', self.index_list)
            str_return = f'whole list:    {self.whole_list}\n' \
                         f'index list:    {self.index_list}\n' \
                         f'index a:       {self.index_a}\n' \
                         f'index b:       {self.index_b}\n' \
                         f'replace list:  {self.replace_list}\n' \
                         f'lists created: {self.lists_created}\n' \
                         f'index_replace: {self.index_replace}\n\n'
            return str_return

    # Step container copies the list so that i won't change the original
    def __init__(self, lst):
        super().__init__(MergeList(lst))


        # indexes for a and b list in merge list, temp list is created of a and b
        self.a_index = None
        self.b_index = None

        self.states = []
        self.index_of_current_list = None
        self.replace_list = None

    def merge_sort(self, data):
        if len(data) == 1:
            return data

        #print(self.lst, 'lst')
        a, b = data.cut_in_half()

        self.states.append(self.State(self.lst, None, self.a_index, self.b_index,
                                      None, (a, b)))

        lst1 = self.merge_sort(a)
        lst2 = self.merge_sort(b)
        #print(self.lst, 'lst')
        return self.merge(lst1, lst2)

    def merge(self, lst1, lst2):
        self.a_index = 0
        self.b_index = 0
        self.replace_list = MergeList([])
        self.index_of_current_list = lst1.out.index

        # ????
        self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                      self.replace_list))

        while True:
            if lst1[self.a_index] < lst2[self.b_index]:
                self.replace_list.append(lst1[self.a_index])
                self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                              self.replace_list))
                last_visited = 'a'
                if (self.a_index + 1) == len(lst1):
                    break

                self.a_index += 1
                self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                              self.replace_list))
            else:
                self.replace_list.append(lst2[self.b_index])
                self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                              self.replace_list))
                last_visited = 'b'
                if (self.b_index + 1) == len(lst2):
                    break

                self.b_index += 1
                self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                              self.replace_list))

        if last_visited == 'a':
            self.replace_list.extend(lst2[self.b_index:])
            self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                          self.replace_list))
        else:
            self.replace_list.extend(lst1[self.a_index:])
            self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                          self.replace_list))

        lst1.out[:] = self.replace_list
        self.states.append(self.State(self.lst, None, self.a_index, self.b_index,
                                      self.replace_list, index_replace=lst1.out.index))
        return lst1.out

    def cut_in_half(self):
        #print('from', self.lst)
        self.lst.cut_in_half()
        #print('to', self.lst)

    def show_states(self):
        for counter, state in enumerate(self.states):
            to_print = f'counter: {counter}\n{str(state):<85}'
            print(to_print)

    def get_states(self, data):
        def inner():
            self.states.append(self.State(self.lst, self.index_of_current_list, self.a_index, self.b_index,
                                          self.replace_list, (data, )))
            self.merge_sort(data)
        inner()
