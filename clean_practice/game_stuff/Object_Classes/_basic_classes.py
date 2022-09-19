import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Battle_Functions")
import copy
from _simple_classes import *
from _constants import *
C = Constants()
from _list_constants import *
L = LConstants()
from _dictionaries import *
D = Dictionaries()
H = Hero_Dictionary()

class Equipment_NPC:
    def __init__(self, name, user, power, effect, element, variety):
        self.name = name
        self.user = user
        self.power = power
        # What kind of effect the equipment has
        self.effect = effect
        self.element = element
        # What kind of equipment it is, ex. weapon, armor, acc.
        self.variety = variety

    def get_element(self):
        element = D.ELEMENTS.get(self.element)
        return element

    def get_effect(self):
        effect_dictionary = D.EQUIPMENT_EFFECTS.get(self.variety)
        effect = effect_dictionary.get(self.effect)
        return effect


class Character(object):
    def __init__(self):
        self.level = 1
        self.class_name = None
        self.name = None
        self.max_health = 0
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.max_mana = 0
        self.mana = 0
        self.max_skill = 0
        self.skill = 0
        self.poison = 0
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.turn = True
        self.magic = True
        self.spell_list = []
        self.skills = True
        self.skill_list = []
        # Image used to display the character.
        self.sprite = None
        # Positive passive effects.
        self.buffs = []
        # Negative passive effects.
        self.status = []

    def get_attack_element(self):
        if self.weapon != None:
            self.weapon : Equipment_NPC
            element = self.weapon.get_element()
            effect = self.weapon.get_effect()
            return element, effect
        return None, None

    def get_defense_element(self):
        if self.armor != None:
            self.armor : Equipment_NPC
            element = self.armor.get_element()
            effect = self.armor.get_effect()
            return element, effect
        return None, None

    def get_attack_effects(self):
        effects = []
        for buff in self.buffs:
            if "Attack" in buff.timing:
                effects.append(buff)
        return effects

    def get_defense_effects(self):
        effects = []
        for buff in self.buffs:
            if "Defense" in buff.timing:
                effects.append(buff)
        return effects

    def update_stats(self):
        pass

    def update_skills(self):
        pass

    def update_buffs(self):
        pass

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()

    def decrease_cooldowns(self):
        for skill in self.skill_list:
            skill: Skill_PC
            if skill.cooldown > 0:
                skill.cooldown -= 1

    def add_effect(self, effect: Passive_Effect_NPC):
        if "Buff" in effect.variety:
            self.buffs.append(effect)
        elif "Status" in effect.variety:
            self.status.append(effect)
    
    # Various beneficial effects.
    def buff_effect(self):
        self.decrease_cooldowns()
        if self.accessory != None:
            self.accessory : Equipment_NPC
            accessory_buff = D.BUFFS.get(self.accessory.effect)
            self.buffs.append(accessory_buff)
            self.accessory = None
        for buff in self.buffs:
            buff : Passive_Effect_NPC
            if "Every_Turn" in buff.timing and "Change_Stats" in buff.effect:
                self.health += D.BUFF_HEALTH.get(buff.effect_specifics) * buff.power
                self.attack += D.BUFF_ATTACK.get(buff.effect_specifics) * buff.power
                self.defense += D.BUFF_DEFENSE.get(buff.effect_specifics) * buff.power
    
    # Various negative effects.
    def status_effect(self):
        if self.poison > 0:
            self.health -= self.poison
        # If there is no status that says otherwise, the character gets a turn
        self.turn = True
        for status in self.status:
            status : Passive_Effect_NPC
            if "Every_Turn" in status.timing and "Change_Stats" in status.effect:
                self.health += D.STATUS_HEALTH.get(status.effect_specifics) * status.power
                self.attack += (D.STATUS_ATTACK.get(status.effect_specifics) * 
                status.power)
                self.defense += (D.STATUS_DEFENSE.get(status.effect_specifics) * 
                status.power)
            if "Disable" in status.effect and status.power > 0:
                if "ALL" in status.effect_specifics:
                    self.turn = False
                if "Magic" in status.effect_specifics:
                    self.magic = False
                if "Skills" in status.effect_specifics:
                    self.skills = False
                status.power -= 1
                if status.power <= 0:
                    self.status.remove(status)

    # Passive skills
    def passive_skill_effect(self):
        pass

    def view_battle_stats(self):
        pass

    def choose_action(self):
        pass


class Monster_NPC(Character):
    def __init__(self, level, race, element: Elements_NPC):
        self.level = level
        self.name = race
        self.element : Elements_NPC = element
        self.sprite = None

    def get_attack_element(self):
        return self.element, None

    def get_defense_element(self):
        return self.element, None

    def basic_attack(self):
        pass

    def choose_action(self):
        pass

    def view_battle_stats(self):
        return str(self.element.name+" "+self.name+" HP: "+str(self.health)+
        " ATK: "+str(self.attack)+" DEF: "+str(self.defense))


class Ally_NPC(object):
    def __init__(self):
        self.level = 1
        self.name = None
        self.attack = 0
        self.sprite = None
    
    def level_up(self):
        self.level += 1

    def update_stats(self):
        pass

    def update_level(self, party):
        pass

    def buff_action(self):
        pass

    def attack_action(self):
        pass

    def advanced_action(self):
        pass

    def legendary_action(self):
        pass

    def choose_action(self):
        pass

    def view_stats(self):
        return str(self.name+" LEVEL: "+str(self.level))


class Hero_PC(Character):
    def __init__(self, name, level, exp):
        self.name = name
        self.level = level
        self.exp = exp

    # Update stats, depending on level and class, only used during battle
    def update_stats(self):
        self.max_health = self.level * H.HERO_BASE_HEALTH.get(self.name)
        self.attack = self.level * H.HERO_BASE_ATTACK.get(self.name)
        self.defense = self.level * H.HERO_BASE_DEFENSE.get(self.name)
        self.max_mana = self.level * H.HERO_BASE_MANA.get(self.name)
        self.max_skill = self.level * H.HERO_BASE_SKILL.get(self.name)
        self.health = self.max_health
        self.mana = self.max_mana
        self.skill = self.max_skill
        self.poison = 0
        self.status = []
        self.buffs = []
        self.skills = True
        self.turn = True
        self.magic = True

    def update_equipment(self, equipment_list: list):
        self.weapon = None
        self.armor = None
        self.accessory = None
        for equip in equipment_list:
            equipment: Equipment_NPC = equip
            if self.name in equipment.user:
                if equipment.variety == "Weapon":
                    self.weapon = equipment
                elif equipment.variety == "Armor":
                    self.armor = equipment
                elif equipment.variety == "Accessory":
                    self.accessory = equipment
    
    def update_skills(self):
        self.skill_list = []
        # First see what kind of skills to get, depending on name.
        skill_words = H.HERO_SKILL_LIST.get(self.name)
        # Then see what skills to actually add, depending on level.
        for number in range(0, self.level):
            word = skill_words.get(number)
            if word != None:
                skill = D.ALL_SKILLS.get(word)
                self.skill_list.append(skill)

    def update_spells(self):
        self.spell_list = []
        if self.mana > 0:
            spell_dictionary = H.HERO_SPELL_LIST.get(self.name)
            for number in range(0, self.level):
                spell = spell_dictionary.get(number)
                if spell != None:
                    self.spell_list.append(spell)

    def update_for_battle(self):
        self.update_stats()
        self.update_skills()
        self.update_spells()

    def update_after_battle(self, battlers: list):
        check_hero = None
        for battler in battlers:
            battler: Character
            check_hero = battler
            if battler.name == self.name:
                self.health = min(battler.health, self.max_health)
                self.skill = min(battler.skill, self.max_skill)
                self.mana = min(battler.mana, self.max_mana)
        if check_hero == None:
            self.health = 0
    
    def level_up(self):
        if self.level < C.LEVEL_CAP and self.exp >= self.level ** C.INCREASE_EXPONENT:
            self.level += 1
        elif self.level >= C.LEVEL_CAP and self.exp >= self.level ** C.INCREASE_EXPONENT:
            pass

    def equip(self, equipment: Equipment_NPC):
        if "Armor" in equipment.variety:
            self.armor = equipment
        elif "Weapon" in equipment.variety:
            self.weapon = equipment
        elif "Accessory" in equipment.variety:
            self.accessory = equipment

    def view_stats(self):
        return str("CLASS: "+self.name+" LEVEL: "+str(self.level))

    def view_battle_stats(self):
        stat_text = str(self.name+" HP: "+str(self.health)+
        " ATK: "+str(self.attack)+" DEF: "+str(self.defense))
        if len(self.skill_list) > 0:
            stat_text += (" SKL: "+str(self.skill))
        if len(self.spell_list) > 0:
            stat_text += (" MANA: "+str(self.mana))
        return stat_text

    def choose_action(self):
        pass


class Party_PC:
    def __init__(self):
        self.heroes = []
        self.battle_party = []
        self.allies = []
        self.equipment = []
        self.items = Item_Bag_PC(0, 0)

    def add_hero(self, hero: Hero_PC):
        self.heroes.append(hero)

    def add_ally(self, ally: Ally_NPC):
        self.allies.append(ally)

    def add_equipment(self, equipment: Equipment_NPC):
        self.equipment.append(equipment)

    def update_battle_party(self):
        self.battle_party = []
        for hero in self.heroes:
            copy_hero : Hero_PC = copy.deepcopy(hero)
            copy_hero.update_for_battle()
            copy_hero.update_equipment(self.equipment)
            self.battle_party.append(copy_hero)