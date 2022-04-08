class MergeList:

    def __init__(self, lst):
        self.lst = lst
        self.a = None
        self.b = None
        self.out = None

    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return str(self.lst)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.lst[item]
        elif isinstance(item, slice):
            return MergeList(self.lst[item.start:item.stop:item.step])

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
        half = int(len(self.lst)/2)
        self.a = self[:half]
        self.b = self[half:]

        self[:] = [self.a, self.b]

        self.a.out = self
        self.b.out = self

        return self.a, self.b

