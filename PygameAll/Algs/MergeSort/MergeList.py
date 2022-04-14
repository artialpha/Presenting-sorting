import copy


class MergeList:

    def __init__(self, lst):
        self.lst = lst
        self.a = None
        self.b = None
        self.out = None
        self.original_list = copy.deepcopy(lst)

        # index - how to get to this list if it is deeply nested
        self.index = '0'
        self.representation = None

    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self.lst)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.lst[item]
        elif isinstance(item, slice):
            return MergeList(self.lst[item.start:item.stop:item.step])
        elif isinstance(item, str):
            current = self
            for counter, x in enumerate(item):
                current = current[int(x)]
            return current

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.lst[key] = value
        elif isinstance(key, slice):
            self.lst[key.start:key.stop:key.step] = MergeList(value)

    def __eq__(self, other):
        if type(other) is MergeList:
            return self.lst == other.lst
        if type(other) is list:
            return self.lst == other

    def __len__(self):
        return len(self.lst)

    def __add__(self, other):
        return self.lst + other.lst

    def append(self, value):
        self.lst.append(value)

    def extend(self, value):
        self.lst.extend(value)

    def cut_in_half(self):
        if isinstance(self.lst[0], MergeList):
            print('I CANT HALF IT - it\'s already done')
            return None
        else:
            half = int(len(self.lst)/2)
            self.a = self[:half]
            self.b = self[half:]

            self.a.index, self.b.index = '', ''

            self.a.index += self.index + '0'
            self.b.index += self.index + '1'

            self[:] = [self.a, self.b]

            self.a.out = self
            self.b.out = self

            return self.a, self.b

    @classmethod
    def flat_list(cls, lst):
        temp = []
        for x in lst:
            if isinstance(x, list) or isinstance(x, cls):
                temp.extend(cls.flat_list(x))
            else:
                temp.append(x)
        return temp

    def merge_representation(self, lst):
        temp = []

        if all(isinstance(x, int) for x in lst):
            return None

        for x in lst:
            if isinstance(x, list):
                self.representation.append(self.flat_list(x))

        for x in lst:
            if isinstance(x, list):
                self.merge_representation(x)

    def create_representation(self):
        self.representation = []
        self.representation.append(self.flat_list(self.lst))
        self.merge_representation(self.lst)




