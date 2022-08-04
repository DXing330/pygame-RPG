import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../../RPG2v3/RPG2v3_functions/")
sys.path.append("../pygame_functions/pygame_general_functions/")
sys.path.append("./pyboss/pydemon_general.py")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import draw_functions as draw_func
import pypick_function as pick_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()
import pydemon_general as pydg_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#check what bosses have been beaten
def trophy_check(h_b):
	y = 0
	return y
#function that will pick a boss to fight
def pick_boss(h_p, h_b, h_m, h_ally, h_wpn, h_amr, qi_npc, a_npc):
	m_p = []
	y = trophy_check(h_b)
	b = random.randint(0, y)
	if b == 0:
		pydg_func.battle(h_p, m_p, h_ally, h_b, h_m,
				 h_wpn, h_amr)
