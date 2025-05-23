from random import choice
from dnd_classes.barbarian import Barbarian
from dnd_classes.warlock import Warlock
from dnd_classes.monk import Monk
from dnd_classes.rogue import Rogue


classes = [Barbarian, Warlock, Monk, Rogue]


def choose_class(characteristics):
    suitable_classes = []
    for item in classes:
        character_class = item()
        conditions = character_class.get_conditions()
        for value in conditions[:-1]:
            if characteristics[value] < 15:
                break
        else:
            count = 0
            for value in conditions[-1]:
                if value is None:
                    count += 1
                elif characteristics[value] >= 14:
                    count += 1
            suitable_classes.extend([item] * count)
    if not suitable_classes:
        return None
    return choice(suitable_classes)
