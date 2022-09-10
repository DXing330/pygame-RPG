from _basic_classes import Character
from _dictionaries import Summon_Dictionary
S = Summon_Dictionary()


class Summon_PC(Character):
    def __init__(self, race, level):
        self.name = race
        self.level = level
        self.health = self.level * S.SUMMON_BASE_HEALTH.get(self.name)
        self.attack = self.level * S.SUMMON_BASE_ATTACK.get(self.name)
        self.defense = self.level * S.SUMMON_BASE_DEFENSE.get(self.name)
        self.poison = 0
        self.buffs = []
        self.status = []
        self.weapon = None
        self.armor = None
        self.accessory = None