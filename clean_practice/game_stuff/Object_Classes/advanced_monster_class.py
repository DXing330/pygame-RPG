import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Object_Classes")
sys.path.append("./General_Functions")
sys.path.append("./Battle_Functions")
import random
from _basic_classes import *
from _list_constants import LConstants
L = LConstants
from _dictionaries import *
M = Monster_Dictionary()
from damage_class import *
from skill_class import *
from _draw_classes import *


class Advanced_Monster(Monster_NPC):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.element = None
        self.poison = 0
        self.buffs = []
        self.status = []
        self.skill_list = []
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.turn = True
        self.skills = True

    def update_skills(self):
        skill_list = M.MONSTER_SKILL_LISTS.get(self.name)
        if skill_list != None:
            for skill in skill_list:
                new_skill : Skill_PC = M.MONSTER_SKILLS.get(skill)
                self.skill_list.append(new_skill)

    def update_stats(self):
        self.max_health = self.level * M.MONSTER_HEALTH.get(self.name)
        self.health = self.max_health
        self.attack = self.level * M.MONSTER_ATTACK.get(self.name)   
        self.defense = self.level * M.MONSTER_DEFENSE.get(self.name)
        self.max_skill = self.level * M.MONSTER_SKILL_POINTS.get(self.name)
        self.skill = self.max_skill
        self.element : Elements_NPC = L.ELEMENTS[random.randint(0, len(L.ELEMENTS) - 1)]
    
    def update_for_battle(self):
        self.update_stats()
        self.update_skills()

    def basic_attack(self):
        self.skill += 1
        damage = Attack_Functions(self, self.enemy)
        damage.calculate()

    def use_skill(self, skill: Skill_PC):
        self.used_skill : Skill_PC = skill
        used_skill = Skill_Functions(self, self.used_skill, self.allies, [], self.enemies)
        used_skill.monster_use()

    def choose_skill(self):
        if len(self.skill_list) > 0:
            skill = self.skill_list[random.randint(0, len(self.skill_list) - 1)]
            self.use_skill(skill)
        else:
            self.basic_attack()

    def choose_action(self, enemies: list, allies: list):
        self.enemies = enemies
        self.allies = allies
        if len(self.enemies) > 0:
            self.enemy = self.enemies[random.randint(0, len(self.enemies) - 1)]
            if self.skill > 0 and self.skills:
                self.choose_skill()
            else:
                self.basic_attack()


class Monster_Groups:
    def __init__(self):
        self.MONSTER_GROUPS = {
        0 : [Monster_NPC(1, "Goblin")],
        1 : [Monster_NPC(2, "Goblin")],
        2 : [Monster_NPC(2, "Goblin"), Monster_NPC(2, "Goblin")]
        }
