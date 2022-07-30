import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../pygame_functions/pygame_general_functions/")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_hunter_function as hunt_func
import rpg2_level_up_function as lvlup_func
import draw_functions as draw_func
import pypick_function as pick_func
from rpg2_constants import Constants
from rpg2_constant_quests import Q_Constants
from rpg2_constant_lists import List_Constants
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
#images
GUILD_RAW = pygame.image.load(os.path.join("Assets", "guild2.png"))
GUILD_IMG = pygame.transform.scale(GUILD_RAW, (P.WIDTH, P.HEIGHT))
ENCHANT_RAW = pygame.image.load(os.path.join("Assets", "enchanter_garden.png"))
ENCHANT_IMG = pygame.transform.scale(ENCHANT_RAW, (P.WIDTH, P.HEIGHT))
TINKERER_RAW = pygame.image.load(os.path.join("Assets", "tinkerer.png"))
TINKERER_IMG = pygame.transform.scale(TINKERER_RAW, (P.WIDTH, P.HEIGHT))
FORGE_RAW = pygame.image.load(os.path.join("Assets", "forge2.png"))
FORGE_IMG = pygame.transform.scale(FORGE_RAW, (P.WIDTH, P.HEIGHT))
HALL_RAW = pygame.image.load(os.path.join("Assets", "hall.png"))
HALL_IMG = pygame.transform.scale(HALL_RAW, (P.WIDTH, P.HEIGHT))
#grandmaster function
def grandmaster(h_p, qi_npc, a_npc):
	choice = True
	hero = None
	price = 0
	train = False
	while choice:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		HALL_IMG = pygame.transform.scale(HALL_RAW, (x, y))
		WIN.blit(HALL_IMG, P.ORIGIN)
		draw_func.draw_grandmaster_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					choice = False
				elif event.key == pygame.K_r:
					for p in h_p:
						p.health = p.maxhealth
						p.mana = p.maxmana
				elif event.key == pygame.K_t:
					choice = False
					train = True
					hero = pick_func.pick_hero(h_p)
					if hero.level >= C.LEVEL_LIMIT * C.INCREASE_EXPONENT:
						x, y = WIN.get_size()
						HALL_IMG = pygame.transform.scale(HALL_RAW, (x, y))
						WIN.blit(HALL_IMG, P.ORIGIN)
						fail_text = REG_FONT.render("Sorry, I can't train you anymore. ", 1, P.WHITE)
						WIN.blit(fail_text, ((x - fail_text.get_width())//2, P.PADDING * 1))
						pygame.display.update()
						pygame.time.delay(1000)
						train = False
					elif hero.level == C.LEVEL_LIMIT:
						price += C.PRESTIGE_PRICE
					elif hero.level > C.LEVEL_LIMIT:
						price += hero.level ** C.INCREASE_EXPONENT
	while train:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		HALL_IMG = pygame.transform.scale(HALL_RAW, (x, y))
		WIN.blit(HALL_IMG, P.ORIGIN)
		draw_func.draw_prestige_price(hero, price)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				x, y = WIN.get_size()
				HALL_IMG = pygame.transform.scale(HALL_RAW, (x, y))
				WIN.blit(HALL_IMG, P.ORIGIN)
				if event.key == pygame.K_l:
					train = False
				elif event.key == pygame.K_n:
					train = False
					grandmaster(h_p, qi_npc, a_npc)
				elif event.key == pygame.K_y:
					train = False
					if qi_npc.managem >= price:
						qi_npc.managem -= price
						if hero.level == C.LEVEL_LIMIT:
							lvl_func.prestige_class(hero)
							lvl_func.prestige_level_up(hero)
						elif hero.level > C.LEVEL_LIMIT:
							lvl_func.prestige_level_up(hero)
						fail_text = REG_FONT.render("Can you feel the energy empowering you? ", 1, P.WHITE)
						WIN.blit(fail_text, ((x - fail_text.get_width())//2, P.PADDING * 1))
						pygame.display.update()
						pygame.time.delay(1000)
					else:
						fail_text = REG_FONT.render("You'll need more mana gems for the process to work. ", 1, P.WHITE)
						WIN.blit(fail_text, ((x - fail_text.get_width())//2, P.PADDING * 1))
						pygame.display.update()
						pygame.time.delay(1000)
					
#enchanter function
def enchanter(h_ally, h_wpn, h_amr, qi_npc, a_npc):
	choice = True
	weapon = None
	armor = None
	enchant = False
	price = C.ENCHANT_PRICE
	while choice:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		ENCHANT_IMG = pygame.transform.scale(ENCHANT_RAW, (x, y))
		WIN.blit(ENCHANT_IMG, P.ORIGIN)
		draw_func.draw_henchanter_menu()
		pygame.display.update()
		if qi_npc.managem < price:
			choice = False
			x, y = WIN.get_size()
			ENCHANT_IMG = pygame.transform.scale(ENCHANT_RAW, (x, y))
			WIN.blit(ENCHANT_IMG, P.ORIGIN)
			fail_text = REG_FONT.render("You don't have enough mana crystals. ", 1, P.RED)
			WIN.blit(fail_text, ((x - fail_text.get_width())//2, P.PADDING * 5))
			pygame.display.update()
			pygame.time.delay(2000)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					choice = False
				elif event.key == pygame.K_a:
					choice = False
					armor = pick_func.pick_hero(h_amr)
					enchant = True
				elif event.key == pygame.K_w:
					choice = False
					weapon = pick_func.pick_hero(h_wpn)
					enchant = True
	while enchant:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		ENCHANT_IMG = pygame.transform.scale(ENCHANT_RAW, (x, y))
		WIN.blit(ENCHANT_IMG, P.ORIGIN)
		if armor != None:
			draw_func.hunter_armor_enchant(qi_npc, a_npc)
			pygame.display.update()
		elif weapon != None:
			draw_func.hunter_weapon_enchant(qi_npc, a_npc)
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					enchant = False
				elif event.key == pygame.K_d and weapon != None:
					weapon.effect = "Death"
					weapon.name = "Death's Call"
					qi_npc.managem -= C.ENCHANT_PRICE
					enchant = False
				elif event.key == pygame.K_n and weapon != None:
					weapon.effect = "Necromancer"
					weapon.name = "Necromantic Blade"
					qi_npc.managem -= C.ENCHANT_PRICE
					enchant = False
				elif event.key == pygame.K_r and armor != None:
					armor.effect = "Revive"
					armor.name = "Phoenix Armor"
					qi_npc.managem -= C.ENCHANT_PRICE
					enchant = False
				elif event.key == pygame.K_b and armor != None:
					armor.effect = "Bomb"
					armor.name = "Explosive Armor"
					qi_npc.managem -= C.ENCHANT_PRICE
					enchant = False
				elif event.key == pygame.K_e:
					if weapon != None:
						weapon.effect = "Explode"
						weapon.name = "Explosive Blade"
						qi_npc.managem -= C.ENCHANT_PRICE
					elif armor != None:
						armor.effect = "Ethereal"
						armor.name = "Ghostly Armor"
						qi_npc.managem -= C.ENCHANT_PRICE
					enchant = False
		
		
#tinkerer function
def tinkerer(h_wpn, h_amr, qi_npc, a_npc):
	choice = True
	upgrade = False
	combine = False
	weapon = None
	armor = None
	weapon2 = None
	armor2 = None
	price = 0
	while choice:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		TINKERER_IMG = pygame.transform.scale(TINKERER_RAW, (x, y))
		WIN.blit(TINKERER_IMG, P.ORIGIN)
		draw_func.draw_tinkerer_menu(qi_npc, a_npc)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					choice = False
				elif event.key == pygame.K_a:
					choice = False
					armor = pick_func.pick_hero(h_amr)
					price += C.ARMOR_PRICE * (armor.upgrade ** C.INCREASE_EXPONENT)
					upgrade = True
				elif event.key == pygame.K_w:
					choice = False
					weapon = pick_func.pick_hero(h_wpn)
					price += C.ARMOR_PRICE * (armor.upgrade ** C.INCREASE_EXPONENT)
					upgrade = True
				elif event.key == pygame.K_c and qi_npc.managem >= C.ENCHANT_PRICE:
					choice = False
					armor = pick_func.pick_hero(h_amr)
					armor2 = pick_func.pick_hero(h_amr)
					price += C.ENCHANT_PRICE
					combine = True
				elif event.key == pygame.K_f and qi_npc.managem >= C.ENCHANT_PRICE:
					choice = False
					weapon = pick_func.pick_hero(h_wpn)
					weapon2 = pick_func.pick_hero(h_wpn)
					price += C.ENCHANT_PRICE
					combine = True
	while upgrade:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		TINKERER_IMG = pygame.transform.scale(TINKERER_RAW, (x, y))
		WIN.blit(TINKERER_IMG, P.ORIGIN)
		if armor != None:
			draw_func.draw_equip_price(armor, price)
			pygame.display.update()
		elif weapon != None:
			draw_func.draw_equip_price(weapon, price)
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					upgrade = False
				elif event.key == pygame.K_y:
					upgrade = False
					if qi_npc.managem >= price:
						qi_npc.managem -= price
						if armor != None:
							armor.upgrade += 1
						elif weapon != None:
							weapon.upgrade += 1
						tinkerer(h_wpn, h_amr, qi_npc, a_npc)
					else:
						x, y = WIN.get_size()
						TINKERER_IMG = pygame.transform.scale(TINKERER_RAW, (x, y))
						WIN.blit(TINKERER_IMG, P.ORIGIN)
						draw_func.poor_text()
				elif event.key == pygame.K_n:
					upgrade = False
					tinkerer(h_wpn, h_amr, qi_npc, a_npc)
	while combine:
		pygame.event.clear()
		clock.tick(P.FPS)
		width, height = WIN.get_size()
		TINKERER_IMG = pygame.transform.scale(TINKERER_RAW, (width, height))
		WIN.blit(TINKERER_IMG, P.ORIGIN)
		if armor != None:
			if armor.effect == armor2.effect:
				fail_text = REG_FONT.render("Those are the same thing. ", 1, P.WHITE)
				WIN.blit(fail_text, ((width - fail_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
			elif " " in armor.effect or " " in armor2.effect:
				fail_text = REG_FONT.render("I can't combine those together. ", 1, P.WHITE)
				WIN.blit(fail_text, ((width - fail_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
			else:
				new_effect = armor.effect + " " + armor2.effect
				new_strength = max(armor.strength, armor2.strength)
				new_defense = max(armor.defense, armor2.defense)
				new_upgrade = max(armor.upgrade, armor2.upgrade)
				new_user = "None"
				new_name = "Chimera Armor: "+new_effect
				new_element = "None"
				new_armor = Armor_PC(new_name, new_user, new_effect,
						     new_strength, new_element, new_defense,
						     new_upgrade)
				new_amr = copy.copy(new_armor)
				h_amr.remove(armor)
				h_amr.remove(armor2)
				h_amr.append(new_amr)
				qi_npc.managem -= C.ENCHANT_PRICE
				success_text = REG_FONT.render("I think it worked!" , 1, P.WHITE)
				WIN.blit(success_text, ((width - success_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
		elif weapon != None:
			if weapon.effect == weapon2.effect:
				fail_text = REG_FONT.render("Those are the same thing. ", 1, P.WHITE)
				WIN.blit(fail_text, ((width - fail_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
			elif " " in weapon.effect or " " in weapon2.effect:
				fail_text = REG_FONT.render("I can't combine those together. ", 1, P.WHITE)
				WIN.blit(fail_text, ((width - fail_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
			else:
				new_effect = weapon.effect + " " + weapon2.effect
				new_strength = max(weapon.strength, weapon2.strength)
				new_atk = max(weapon.atk, weapon2.atk)
				new_upgrade = max(weapon.upgrade, weapon2.upgrade)
				new_user = "None"
				new_name = "Chimera Weapon: "+new_effect
				new_element = "None"
				new_weapon = Weapon_PC(new_name, new_user, new_effect,
						       new_strength, new_element, new_atk,
						       new_upgrade)
				new_wpn = copy.copy(new_weapon)
				h_wpn.remove(weapon)
				h_wpn.remove(weapon2)
				h_wpn.append(new_wpn)
				qi_npc.managem -= C.ENCHANT_PRICE
				success_text = REG_FONT.render("I think it worked!" , 1, P.WHITE)
				WIN.blit(success_text, ((width - success_text.get_width())//2, P.PADDING * 1))
				pygame.display.update()
				pygame.time.delay(1000)
		combine = False
				
				
#armorer function
def armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc):
	choice = True
	sell = False
	buy = False
	weapon = None
	armor = None
	equip = None
	price = 0
	while choice:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		draw_func.draw_armorer_menu(h_bag, qi_npc, a_npc)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					choice = False
				elif event.key == pygame.K_a:
					armor = pick_func.pick_hero(h_amr)
					price += (armor.strength ** C.INCREASE_EXPONENT) * C.ARMOR_PRICE
					price += (armor.defense ** C.INCREASE_EXPONENT) * C.ARMOR_PRICE
					choice = False
					sell = True
				elif event.key == pygame.K_w:
					weapon = pick_func.pick_hero(h_wpn)
					price += (weapon.strength ** C.INCREASE_EXPONENT) * C.WEAPON_PRICE
					price += (weapon.atk ** C.INCREASE_EXPONENT) * C.WEAPON_PRICE
					choice = False
					sell = True
				elif event.key == pygame.K_b and a_npc.rank > 10:
					choice = False
					buy = True
	while sell:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		pygame.display.update()
		#depending on what you're selling you get a different price
		if armor != None:
			draw_func.draw_equip_price(armor, price)
			pygame.display.update()
		elif weapon != None:
			draw_func.draw_equip_price(weapon, price)
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					sell = False
					armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc)
				if event.key == pygame.K_y:
					sell = False
					h_bag.coins += price
					if armor != None:
						h_amr.remove(armor)
						armor = None
					elif weapon != None:
						h_wpn.remove(weapon)
						weapon = None
					armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc)
				elif event.key == pygame.K_n:
					sell = False
					armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc)
	while buy:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
		WIN.blit(FORGE_IMG, P.ORIGIN)
		draw_func.draw_unique_equip(h_wpn, qi_npc)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					buy = False
					armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc)
				elif event.key == pygame.K_o:
					if qi_npc.managem >= C.ENCHANT_PRICE:
						wpn = Weapon_PC("Observer", "None", "None", 1, "None", 1)
						copy_wpn = copy.copy(wpn)
						h_wpn.append(copy_wpn)
						qi_npc.managem -= C.ENCHANT_PRICE
					else:
						buy = False
						x, y = WIN.get_size()
						FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
						WIN.blit(FORGE_IMG, P.ORIGIN)
						draw_func.poor_text()
				elif event.key == pygame.K_n:
					if qi_npc.managem >= C.ENCHANT_PRICE:
						wpn = Weapon_PC("Dagger", "None", "Hidden Dagger", 1, "None", 1)
						copy_wpn = copy.copy(wpn)
						h_wpn.append(copy_wpn)
						qi_npc.managem -= C.ENCHANT_PRICE
					else:
						buy = False
						x, y = WIN.get_size()
						FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
						WIN.blit(FORGE_IMG, P.ORIGIN)
						draw_func.poor_text()
				elif event.key == pygame.K_s:
					if qi_npc.managem >= C.ENCHANT_PRICE:
						wpn = Weapon_PC("Summon Staff", "None", "Summon", 1, "None", 1)
						copy_wpn = copy.copy(wpn)
						h_wpn.append(copy_wpn)
						qi_npc.managem -= C.ENCHANT_PRICE
					else:
						buy = False
						x, y = WIN.get_size()
						FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
						WIN.blit(FORGE_IMG, P.ORIGIN)
						draw_func.poor_text()
				elif event.key == pygame.K_c:
					if qi_npc.managem >= C.ENCHANT_PRICE:
						wpn = Weapon_PC("Heal Staff", "None", "Heal", 1, "None", 1)
						copy_wpn = copy.copy(wpn)
						h_wpn.append(copy_wpn)
						qi_npc.managem -= C.ENCHANT_PRICE
					else:
						buy = False
						x, y = WIN.get_size()
						FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
						WIN.blit(FORGE_IMG, P.ORIGIN)
						draw_func.poor_text()
				elif event.key == pygame.K_c:
					if qi_npc.managem >= C.ENCHANT_PRICE:
						wpn = Weapon_PC("Shield", "None", "Shield", 1, "None", 1)
						copy_wpn = copy.copy(wpn)
						h_wpn.append(copy_wpn)
						qi_npc.managem -= C.ENCHANT_PRICE
					else:
						buy = False
						x, y = WIN.get_size()
						FORGE_IMG = pygame.transform.scale(FORGE_RAW, (x, y))
						WIN.blit(FORGE_IMG, P.ORIGIN)
						draw_func.poor_text()
#function which controls the monsters hunter guild
def monster_hunter_guild(h_p, h_bag, h_ally, h_wpn, h_amr, qi_npc, a_npc):
	guild = True
	while guild:
		pygame.event.clear()
		clock.tick(P.FPS)
		x, y = WIN.get_size()
		GUILD_IMG = pygame.transform.scale(GUILD_RAW, (x, y))
		WIN.blit(GUILD_IMG, P.ORIGIN)
		draw_func.draw_guild_menu(qi_npc, a_npc)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				guild = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					guild = False
				elif event.key == pygame.K_q and qi_npc.package < a_npc.rank:
					qi_npc.package += max(a_npc.rank - qi_npc.package, 0)
				elif event.key == pygame.K_r and qi_npc.rpackage > 0:
					qi_npc.managem += qi_npc.rpackage * round(a_npc.rank ** 0.5)
					qi_npc.rpackage = 0
					x, y = WIN.get_size()
					GUILD_IMG = pygame.transform.scale(TOWER_RAW, (x, y))
					WIN.blit(GUILD_IMG, P.ORIGIN)
					thank_text = REG_FONT.render("Thank you for your hard work!", 1, P.BLACK)
					WIN.blit(thank_text, ((x - thank_text.get_width())//2, P.PADDING * 2))
					pygame.display.update()
					pygame.time.delay(1000)
				elif event.key == pygame.K_a:
					armorer(h_bag, h_wpn, h_amr, qi_npc, a_npc)
				elif event.key == pygame.K_t:
					tinkerer(h_wpn, h_amr, qi_npc, a_npc)
				elif event.key == pygame.K_e:
					enchanter(h_ally, h_wpn, h_amr, qi_npc, a_npc)
				elif event.key == pygame.K_g:
					grandmaster(h_p, qi_npc, a_npc)
