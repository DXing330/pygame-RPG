import copy
import random
import sys
import cowsay
sys.path.append("../RPG2v3_functions/RPG2v3_def")
sys.path.append("../RPG2v3_functions/RPG2v3_battle")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
L = List_Constants()
C = Constants()

cowsay.cow("Zelene was right again. ")
cowsay.dragon("Duke was right again. ")
