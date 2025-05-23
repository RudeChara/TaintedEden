from dnd_class import DnDClass


class Monk(DnDClass):
    NAME = "Монах"

    def get_conditions(self):
        return [1, 4, [None, None, None, None]]
