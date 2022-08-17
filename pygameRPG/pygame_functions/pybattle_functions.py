import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("./pybattle_functions/pybattle_hero_attack.py")
sys.path.append("./pygame_general_functions")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_constants import Constants
C = Constants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import pyparty_functions as party_func
import pymonster_function as monster_func
import pybattle_pet_action as pet_func
import pyelement_function as element_func
import pymoneffect_function as me_func
import pybattle_hero_skill as hskl_func
import pypick_function as pick_func
import draw_functions as draw_func
import draw_effects as drawe_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#also need any specific images
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
#function that gives gold and exp after battle
def drop_step(h_p, m_p, h_bag):
	coin = 0
	#get gold
	for mon in m_p:
		fcoin = random.randint(h_bag.flow//2, h_bag.flow)
		h_bag.coins += (mon.dropchance + fcoin) * 2
		coin += (mon.dropchance + fcoin) * 2
	x, y = WIN.get_size()
	FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
	WIN.blit(FOREST_IMG, P.ORIGIN)
	coins_text = REG_FONT.render("You find "+str(coin)+" coins worth of harvestable material.", 1, P.WHITE)
	WIN.blit(coins_text, ((x - coins_text.get_width())//2, P.PADDING))
	pygame.display.update()
	pygame.time.delay(500)

	#get exp
	for hero in h_p:
		for mon in m_p:
			x = random.randint(0, hero.exp)
			if x <= mon.dropchance:
				hero.exp += 1
	for hero in h_p:
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		x = party_func.check_exp(hero)
		if x == 1:
			drawe_func.hero_level_up(hero)
	m_p.clear()
	h_bag.flow += 1

#function that controls using an item in battle
def use_item(hero, h_b, h_p, h_ally, m_p):
	use = True
	while use:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		draw_func.draw_item_menu(h_b)
		draw_func.draw_hero_stats(hero)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_h:
					use = False
					if h_b.heal >= hero.level:
						h_b.heal -= hero.level
						hero.health += hero.maxhealth//2
						hero.health = min(hero.health, hero.maxhealth)
					break
				if event.key == pygame.K_m:
					use = False
					if h_b.mana >= hero.level:
						h_b.mana -= hero.level
						hero.mana += hero.maxmana//2
					break
				if event.key == pygame.K_b:
					use = False
					if h_b.buff >= hero.level:
						h_b.buff -= hero.level
						hero.atk = round(hero.atk * C.BUFF)
					break
					
						
#function that controls the turns in battle
def hero_turn(hero, h_p, m_p, h_ally, h_bag,
	      h_magic, h_wpn, h_amr):
	x, y = WIN.get_size()
	FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
	WIN.blit(FOREST_IMG, P.ORIGIN)
	draw_func.draw_heroes(h_p, h_ally)
	draw_func.draw_monsters(m_p)
	draw_func.draw_battle_menu(hero)
	draw_func.draw_hero_stats(hero)
	pygame.display.update()
	turn = True
	while turn:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		if "Totem" in hero.name:
			pet_func.totem_turn(hero, h_p, m_p, h_ally)
			turn = False
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_a and len(m_p) == 1:
					pygame.event.clear()
					turn = False
					mon = m_p[0]
					hskl_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
					WIN.blit(FOREST_IMG, P.ORIGIN)
					weapon = party_func.check_equipment(hero, h_wpn)
					drawe_func.hero_attack(hero, weapon, mon)
					pygame.display.update()
					break
				if event.key == pygame.K_a and len(m_p) > 1:
					pygame.event.clear()
					turn = False
					mon = pick_func.pick_hero(m_p)
					pygame.event.clear()
					hskl_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
					WIN.blit(FOREST_IMG, P.ORIGIN)
					weapon = party_func.check_equipment(hero, h_wpn)
					drawe_func.hero_attack(hero, weapon, mon)
					pygame.display.update()
					break
				if event.key == pygame.K_s:
					turn = False
					WIN.blit(FOREST_IMG, P.ORIGIN)
					pygame.display.update()
					hskl_func.hero_skill(hero, h_p, m_p, h_ally, h_wpn, h_amr, h_bag, h_magic)
					break
				if event.key == pygame.K_m and len(h_magic) > 0:
					if hero.mana > 0:
						turn = False
						spell = pick_func.pick_hero(h_magic)
						hskl_func.magical_attack(spell, hero, m_p)
						pygame.display.update()
						break
				if event.key == pygame.K_i:
					turn = False
					use_item(hero, h_bag, h_p, h_ally, m_p)
					break


#function that will control the battle
def battle(h_p, m_p, h_ally, h_bag,
	   h_magic, h_wpn, h_amr):
	new_h_p = []
	new_h_ally = []
	new_h_wpn = []
	new_h_amr = []
	for hero in h_p:
		copy_hero = copy.copy(hero)
		new_h_p.append(copy_hero)
	for ally in h_ally:
		copy_ally = copy.copy(ally)
		new_h_ally.append(copy_ally)
	for wpn in h_wpn:
		copy_weapon = copy.copy(wpn)
		new_h_wpn.append(copy_weapon)
	for amr in h_amr:
		copy_armor = copy.copy(amr)
		new_h_amr.append(copy_armor)
	new_m_p = list(m_p)
	clock = pygame.time.Clock()
	battle = True
	x, y = WIN.get_size()
	FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
	WIN.blit(FOREST_IMG, P.ORIGIN)
	draw_func.draw_heroes(new_h_p, new_h_ally)
	draw_func.draw_monsters(new_m_p)
	pygame.display.update()
	while battle:
		clock.tick(P.SLOWFPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				battle = False
				pygame.quit()
		for hero in new_h_p:
			if hero.health <= 0:
				new_h_p.remove(hero)
		
		for hero in new_h_p:
			if hero.health > 0:
				hero_turn(hero, new_h_p, new_m_p, new_h_ally, h_bag,
					  h_magic, new_h_wpn, new_h_amr)
		for num in range(0, len(m_p)):
			for mon in new_m_p:
				if mon.health <= 0:
					new_m_p.remove(mon)
		if len(new_m_p) > 0:
			pet_func.ally_action(new_h_ally, new_h_p, new_m_p)
		for mon in new_m_p:
			x, y = WIN.get_size()
			FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
			WIN.blit(FOREST_IMG, P.ORIGIN)
			if mon.status == "Stun":
				mon.status = None
			elif mon.health > 0:
				hero = party_func.pick_random_healthy_hero(new_h_p)
				monster_func.monster_attack(mon, hero, new_h_amr, new_h_p, new_m_p)
		for num in range(0, len(m_p)):
			for mon in new_m_p:
				if mon.health <= 0:
					new_m_p.remove(mon)
		for hero in new_h_p:
			if hero.health <= 0:
				new_h_p.remove(hero)
		if len(new_h_p) == 0 or len(new_m_p) == 0:
			battle = False
			if len(new_h_p) == 0:
				WIN.blit(FOREST_IMG, P.ORIGIN)
				fail_text = REG_FONT.render("The heroes are defeated and flee. ", 1, P.RED)
				WIN.blit(fail_text, ((x - fail_text.get_width())//2, P.PADDING * 2))
				pygame.display.update()
				pygame.time.delay(1000)
	if not battle:
		#adjust the hp of the heroes after battles
		for hero in h_p:
			check = None
			for heero in new_h_p:
				if hero.name == heero.name:
					check = heero
			#if there is no matching hero then the hero's health goes to zero
			if check == None and hero.name != "Knight":
				hero.health = 0
				hero.mana = 0
			#if there is a matching hero then the hero's health becomes equal
			elif check != None:
				hero.health = min(check.health, hero.maxhealth)
				hero.mana = min(check.mana, hero.maxmana)
			elif check == None and hero.name == "Knight":
				for heeero in new_h_p:
					if heeero.name == "Defender":
						check = heeero
				if check == None:
					hero.health = 0
					hero.mana = 0
				elif check != None:
					hero.health = min(check.health, hero.maxhealth)
					hero.mana = min(check.mana, hero.maxmana)
		if len(new_h_p) > 0:
			drop_step(h_p, m_p, h_bag)
		while len(m_p) > 0:
			m_p.clear()
