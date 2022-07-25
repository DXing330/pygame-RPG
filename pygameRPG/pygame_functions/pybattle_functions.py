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
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_act_func
import rpg2_pet_action_function as pet_func
import rpg2_element_function as element_func
import rpg2_monster_effect_function as me_func
import pybattle_hero_attack as hatk_func
import pybattle_hero_skill as hskl_func
import pybattle_hero_magic as hmagic_func
import draw_functions as draw_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#also need any specific images
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))

		
#function that controls the turns in battle
def hero_turn(hero, h_p, m_p, h_ally, h_bag,
	      h_magic, h_wpn, h_amr):
	hero_stat_text = REG_FONT.render("Hero: " + hero.name + " ATK: " + str(hero.atk)
					 + " ATKBONUS: " + str(hero.atkbonus)
					 , 1, P.RED)
	hero_def_stat = REG_FONT.render("HP: " + str(hero.health) + " MAX HP: " + str(hero.maxhealth) +
					" DEF: " + str(hero.defense) + (" DEFBONUS: ") + str(hero.defbonus),
					1, P.RED)
	hero_other_stat = REG_FONT.render("SKILL: " + str(hero.skill) + " MANA: " + str(hero.mana)
					  + " MAX MANA: " + str(hero.maxmana),
					  1, P.RED)
	turn = True
	while turn:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		draw_func.draw_battle_menu(h_p, m_p, h_ally, h_magic, h_wpn, h_amr)
		WIN.blit(hero_stat_text, (P.WIDTH - hero_stat_text.get_width() - P.PADDING,
					  P.PADDING + hero_stat_text.get_height()))
		WIN.blit(hero_def_stat, (P.WIDTH - hero_def_stat.get_width() - P.PADDING,
					 P.PADDING + hero_def_stat.get_height() * 2))
		WIN.blit(hero_other_stat, (P.WIDTH - hero_other_stat.get_width() - P.PADDING,
					   P.PADDING + hero_other_stat.get_height() * 3))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_a and len(m_p) == 1:
					turn = False
					mon = m_p[0]
					player_act_func.player_attack(hero, mon, h_wpn,
								      h_amr, h_p, m_p)
					break
				if event.key == pygame.K_a and len(m_p) > 1:
					turn = False
					hatk_func.hero_attack(hero, h_p, m_p, h_ally, h_wpn, h_amr)
					break
				if event.key == pygame.K_s:
					turn = False
					hskl_func.hero_skill(hero, h_p, m_p, h_ally, h_wpn, h_amr)
					break
				if event.key == pygame.K_m and len(h_magic) > 0:
					if hero.mana > 0:
						turn = False
						hmagic_func.hero_magic(hero, h_p, m_p, h_ally, h_bag, h_magic)
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
	while battle:
		clock.tick(P.SLOWFPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW,
						    (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		draw_func.draw_heroes(new_h_p, new_h_ally)
		draw_func.draw_monsters(new_m_p)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				battle = False
				pygame.quit()
		for hero in new_h_p:
			if hero.health > 0:
				hero_turn(hero, new_h_p, new_m_p, new_h_ally, h_bag,
					  h_magic, new_h_wpn, new_h_amr)
		for ally in new_h_ally:
			#maybe later we can make this more animated
			player_act_func.pet_action(new_h_ally, new_h_p, new_m_p)
		for mon in new_m_p:
			if mon.health > 0:
				hero = party_func.pick_random_healthy_hero(new_h_p)
				monster_func.monster_attack(mon, hero, new_h_amr, new_h_p, new_m_p)
		for mon in new_m_p:
			if mon.health <= 0:
				new_m_p.remove(mon)
		for hero in new_h_p:
			if hero.health <= 0:
				new_h_p.remove(hero)
		if len(new_h_p) == 0 or len(new_m_p) == 0:
			battle = False
	if not battle:
		while len(m_p) > 0:
			m_p.clear()
