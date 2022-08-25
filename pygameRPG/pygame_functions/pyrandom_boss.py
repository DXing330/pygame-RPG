import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../pygame_functions/pygame_general_functions/")
sys.path.append("./pyboss/pydemon_general.py")
sys.path.append("./pyboss/pyhydra.py")
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
import pyhydra as pyhydra_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
CITY_RAW = pygame.image.load(os.path.join("Assets", "village2.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
THRONE_RAW = pygame.image.load(os.path.join("Assets", "throne2.png"))
THRONE_IMG = pygame.transform.scale(THRONE_RAW, (P.WIDTH, P.HEIGHT))
#check what bosses have been beaten
def trophy_check(h_b, a_npc):
	y = 1
	return y
#function that will pick a boss to fight
def pick_boss(h_p, h_b, h_m, h_ally, h_wpn, h_amr, qi_npc, a_npc):
	width, height = WIN.get_size()
	CITY_IMG = pygame.transform.scale(CITY_RAW, (width, height))
	WIN.blit(CITY_IMG, (0, 0))
	m_p = []
	y = trophy_check(h_b, a_npc)
	b = random.randint(0, y)
	if b == 0:
		ask = True
		ask_text = REG_FONT.render("Please help us. A demon general is terrorizing our town.", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 2))
		answer_text = REG_FONT.render("YES/NO?", 1, P.RED)
		WIN.blit(answer_text, ((width - answer_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		while ask:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ask = False
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					pygame.event.clear()
					if event.key == pygame.K_y:
						ask = False
						a_npc.posrep += 1
						WIN.blit(CITY_IMG, (0, 0))
						thank_text = REG_FONT.render("Good luck, he's in the castle over there.", 1, P.RED)
						WIN.blit(thank_text, ((width - thank_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(1000)
						THRONE_IMG = pygame.transform.scale(THRONE_RAW, (width, height))
						WIN.blit(THRONE_IMG, (0, 0))
						walk_text = REG_FONT.render("The heroes march up to the castle.", 1, P.RED)
						WIN.blit(walk_text, ((width - walk_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(1000)
						pydg_func.battle(h_p, m_p, h_ally, h_b, h_m,
								 h_wpn, h_amr)
					elif event.key == pygame.K_n:
						ask = False
						a_npc.negrep += 1
						a_npc.fame -= min(a_npc.fame, a_npc.rank)
						WIN.blit(CITY_IMG, (0, 0))
						sad_text = REG_FONT.render("We understand, perhaps a braver soul will save us.", 1, P.RED)
						WIN.blit(sad_text, ((width - sad_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(1000)
	elif b == 1:
		ask = True
		ask_text = REG_FONT.render("Please help us. A hydra is terrorizing our swamp!", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 2))
		answer_text = REG_FONT.render("YES/NO?", 1, P.RED)
		WIN.blit(answer_text, ((width - answer_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		while ask:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ask = False
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					pygame.event.clear()
					if event.key == pygame.K_y:
						ask = False
						a_npc.posrep += 1
						WIN.blit(CITY_IMG, (0, 0))
						thank_text = REG_FONT.render("Good luck, it's somewhere in the swamp.", 1, P.RED)
						WIN.blit(thank_text, ((width - thank_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(1000)
						pyhydra_func.battle(h_p, m_p, h_ally, h_b, h_m, h_wpn, h_amr)
					elif event.key == pygame.K_n:
						ask = False
						a_npc.negrep += 1
						a_npc.fame -= min(a_npc.fame, a_npc.rank)
						WIN.blit(CITY_IMG, (0, 0))
						sad_text = REG_FONT.render("We understand, perhaps a braver soul will save us.", 1, P.RED)
						WIN.blit(sad_text, ((width - sad_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(1000)
						
