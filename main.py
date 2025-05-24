from create_character import Character


level = int(input("Уровень: "))
character = Character(level)
print(*character.get_information())
