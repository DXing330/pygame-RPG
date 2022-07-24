import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_def")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_level_up_function as lvlup_func
import rpg2_player_action_function as player_act_func
import rpg2_pet_action_function as pet_func
import draw_functions as draw_func
from rpg2_constants import Constants
C = Constants()
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#images
TOWER_RAW = pygame.image.load(os.path.join("Assets", "tower.png"))
TOWER_IMG = pygame.transform.scale(TOWER_RAW, (P.WIDTH, P.HEIGHT))
PORTAL_RAW = pygame.image.load(os.path.join("Assets", "portal.png"))
PORTAL_IMG = pygame.transform.scale(PORTAL_RAW, (P.WIDTH, P.HEIGHT))
ARENA_RAW = pygame.image.load(os.path.join("Assets", "magic_arena.png"))
ARENA_IMG = pygame.transform.scale(ARENA_RAW, (P.WIDTH, P.HEIGHT))
ENCHANTER_IMG = pygame.image.load(os.path.join("Assets", "enchanter_forest.png"))
ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_IMG, (P.WIDTH, P.HEIGHT))
#things inside the mage tower
new_summon = Pet_NPC("Angel", 1, 2)
new_spell = Spell_PC("new", 1, 1, None, 1)
#enchanter
def armor_enchanter(h_a, h_b):
        pick = True
        armor = None
        enchant = False
        while pick:
                clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_a)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
                                        armor = h_a[0]
                                        pick = False
                                        enchant = True
        while enchant:
                clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_armor_enchant_menu(armor, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
                
        
def weapon_enchanter(h_w, h_b):
        pick = True
        weapon = None
        enchant = False
        while pick:
                clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_w)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
                                        weapon = h_w[0]
                                        pick = False
                                        enchant = True
        while enchant:
                clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_armor_enchant_menu(weapon, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
                
        
def enchanter(h_b, h_w, h_a):
        enchant = True
        while enchant:
                clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_enchanter_menu()
		pygame.display.update()
		if len(h_w) <= 0 and len(h_a) <= 0:
                        WIN.fill(P.WHITE)
                        WIN.blit(ENCHANTER_IMG, P.ORIGIN)
                        error_text = REG_FONT.render("You have nothin to enchant. ", 1, P.RED)
                        WIN.blit(error_text, ((P.WIDTH - error_text.get_width())//2, P.PADDING))
                        pygame.display.update()
                        pygame.time.delay(P.SMALLDELAY)
                        enchant = False
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.QUIT:
					enchant = False
					tower = False
					pygame.quit()
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_a and len(h_a) > 0:
                                        armor_enchanter(h_a, h_b)
                                if event.key == pygame.K_w and len(h_w) > 0:
                                        weapon_enchanter(h_w, h_b)
        
#training area
def trainer(h_b, h_m):
	spell = None
	train = False
	pick = True
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_spell_list(h_m)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.QUIT:
					pick = False
					tower = False
					pygame.quit()
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					spell = h_m[0]
					pick = False
					train = True
				if event.key == pygame.K_2 and len(h_m) > 1:
					spell = h_m[1]
					pick = False
					train = True
				if event.key == pygame.K_3 and len(h_m) > 2:
					spell = h_m[2]
					pick = False
					train = True
				if event.key == pygame.K_4 and len(h_m) > 3:
					spell = h_m[3]
					pick = False
					train = True
				if event.key == pygame.K_5 and len(h_m) > 4:
					spell = h_m[4]
					pick = False
					train = True
				if event.key == pygame.K_6 and len(h_m) > 5:
					spell = h_m[5]
					pick = False
					train = True
				if event.key == pygame.K_7 and len(h_m) > 6:
					spell = h_m[5]
					pick = False
					train = True
				if event.key == pygame.K_8 and len(h_m) > 7:
					spell = h_m[5]
					pick = False
					train = True
				if event.key == pygame.K_9 and len(h_m) > 8:
					spell = h_m[5]
					pick = False
					train = True
	while train:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_train_spell_menu(spell, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.QUIT:
					train = False
					tower = False
					pygame.quit()
				if event.key == pygame.K_l:
					train = False
				if event.key == pygame.K_p:
					if h_b.coins >= spell.power ** C.INCREASE_EXPONENT:
						h_b.coins -= spell.power ** C.INCREASE_EXPONENT
						spell.power += 1
						spell.cost += 1
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ARENA_IMG, P.ORIGIN)
						draw_func.poor_text()
						train = False
				if event.key == pygame.K_a and spell.targets <= 1:
					if h_b.coins >= (C.SPELL_PRICE ** C.INCREASE_EXPONENT):
						h_b.coins -= (C.SPELL_PRICE ** C.INCREASE_EXPONENT)
						spell.targets = 2
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ARENA_IMG, P.ORIGIN)
						draw_func.poor_text()
						train = False
				if event.key == pygame.K_c and spell.cost > 1:
					if h_b.coins >= spell.power ** C.INCREASE_EXPONENT:
						h_b.coins -= spell.power ** C.INCREASE_EXPONENT
						spell.cost -= 1
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ARENA_IMG, P.ORIGIN)
						draw_func.poor_text()
						train = False
	
#summoning area
def summoner(h_p, h_ally, h_b):
	summoner = None
	angel = None
	summon = True
	while summon:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(PORTAL_IMG, P.ORIGIN)
		for hero in h_p:
			if "Summoner" in hero.name:
				summoner = hero
		if summoner == None:
			summon = False
			deny_text = REG_FONT.render("You don't have a summoner.", 1, P.BLACK)
			WIN.blit(deny_text, ((P.WIDTH - deny_text.get_width())//2, P.PADDING))
			pygame.display.update()
			pygame.time.delay(P.SMALLDELAY)
		elif summoner != None:
			for ally in h_ally:
				if "Angel" in ally.name:
					angel = ally
			draw_func.draw_summon_menu(h_ally)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.type == pygame.QUIT:
						summon = False
						tower = False
						pygame.quit()
					if event.key == pygame.K_l:
						summon = False
					if event.key == pygame.K_s:
						if angel == None:
							copy_summon = copy.copy(new_summon)
							h_ally.append(copy_summon)
						elif angel.stage < C.STAGE_LIMIT:
							if h_b.coins >= angel.atk**angel.stage:
								h_b.coins -= angel.atk**angel.stage
								lvlup_func.angel_stage_up(angel)
							else:
								WIN.fill(P.WHITE)
								WIN.blit(PORTAL_IMG, P.ORIGIN)
								draw_func.poor_text()
								summon = False
						elif angel.stage >= C.STAGE_LIMIT:
							if h_b.coins >= (angel.atk * angel.stage) ** C.INCREASE_EXPONENT:
								h_b.coins -= (angel.atk * angel.stage) ** C.INCREASE_EXPONENT
								lvlup_func.pet_atk_up(angel)
							else:
								WIN.fill(P.WHITE)
								WIN.blit(PORTAL_IMG, P.ORIGIN)
								draw_func.poor_text()
								summon = False
#mage tower
def mage_tower(h_p, h_ally, h_b, h_m, h_w, h_a):
	tower = True
	while tower:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(TOWER_IMG, P.ORIGIN)
		draw_func.draw_mage_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				tower = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					tower = False
				if event.key == pygame.K_s:
					summoner(h_p, h_ally, h_b)
				if event.key == pygame.K_t and len(h_m) > 0:
					trainer(h_b, h_m)
				if event.key == pygame.K_e:
					enchanter(h_b, h_w, h_a)
				if event.key == pygame.K_b:
					bookstore(h_b, h_m)
						
