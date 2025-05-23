from dnd_class import DnDClass


class Barbarian(DnDClass):
    NAME = "Варвар"

    def get_conditions(self):
        return [0, 2, [None, 4, None, None]]
