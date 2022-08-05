import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("./pyquest")
sys.path.append("../pygame_functions/pygame_general_functions/")
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
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
import pyquest_battle as battle_func
import pyquestmon_functions as mon_func
#import rpg2_orc_quest as orc_func
#import rpg2_giant_quest as giant_func
#images
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
VILLAGE_RAW = pygame.image.load(os.path.join("Assets", "village.png"))
VILLAGE_IMG = pygame.transform.scale(VILLAGE_RAW, (P.WIDTH, P.HEIGHT))
#quest five is dealing with elementals
def quest_five(h_p, h_bag, s_pc, p_npc, h_w, h_a, q_i, a_i):
	x, y = WIN.get_size()
	VILLAGE_IMG = pygame.transform.scale(VILLAGE_RAW, (x, y))
	WIN.blit(VILLAGE_IMG, (0, 0))
	quest_text = REG_FONT.render("Some elementals are running wild!", 1, P.RED)
	WIN.blit(quest_text, ((x - quest_text.get_width())//2, y//3))
	pygame.display.update()
	pygame.time.delay(1000)
	new_h_p = []
	for hro in h_p:
		copy_hero = copy.copy(hro)
		new_h_p.append(copy_hero)
	e_p = []
	q_i.package -= 1
	y = a_i.rank
	for m in range(0, y):
		for hero in h_p:
			mon = mon_func.elemental_maker(h_bag)
			e_p.append(mon)
	battle_func.battle_phase(new_h_p, e_p, p_npc, ib_pc,
				 s_pc, h_w, h_a, q_i)
	if len(new_h_p) <= 0:
		print ("You look like a mess. ")
		print ("At least we managed to deal with most of the elementals. ")
		print ("The fees for saving you will be taken out of your pay, by the way. ")
	elif len(new_h_p) > 0:
		print ("I knew I could count on you.  Thanks.")
		q_i.rpackage += 1
		a_i.fame += a_i.rank//C.INCREASE_EXPONENT
		h_bag.coins += a_i.rank
'''#quest four is dealing with giants
def quest_four(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
	print ("There are reports of some giants fighting nearby. ")
	print ("Something like that is too dangerous to allow. ")
	print ("Go find out why they're fighting and stop them. ")
	new_h_p = []
	for hro in h_p:
		copy_hero = copy.copy(hro)
		new_h_p.append(copy_hero)
	g_p = []
	q_i.package -= 1
	y = len(h_p)
	g = random.randint(2, max(3, len(h_p)))
	for p in range(0, g):
		mon = mon_func.giant_maker()
		g_p.append(mon)
	print ("You see the giants fighting from atop a hill. ")
	print ("After a lot of shouting at them, they pause to take a breather. ")
	print ("Finally noticing your shouts, they stomp over. ")
	print ("The hills shake with every step. ")
	giant_func.giant_quest(new_h_p, g_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
	if len(new_h_p) <= 0:
		print ("You look pretty bad. ")
		print ("At least you survived an encounter with giants. ")
		print ("A lot of people aren't that lucky. ")
	elif len(new_h_p) > 0:
		print ("I knew I could count on you.  Thanks.")
		q_i.rpackage += 1
		a_i.fame += a_i.rank

#quest two is advanced goblin fighting
#fight goblins until the town is saved
def quest_two(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
	print ("Those goblins are trying to invade the local village. ")
	print ("We'll need to eliminate them before they get close. ")
	new_h_p = []
	for hro in h_p:
		copy_hero = copy.copy(hro)
		new_h_p.append(copy_hero)
	g_p = []
	q_i.package -= 1
	y = len(h_p)
	r = a_i.rank//2
	#at higher ranks you need to fight more goblins
	for x in range(0, y):
		for z in range(0, r):
			mon = mon_func.super_goblin_maker()
			g_p.append(mon)
		print ("You see a band of goblins approaching. ")
		battle_func.battle_phase(new_h_p, g_p, p_npc, ib_pc,
					 s_pc, h_w, h_a, q_i)
		for hero in new_h_p:
			if hero.health <= 0:
				new_h_p.remove(hero)
		if len(new_h_p) == 0:
			break
		elif len(new_h_p) > 0:
			r += a_i.rank//2
	if len(new_h_p) <= 0:
		print ("You ok? We managed to push the goblins back for now. ")
		print ("The fees for saving you will be taken out of your pay, by the way. ")
	elif len(new_h_p) > 0:
		print ("You were a big help, thanks. ")
		q_i.rpackage += 1
		a_i.fame += round(a_i.rank ** C.DECREASE_EXPONENT)'''
#quest one is goblin hunting
#fight goblins until you get the package back
def quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
	x, y = WIN.get_size()
	VILLAGE_IMG = pygame.transform.scale(VILLAGE_RAW, (x, y))
	WIN.blit(VILLAGE_IMG, (0, 0))
	quest_text = REG_FONT.render("Some goblins stole the package, go find it!", 1, P.RED)
	WIN.blit(quest_text, ((x - quest_text.get_width())//2, y//3))
	pygame.display.update()
	pygame.time.delay(1000)
	#make a copy of the heroes party to track if they are defeated
	new_h_p = []
	for hro in h_p:
		copy_hero = copy.copy(hro)
		new_h_p.append(copy_hero)
	#make a party to fill with goblin monsters
	g_p = []
	#take away a package to start the quest
	q_i.package -= 1
	#keep track of the current rpackages that the player has
	x = q_i.rpackage
	#the goblin waves will keep increasing until you find the package
	y = len(h_p) ** C.INCREASE_EXPONENT
	#after they find another rpackage then the quest is over
	while q_i.rpackage == x and len(new_h_p) > 0:
		for z in range(0, y):
			mon = mon_func.super_goblin_maker(h_bag)
			g_p.append(mon)
		battle_func.battle_phase(new_h_p, g_p, p_npc, ib_pc, s_pc,
					 h_w, h_a, q_i, a_i)
		for hero in new_h_p:
			if hero.health <= 0:
				new_h_p.remove(hero)
		y += len(h_p) ** C.INCREASE_EXPONENT
	#if the heroes lose then they get no reward
	if len(new_h_p) <= 0:
		q_i.rpackage = x
	#if they find a pacakge then the quest is over
	elif q_i.rpackage > x:
		#make sure they only get one rpackage from the quest
		q_i.rpackage = x + 1
		#give them a fame
		a_i.fame += 1
		h_bag.coins += a_i.rank

#function that decides what quest to give to the player
#quests can depend on their rank in the guild and fame
def quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i):
	#check whether the party has any packages
	if q_i.package > 0:
		#if so then make a quest
		x = random.randint(0, a_i.rank)
		if x == 0:
			quest_one(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		elif x == 5:
			quest_five(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		else:
                        quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		'''elif x == 7:
			quest_three(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		elif x == 8:
			quest_five(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		elif x == 10:
			quest_four(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)
		else:
			quest(h_p, ib_pc, s_pc, p_npc, h_w, h_a, q_i, a_i)'''
		
	else:
		print ("You don't have an assignment. ")

