from random import choice


skills = []


def add_skill(roster=None):
    if roster is None:
        roster = ["Акробатика", "Анализ", "Атлетика", "Внимательность", "Выживание", "Выступление", "Запугивание",
                  "История", "Ловкость рук", "Магия", "Медицина", "Обман", "Природа", "Проницательность", "Религия",
                  "Скрытность", "Убеждение", "Уход за животными"]

    skill = choice(roster)
    while skill in skills:
        skill = choice(roster)
    skills.append(skill)
    return skill


def return_skills():
    return skills
