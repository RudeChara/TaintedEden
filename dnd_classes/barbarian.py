from dnd_class import DnDClass


class Barbarian(DnDClass):
    def __init__(self):
        super().__init__(2, ['Уход за животными', 'Атлетика', 'Природа', 'Запугивание', 'Внимательность', 'Выживание'])
        self.name = "Варвар"
        self.conditions = [0, 2]
        self.subclasses = [("Путь берсерка", None), ("Путь дикого сердца", 4), ("Путь Мирового древа", None),
                           ("Путь фанатика", None)]

