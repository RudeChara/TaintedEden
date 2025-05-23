from dnd_class import DnDClass


class Rogue(DnDClass):
    NAME = "Плут"

    def get_conditions(self):
        return [1, [3, None, 3, None]]
