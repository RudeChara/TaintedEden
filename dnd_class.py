from random import choice

from skills_manager import add_skill


class DnDClass:
    def __init__(self, count_skills, class_skills):
        self.conditions = []
        self.subclasses = []

        for _ in range(count_skills):
            class_skills.remove(add_skill(class_skills))

    def choose_subclass(self):
        return choice(self.subclasses)

    def get_conditions(self):
        return self.conditions
