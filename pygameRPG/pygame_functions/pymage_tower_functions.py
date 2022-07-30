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
x, y = WIN.get_size()
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
ENCHANTER_RAW = pygame.image.load(os.path.join("Assets", "enchanter_forest.png"))
ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (P.WIDTH, P.HEIGHT))
BOOKSTORE_RAW = pygame.image.load(os.path.join("Assets", "bookstore.png"))
BOOKSTORE_IMG = pygame.transform.scale(BOOKSTORE_RAW, (P.WIDTH, P.HEIGHT))
#things inside the mage tower
new_summon = Pet_NPC("Angel", 1, 2)
new_spell = Spell_PC("new", 1, 1, None, 1)
#bookstore
def sell_spells(h_m, h_b):
	pick = True
	spell = None
	sell = False
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		BOOKSTORE_IMG = pygame.transform.scale(BOOKSTORE_RAW, (x, y))
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		draw_func.draw_spell_list(h_m)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					spell = h_m[0]
					pick = False
					sell = True
				if event.key == pygame.K_2 and len(h_m) > 1:
					spell = h_m[1]
					pick = False
					sell = True
				if event.key == pygame.K_3 and len(h_m) > 2:
					spell = h_m[2]
					pick = False
					sell = True
				if event.key == pygame.K_4 and len(h_m) > 3:
					spell = h_m[3]
					pick = False
					sell = True
				if event.key == pygame.K_5 and len(h_m) > 4:
					spell = h_m[4]
					pick = False
					sell = True
				if event.key == pygame.K_6 and len(h_m) > 5:
					spell = h_m[5]
					pick = False
					sell = True
				if event.key == pygame.K_7 and len(h_m) > 6:
					spell = h_m[6]
					pick = False
					sell = True
				if event.key == pygame.K_8 and len(h_m) > 7:
					spell = h_m[7]
					pick = False
					sell = True
				if event.key == pygame.K_9 and len(h_m) > 8:
					spell = h_m[8]
					pick = False
					sell = True
	while sell:
		spell_price = spell.power ** C.INCREASE_EXPONENT
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		draw_func.draw_sell_spell_menu(spell, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					sell = False
				if event.key == pygame.K_y:
					h_b.coins += spell_price
					h_m.remove(spell)
					if len(h_m) > 0:
						sell_spells(h_m, h_b)
					else:
						sell = False
				if event.key == pygame.K_n:
					sell_spells(h_m, h_b)
		
def edit_spells(h_m):
	pick = True
	edit = False
	spell = None
	user_text = ""
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		BOOKSTORE_IMG = pygame.transform.scale(BOOKSTORE_RAW, (x, y))
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		draw_func.draw_spell_list(h_m)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					spell = h_m[0]
					pick = False
					edit = True
				if event.key == pygame.K_2 and len(h_m) > 1:
					spell = h_m[1]
					pick = False
					edit = True
				if event.key == pygame.K_3 and len(h_m) > 2:
					spell = h_m[2]
					pick = False
					edit = True
				if event.key == pygame.K_4 and len(h_m) > 3:
					spell = h_m[3]
					pick = False
					edit = True
				if event.key == pygame.K_5 and len(h_m) > 4:
					spell = h_m[4]
					pick = False
					edit = True
				if event.key == pygame.K_6 and len(h_m) > 5:
					spell = h_m[5]
					pick = False
					edit = True
				if event.key == pygame.K_7 and len(h_m) > 6:
					spell = h_m[6]
					pick = False
					edit = True
				if event.key == pygame.K_8 and len(h_m) > 7:
					spell = h_m[7]
					pick = False
					edit = True
				if event.key == pygame.K_9 and len(h_m) > 8:
					spell = h_m[8]
					pick = False
					edit = True
	while edit:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		name_text = REG_FONT.render("NAME: " + spell.name, 1, P.WHITE)
		WIN.blit(name_text, ((P.WIDTH - name_text.get_width())//2, P.PADDING * 1))
		rename_text = REG_FONT.render("NEW NAME: " + str(user_text), 1, P.WHITE)
		WIN.blit(rename_text, ((P.WIDTH - rename_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					spell.name = str(user_text)
					edit = False
					edit_spells(h_m)
				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				else:
					user_text += event.unicode

		
def bookstore(h_b, h_m):
	store = True
	buy = False
	while store:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		BOOKSTORE_IMG = pygame.transform.scale(BOOKSTORE_RAW, (x, y))
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		draw_func.draw_bookstore_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					store = False
				if event.key == pygame.K_b:
					buy = True
					store = False
				if event.key == pygame.K_e and len(h_m) > 0:
					store = False
					edit_spells(h_m)
				if event.key == pygame.K_s and len(h_m) > 0:
					store = False
					sell_spells(h_m, h_b)
	while buy:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
		draw_func.draw_buy_spell_menu(h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					buy = False
				if event.key == pygame.K_a and h_b.coins >= C.ENCHANT_PRICE:
					h_b.coins -= C.ENCHANT_PRICE
					copy_spell = copy.copy(new_spell)
					copy_spell.element = "Air"
					h_m.append(copy_spell)
				if event.key == pygame.K_e and h_b.coins >= C.ENCHANT_PRICE:
					h_b.coins -= C.ENCHANT_PRICE
					copy_spell = copy.copy(new_spell)
					copy_spell.element = "Earth"
					h_m.append(copy_spell)
				if event.key == pygame.K_f and h_b.coins >= C.ENCHANT_PRICE:
					h_b.coins -= C.ENCHANT_PRICE
					copy_spell = copy.copy(new_spell)
					copy_spell.element = "Fire"
					h_m.append(copy_spell)
				if event.key == pygame.K_w and h_b.coins >= C.ENCHANT_PRICE:
					h_b.coins -= C.ENCHANT_PRICE
					copy_spell = copy.copy(new_spell)
					copy_spell.element = "Water"
					h_m.append(copy_spell)
				if event.key == pygame.K_d:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
						copy_spell = copy.copy(new_spell)
						copy_spell.element = "Dark"
						h_m.append(copy_spell)
					else:
						WIN.fill(P.WHITE)
						WIN.blit(BOOKSTORE_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						buy = False

#enchanter
def weapon_effect_enchant(wpn, h_b):
	enchant = True
	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_weapon_enchant_menu(wpn, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_a and h_b.coins >= C.ENCHANT_PRICE:
					wpn.effect = "Attack"
					h_b.coins -= C.ENCHANT_PRICE
					wpn.name = "Weapon"      
				if event.key == pygame.K_i and h_b.coins >= C.ENCHANT_PRICE:
					wpn.effect = "Lifesteal"
					h_b.coins -= C.ENCHANT_PRICE
					if wpn.name == "Weapon":
						wpn.name == "Lifesteal Weapon"
				if event.key == pygame.K_p:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						wpn.effect = "Poison"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
						if wpn.name == "Weapon":
							wpn.name == "Poison Weapon"
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
				if event.key == pygame.K_m:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						wpn.effect = "ManaDrain"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
						if wpn.name == "Weapon":
							wpn.name == "ManaDrain Weapon"
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
				if event.key == pygame.K_s:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						wpn.effect = "SkillDrain"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
						if wpn.name == "Weapon":
							wpn.name == "SkillDrain Weapon"
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
def armor_effect_enchant(amr, h_b):
	enchant = True
	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_armor_enchant_menu(amr, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_a and h_b.coins >= C.ENCHANT_PRICE:
					amr.effect = "Absorb"
					h_b.coins -= C.ENCHANT_PRICE
					if amr.name == "Armor":
						amr.name = "Absorb Armor"
				if event.key == pygame.K_b and h_b.coins >= C.ENCHANT_PRICE:
					amr.effect = "Block"
					h_b.coins -= C.ENCHANT_PRICE
					amr.name = "Armor"
				if event.key == pygame.K_p:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						amr.effect = "Poison"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
						if amr.name == "Armor":
							amr.name = "Poison Armor"
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
def element_enchant(eqp, h_b):
	enchant = True
	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_element_enchant(eqp, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_f and h_b.coins >= C.ENCHANT_PRICE:
					eqp.element = "Fire"
					h_b.coins -= C.ENCHANT_PRICE
				if event.key == pygame.K_a and h_b.coins >= C.ENCHANT_PRICE:
					eqp.element = "Air"
					h_b.coins -= C.ENCHANT_PRICE
				if event.key == pygame.K_e and h_b.coins >= C.ENCHANT_PRICE:
					eqp.element = "Earth"
					h_b.coins -= C.ENCHANT_PRICE
				if event.key == pygame.K_w and h_b.coins >= C.ENCHANT_PRICE:
					eqp.element = "Water"
					h_b.coins -= C.ENCHANT_PRICE
				if event.key == pygame.K_d:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						eqp.element = "Dark"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
				if event.key == pygame.K_i:
					if h_b.coins >= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT:
						eqp.element = "Light"
						h_b.coins -= C.ENCHANT_PRICE ** C.INCREASE_EXPONENT
					else:
						WIN.fill(P.WHITE)
						WIN.blit(ENCHANTER_IMG, P.ORIGIN)
						draw_func.poor_text_3()
						enchant = False
def armor_enchanter(h_e, h_b):
	pick = True
	equip = None
	enchant = False
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_e)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					equip = h_e[0]
					pick = False
					enchant = True
				if event.key == pygame.K_2 and len(h_e) > 1:
					equip = h_e[1]
					pick = False
					enchant = True
				if event.key == pygame.K_3 and len(h_e) > 2:
					equip = h_e[2]
					pick = False
					enchant = True
				if event.key == pygame.K_4 and len(h_e) > 3:
					equip = h_e[3]
					pick = False
					enchant = True
				if event.key == pygame.K_5 and len(h_e) > 4:
					equip = h_e[4]
					pick = False
					enchant = True
				if event.key == pygame.K_6 and len(h_e) > 5:
					equip = h_e[5]
					pick = False
					enchant = True
				if event.key == pygame.K_7 and len(h_e) > 6:
					equip = h_e[6]
					pick = False
					enchant = True
				if event.key == pygame.K_8 and len(h_e) > 7:
					equip = h_e[7]
					pick = False
					enchant = True
				if event.key == pygame.K_9 and len(h_e) > 8:
					equip = h_e[8]
					pick = False
					enchant = True
	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_equip_enchant_menu(equip, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_e:
					enchant = False
					element_enchant(equip, h_b)
				if event.key == pygame.K_f:
					enchant = False
					armor_effect_enchant(equip, h_b)
		
	
def weapon_enchanter(h_e, h_b):
	pick = True
	equip = None
	enchant = False
	while pick:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_reorder_eqp_menu(h_e)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					pick = False
				if event.key == pygame.K_1:
					equip = h_e[0]
					pick = False
					enchant = True
				if event.key == pygame.K_2 and len(h_e) > 1:
					equip = h_e[1]
					pick = False
					enchant = True
				if event.key == pygame.K_3 and len(h_e) > 2:
					equip = h_e[2]
					pick = False
					enchant = True
				if event.key == pygame.K_4 and len(h_e) > 3:
					equip = h_e[3]
					pick = False
					enchant = True
				if event.key == pygame.K_5 and len(h_e) > 4:
					equip = h_e[4]
					pick = False
					enchant = True
				if event.key == pygame.K_6 and len(h_e) > 5:
					equip = h_e[5]
					pick = False
					enchant = True
				if event.key == pygame.K_7 and len(h_e) > 6:
					equip = h_e[6]
					pick = False
					enchant = True
				if event.key == pygame.K_8 and len(h_e) > 7:
					equip = h_e[7]
					pick = False
					enchant = True
				if event.key == pygame.K_9 and len(h_e) > 8:
					equip = h_e[8]
					pick = False
					enchant = True

	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_equip_enchant_menu(equip, h_b)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					enchant = False
				if event.key == pygame.K_e:
					enchant = False
					element_enchant(equip, h_b)
				if event.key == pygame.K_f:
					enchant = False
					weapon_effect_enchant(equip, h_b)
		
	
def enchanter(h_b, h_w, h_a):
	enchant = True
	while enchant:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ENCHANTER_IMG = pygame.transform.scale(ENCHANTER_RAW, (x, y))
		WIN.blit(ENCHANTER_IMG, P.ORIGIN)
		draw_func.draw_enchanter_menu()
		pygame.display.update()
		if len(h_w) <= 0 and len(h_a) <= 0:
			WIN.fill(P.WHITE)
			WIN.blit(ENCHANTER_IMG, P.ORIGIN)
			error_text = REG_FONT.render("You have nothing to enchant. ", 1, P.RED)
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
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
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
					spell = h_m[6]
					pick = False
					train = True
				if event.key == pygame.K_8 and len(h_m) > 7:
					spell = h_m[7]
					pick = False
					train = True
				if event.key == pygame.K_9 and len(h_m) > 8:
					spell = h_m[8]
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
		x, y = WIN.get_size()
		PORTAL_IMG = pygame.transform.scale(PORTAL_RAW, (x, y))
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
		x, y = WIN.get_size()
		TOWER_IMG = pygame.transform.scale(TOWER_RAW, (x, y))
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
						
