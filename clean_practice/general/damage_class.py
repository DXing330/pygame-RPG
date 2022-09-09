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
        self.attack_effects = []
        self.defense_effects = []

    def check_elements(self):
        if self.attack_element != None and self.defense_element != None:
            if self.attack_element.name in self.defense_element.weakness:
                self.attack = self.attack * C.ELEMENTAL_ADVANTAGE
            elif self.attack_element.name in self.defense_element.strength:
                self.attack = self.attack // C.ELEMENTAL_ADVANTAGE
        return self.attack

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
            if "Increase_FLAT" in buff.effect:
                self.attack += buff.effect_specifics * buff.power
            if "Increase_SCALE" in buff.effect:
                self.attack = round(self.attack * (1 + ((buff.effect_specifics * buff.power) / 100)))
            if "Change_Stats" in buff.effect:
                self.attacker.health += buff.power * D.BUFF_HEALTH.get(buff.effect_specifics)
                self.attacker.attack += buff.power * D.BUFF_ATTACK.get(buff.effect_specifics)
                self.attacker.defense += buff.power * D.BUFF_DEFENSE.get(buff.effect_specifics)
        return self.attack

    def check_defense_effects(self):
        for buff in self.defense_effects:
            buff : Passive_Effect_NPC
            if "Inflict_Status" in buff.effect:
                status = D.STATUSES.get(buff.effect_specifics)
                self.attacker.add_effect(status)
            if "Increase_FLAT" in buff.effect:
                self.attack -= buff.effect_specifics * buff.power
            if "Increase_SCALE" in buff.effect:
                self.attack = round(self.attack * (1 - ((buff.effect_specifics * buff.power) / 100)))
            if "Change_Stats" in buff.effect:
                self.attacker.health -= buff.power * D.BUFF_HEALTH.get(buff.effect_specifics)
                self.attacker.attack -= buff.power * D.BUFF_ATTACK.get(buff.effect_specifics)
                self.attacker.defense -= buff.power * D.BUFF_DEFENSE.get(buff.effect_specifics)
        self.attack -= self.defender.defense
        return self.attack

    def calculate(self):
        self.attack_element = self.attacker.get_attack_element()
        self.defense_element = self.defender.get_defense_element()
        self.attack_effects = self.attacker.get_attack_effects()
        self.defense_effects = self.defender.get_defense_effects()
        self.attack = self.check_elements()
        self.attack = self.check_attack_effects()
        self.attack = self.check_defense_effects()
        self.defender.health -= max(self.attack, 1)