from random import choice, randint

from skills_manager import add_skill


def aasimar(level):
    abilities = ["Небесное сопротивление", "Тёмное зрение", "Исцеляющие руки", "Несущий свет"]
    if level >= 3:
        abilities.append("Небесное откровение")
    return abilities


def goliath(level):
    abilities = ["Наследие великанов: " + choice(["Облачная прогулка (Облачный великан)",
                                                  "Огненный ожог (Огненный великан)",
                                                  "Морозный иней (Ледяной великан)",
                                                  "Обрушение холма (Холмовой великан)",
                                                  "Выносливость камня (Каменный великан)",
                                                  "Грохот бури (Штормовой великан)"]),
                 "Мощное телосложение"]
    if level >= 5:
        abilities.append("Большая форма")
    return abilities


def dragonborn(level):
    abilities = ["Наследие драконов: " + choice(["Холод (Белый)", "Электричество (Бронзовый)", "Яд (Зелёный)",
                                                 "Огонь (Золотой)", "Огонь (Красный)", "Огонь (Латунный)",
                                                 "Кислота (Медный)", "Холод (Серебряный)", "Электричество (Синий)",
                                                 "Кислота (Чёрный)"]),
                 "Оружие дыхания", "Сопротивление урону", "Тёмное зрение"]
    if level >= 5:
        abilities.append("Драконий полёт")
    return abilities


def orc(level):
    abilities = ["Выброс адреналина", "Тёмное зрение", "Непоколебимая стойкость"]
    return abilities


def tiefling(level):
    abilities = ["Тёмное зрение", "Потустороннее присутствие"]
    heritage = randint(0, 2)
    match heritage:
        case 0:
            abilities.append("Инфернальное наследие")
        case 1:
            abilities.append("Наследие Бездны")
        case 2:
            abilities.append("Хтоническое наследие")
    abilities[-1] = abilities[-1] + f" (+, {"+" if level >= 3 else "-"}, {"+" if level >= 5 else "-"})"
    return abilities


def human(level):
    abilities = ["Находчивый", f"Умелость: {add_skill()}", f"Универсальность {0}"]
    return abilities


def elf(level):
    abilities = ["Тёмное зрение", "Наследие фей", f"Обострённые чувства: {add_skill(["Проницательность", 
                                                                                     "Внимательность", 
                                                                                     "Выживание"])}",
                 "Транс"]
    heritage = randint(0, 2)
    match heritage:
        case 0:
            abilities.append("Дроу")
        case 1:
            abilities.append("Высшие эльфы")
        case 2:
            abilities.append("Лесные эльфы")
    abilities[-1] = abilities[-1] + f" (+, {"+" if level >= 3 else "-"}, {"+" if level >= 5 else "-"})"
    return abilities


types_of_character = [("Аасимар", aasimar), ("Голиаф", goliath), ("Драконорождённый", dragonborn), ("Орк", orc),
                      ("Тифлинг", tiefling), ("Человек", human), ("Эльф", elf)]


def select():
    return choice(types_of_character)

