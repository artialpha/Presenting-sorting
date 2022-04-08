import copy


class StepContainer:

    def __init__(self, lst):
        self.lst = copy.copy(lst)
        self.steps = []

    def __iadd__(self, other):
        self.steps.append(other)
        return self

    def __getitem__(self, index):
        return self.steps[index]

    def prepare_steps(self):
        pass

    def execute_steps(self):
        pass

    def step_back(self):
        pass
