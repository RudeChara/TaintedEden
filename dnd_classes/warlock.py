from dnd_class import DnDClass


class Warlock(DnDClass):
    NAME = "Колдун"

    def get_conditions(self):
        return [5, [None, None, None, None]]
