import pygame
pygame.init()
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../pygame_general_functions/")
sys.path.append("../")
sys.path.append("../../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import random_item_generators as item_func
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
REG_FONT = pygame.font.SysFont("comicsans", 25)
#always make a clock
clock = pygame.time.Clock()
CITY_RAW = pygame.image.load("../../Assets/village2.png")
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
#functions for different events
def random_store(h_b, h_wpn, h_amr, qi_npc, a_npc):
	width, height = WIN.get_size()
	equip, equip_text = item_func.random_equip(h_b, qi_npc, a_npc)
	CITY_IMG = pygame.transform.scale(CITY_RAW, (width, height))
	WIN.blit(CITY_IMG, (0, 0))
	WIN.blit(equip_text, ((width - equip_text.get_width())//2, P.PADDING * 1))
	price_text = REG_FONT.render("I only sell the best, it'll cost 100000 coins.", 1, P.BLACK)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 2))
	answer_text = REG_FONT.render("BUY/LEAVE?", 1, P.BLACK)
	WIN.blit(answer_text, ((width - answer_text.get_width())//2, P.PADDING * 3))
	pygame.display.update()
	store = True
	while store:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				store = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_b:
					store = False
					if h_b.coins >= 100000:
						h_b.coins -= 100000
						h_wpn.append(equip)
						WIN.blit(CITY_IMG, (0, 0))
						happy_text = REG_FONT.render("You won't regret this!", 1, P.RED)
						WIN.blit(happy_text, ((width - happy_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(500)
					elif h_b.coins < 100000:
						WIN.blit(CITY_IMG, (0, 0))
						sad_text = REG_FONT.render("You can't afford that.", 1, P.RED)
						WIN.blit(sad_text, ((width - sad_text.get_width())//2, P.PADDING * 3))
						pygame.display.update()
						pygame.time.delay(500)
				elif event.key == pygame.K_l:
					store = False
					WIN.blit(CITY_IMG, (0, 0))
					sad_text = REG_FONT.render("Oh well, I'm sure someone wiser will come and take this great deal.", 1, P.RED)
					WIN.blit(sad_text, ((width - sad_text.get_width())//2, P.PADDING * 3))
					pygame.display.update()
					pygame.time.delay(1000)

