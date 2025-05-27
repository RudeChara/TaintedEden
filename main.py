from create_character import Character
from skills_manager import return_skills


level = int(input("Уровень: "))
character = Character(level)
print(*character.get_information())
print(return_skills())
