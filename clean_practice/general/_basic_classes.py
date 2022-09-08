import random
from _simple_classes import *
from _constants import *
C = Constants()
from _list_constants import *
L = LConstants()
from _dictionaries import *
D = Dictionaries()


class Character(object):
    def __init__(self):
        self.level = 1
        self.name = None
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.mana = 0
        self.skill = 0
        self.poison = 0
        self.weapon = None
        self.armor = None
        self.accessory = None
        # Image used to display the character.
        self.sprite = None
        # Positive passive effects.
        self.buffs = []
        # Negative passive effects.
        self.status = []

    def get_attack_element(self):
        return None

    def get_defense_element(self):
        return None

    def get_attack_effects(self):
        effects = []
        if self.weapon != None:
            effects.append(self.weapon.effect)
        for buff in self.buffs:
            if "Attack" in buff.timing:
                effects.append(buff)
        return effects

    def get_defense_effects(self):
        effects = []
        if self.armor != None:
            effects.append(self.weapon.effect)
        for buff in self.buffs:
            if "Defense" in buff.timing:
                effects.append(buff)
        return effects

    def update_stats(self):
        pass

    def add_effect(self, effect: Passive_Effect_NPC):
        if "Buff" in effect.variety:
            self.buffs.append(effect)
        elif "Status" in effect.variety:
            self.status.append(effect)

    def reduce_health(self, value):
        self.health -= value

    def increase_health(self, value):
        self.health += value
    
    def buff_effect(self):
        for buff in self.buffs:
            if "every_turn" in buff.timing:
                self.health -= D.BUFF_HEALTH.get(buff.effect_specifics) * buff.power
                self.attack -= D.BUFF_ATTACK.get(buff.effect_specifics) * buff.power
                self.defense -= D.BUFF_DEFENSE.get(buff.effect_specifics) * buff.power
    
    def status_effect(self):
        self.health -= max(0, self.poison)
        for status in self.status:
            if "every_turn" in status.timing:
                self.health -= D.STATUS_HEALTH.get(status.effect_specifics) * status.power
                self.attack -= D.STATUS_ATTACK.get(status.effect_specifics) * status.power
                self.defense -= D.STATUS_DEFENSE.get(status.effect_specifics) * status.power

    def view_stats(self):
        print ("HEALTH: "+str(self.health)+" ATTACK: "+str(self.attack)+" DEFENSE: "+str(self.defense))


class Hero_PC(Character):
    def __init__(self, class_name, level, exp):
        self.class_name = class_name
        self.level = 1
        self.exp = 0

    def get_attack_element(self):
        if self.weapon != None:
            return self.weapon.element
        return None

    def get_defense_element(self):
        if self.armor != None:
            return self.armor.element
        return None

    # Update stats, depending on level and class, only used during battle
    def update_stats(self):
        self.max_health = self.level * D.HERO_BASE_HEALTH.get(self.class_name)
        self.attack = self.level * D.HERO_BASE_ATTACK.get(self.class_name)
        self.defense = self.level * D.HERO_BASE_DEFENSE.get(self.class_name)
        self.max_mana = self.level * D.HERO_BASE_MANA.get(self.class_name)
        self.max_skill = self.level * D.HERO_BASE_SKILL.get(self.class_name)
        self.health = self.max_health
        self.mana = self.max_mana
        self.skill = self.max_skill
    
    def update_skills(self):
        self.skill_list = []
        # First see which skill list to pull from, depending on class.
        skill_dictionary = D.HERO_SKILL_LIST.get(self.class_name)
        # Then see what skills to add, depending on level.
        for number in range(0, self.level):
            skill = skill_dictionary.get(number)
            self.skill_list.append(skill)

    def update_spells(self):
        pass
    
    def level_up(self):
        if self.exp >= self.level ** C.INCREASE_EXPONENT:
            self.level += 1
            self.update_stats()
    
    def add_skill(self, skill: Skill_PC):
        self.skill_list.append(skill)
    
    def add_spell(self, spell: Spell_PC):
        self.spell_list.append(spell)

    def equip(self, equipment: Equipment_NPC):
        if "Armor" in equipment.variety:
            self.armor = equipment
        elif "Weapon" in equipment.variety:
            self.weapon = equipment
        elif "Accessory" in equipment.variety:
            self.accessory = equipment

    def add_name(self, name):
        self.name = name


class Monster_NPC(Character):
    def __init__(self, level, race, element: Elements_NPC):
        self.level = level
        self.race = race
        self.element = element
        self.sprite = None

    def update_stats(self):
        self.attack = random.randint(self.level//2, self.level) * C.monster_base_attack
        self.defense = random.randint(self.level//2, self.level) * C.monster_base_defense
        self.health = random.randint(self.level//2, self.level) * C.monster_base_health

    def get_attack_element(self):
        return self.element

    def get_defense_element(self):
        return self.element

    def basic_attack(self, hero: Hero_PC):
        pass


class Ally_NPC(object):
    def __init__(self):
        self.level = 1
        self.race = None
        self.attack = 0
    
    def level_up(self):
        self.level += 1

    def update_stats(self):
        pass

    def buff_action(self, hero: Hero_PC):
        pass

    def attack_action(self, monster: Monster_NPC):
        pass

    def advanced_action(self, hero: Hero_PC, monster: Monster_NPC):
        pass

    def legendary_action(self, heroes_list, monsters_list):
        pass

    def choose_action(self, heroes_list, monsters_list):
        pass


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

    def add_equipment(self, equipment: Equipment_NPC):
        self.equipment.append(equipment)