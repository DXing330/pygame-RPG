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
#also need any specific images
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
INN_RAW = pygame.image.load(os.path.join("Assets", "inn.png"))
INN_IMG = pygame.transform.scale(INN_RAW, (P.WIDTH, P.HEIGHT))
INNB_RAW = pygame.image.load(os.path.join("Assets", "inn_bedroom.png"))
INNB_IMG = pygame.transform.scale(INN_RAW, (P.WIDTH, P.HEIGHT))
ARENA_RAW = pygame.image.load(os.path.join("Assets", "practice_arena.png"))
ARENA_IMG = pygame.transform.scale(ARENA_RAW, (P.WIDTH, P.HEIGHT))
FORGE_RAW = pygame.image.load(os.path.join("Assets", "forge.png"))
FORGE_IMG = pygame.transform.scale(FORGE_RAW, (P.WIDTH, P.HEIGHT))
#need additional images for the inn, equipment store and practice arena
#store the starter characters incase the player recruits them
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 2, 2, 2)
cleric = Player_PC("Cleric", 1, 10, 10, 3, 3, 2, 3, 3)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 2, 5, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 2, 0, 0)
ninja = Player_PC("Ninja", 1, 15, 15, 3, 3, 5, 2, 2)
knight = Player_PC("Knight", 1, 20, 20, 3, 4, 2, 0, 0)
tactician = Player_PC("Tactician", 1, 10, 10, 1, 1, 5, 0, 0)
#function that will train equipment stats
def forge(h_b, h_w, h_a):
	weapon = None
	armor = None
	upgrade_power = False
	upgrade_stat = False
	pick_wpn = False
	pick_amr = False
	choose = True
	while choose:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW,
						   (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		draw_func.draw_forge_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					choose = False
				if event.key == pygame.K_w:
					if h_b.coins >= C.WEAPON_PRICE:
						h_b.coins -= C.WEAPON_PRICE
						new = Weapon_PC("Weapon", "None", "Attack", 1, "None", 1)
						h_w.append(new)
					else:
						WIN.fill(P.WHITE)
						WIN.blit(FORGE_IMG, P.ORIGIN)
						poor_text = REG_FONT.render("You can't afford that right now. ",
									    1, P.RED)
						WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
						pygame.display.update()
						pygame.time.delay(P.SMALLDELAY)
				if event.key == pygame.K_a:
					if h_b.coins >= C.ARMOR_PRICE:
						h_b.coins -= C.ARMOR_PRICE
						new = Armor_PC("Armor", "None", "Block", 1, "None", 1)
						h_a.append(new)
					else:
						WIN.fill(P.WHITE)
						WIN.blit(FORGE_IMG, P.ORIGIN)
						poor_text = REG_FONT.render("You can't afford that right now. ",
									    1, P.RED)
						WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
						pygame.display.update()
						pygame.time.delay(P.SMALLDELAY)
				#when this happens, first pick the weapon
				#then go to the upgrade screen
				if event.key == pygame.K_s and len(h_w) > 0:
					pick_wpn = True
					upgrade_stat = True
					choose = False
				if event.key == pygame.K_i and len(h_w) > 0:
					pick_wpn = True
					upgrade_power = True
					choose = False
				if event.key == pygame.K_e and len(h_a) > 0:
					pick_amr = True
					upgrade_stat = True
					choose = False
				if event.key == pygame.K_b and len(h_a) > 0:
					pick_amr = True
					upgrade_power = True
					choose = False
	while pick_wpn:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW,
						   (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_w)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick_wpn = False
				if event.key == pygame.K_1:
					weapon = h_w[0]
					pick_wpn = False
				if event.key == pygame.K_2 and len(h_w) > 1:
					weapon = h_w[1]
					pick_wpn = False
				if event.key == pygame.K_3 and len(h_w) > 2:
					weapon = h_w[2]
					pick_wpn = False
				if event.key == pygame.K_4 and len(h_w) > 3:
					weapon = h_w[3]
					pick_wpn = False
				if event.key == pygame.K_5 and len(h_w) > 4:
					weapon = h_w[4]
					pick_wpn = False
				if event.key == pygame.K_6 and len(h_w) > 5:
					weapon = h_w[5]
					pick_wpn = False
				if event.key == pygame.K_7 and len(h_w) > 6:
					weapon = h_w[6]
					pick_wpn = False
				if event.key == pygame.K_8 and len(h_w) > 7:
					weapon = h_w[7]
					pick_wpn = False
				if event.key == pygame.K_9 and len(h_w) > 8:
					weapon = h_w[8]
					pick_wpn = False
	while pick_amr:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW,
						   (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_a)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick_amr = False
				if event.key == pygame.K_1:
					armor = h_a[0]
					pick_amr = False
				if event.key == pygame.K_2 and len(h_a) > 1:
					armor = h_a[1]
					pick_amr = False
				if event.key == pygame.K_3 and len(h_a) > 2:
					armor = h_a[2]
					pick_amr = False
				if event.key == pygame.K_4 and len(h_a) > 3:
					armor = h_a[3]
					pick_amr = False
				if event.key == pygame.K_5 and len(h_a) > 4:
					armor = h_a[4]
					pick_amr = False
				if event.key == pygame.K_6:
					if len(h_a) > 5:
						armor = h_a[5]
						pick_amr = False
				if event.key == pygame.K_7 and len(h_a) > 6:
					armor = h_a[6]
					pick_amr = False
				if event.key == pygame.K_8 and len(h_a) > 7:
					armor = h_a[7]
					pick_amr = False
				if event.key == pygame.K_9 and len(h_a) > 8:
					armor = h_a[8]
					pick_amr = False
	while upgrade_power:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW,
						   (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		pygame.display.update()
		if weapon != None:
			wpn_stats = REG_FONT.render("EFFECT: " + weapon.effect + " POWER: " + str(weapon.strength), 1, P.RED)
			WIN.blit(wpn_stats, ((P.WIDTH - wpn_stats.get_width())//2, P.PADDING))
			upgrade_text = REG_FONT.render("U/UPGRADE PRICE: " + str(C.WEAPON_PRICE * (weapon.strength ** C.INCREASE_EXPONENT)),
						       1, P.RED)
			WIN.blit(upgrade_text, ((P.WIDTH - upgrade_text.get_width())//2, P.PADDING * 2))
			coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.RED)
			WIN.blit(coins_text, ((P.WIDTH - coins_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 4))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						upgrade_power = False
					if event.key == pygame.K_u:
						if h_b.coins >= C.WEAPON_PRICE * (weapon.strength ** C.INCREASE_EXPONENT):
							h_b.coins -= C.WEAPON_PRICE * (weapon.strength ** C.INCREASE_EXPONENT)
							weapon.strength += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(FORGE_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
							upgrade_power = False
		elif armor != None:
			amr_stats = REG_FONT.render("EFFECT: " + armor.effect + " POWER: " + str(armor.strength), 1, P.RED)
			WIN.blit(amr_stats, ((P.WIDTH - amr_stats.get_width())//2, P.PADDING))
			upgrade_text = REG_FONT.render("U/UPGRADE PRICE: " + str(C.ARMOR_PRICE * (armor.strength ** C.INCREASE_EXPONENT)),
						       1, P.RED)
			WIN.blit(upgrade_text, ((P.WIDTH - upgrade_text.get_width())//2, P.PADDING * 2))
			coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.RED)
			WIN.blit(coins_text, ((P.WIDTH - coins_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 4))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						upgrade_power = False
					if event.key == pygame.K_u:
						if h_b.coins >= C.ARMOR_PRICE * (armor.strength ** C.INCREASE_EXPONENT):
							h_b.coins -= C.ARMOR_PRICE * (armor.strength ** C.INCREASE_EXPONENT)
							armor.strength += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(FORGE_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
							upgrade_power = False
		elif armor == None and weapon == None:
			upgrade_power = False
							
	while upgrade_stat:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW,
						   (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		pygame.display.update()
		if weapon != None:
			wpn_stats = REG_FONT.render("ATK POWER: " + str(weapon.atk), 1, P.RED)
			WIN.blit(wpn_stats, ((P.WIDTH - wpn_stats.get_width())//2, P.PADDING))
			upgrade_text = REG_FONT.render("U/UPGRADE PRICE: " + str(C.WEAPON_PRICE * (weapon.atk ** C.INCREASE_EXPONENT)),
						       1, P.RED)
			WIN.blit(upgrade_text, ((P.WIDTH - upgrade_text.get_width())//2, P.PADDING * 2))
			coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.RED)
			WIN.blit(coins_text, ((P.WIDTH - coins_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 4))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						upgrade_stat = False
					if event.key == pygame.K_u:
						if h_b.coins >= C.WEAPON_PRICE * (weapon.atk ** C.INCREASE_EXPONENT):
							h_b.coins -= C.WEAPON_PRICE * (weapon.atk ** C.INCREASE_EXPONENT)
							weapon.atk += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(FORGE_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
							upgrade_stat = False
		elif armor != None:
			amr_stats = REG_FONT.render("DEFENSE: " + str(armor.defense), 1, P.RED)
			WIN.blit(amr_stats, ((P.WIDTH - amr_stats.get_width())//2, P.PADDING))
			upgrade_text = REG_FONT.render("U/UPGRADE PRICE: " + str(C.ARMOR_PRICE * (armor.defense ** C.INCREASE_EXPONENT)),
						       1, P.RED)
			WIN.blit(upgrade_text, ((P.WIDTH - upgrade_text.get_width())//2, P.PADDING * 2))
			coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.RED)
			WIN.blit(coins_text, ((P.WIDTH - coins_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 4))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						upgrade_stat = False
					if event.key == pygame.K_u:
						if h_b.coins >= C.ARMOR_PRICE * (armor.defense ** C.INCREASE_EXPONENT):
							h_b.coins -= C.ARMOR_PRICE * (armor.defense ** C.INCREASE_EXPONENT)
							armor.defense += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(FORGE_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
							upgrade_stat = False
		elif armor == None and weapon == None:
			upgrade_stat = False

#function that will train hero stats
def practice_arena(h_p, h_b):
	hero = None
	pick = True
	train = False
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW,
						   (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		ask_text = REG_FONT.render("Who wants to train?", 1, P.WHITE)
		WIN.blit(ask_text, ((P.WIDTH - ask_text.get_width())//2, P.PADDING))
		draw_func.draw_hero_list(h_p)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					hero = h_p[0]
					pick = False
					train = True
				if event.key == pygame.K_2:
					hero = h_p[1]
					pick = False
					train = True
				if event.key == pygame.K_3 and len(h_p) > 2:
					hero = h_p[2]
					pick = False
					train = True
				if event.key == pygame.K_4 and len(h_p) > 3:
					hero = h_p[3]
					pick = False
					train = True
	while train:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW,
						   (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		if hero.level >= C.LEVEL_LIMIT:
			ask_text = REG_FONT.render("What do you want to train?", 1, P.WHITE)
			WIN.blit(ask_text, ((P.WIDTH - ask_text.get_width())//2, P.PADDING))
			stat_text = REG_FONT.render("H/HP: " + str(hero.maxhealth) + " A/ATK: " + str(hero.atkbonus), 1, P.RED)
			WIN.blit(stat_text, ((P.WIDTH - stat_text.get_width())//2, P.PADDING * 2))
			stat_2_text = REG_FONT.render("D/DEFENSE: " + str(hero.defbonus) + " S/SKILL: " + str(hero.skill), 1, P.RED)
			WIN.blit(stat_2_text, ((P.WIDTH - stat_2_text.get_width())//2, P.PADDING * 3))
			stat_3_text = REG_FONT.render("M/MANA: " + str(hero.maxmana) + " COINS: " + str(h_b.coins), 1, P.RED)
			WIN.blit(stat_3_text, ((P.WIDTH - stat_3_text.get_width())//2, P.PADDING * 4))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 5))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						train = False
					if event.key == pygame.K_h:
						if h_b.coins >= (hero.maxhealth ** C.INCREASE_EXPONENT) // C.STAT_PRICE:
							h_b.coins -= round((hero.maxhealth ** C.INCREASE_EXPONENT) // C.STAT_PRICE)
							hero.maxhealth += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
					if event.key == pygame.K_m:
						if h_b.coins >= C.STAT_PRICE * (hero.maxmana ** C.INCREASE_EXPONENT):
							h_b.coins -= C.STAT_PRICE * (hero.maxmana ** C.INCREASE_EXPONENT)
							hero.maxmana += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
					if event.key == pygame.K_s:
						if h_b.coins >= C.STAT_PRICE * (hero.skill ** C.INCREASE_EXPONENT):
							h_b.coins -= C.STAT_PRICE * (hero.skill ** C.INCREASE_EXPONENT)
							hero.skill += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
					if event.key == pygame.K_a:
						if h_b.coins >= C.STAT_PRICE * (hero.atkbonus ** C.INCREASE_EXPONENT):
							h_b.coins -= C.STAT_PRICE * (hero.atkbonus ** C.INCREASE_EXPONENT)
							hero.atkbonus += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
					if event.key == pygame.K_d:
						if h_b.coins >= C.STAT_PRICE * (hero.defbonus ** C.INCREASE_EXPONENT):
							h_b.coins -= C.STAT_PRICE * (hero.defbonus ** C.INCREASE_EXPONENT)
							hero.defbonus += 1
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
		else:
			start_text = REG_FONT.render("You have a lot to work on.", 1, P.RED)
			WIN.blit(start_text, ((P.WIDTH - start_text.get_width())//2, P.PADDING))
			price_text = REG_FONT.render("For someone like you I'll charge " + str(C.LEVEL_PRICE*(hero.level**C.INCREASE_EXPONENT)),
						     1, P.RED)
			WIN.blit(price_text, ((P.WIDTH - price_text.get_width())//2, P.PADDING * 2))
			ask_test = REG_FONT.render("TRAIN: T", 1, P.RED)
			WIN.blit(ask_test, ((P.WIDTH - ask_test.get_width())//2, P.PADDING * 3))
			stat_text = REG_FONT.render("LEVEL: " + str(hero.level) + " COINS: " + h_b.coins, 1, P.RED)
			WIN.blit(stat_text, ((P.WIDTH - stat_text.get_width())//2, P.PADDING * 4))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
			WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 5))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						train = False
					if event.key == pygame.K_t:
						if h_b.coins >= (C.LEVEL_PRICE*(hero.level**C.INCREASE_EXPONENT)):
							h_b.coins -= (C.LEVEL_PRICE*(hero.level**C.INCREASE_EXPONENT))
							lvlup_func.level_up(hero)
						else:
							WIN.fill(P.WHITE)
							WIN.blit(ARENA_IMG, P.ORIGIN)
							poor_text = REG_FONT.render("You can't afford that much training right now. ",
										    1, P.RED)
							WIN.blit(poor_text, ((P.WIDTH - poor_text.get_width())//2, P.PADDING))
							pygame.display.update()
							pygame.time.delay(P.SMALLDELAY)
						
		
#function that will adjust weapon owners
def reorder_equip(h_p, h_e):
	equip = None
	hero = None
	pick = False
	reorder = True
	while reorder:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INNB_IMG = pygame.transform.scale(INNB_RAW,
						  (x, y))
		WIN.blit(INNB_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_e)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					reorder = False
				if event.key == pygame.K_1:
					equip = h_e[0]
					pick = True
				if event.key == pygame.K_2 and len(h_e) > 1:
					equip = h_e[1]
					pick = True
				if event.key == pygame.K_3 and len(h_e) > 2:
					equip = h_e[2]
					pick = True
				if event.key == pygame.K_4 and len(h_e) > 3:
					equip = h_e[3]
					pick = True
				if event.key == pygame.K_5 and len(h_e) > 4:
					equip = h_e[4]
					pick = True
				if event.key == pygame.K_6 and len(h_e) > 5:
					equip = h_e[5]
					pick = True
				if event.key == pygame.K_7 and len(h_e) > 6:
					equip = h_e[6]
					pick = True
				if event.key == pygame.K_8 and len(h_e) > 7:
					equip = h_e[7]
					pick = True
				if event.key == pygame.K_9 and len(h_e) > 8:
					equip = h_e[8]
					pick = True

		while pick:
			WIN.fill(P.WHITE)
			x, y = WIN.get_size()
			INNB_IMG = pygame.transform.scale(INNB_RAW,
							  (x, y))
			WIN.blit(INNB_IMG, P.ORIGIN)
			ask_text = REG_FONT.render("Who do you want to equip it to?", 1, P.WHITE)
			WIN.blit(ask_text, ((P.WIDTH - ask_text.get_width())//2, P.PADDING))
			draw_func.draw_hero_list(h_p)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_l:
						pick = False
						reorder = False
					if event.key == pygame.K_1:
						hero = h_p[0]
						for eqp in h_e:
							if eqp.user == hero.name:
								eqp.user = "None"
						equip.user = hero.name
						pick = False
					if event.key == pygame.K_2:
						hero = h_p[1]
						for eqp in h_e:
							if eqp.user == hero.name:
								eqp.user = "None"
						equip.user = hero.name
						pick = False
					if event.key == pygame.K_3 and len(h_p) > 2:
						hero = h_p[2]
						for eqp in h_e:
							if eqp.user == hero.name:
								eqp.user = "None"
						equip.user = hero.name
						pick = False
					if event.key == pygame.K_4 and len(h_p) > 3:
						hero = h_p[3]
						for eqp in h_e:
							if eqp.user == hero.name:
								eqp.user = "None"
						equip.user = hero.name
						pick = False

#function that removes party members
def remove_party(h_p):
	remove = True
	while remove:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INNB_IMG = pygame.transform.scale(INNB_RAW,
						  (x, y))
		WIN.blit(INNB_IMG, P.ORIGIN)
		draw_func.draw_prremove_menu(h_p)
		pygame.display.update()
		if len(h_p) <= 2:
			remove = False
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					remove = False
				if event.key == pygame.K_1 or event.key == pygame.K_a:
					h_p.pop(0)
				if event.key == pygame.K_2 or event.key == pygame.K_s:
					h_p.pop(1)
				if event.key == pygame.K_3 and len(h_p) > 2:
					h_p.pop(2)
				if event.key == pygame.K_4 and len(h_p) > 3:
					h_p.pop(3)
		
#function that manages adjusting party members
def reorder_party(h_p):
	reorder = True
	while reorder:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INNB_IMG = pygame.transform.scale(INNB_RAW,
						  (x, y))
		WIN.blit(INNB_IMG, P.ORIGIN)
		draw_func.draw_prreorder_menu(h_p)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					reorder = False
				if event.key == pygame.K_1 or event.key == pygame.K_a:
					hero = h_p[0]
					copy_hero = copy.copy(hero)
					h_p.remove(hero)
					h_p.append(copy_hero)
				if event.key == pygame.K_2 or event.key == pygame.K_s:
					hero = h_p[1]
					copy_hero = copy.copy(hero)
					h_p.remove(hero)
					h_p.append(copy_hero)
				if event.key == pygame.K_3 and len(h_p) > 2:
					hero = h_p[2]
					copy_hero = copy.copy(hero)
					h_p.remove(hero)
					h_p.append(copy_hero)
				if event.key == pygame.K_4 and len(h_p) > 3:
					hero = h_p[3]
					copy_hero = copy.copy(hero)
					h_p.remove(hero)
					h_p.append(copy_hero)
		
#function that manages adjusting heroes and armor
def private_room(h_p, h_w, h_a):
	room = True
	while room:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INNB_IMG = pygame.transform.scale(INNB_RAW,
						  (x, y))
		WIN.blit(INNB_IMG, P.ORIGIN)
		draw_func.draw_proom_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					room = False
				if event.key == pygame.K_p:
					reorder_party(h_p)
				if event.key == pygame.K_r:
					remove_party(h_p)
				if event.key == pygame.K_w and len(h_w) > 0:
					reorder_equip(h_p, h_w)
				if event.key == pygame.K_a and len(h_a) > 0:
					reorder_equip(h_p, h_a)
		
#function that controls adding heroes to the party
def recruit(h_p):
	recruit = True
	while recruit:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INN_IMG = pygame.transform.scale(INN_RAW,
						 (x, y))
		WIN.blit(INN_IMG, P.ORIGIN)
		draw_func.draw_recruit_menu(h_p)
		pygame.display.update()
		knght = None
		smner = None
		tact = None
		#check for duplicates
		for hero in h_p:
			if "Knight" in hero.name:
				knght = hero
			if "Summoner" in hero.name:
				smner = hero
			if "Tactician" in hero.name:
				tact = hero
		if len(h_p) >= C.PARTY_LIMIT:
			recruit = False
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					recruit = False
				#should show character and text after successful recruit
				if event.key == pygame.K_s and smner == None:
					new_hero = copy.copy(summoner)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_k and knght == None:
					new_hero = copy.copy(knight)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_t and tact == None:
					new_hero = copy.copy(tactician)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_w:
					new_hero = copy.copy(warrior)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_c:
					new_hero = copy.copy(cleric)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_m:
					new_hero = copy.copy(mage)
					party_func.add_to_party(h_p, new_hero)
				if event.key == pygame.K_n:
					new_hero = copy.copy(ninja)
					party_func.add_to_party(h_p, new_hero)
				
#function that controls the inn of the city
def inn(h_p, h_b, h_w, h_a):
	inn = True
	while inn:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		INN_IMG = pygame.transform.scale(INN_RAW,
						 (x, y))
		WIN.blit(INN_IMG, P.ORIGIN)
		draw_func.draw_inn_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					for hero in h_p:
						hero.health = hero.maxhealth
						hero.mana = hero.maxmana
					h_b.coins -= min(len(h_p), h_b.coins)
					inn = False
				if event.key == pygame.K_l:
					inn = False
				if event.key == pygame.K_p:
					private_room(h_p, h_w, h_a)
				if event.key == pygame.K_r and len(h_p) < C.PARTY_LIMIT:
					recruit(h_p)
		
	
#function that will make the city
def city(h_p, h_b, h_w, h_a):
	city = True
	while city:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		CITY_IMG = pygame.transform.scale(CITY_RAW,
						  (x, y))
		WIN.blit(CITY_IMG, P.ORIGIN)
		draw_func.draw_city_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				city = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_i:
					inn(h_p, h_b, h_w, h_a)
				if event.key == pygame.K_l:
					city = False
				if event.key == pygame.K_f:
					forge(h_b, h_w, h_a)
				if event.key == pygame.K_p:
					practice_arena(h_p, h_b)
