from re import A
import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Object_Classes")
sys.path.append("./General_Functions")
import copy
from _basic_classes import *
from _simple_classes import *
from general_class import *
from damage_class import *
from _constants import Constants
C = Constants()
from _dictionaries import Dictionaries
D = Dictionaries()
H = Hero_Dictionary()
from summon_classes import *
S = Summon_Dictionary()

class Skill_Functions:
    def __init__(self, user, skill: Skill_PC, allies: list, summons: list, enemies: list):
        self.user = user
        self.skill = skill
        self.allies = allies
        self.summons = summons
        self.enemies = enemies

    def apply_cost(self):
        self.user.skill -= self.skill.cost
        self.skill.cooldown += self.skill.cooldown_counter

    def compound_skill(self):
        self.skill_list = H.COMPOUND_SKILLS.get(self.skill.effect_specifics)
        for word in self.skill_list:
            skill = H.ALL_SKILLS.get(word)
            use_skill = Skill_Functions(self.user, skill, self.allies,
            self.summons, self.enemies)
            use_skill.compound_use()

    def attack_skill(self, target : Character):
        attack = Attack_Functions(self.user, target)
        for num in range(0, self.skill.power):
            if "Basic" in self.skill.effect_specifics:
                attack.calculate()
            elif "Ignore_Defense" in self.skill.effect_specifics:
                attack.calculate_ignore_defense()

    def change_stats(self, target):
        if "Health" in self.skill.effect_specifics:
            target.health += self.skill.power * self.user.level
        elif "Attack" in self.skill.effect_specifics:
            target.attack += self.skill.power * self.user.level//2
        elif "Defense" in self.skill.effect_specifics:
            target.defense += self.skill.power * self.user.level//4

    # The monster will choose targets randomly.
    # The player will choose targets manually.
    def pick_targets(self, pick_randomly = True):
        self.targets = []
        if "Self" in self.skill.target:
            self.targets.append(self.user)
        elif "Ally" in self.skill.target:
            pick_from = Pick_Functions(self.allies)
            ally = pick_from.pick(pick_randomly)
            self.targets.append(ally)
        elif "All_Ally" in self.skill.target:
            self.targets = self.allies
        elif "Enemy" in self.skill.target:
            pick_from = Pick_Functions(self.enemies)
            enemy = pick_from.pick(pick_randomly)
            self.targets.append(enemy)
        elif "All_Enemy" in self.skill.target:
            self.targets = self.enemies
        elif "Summon" in self.skill.target:
            pick_from = Pick_Functions(self.summons)
            summon = pick_from.pick(pick_randomly)
            self.targets.append(summon)
        elif "All_Summon" in self.skill.target:
            self.targets = self.summons

    def apply_effect(self):
        for target in self.targets:
            if "Change_Stats" in self.skill.effect:
                self.change_stats(target)
            elif "Add_Buff" in self.skill.effect:
                buff = D.BUFFS.get(self.skill.effect_specifics)
                for num in range(0, self.skill.power):
                    target.add_effect(buff)
            elif "Inflict_Status" in self.skill.effect:
                status = D.STATUSES.get(self.skill.effect_specifics)
                for num in range(0, self.skill.power):
                    target.add_effect(status)
            elif "Cure_Status" in self.skill.effect:
                for num in range(0, min(self.skill.power, len(target.status))):
                    target.status.pop(0)
            elif "Command" in self.skill.effect:
                for num in range(0, self.skill.power):
                    target.choose_action(self.allies, self.enemies)
            elif "Attack" in self.skill.effect:
                self.attack_skill(target)
        if "Summon" in self.skill.effect:
            summon = Summon_PC(self.skill.effect_specifics, self.user.level)
            summon.update_for_battle()
            for num in range(0, self.skill.power):
                copy_summon = copy.deepcopy(summon)
                self.allies.append(copy_summon)
        if "Skill" in self.skill.effect:
            self.compound_skill()

    def use(self):
        if self.skill.cooldown <= 0:
            self.apply_cost()
            if self.user.skill >= 0:
                self.pick_targets(pick_randomly=False)
                self.apply_effect()

    def compound_use(self):
        self.pick_targets(pick_randomly=False)
        self.apply_effect()

    def monster_use(self):
        self.apply_cost()
        self.pick_targets(pick_randomly=True)
        self.apply_effect()

    def summon_use(self):
        self.pick_targets(pick_randomly=True)
        self.apply_effect()


class Spell_Functions:
    def __init__(self, user: Character, spell: Spell_PC, enemies: list):
        self.user = user
        self.spell = spell
        self.enemies = enemies
        self.attack = self.spell.power + self.user.mana
        self.element = self.spell.element.name
        self.defender_element = None

    def apply_cost(self):
        self.user.mana -= self.spell.cost

    def apply_damage(self):
        for enemy in self.enemies:
            enemy : Character
            self.element : Elements_NPC
            self.defender_element : Elements_NPC = enemy.get_defense_element()
            if self.defender_element != None:
                if self.element.name in self.defender_element.weakness:
                    enemy.health -= self.attack * C.ELEMENTAL_ADVANTAGE
                elif self.element.name in self.defender_element.strength:
                    enemy.health -= self.attack // C.ELEMENTAL_ADVANTAGE
                else:
                    enemy.health -= self.attack
            elif self.defender_element == None:
                enemy.health -= self.attack
    
    def apply_effect(self):
        if "Inflict_Status" in self.spell.effect:
            status = D.STATUSES.get(self.spell.effect_specifics)
            for enemy in self.enemies:
                if enemy.health > 0:
                    inflict = random.randint(0, enemy.health)
                    if inflict <= self.attack:
                        enemy.add_effect(status)
        if "Decrease_Stats" in self.spell.effect:
            if "Health" in self.spell.effect_specifics:
                for enemy in self.enemies:
                    enemy.health -= self.spell.power
            if "Attack" in self.spell.effect_specifics:
                for enemy in self.enemies:
                    enemy.attack -= self.spell.power
            if "Defense" in self.spell.effect_specifics:
                for enemy in self.enemies:
                    enemy.defense -= self.spell.power

    def cast(self):
        self.apply_cost()
        if self.user.mana >= 0:
            self.apply_damage()
            self.apply_effect()

