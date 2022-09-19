import random
from _basic_classes import Character
from _dictionaries import *
D = Dictionaries()
S = Summon_Dictionary()


class Summon_PC(Character):
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.skill = 0
        self.mana = 0
        self.poison = 0
        self.buffs = []
        self.status = []
        self.skill_list = []
        self.skills = True
        self.weapon = None
        self.armor = None
        self.accessory = None

    def update_stats(self):
        while self.level == 0:
            self.level = round(random.gauss(S.SUMMON_MEAN_LEVEL.get(self.name),
            S.SUMMON_LEVEL_VAR.get(self.name)))
        self.health = self.level * S.SUMMON_BASE_HEALTH.get(self.name)
        self.attack = self.level * S.SUMMON_BASE_ATTACK.get(self.name)
        self.defense = self.level * S.SUMMON_BASE_DEFENSE.get(self.name)
        self.skill = self.level * S.SUMMON_BASE_SKILL.get(self.name)
        self.mana = 0

    def update_skills(self):
        if self.skill > 0:
            word_list = S.SUMMON_SKILLS.get(self.name)
            for word in word_list:
                skill = D.ALL_SKILLS.get(word)
                self.skill_list.append(skill)

    def view_battle_stats(self):
        return (self.name+" HP: "+str(self.health)+
        " ATK: "+str(self.attack)+" DEF: "+str(self.defense))