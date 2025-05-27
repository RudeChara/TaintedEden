from random import choice

from generate_characteristics import generate
from type_selection import select
from background_selection import select
from dnd_classes.barbarian import Barbarian
from dnd_classes.warlock import Warlock
from dnd_classes.monk import Monk
from dnd_classes.rogue import Rogue


classes = [Barbarian, Warlock, Monk, Rogue]


class Character:
    def __init__(self, level):
        self.level = level

        self.type_of_character = select()
        self.background_of_character = select()

        self.character_class = choice(classes)()
        self.subclass = None
        if self.level >= 3:
            self.subclass = self.character_class.choose_subclass()

        self.characteristics = None
        while self.characteristics is None:
            characteristics = generate()
            for item in self.character_class.get_conditions():
                if characteristics[item] < 15:
                    break
            else:
                if self.subclass is None:
                    self.characteristics = characteristics
                elif self.subclass[1] is None:
                    self.characteristics = characteristics
                elif characteristics[self.subclass[1]] >= 14:
                    self.characteristics = characteristics

    def get_information(self):
        if self.subclass is None:
            return (self.character_class.name, self.characteristics, self.type_of_character[0],
                    self.type_of_character[1](self.level))
        return (self.character_class.name, self.subclass[0], self.characteristics, self.type_of_character[0],
                self.type_of_character[1](self.level))

