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
D = Dictionaries()
from damage_class import *
from skill_class import *
from _draw_classes import *


class Advanced_Monster(Monster_NPC):
    def __init__(self, name, level = 0):
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

    def update_buffs(self):
        buff_list = M.MONSTER_BUFF_LISTS.get(self.name)
        if buff_list != None:
            for buff in buff_list:
                new_buff : Passive_Effect_NPC = D.BUFFS.get(buff)
                self.add_effect(new_buff)

    def update_element(self):
        element_name : str = self.elements[random.randint(0, len(self.elements) - 1)]
        self.element = D.ELEMENTS.get(element_name)

    def update_stats(self):
        while self.level <= 0:
            self.level = round(random.gauss(M.MONSTER_MEAN_LEVEL.get(self.name),
            M.MONSTER_LEVEL_VAR.get(self.name)))
        self.max_health = self.level * M.MONSTER_HEALTH.get(self.name)
        self.health = self.max_health
        self.attack = self.level * M.MONSTER_ATTACK.get(self.name)   
        self.defense = self.level * M.MONSTER_DEFENSE.get(self.name)
        self.max_skill = self.level * M.MONSTER_SKILL_POINTS.get(self.name)
        self.skill = self.max_skill
        self.elements : list = M.MONSTER_ELEMENTS.get(self.name)
    
    def update_for_battle(self):
        self.update_stats()
        self.update_element()
        self.update_skills()
        self.update_buffs()

    def basic_attack(self):
        self.skill += 1
        damage = Attack_Functions(self, self.enemy)
        damage.calculate()

    def use_skill(self, skill: Skill_PC):
        self.used_skill : Skill_PC = skill
        used_skill = Skill_Functions(self, self.used_skill,
        self.allies, [], self.enemies)
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

    def death_action(self, enemies: list, allies: list):
        self.enemies = enemies
        self.allies = allies
        self.death_actions = []
        for buff in self.buffs:
            buff : Passive_Effect_NPC
            if buff.timing == "Death":
                skill : Skill_PC = D.ALL_SKILLS.get(buff.effect_specifics)
                for num in range(0, buff.power):
                    copy_skill = copy.copy(skill)
                    self.passive_skills.append(copy_skill)
        if len(self.enemies) > 0:
            for skill in self.death_actions:
                self.use_skill(skill)

    def passive_skill_effect(self, enemies: list, allies: list):
        self.enemies = enemies
        self.allies = allies
        self.passive_skills = []
        for buff in self.buffs:
            buff : Passive_Effect_NPC
            if buff.timing == "Every_Turn" and buff.effect == "Skill":
                skill = D.ALL_SKILLS.get(buff.effect_specifics)
                for num in range(0, buff.power):
                    copy_skill = copy.copy(skill)
                    self.passive_skills.append(copy_skill)
        if len(self.enemies) > 0:
            for skill in self.passive_skills:
                self.use_skill(skill)
        


class Monster_Groups:
    def __init__(self):
        self.MONSTER_GROUPS = {
        0 : [Advanced_Monster("Goblin")],
        1 : [Advanced_Monster("Goblin"), Advanced_Monster("Goblin")],
        2 : [Advanced_Monster("Goblin"), Advanced_Monster("Goblin"), Advanced_Monster("Goblin")],
        3 : [Advanced_Monster("Goblin", 5), Advanced_Monster("Goblin"), Advanced_Monster("Goblin")],
        4 : [Advanced_Monster("Werewolf")],
        5 : [Advanced_Monster("Werewolf"), Advanced_Monster("Werewolf")]
        }
