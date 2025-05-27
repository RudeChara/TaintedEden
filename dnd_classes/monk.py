from dnd_class import DnDClass


class Monk(DnDClass):
    def __init__(self):
        super().__init__(2, ['Акробатика', 'Атлетика', 'История', 'Проницательность', 'Религия', 'Скрытность'])
        self.name = "Монах"
        self.conditions = [1, 4]
        self.subclasses = [("Воин милосердия", None), ("Воин открытой ладони", None), ("Воин стихий", None),
                           ("Воин теней", None)]
