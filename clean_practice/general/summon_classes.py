from _basic_classes import Character
from _dictionaries import Summon_Dictionary
S = Summon_Dictionary()


class Summon_PC(Character):
    def __init__(self, race, level):
        self.class_name = race
        self.level = level
        self.health = self.level * S.SUMMON_BASE_HEALTH.get(self.race)
        self.attack = self.level * S.SUMMON_BASE_ATTACK.get(self.race)
        self.defense = self.level * S.SUMMON_BASE_DEFENSE.get(self.race)
        self.poison = 0
        self.buffs = []
        self.status = []
        self.weapon = None
        self.armor = None
        self.accessory = None