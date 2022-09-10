import copy
from _basic_classes import *
from _simple_classes import *
from general_class import *
from _constants import Constants
C = Constants()
from _dictionaries import Dictionaries
D = Dictionaries()
from summon_classes import *
S = Summon_Dictionary()

class Skill_Functions:
    def __init__(self, hero: Character, skill: Skill_PC, allies: list, summons: list, enemies: list):
        self.hero = hero
        self.skill = skill
        self.allies = allies
        self.summons = summons
        self.enemies = enemies

    def apply_cost(self):
        print (self.hero.skill)
        self.hero.skill -= self.skill.cost
        if self.hero.skill > self.hero.max_skill:
            self.hero.skill = self.hero.max_skill

    def update_target(self):
        self.targets = []
        if "Self" in self.skill.target:
            self.targets.append(self.hero)
        if "Summoned_Ally" in self.skill.target:
            pick_from = Pick_Functions(self.summons)
            summon = pick_from.pick()
            self.targets.append(summon)
        if "All_Summoned_Ally" in self.skill.target:
            for summon in self.summons:
                self.targets.append(summon)
        if "Ally" in self.skill.target:
            pick_from = Pick_Functions(self.allies)
            ally = pick_from.pick()
        if "All_Ally" in self.skill.target:
            for ally in self.allies:
                self.targets.append(ally)
        if "Enemy" in self.skill.target:
            pick_from = Pick_Functions(self.enemies)
            enemy = pick_from.pick()
        if "All_Enemy" in self.skill.target:
            for enemy in self.enemies:
                self.targets.append(enemy)

    def apply_effect(self):
        if "Increase_Stats" in self.skill.effect:
            if "Health" in self.skill.effect_specifics:
                for target in self.targets:
                    target.health += self.skill.power + self.hero.level
            if "Attack" in self.skill.effect_specifics:
                for target in self.targets:
                    target.attack += self.skill.power + self.hero.level//2
            if "Defense" in self.skill.effect_specifics:
                for target in self.targets:
                    target.defense += self.skill.power + self.hero.level//4
        if "Decrease_Stats" in self.skill.effect:
            if "Health" in self.skill.effect_specifics:
                for target in self.targets:
                    target.health -= self.skill.power + self.hero.level
            if "Attack" in self.skill.effect_specifics:
                for target in self.targets:
                    target.attack -= self.skill.power + self.hero.level//2
            if "Defense" in self.skill.effect_specifics:
                for target in self.targets:
                    target.defense -= self.skill.power + self.hero.level//4
        if "Add_Buff" in self.skill.effect:
            buff = D.BUFFS.get(self.skill.effect_specifics)
            for target in self.targets:
                target.add_effect(buff)
        if "Inflict_Status" in self.skill.effect:
            status = D.STATUSES.get(self.skill.effect_specifics)
            for target in self.targets:
                target.add_effect(status)
        if "Cure_Status" in self.skill.effect:
            for target in self.targets:
                for num in range(0, min(self.skill.power, len(target.status))):
                    target.status.pop(0)
        if "Summon" in self.skill.effect:
            summon = Summon_PC(self.skill.effect_specifics, self.hero.level)
            for num in range(0, self.skill.power):
                copy_summon = copy.copy(summon)
                self.allies.append(copy_summon)
        if "Command" in self.skill.effect:
            for target in self.targets:
                target: Ally_NPC
                target.choose_action(self.allies, self.enemies)

    def use(self):
        self.apply_cost
        if self.hero.skill >= 0:
            self.update_target()
            self.apply_effect()


class Spell_Functions:
    def __init__(self, hero: Character, spell: Spell_PC, enemies: list):
        self.hero = hero
        self.spell = spell
        self.enemies = enemies
        self.attack = self.spell.power + self.hero.mana
        self.element = self.spell.element.name
        self.defender_element = None

    def apply_cost(self):
        self.hero.mana -= self.spell.cost

    def apply_damage(self):
        for enemy in self.enemies:
            self.defender_element : Elements_NPC = enemy.get_defense_element()
            if self.defender_element != None:
                if self.element in self.defender_element.weakness:
                    enemy.health -= self.attack * C.ELEMENTAL_ADVANTAGE
                elif self.element in self.defender_element.strength:
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
        if self.hero.mana >= 0:
            self.apply_damage()
            self.apply_effect()

