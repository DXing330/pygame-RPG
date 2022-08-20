import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../pygame_functions/pygame_general_functions/")
sys.path.append("../pygame_functions/pyrandom_events/")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import draw_functions as draw_func
import pypick_function as pick_func
import pyrandom_events as event_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()
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
#check what has happened already
def event_check(h_b, a_npc):
	y = 1
	return y
#function that will pick what event occurs
def pick_event(h_p, h_b, h_m, h_ally, h_wpn, h_amr, qi_npc, a_npc):
	width, height = WIN.get_size()
	CITY_IMG = pygame.transform.scale(CITY_RAW, (width, height))
	WIN.blit(CITY_IMG, (0, 0))
	m_p = []
	y = event_check(h_b, a_npc)
	b = random.randint(0, y)
	if b == 0:
		ask = True
		ask_text = REG_FONT.render("Hello, fellow traveler. Want to trade?", 1, P.RED)
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
						WIN.blit(CITY_IMG, (0, 0))
						thank_text = REG_FONT.render("Excellent, let me show you my wares.", 1, P.RED)
						WIN.blit(thank_text, ((width - thank_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(500)
						event_func.random_store(h_b, h_wpn, h_amr, qi_npc, a_npc)
					elif event.key == pygame.K_n:
						ask = False
						WIN.blit(CITY_IMG, (0, 0))
						sad_text = REG_FONT.render("Alright, your loss.", 1, P.RED)
						WIN.blit(sad_text, ((width - sad_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(500)
						
