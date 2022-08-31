import copy
import random
import sys
sys.path.append("../pygame_general_functions")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import pyparty_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from rpg2_constant_quests import Q_Constants
L = List_Constants()
C = Constants()
Q = Q_Constants()

e = len(L.ELEMENTS_LIST) - 1
b = len(L.MONSTER_BUFF_LIST) - 1
#function that makes goblins
def super_goblin_maker(bag):
	x = random.randint(0, 2)
	if x == 0:
		mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
				  Q.GOBLIN_DEF, Q.GOBLIN_SKILL, "Earth",
				  Q.GOBLIN_DC)
	elif x == 1:
		mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
				  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
				  Q.HGOBLIN_SKILL, "Earth", Q.HGOBLIN_DC)
	elif x == 2:
		y = random.randint(0, 2)
		if y == 0:
			mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
					  Q.GOBLIN_DEF, Q.GOBLIN_SKILL,
					  "Earth", Q.GOBLIN_DC)
		elif y == 1:
			mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
					  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
					  Q.HGOBLIN_SKILL, "Earth", Q.HGOBLIN_DC)
		elif y == 2:
			hp = Q.CGOBLIN_HP + random.randint(0, bag.flow)
			atk = Q.CGOBLIN_ATK + random.randint(0, bag.flow//2)
			mon = Monster_NPC("Goblin Champion", hp, atk,
					  Q.CGOBLIN_DEF, Q.CGOBLIN_SKILL,
					  "Earth", Q.CGOBLIN_DC)
	return mon
def random_goblin_maker(bag):
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	x = random.randint(0, 2)
	if x == 0:
		mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
				  Q.GOBLIN_DEF, Q.GOBLIN_SKILL, element,
				  Q.GOBLIN_DC)
	elif x == 1:
		mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
				  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
				  Q.HGOBLIN_SKILL, element, Q.HGOBLIN_DC)
	elif x == 2:
		y = random.randint(0, 2)
		if y == 0:
			mon = Monster_NPC("Goblin", Q.GOBLIN_HP, Q.GOBLIN_ATK,
					  Q.GOBLIN_DEF, Q.GOBLIN_SKILL,
					  element, Q.GOBLIN_DC)
		elif y == 1:
			mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
					  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
					  Q.HGOBLIN_SKILL, element, Q.HGOBLIN_DC)
		elif y == 2:
			hp = Q.CGOBLIN_HP + random.randint(0, bag.flow//2)
			atk = Q.CGOBLIN_ATK + random.randint(0, bag.flow//4)
			mon = Monster_NPC("Goblin Champion", hp, atk,
					  Q.CGOBLIN_DEF, Q.CGOBLIN_SKILL,
					  element, Q.CGOBLIN_DC)
	return mon

def random_effect_goblin_maker(bag):
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	buf = random.randint(0, b)
	buff = L.MONSTER_BUFF_LIST[buf]
	x = random.randint(1, 2)
	if x == 1:
		mon = Monster_NPC("Hob Goblin", Q.HGOBLIN_HP,
				  Q.HGOBLIN_ATK, Q.HGOBLIN_DEF,
				  Q.HGOBLIN_SKILL, element, Q.HGOBLIN_DC, 0, buff)
	elif x == 2:
		y = random.randint(1, 2)
		if y == 1:
			hp = Q.HGOBLIN_HP + random.randint(0, bag.flow//2)
			atk = Q.HGOBLIN_ATK + random.randint(0, bag.flow//4)
			mon = Monster_NPC("Hob Goblin", hp,
					  atk, Q.HGOBLIN_DEF,
					  Q.HGOBLIN_SKILL, element, Q.HGOBLIN_DC,
					  0, buff)
		elif y == 2:
			hp = Q.CGOBLIN_HP + random.randint(0, bag.flow)
			atk = Q.CGOBLIN_ATK + random.randint(0, bag.flow//2)
			defense = Q.CGOBLIN_DEF + random.randint(0, bag.flow//4)
			mon = Monster_NPC("Goblin Champion", hp, atk,
					  defense, Q.CGOBLIN_SKILL,
					  element, Q.CGOBLIN_DC, 0, buff)
	return mon

#function that makes orcs
def orc_maker():
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	mon = Monster_NPC(element + " Orc",
			  Q.ORC_HP, Q.ORC_ATK,
			  Q.ORC_DEF, Q.ORC_SKILL,
			  element, Q.ORC_DC)
	return mon

def orc_chief():
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	mon = Monster_NPC(element + " Orc Chief",
			  Q.CORC_HP, Q.CORC_ATK,
			  Q.CORC_DEF, Q.CORC_SKILL,
			  element, Q.CORC_DC)
	return mon

#function that makes giants
def giant_maker(bag):
	buf = random.randint(0, b)
	buff = L.MONSTER_BUFF_LIST[buf]
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	mon = Monster_NPC(element + " Giant",
			  Q.GIANT_HP, Q.GIANT_ATK,
			  Q.GIANT_DEF, Q.GIANT_SKILL,
			  element, Q.GIANT_DC, 0, buff)
	return mon

#function that makes wild elementals
def elemental_maker(bag):
	elmnt = random.randint(0, e)
	element = L.ELEMENTS_LIST[elmnt]
	buf = random.randint(0, b)
	buff = L.MONSTER_BUFF_LIST[buf]
	hp = C.MONSTER_MAX_HP + random.randint(0, bag.flow)
	atk = C.MONSTER_MAX_ATK + random.randint(0, bag.flow//2)
	defense = C.MONSTER_MAX_DEF + random.randint(0, bag.flow//4)
	mon = Monster_NPC(element + "Elemental", 
			  hp, atk, defense, C.MONSTER_MAX_SKILL,
			  element, C.MONSTER_MAX_DC, 0, buff)
	return mon
