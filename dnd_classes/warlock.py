from dnd_class import DnDClass


class Warlock(DnDClass):
    def __init__(self):
        super().__init__()
        self.name = "Колдун"
        self.conditions = [1]
        self.subclasses = [("Великий древний", None), ("Архифея", None), ("Исчадие", None),
                           ("Небожитель", None)]
