import random
from _basic_classes import *
from _constants import *
M = Monster_Constants()
from damage_class import *
from general_class import *

class Advanced_Monster(Monster_NPC):
    def __init__(self, race, level, element: Elements_NPC):
        self.race = race
        self.level = level
        self.element : Elements_NPC = element
        self.health = self.level * M.MONSTER_HEALTH_DICTIONARY.get(self.race)
        self.attack = self.level * M.MONSTER_ATTACK_DICTIONARY.get(self.race)   
        self.defense = self.level * M.MONSTER_DEFENSE_DICTIONARY.get(self.race)
        self.poison = 0
        self.buffs = []
        self.status = []
        self.weapon = None
        self.armor = None
        self.accessory = None

    def basic_attack(self, hero: Hero_PC):
        damage = Attack_Functions(self, hero)
        damage.calculate()

    def double_attack(self, hero: Hero_PC):
        damage = Attack_Functions(self, hero)
        damage.calculate()
        damage.calculate()

    def choose_action(self, heroes: list):
        hero = heroes[random.randint(0, len(heroes) - 1)]
        choice = random.randint(0, 3)
        if choice == 4:
            self.double_attack(hero)
        else:
            print (self.race+" attacks "+hero.class_name)
            self.basic_attack(hero)
