from dnd_class import DnDClass


class Rogue(DnDClass):
    def __init__(self):
        super().__init__()
        self.name = "Плут"
        self.conditions = [1]
        self.subclasses = [("Вор", 3), ("Клинок душ", None), ("Мистический ловкач", 3),
                           ("Убийца", None)]
