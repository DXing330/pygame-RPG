import random
from _basic_classes import *
from _constants import *
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

    def buff_self(self):
        self.attack += 1
    
    def heal_action(self, hero: Character):
        hero.health += self.level

    def buff_action(self, hero: Character):
        self.buff_name = self.buff_list[random.randint(0, len(self.buff_list) - 1)]
        buff: Passive_Effect_NPC = D.BUFFS.get(self.buff_name)
        hero.buffs.append(buff)

    def cleanse_action(self, hero: Character):
        if len(hero.status) > 0:
            hero.status.pop(0)
        else:
            hero.attack += round(self.level ** C.DECREASE_EXPONENT)

    def debuff_action(self, monster: Character):
        if len(monster.buffs) > 0:
            monster.buffs.pop(0)
        else:
            monster.attack -= round(self.level ** C.DECREASE_EXPONENT)

    def attack_action(self, monster: Character):
        monster.health -= max(self.attack - monster.defense, 1)

    def advanced_action(self, hero: Character, monster: Character):
        self.heal_action(hero)
        self.attack_action(monster)

    def legendary_action(self, heroes_list, monsters_list):
        self.attack += self.level
        for hero in heroes_list:
            self.heal_action(hero)
            self.cleanse_action(hero)
            self.buff_action(hero)
        for monster in monsters_list:
            monster : Character
            self.attack_action(monster)
            self.debuff_action(monster)
    
    def choose_action(self, heroes_list, monsters_list):
        if len(monsters_list) > 0 and len(heroes_list) > 0:
            hero = heroes_list[random.randint(0, len(heroes_list) - 1)]
            monster = monsters_list[random.randint(0, len(monsters_list) - 1)]
            choice = random.randint(0, 5)
            if choice == 0:
                self.heal_action(hero)
            elif choice == 1:
                self.attack_action(monster)
            elif choice == 2:
                self.buff_action(hero)
            elif choice == 3:
                self.cleanse_action(hero)
            elif choice == 4:
                self.debuff_action(monster)
            elif choice == 5:
                advanced_choice = random.randint(0, 2)
                if advanced_choice == 0:
                    self.legendary_action(heroes_list, monsters_list)
                else:
                    self.advanced_action(hero, monster)