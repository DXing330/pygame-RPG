import random
from _basic_classes import *
from _constants import *

class Angel_NPC(Ally_NPC):
    def __init__(self, race, level):
        self.race = "Angel"
        self.level = level

    def update_stats(self):
        self.attack = self.level * C.angel_base_attack
    
    def buff_action(self, hero: Hero_PC):
        hero.health += self.attack

    def attack_action(self, monster: Monster_NPC):
        monster.health -= self.attack//2
        monster.attack -= self.attack//4
        monster.defense -= self.attack//8

    def advanced_action(self, hero: Hero_PC, monster: Monster_NPC):
        hero.health += self.attack
        hero.attack += self.attack//2
        hero.defense += self.defense//4
        monster.health -= self.attack//2
        monster.attack -= self.attack//4
        monster.defense -= self.attack//8

    def legendary_action(self, heroes_list, monsters_list):
        self.attack += self.level
        for hero in heroes_list:
            hero.health += self.attack
            hero.attack += self.attack//2
            hero.defense += self.attack//4
            if len(hero.status) > 0:
                hero.status.pop(0)
        for monster in monsters_list:
            monster.health -= self.attack//2
            monster.attack -= self.attack//4
            monster.defense -= self.attack//8
    
    def choose_action(self, heroes_list, monsters_list):
        hero = heroes_list[random.randint(0, len(heroes_list) - 1)]
        monster = monsters_list[random.randint(0, len(monsters_list) - 1)]
        choice = random.randint(0, 2)
        if choice == 0:
            self.buff_action(hero)
        elif choice == 1:
            self.attack_action(monster)
        elif choice == 2:
            advanced_choice = random.randint(0, 2)
            if advanced_choice == 0:
                self.legendary_action(heroes_list, monsters_list)
            else:
                self.advanced_action(hero, monster)