from dnd_class import DnDClass


class Warlock(DnDClass):
    def __init__(self):
        super().__init__(2, ["Магия", "Обман", "История", "Запугивание", "Анализ", "Природа",
                             "Религия"])
        self.name = "Колдун"
        self.conditions = [5]
        self.subclasses = [("Великий древний", None), ("Архифея", None), ("Исчадие", None),
                           ("Небожитель", None)]
