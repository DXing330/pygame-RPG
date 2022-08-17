import pygame
pygame.init()
import os
import sys
import json
import copy
import random
sys.path.append(".")
sys.path.append("./pygame_functions")
sys.path.append("../RPG2v3/RPG2v3_functions")
sys.path.append("./pygame_functions/pyquest")
sys.path.append("../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../RPG2v3/RPG2v3_functions/bossbattles")
sys.path.append("./pygame_functions/pybattle_functions")
sys.path.append("./pygame_functions/pygame_general_functions")
sys.path.append("./pygame_functions/pygame_draw")
sys.path.append("./pygame_functions/pyboss")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import pyparty_functions as party_func
import pymonster_function as monster_func
import rpg2_save_function as save_func
import pyrandom_boss as boss_func
from rpg2_constants import Constants
C = Constants()
from rpg2_constant_lists import List_Constants
L = List_Constants()
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import pybattle_functions as pybattle_func
import pycity_functions as pycity_func
import pymage_tower_functions as pymage_func
import pymonster_hunter_functions as pyhunt_func
import pyquest_function as pyquest_func
import pytutorial as tutorial_func
#clock
clock = pygame.time.Clock()
#makes fonts
pygame.font.init()
#makes sound
pygame.mixer.init()
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT), pygame.RESIZABLE)
ww, wh = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#images used
PLAINS_RAW = pygame.image.load(os.path.join("Assets", "plains.png"))
PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (P.WIDTH, P.HEIGHT))
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
SPACE_RAW = pygame.image.load(os.path.join("Assets", "space.png"))
SPACE_IMG = pygame.transform.scale(SPACE_RAW, (P.WIDTH, P.HEIGHT))


#function will make the plains background        
def draw_plains(h_p, bag, q):
	WIN.fill(P.WHITE)
	width, height = WIN.get_size()
	PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (width, height))
	WIN.blit(PLAINS_IMG, P.ORIGIN)
	draw_func.draw_menu(q)
	x = 1
	for hero in h_p:
		stat_text = REG_FONT.render("Hero: "+hero.name+" ATK: "+str(hero.atk+hero.atkbonus)+
					    " DEF: "+str(hero.defense+hero.defbonus)+" HP%: "+str((round(hero.health/hero.maxhealth, 2))*100)+
					    " MP: "+str(hero.mana)+" SKL: "+str(hero.skill)+" PSN: "+str(hero.poison), 1, P.WHITE)
		WIN.blit(stat_text, ((width - stat_text.get_width() - P.PADDING), P.PADDING * x))
		x +=1
	coins_text = REG_FONT.render("GOLD: "+str(bag.coins), 1, P.WHITE)
	WIN.blit(coins_text, ((width - coins_text.get_width() - P.PADDING), P.PADDING * x))
	pygame.display.update()

def RPG(h_party, h_magic, h_bag, h_ally, h_wpn, h_amr, quest, access):
	m_p = []
	game = True
	while game:
		pygame.event.clear()
		draw_plains(h_party, h_bag, quest)
		draw_func.draw_heroes(h_party, h_ally)
		clock.tick(1)
		for event in pygame.event.get():
			pygame.event.clear()
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_a:
					pygame.event.clear()
					for hero in h_party:
						x = random.randint(0, 2)
						if x > 0:
							for y in range(0, x):
								mon = monster_func.random_scaled_monster(hero, h_bag)
								m_p.append(mon)
					pybattle_func.battle(h_party, m_p, h_ally, h_bag,
							     h_magic, h_wpn, h_amr)
				elif event.key == pygame.K_c:
					pygame.event.clear()
					pycity_func.city(h_party, h_bag, h_wpn, h_amr)
				elif event.key == pygame.K_t:
					pygame.event.clear()
					tutorial_func.old_warrior(access)
				elif event.key == pygame.K_v:
					pygame.event.clear()
					boss_func.pick_boss(h_party, h_bag, h_magic, h_ally,
							    h_wpn, h_amr, quest, access)
				elif event.key == pygame.K_w:
					pygame.event.clear()
					pymage_func.mage_tower(h_party, h_ally, h_bag,
							       h_magic, h_wpn, h_amr)
				elif event.key == pygame.K_p:
					pygame.event.clear()
					pyquest_func.quest(h_party, h_bag, h_magic, h_ally,
							   h_wpn, h_amr, quest, access)
				elif event.key == pygame.K_m:
					pygame.event.clear()
					if h_bag.dg_trophy > 0:
						pyhunt_func.monster_hunter_guild(h_party, h_bag, h_ally,
										 h_wpn, h_amr, quest, access)
					else:
						x, y = WIN.get_size()
						PLAINS_IMG = pygame.transform.scale(PLAINS_RAW,
						    (x, y))
						WIN.blit(PLAINS_IMG, P.ORIGIN)
						reject_text = REG_FONT.render("Come back when you've proven yourself.",
									    1, P.WHITE)
						WIN.blit(reject_text, ((x - reject_text.get_width())//2, y//3))
						pygame.display.update()
						pygame.time.delay(1000)
				elif event.key == pygame.K_r:
					pygame.event.clear()
					save_func.write_to_files(h_party, h_magic,
								 h_bag, h_ally,
								 h_wpn, h_amr,
								 quest, access,
								 "RPG2_ \n ")
					x, y = WIN.get_size()
					PLAINS_IMG = pygame.transform.scale(PLAINS_RAW,
					    (x, y))
					WIN.blit(PLAINS_IMG, P.ORIGIN)
					save_text = REG_FONT.render("You've recorded your adventures.",
								    1, P.GREEN)
					WIN.blit(save_text, ((x - save_text.get_width())//2, y//3))
					pygame.display.update()
					pygame.time.delay(1000)
				elif event.key == pygame.K_s:
					game = False
					pygame.quit()
					

def Start():
	#inital variables
	heroes_party = []
	heroes_magic = []
	heroes_allies = []
	heroes_bag = ItemBag_PC(1, 1, 1, 50)
	heroes_weapons = []
	heroes_armor = []
	q_items = QuestItems_NPC()
	a_items = Access_NPC()
	hero = Player_PC("Hero", 1, 15, 15, 5, 4, 2, 2, 2)
	hero_sword = Weapon_PC("LS", "Hero", "Attack", 1, "Light", 1)
	hero_armor = Armor_PC("LA", "Hero", "Block", 1, "Light", 1)
	start = True
	while start:
		clock.tick(P.FPS)
		continue_text = REG_FONT.render("CONTINUE: C", 1, P.WHITE)
		start_text = REG_FONT.render("START: S", 1, P.WHITE)
		WIN.fill(P.BLACK)
		x, y = WIN.get_size()
		SPACE_IMG = pygame.transform.scale(SPACE_RAW, (x, y))
		WIN.blit(SPACE_IMG, P.ORIGIN)
		WIN.blit(continue_text, ((x - continue_text.get_width())//2, y//3))
		WIN.blit(start_text, ((x - start_text.get_width())//2, y//3 + P.PADDING * 2))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					party_func.add_to_party(heroes_party, hero)
					heroes_weapons.append(hero_sword)
					heroes_armor.append(hero_armor)
					start = False
					
				if event.key == pygame.K_c:
					heroes_list, heroes_magic_list, items_bag_obj, allies, weapons, armor, quest, access = save_func.read()
					heroes_party = heroes_list
					heroes_magic = heroes_magic_list
					heroes_bag = items_bag_obj
					heroes_allies = allies
					heroes_weapons = weapons
					heroes_armor = armor
					q_items = quest
					a_items = access
					start = False
					
	RPG(heroes_party, heroes_magic, heroes_bag, heroes_allies,
	    heroes_weapons, heroes_armor, q_items, a_items)

Start()
#roadmap:
#quest battles +
#boss battles
#better animations
#better sprites
#steal more artwork
