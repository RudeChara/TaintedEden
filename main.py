from generating_characteristics import generate
from class_selection import choose_class


characteristics = generate()
character_class = choose_class(characteristics)
while character_class is None:
    characteristics = generate()
    character_class = choose_class(characteristics)
print(characteristics)
print(character_class.NAME)
