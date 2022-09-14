import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Object_Classes")
import random
from _basic_classes import Character, Elements_NPC, Passive_Effect_NPC
from _constants import Constants
C = Constants()
from _dictionaries import Dictionaries
D = Dictionaries()

class Attack_Functions():
    def __init__(self, attacker: Character, defender: Character):
        self.attacker = attacker
        self.defender = defender
        self.attack = self.attacker.attack
        self.defense = self.defender.defense
        self.attack_element : Elements_NPC = None
        self.defense_element : Elements_NPC = None
        self.attack_element_effect : Passive_Effect_NPC = None
        self.defense_element_effect : Passive_Effect_NPC = None
        self.attack_effects = []
        self.defense_effects = []

    def check_elements(self):
        if self.attack_element != None and self.defense_element != None:
            if self.attack_element.name in self.defense_element.weakness:
                self.attack = self.attack * C.ELEMENTAL_ADVANTAGE
            elif self.attack_element.name in self.defense_element.strength:
                self.attack = self.attack // C.ELEMENTAL_ADVANTAGE
        return self.attack

    def check_attack_element_effect(self):
        if self.attack_element_effect != None and self.defense_element != None:
            if self.defense_element.name in self.attack_element_effect.effect_specifics:
                if "Slay" in self.attack_element_effect.effect:
                    self.attack = self.attack * self.attack_element_effect.power
                if "Absorb" in self.attack_element_effect.effect:
                    self.attacker.health += self.attack * self.attack_element_effect.power
        return self.attack

    def check_defense_element_effect(self):
        if self.defense_element_effect != None and self.attack_element != None:
            if self.attack_element.name in self.defense_element_effect.effect_specifics:
                if "Absorb" in self.defense_element_effect.effect:
                    self.defender.health += self.defense_element_effect.power
                    self.attack = 0
                elif "Resist" in self.defense_element_effect.effect:
                    self.attack = self.attack // self.defense_element_effect.power
                elif "Negate" in self.defense_element_effect.effect:
                    self.attack = round(self.attack * (1 - (self.defense_element_effect.power / 100)))
        return self.attack
    
    def check_element_effects(self):
        self.attack = self.check_elements()
        self.attack = self.check_attack_element_effect()
        self.attack = self.check_defense_element_effect()
        return self.attack

    def change_stats(self, effect_list: list):
        for buff in effect_list:
            buff: Passive_Effect_NPC
            if "Change_Stats" in buff.effect:
                self.attacker.health += (buff.power * 
                D.BUFF_HEALTH.get(buff.effect_specifics))
                self.attacker.attack += (buff.power * 
                D.BUFF_ATTACK.get(buff.effect_specifics))
                self.attacker.defense += (buff.power * 
                D.BUFF_DEFENSE.get(buff.effect_specifics))

    def check_attack_effects(self):
        for buff in self.attack_effects:
            buff : Passive_Effect_NPC
            if "Inflict_Status" in buff.effect:
                inflict = random.randint(0, self.defender.health)
                status = D.STATUSES.get(buff.effect_specifics)
                if inflict <= self.attack * buff.power:
                    self.defender.add_effect(status)
            if "Inflict_Poison" in buff.effect:
                self.defender.poison += buff.power
            if "Increase_Attack" in buff.effect:
                if "Flat" in buff.effect_specifics:
                    self.attack += buff.power
                elif "Percentage" in buff.effect_specifics:
                    self.attack = round(self.attack * (1 + ((buff.power) / 100)))
        self.change_stats(self.attack_effects)
        return self.attack

    def check_defense_effects(self):
        for buff in self.defense_effects:
            buff : Passive_Effect_NPC
            if "Inflict_Status" in buff.effect:
                status = D.STATUSES.get(buff.effect_specifics)
                self.attacker.add_effect(status)
            if "Decrease_Attack" in buff.effect:
                if "Flat" in buff.effect_specifics:
                    self.attack -= buff.power
                if "Percentage" in buff.effect:
                    self.attack = round(self.attack * (1 - ((buff.power) / 100)))
        self.change_stats(self.defense_effects)
        self.attack -= self.defense
        return self.attack

    def calculate_ignore_defense(self):
        self.attack_element, self.attack_element_effect = self.attacker.get_attack_element()
        self.defense_element, self.defense_element_effect = self.defender.get_defense_element()
        self.attack_effects = self.attacker.get_attack_effects()
        self.attack = self.check_element_effects()
        self.attack = self.check_attack_effects()
        self.defender.health -= max(self.attack, 1)

    def calculate(self):
        self.attack_element, self.attack_element_effect = self.attacker.get_attack_element()
        self.defense_element, self.defense_element_effect = self.defender.get_defense_element()
        self.attack_effects = self.attacker.get_attack_effects()
        self.defense_effects = self.defender.get_defense_effects()
        self.attack = self.check_element_effects()
        self.attack = self.check_attack_effects()
        self.attack = self.check_defense_effects()
        self.defender.health -= max(self.attack, 1)