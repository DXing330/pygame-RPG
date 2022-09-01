import math
import random
import sys
from _constants import Constants
C = Constants

class Hero_PC:
    def __init__(self, name, level, class_name):
        self.name = name
        self.level = level
        self.class_name = class_name
    def get_stats(self):
        if "Summoner" in self.class_name:
            self.max_health = self.level * C.summoner_base_health
            self.attack = self.level * C.summoner_base_attack
            self.defense = self.level * C.summoner_base_defense
            self.max_mana = self.level * C.summoner_base_mana
            self.max_skill = self.level * C.summoner_base_skill

class Ally_NPC:
    def __init__(self, level, race):
        self.level = level
        self.race = race
    def get_stats(self):
        if "Angel" in self.race:
            self.attack = self.level * C.angel_base_attack

class Equipment_NPC:
    def __init__(self, user, level, type, effect):
        self.user = user
        self.level = level
        self.type = type
        self.effect = effect
    def assign_user(hero: Hero_PC):
        self.user = hero.name

class Item_Bag_PC:
    def __init__(self, coins, potions):
        self.coins = coins
        self.potions = potions

class Party_PC:
    def __init__(self):
        self.heroes = []
        self.allies = []
        self.equipment = []
        self.items = Item_Bag_PC
    def add_hero(hero: Hero_PC):
        self.heroes.append(hero)
    def add_ally(ally: Ally_NPC):
        self.allies.append(ally)
    def add_equipment(equip: Equipment_NPC):
        self.equipment.append(equip)

class Monster_NPC:
    def __init__(self, level, race, element):
        self.level = level
        self.race = race
        self.element = element
    def get_stats(self):
        self.attack = self.level * C.monster_base_attack
        self.defense = self.level * C.monster_base_defense
        self.health = self.level * C.monster_base_health