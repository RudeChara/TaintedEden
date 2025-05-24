from random import choice


class DnDClass:
    def __init__(self):
        self.conditions = []
        self.subclasses = []

    def choose_subclass(self):
        return choice(self.subclasses)

    def get_conditions(self):
        return self.conditions
