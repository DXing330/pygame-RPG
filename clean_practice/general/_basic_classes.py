from ast import Pass
import math
import random
import sys
from unicodedata import name
from _constants import Constants
C = Constants()

# Effects that do something without the player's input.
class Passive_Effect_NPC:
    def __init__(self, effect, power, target, variety):
        # What the effect does.
        self.effect = effect
        # How strong the effect is.
        self.power = power
        # Who it effects, ex. the self, enemies, allies, etc.
        self.target = target
        # What kind of passive it is, ex. buff, passive, or status.
        self.variety = variety
    
    def add_power(self):
        self.power += 1


# Spells are generally AOE effects that are cast by the player and cost mana.
class Spell_PC:
    def __init__(self, name, power, element, effect, target, cost):
        self.name = name
        self.power = power
        # Some elements are stronger or weaker against other elements
        self.element = element
        self.effect = effect
        self.target = target
        self.cost = cost
    
    

# Skills are effects cast by the player, usually costing skill.
class Skill_PC:
    def __init__(self, name, effect, target, cost):
        self.name = name
        self.effect = effect
        self.target = target
        self.cost = cost
    

class Hero_PC:
    def __init__(self, class_name):
        self.name = None
        self.class_name = class_name
        self.level = 1
        self.skill_list = []
        self.spell_list = []
        # Buffs are effects gained during battle.
        self.buffs = []
        # Passives are permanant effects.
        self.passives = []
        # Statuses are negative effects.
        self.status = []
        # The hero will have no stats until battle
        self.max_health = 0
        self.attack = 0
        self.defense = 0
        self.max_mana = 0
        self.max_skill = 0
        self.health = 0
        self.mana = 0
        self.skill = 0
        self.exp = 0
        self.poison = 0

    # Stats will be given to the hero during battle
    def get_stats(self):
        if "Summoner" in self.class_name:
            self.max_health = self.level * C.summoner_base_health
            self.attack = self.level * C.summoner_base_attack
            self.defense = self.level * C.summoner_base_defense
            self.max_mana = self.level * C.summoner_base_mana
            self.max_skill = self.level * C.summoner_base_skill
    
    def level_up(self):
        self.level += 1
    
    def add_skill(self, skill: Skill_PC):
        self.skill_list.append(skill)
    
    def add_spell(self, spell: Spell_PC):
        self.spell_list.append(spell)
    
    def add_effect(self, effect: Passive_Effect_NPC):
        if "Passive" in effect.variety:
            self.passives.append(effect)
        elif "Buff" in effect.variety:
            self.buffs.append(effect)
        elif "Status" in effect.variety:
            self.status.append(effect)
        
    def add_name(self, name):
        self.name = name
    
    def minus_cost(self, list, index):
        if list == self.spell_list:
            spell = self.spell_list[index]
            spell.cost -= 1
        elif list == self.skill_list:
            skill = self.skill_list[index]
            skill.cost -= 1


class Ally_NPC:
    def __init__(self, level, race):
        self.level = level
        self.race = race
        self.attack = 0

    def get_stats(self):
        if "Angel" in self.race:
            self.attack = self.level * C.angel_base_attack


class Equipment_NPC:
    def __init__(self, user, level, type, effect):
        self.user = user
        self.level = level
        self.type = type
        self.effect = effect
        self.element = None

    def assign_user(self, hero: Hero_PC):
        self.user = hero.name

    def add_element(self):
        pass


class Item_Bag_PC:
    def __init__(self, coins, potions):
        self.coins = coins
        self.potions = potions


class Party_PC:
    def __init__(self):
        self.heroes = []
        self.allies = []
        self.equipment = []
        self.items = Item_Bag_PC(0, 0)

    def add_hero(self, hero: Hero_PC):
        self.heroes.append(hero)

    def add_ally(self, ally: Ally_NPC):
        self.allies.append(ally)

    def add_equipment(self, equip: Equipment_NPC):
        self.equipment.append(equip)


class Monster_NPC:
    def __init__(self, level, race, element):
        self.level = level
        self.race = race
        self.element = element
        self.attack = 0
        self.defense = 0
        self.health = 0
        self.buffs = []
        self.status = []
        self.poison = 0

    def get_stats(self):
        self.attack = random.randint(self.level//2, self.level) * C.monster_base_attack
        self.defense = random.randint(self.level//2, self.level) * C.monster_base_defense
        self.health = random.randint(self.level//2, self.level) * C.monster_base_health

    def get_attack(self):
        attack = self.attack
        return attack

    def get_attack_effect(self):
        effect = None
        return effect
    
    def add_effect(self, effect: Passive_Effect_NPC):
        if "Buff" in effect.variety:
            self.buffs.append(effect)
        elif "Status" in effect.variety:
            self.status.append(effect)