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
        self.class_name = None
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
        self.turn = True
        # Image used to display the character.
        self.sprite = None
        # Positive passive effects.
        self.buffs = []
        # Negative passive effects.
        self.status = []

    def get_attack_element(self):
        if self.weapon != None:
            return self.weapon.element
        return None

    def get_defense_element(self):
        if self.armor != None:
            return self.armor.element
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
        if self.accessory != None:
            self.accessory : Equipment_NPC = self.accessory
            self.health += D.BUFF_HEALTH.get(self.accessory.effect.effect_specifics) * self.accessory.power
            self.attack += D.BUFF_ATTACK.get(self.accessory.effect.effect_specifics) * self.accessory.power
            self.defense += D.BUFF_DEFENSE.get(self.accessory.effect.effect_specifics) * self.accessory.power
        for buff in self.buffs:
            buff : Passive_Effect_NPC = buff
            if "every_turn" in buff.timing:
                if "Increase_Stats" in buff.effect:
                    self.health += D.BUFF_HEALTH.get(buff.effect_specifics) * buff.power
                    self.attack += D.BUFF_ATTACK.get(buff.effect_specifics) * buff.power
                    self.defense += D.BUFF_DEFENSE.get(buff.effect_specifics) * buff.power
    
    def status_effect(self):
        if self.poison > 0:
            self.health -= self.poison
        # If there is no status that says otherwise, the character gets a turn
        self.turn = True
        for status in self.status:
            if "every_turn" in status.timing:
                self.health -= D.STATUS_HEALTH.get(status.effect_specifics) * status.power
                self.attack -= min(D.STATUS_ATTACK.get(status.effect_specifics) * status.power, self.attack)
                self.defense -= min(D.STATUS_DEFENSE.get(status.effect_specifics) * status.power, self.defense)
            if "Disable" in status.effect and "ALL" in status.effect_specifics and status.power > 0:
                self.turn = False
                status.power -= 1
                if status.power <= 0:
                    self.status.remove(status)

    def view_battle_stats(self):
        pass


class Hero_PC(Character):
    def __init__(self, class_name, level, exp):
        self.class_name = class_name
        self.level = level
        self.exp = exp

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
        self.poison = 0
        self.status = []
        self.buffs = []

    def update_equipment(self, equipment_list: list):
        self.weapon = None
        self.armor = None
        self.accessory = None
        for equip in equipment_list:
            equipment: Equipment_NPC = equip
            if self.class_name in equipment.user:
                if equipment.variety == "Weapon":
                    self.weapon = equipment
                elif equipment.variety == "Armor":
                    self.armor = equipment
                elif equipment.variety == "Accessory":
                    self.accessory = equipment
    
    def update_skills(self):
        self.skill_list = []
        # First see which skill list to pull from, depending on class.
        skill_dictionary = D.HERO_SKILL_LIST.get(self.class_name)
        # Then see what skills to add, depending on level.
        for number in range(0, self.level):
            skill : Skill_PC = skill_dictionary.get(number)
            if skill != None:
                self.skill_list.append(skill)

    def update_spells(self):
        self.spell_list = []
        spell_dictionary = D.HERO_SPELL_LIST.get(self.class_name)
        for number in range(0, self.level):
            spell : Spell_PC = spell_dictionary.get(number)
            if spell != None:
                self.spell_list.append(spell)
    
    def level_up(self):
        if self.exp >= self.level ** C.INCREASE_EXPONENT:
            self.level += 1

    def equip(self, equipment: Equipment_NPC):
        if "Armor" in equipment.variety:
            self.armor = equipment
        elif "Weapon" in equipment.variety:
            self.weapon = equipment
        elif "Accessory" in equipment.variety:
            self.accessory = equipment

    def add_name(self, name):
        self.name = name

    def view_stats(self):
        return str("CLASS: "+self.class_name+" LEVEL: "+str(self.level))

    def view_battle_stats(self):
        return str(self.class_name+" HP: "+str(self.health)+
        " ATK: "+str(self.attack)+" DEF: "+str(self.defense))


class Monster_NPC(Character):
    def __init__(self, level, race, element: Elements_NPC):
        self.level = level
        self.race = race
        self.element : Elements_NPC = element
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

    def view_battle_stats(self):
        return str(self.element.name+" "+self.race+" HP: "+str(self.health)+
        " ATK: "+str(self.attack)+" DEF: "+str(self.defense))


class Ally_NPC(object):
    def __init__(self):
        self.level = 1
        self.race = None
        self.attack = 0
        self.sprite = None
    
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