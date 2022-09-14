import random
from _basic_classes import *
from _constants import *
from upgrade_class import *
from advanced_monster_class import M
C = Constants()
from _dictionaries import *
D = Dictionaries()

class Angel_NPC(Ally_NPC):
    def __init__(self, name, level):
        self.name = "Angel"
        self.level = level

    def update_stats(self):
        self.health = 1
        self.attack = self.level * C.ANGEL_BASE_ATTACK
        self.defense = 1
        self.buff_list = C.ANGEL_BUFF_LIST

    def update_level(self, party: Party_PC):
        upgrade = Upgrade(party)
        upgrade.upgrade_ally()

    def buff_self(self):
        self.attack += 1
    
    def heal_action(self):
        self.hero.health += self.level

    def buff_action(self):
        self.buff_name = self.buff_list[random.randint(0, len(self.buff_list) - 1)]
        buff: Passive_Effect_NPC = D.BUFFS.get(self.buff_name)
        self.hero.buffs.append(buff)

    def cleanse_action(self):
        if len(self.hero.status) > 0:
            self.hero.status.pop(0)
        else:
            self.hero.attack += round(self.level ** C.DECREASE_EXPONENT)

    def debuff_action(self):
        if len(self.monster.buffs) > 0:
            self.monster.buffs.pop(0)
        else:
            self.monster.attack -= round(self.level ** C.DECREASE_EXPONENT)

    def attack_action(self):
        self.monster.health -= max(self.attack - self.monster.defense, 1)

    def advanced_action(self):
        self.heal_action()
        self.attack_action()

    def legendary_action(self):
        self.attack += self.level
        for hero in self.heroes_list:
            self.heal_action(hero)
            self.cleanse_action(hero)
            self.buff_action(hero)
        for monster in self.monsters_list:
            monster : Character
            self.attack_action(monster)
            self.debuff_action(monster)
    
    def choose_action(self, heroes_list, monsters_list):
        self.heroes_list = heroes_list
        self.monsters_list = monsters_list
        self.hero = None
        self.monster = None
        if len(self.monsters_list) > 0 and len(self.heroes_list) > 0:
            self.hero : Character = heroes_list[random.randint(0, len(heroes_list) - 1)]
            self.monster : Character = monsters_list[random.randint(0, len(monsters_list) - 1)]
            choice = random.randint(0, 5)
            if choice == 0:
                advanced_choice = random.randint(0, 2)
                if advanced_choice == 0:
                    self.legendary_action()
                else:
                    self.advanced_action()
            elif choice == 1:
                self.heal_action()
            elif choice == 2:
                self.attack_action()
            elif choice == 3:
                self.buff_action()
            elif choice == 4:
                self.cleanse_action()
            elif choice == 5:
                self.debuff_action()