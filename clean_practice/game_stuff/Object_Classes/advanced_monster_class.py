import random
from _basic_classes import *
from _dictionaries import *
M = Monster_Dictionary()
from damage_class import *


class Advanced_Monster(Monster_NPC):
    def __init__(self, race, level, element: Elements_NPC):
        self.name = race
        self.level = level
        self.element : Elements_NPC = element
        self.health = self.level * M.MONSTER_HEALTH.get(self.name)
        self.attack = self.level * M.MONSTER_ATTACK.get(self.name)   
        self.defense = self.level * M.MONSTER_DEFENSE.get(self.name)
        self.poison = 0
        self.buffs = []
        self.status = []
        self.weapon = None
        self.armor = None
        self.accessory = None

    def basic_attack(self, hero: Hero_PC):
        damage = Attack_Functions(self, hero)
        damage.calculate()

    def buff_action(self):
        buff: Passive_Effect_NPC = M.MONSTER_BUFFS.get(self.name)
        self.buffs.append(buff)

    def double_attack(self, hero: Hero_PC):
        damage = Attack_Functions(self, hero)
        damage.calculate()
        damage.calculate()

    def choose_action(self, heroes: list):
        hero = heroes[random.randint(0, len(heroes) - 1)]
        choice = random.randint(0, 2)
        if choice == 2:
            self.double_attack(hero)
        elif choice == 1:
            self.buff_action()
        else:
            self.basic_attack(hero)
