import random
from _basic_classes import *
from _constants import *
from upgrade_class import *
from skill_class import *
from advanced_monster_class import M
C = Constants()
from _dictionaries import *
A = Ally_Dictionary()

class Angel_NPC(Ally_NPC):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def update_stats(self):
        self.skill_list = []
        skill_dictionary = A.SKILL_LISTS.get(self.name)
        for number in range(0, self.level):
            skill = skill_dictionary.get(number)
            if skill != None:
                self.skill_list.append(skill)

    def update_level(self, party: Party_PC):
        upgrade = Upgrade(party)
        upgrade.upgrade_ally()
    
    def choose_action(self, heroes_list, monsters_list):
        if len(heroes_list) > 0 and len(monsters_list) > 0:
            self.skill = self.skill_list[random.randint(0, len(self.skill_list) - 1)]
            use_skill = Skill_Functions(self, self.skill, heroes_list, None, monsters_list)
            use_skill.summon_use()