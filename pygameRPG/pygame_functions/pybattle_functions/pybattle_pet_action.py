import pygame
pygame.init()
import random
import sys
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("..")
sys.path.append("../pygame_draw")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
				   ItemBag_PC, Spell_PC)
import pyparty_functions as party_func
from rpg2_constants import Constants
C = Constants()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_effects as draw_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#function that controls what the pet will do during battle
#need to input the pet and both parties
def angel_random_action(ally, h_p, m_p):
	z = random.randint(0, ally.stage)
	if z == 0:
		hero = party_func.pet_pick_random_injured_hero(h_p)
		hero.poison -= min(ally.stage, hero.poison)
		hero.health = min((hero.health + round(ally.atk ** C.PET_HP_BUFF)), hero.maxhealth)
		draw_func.angel_heal_action(ally, hero)
		hero = party_func.pet_pick_random_injured_hero(h_p)
		hero.poison -= min(ally.stage, hero.poison)
		hero.health = min((hero.health + round(ally.atk ** C.PET_HP_BUFF)), hero.maxhealth)
		draw_func.angel_heal_action(ally, hero)
	elif z == 1:
		monster = party_func.pick_random_healthy_monster(m_p)
		monster.health -= max((ally.atk - monster.defense), 1)
		draw_func.angel_debuff_action(ally, monster)
		hero = party_func.pet_pick_random_injured_hero(h_p)
		hero.poison -= min(ally.stage, hero.poison)
		hero.health = min((hero.health + round(ally.atk ** C.PET_HP_BUFF)), hero.maxhealth)
		draw_func.angel_heal_action(ally, hero)
	elif z == 2:
		hero = party_func.pet_pick_random_healthy_hero(h_p)
		hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
		hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
		hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
		hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
		draw_func.angel_buff_action(ally, hero)
	elif z == 3:
		monster = party_func.pick_random_healthy_monster(m_p)
		monster.atk = max(monster.atk - round(ally.atk ** C.PET_ATK_BUFF), 0)
		monster.defense = max(monster.defense - round(ally.atk ** C.PET_DEF_BUFF), 0)
		draw_func.angel_debuff_action(ally, monster)
	elif z == 4:
		hero = party_func.pet_pick_random_healthy_hero(h_p)
		hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
		hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
		hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
		hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
		draw_func.angel_buff_action(ally, hero)
		hero = party_func.pet_pick_random_healthy_hero(h_p)
		hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
		hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
		hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
		hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
		draw_func.angel_buff_action(ally, hero)
	elif z == 5:
		monster = party_func.pick_random_healthy_monster(m_p)
		monster.atk = max(monster.atk - round(ally.atk ** C.PET_ATK_BUFF), 0)
		monster.defense = max(monster.defense - round(ally.atk ** C.PET_DEF_BUFF), 0)
		draw_func.angel_debuff_action(ally, monster)
		monster = party_func.pick_random_healthy_monster(m_p)
		monster.atk = max(monster.atk - round(ally.atk ** C.PET_ATK_BUFF), 0)
		monster.defense = max(monster.defense - round(ally.atk ** C.PET_DEF_BUFF), 0)
		draw_func.angel_debuff_action(ally, monster)
	elif z >= 6:
		draw_func.angel_legendary_action(ally, h_p, m_p)
		for hero in h_p:
			if "Totem" in hero.name:
				hero.maxhealth += ally.atk
			else:
				hero.poison -= min(ally.stage, hero.poison)
				hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
				hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
				hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
				hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
				hero.health = min(hero.health + round(ally.atk ** C.PET_HP_BUFF), hero.maxhealth)
				
		for monster in m_p:
			monster.atk = max(monster.atk - round(ally.atk ** C.PET_ATK_BUFF), 0)
			monster.defense = max(monster.defense - round(ally.atk ** C.PET_DEF_BUFF), 0)
			monster.health -= ally.atk

def angel_action(ally, h_p, m_p):
	for hero in h_p:
		if "Summoner" in hero.name:
			angel_random_action(ally, h_p, m_p)
		elif "Hero" in hero.name:
			hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
			hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
			hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
			hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
			hero.poison -= min(ally.stage, hero.poison)
			draw_func.angel_buff_action(ally, hero)
		elif "Totem" in hero.name:
			if hero.atk > 0:
				monster = party_func.pick_random_healthy_monster(m_p)
				monster.health -= max((ally.atk - monster.defense), 1)
			elif hero.skill > 0:
				hero = party_func.pet_pick_random_healthy_hero(h_p)
				hero.maxhealth += round(ally.atk ** C.PET_HP_BUFF)
				hero.atkbonus += round(ally.atk ** C.PET_ATK_BUFF)
				hero.defbonus += round(ally.atk ** C.PET_DEF_BUFF)
				hero.skill += round(ally.atk ** C.PET_SKILL_BUFF)
			elif hero.defense > 0:
				hero = party_func.pet_pick_random_injured_hero(h_p)
				hero.poison -= min(ally.stage, hero.poison)
				hero.health = min((hero.health + ally.atk), hero.maxhealth)
			elif hero.mana > 0:
				monster = party_func.pick_random_healthy_monster(m_p)
				monster.atk = max(monster.atk - round(ally.atk ** C.PET_ATK_BUFF), 0)
				monster.defense = max(monster.defense - round(ally.atk ** C.PET_DEF_BUFF), 0)
		else:
			x = random.randint(0, C.PET_ACTION_UP * len(h_p) * len(m_p))
			if x == 0:
				angel_random_action(ally, h_p, m_p)

#companions actions
def companion_action(ally, h_p, m_p):
	for hero in h_p:
		if "Hunter" in hero.name:
			x = random.randint(0, ally.stage)
			if x < 3:
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)
			elif x < 6:
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)
			else:
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)
				mon = party_func.pet_pick_random_monster(m_p)
				mon.poison += ally.atk//ally.stage
				mon.health -= mon.poison
				draw_func.spirit_companion_atk(ally, mon)

def ally_action(h_ally, h_p, m_p):
	#check if there is an angel ally
	angel = None
	comp = None
	for ally in h_ally:
		if "Angel" in ally.name:
			angel = ally
	for ally in h_ally:
		if "Spirit" in ally.name:
			comp = ally
	if angel != None:
		angel_action(angel, h_p, m_p)
	if comp != None:
		companion_action(comp, h_p, m_p)

def totem_turn(totem, h_p, m_p, h_ally):
	if "Attack" in totem.name:
		for ally in h_ally:
			ally.atk += 1
	if "Heal" in totem.name:
		for hero in h_p:
			hero.health += hero.level
	if "Debuff" in totem.name:
		for mon in m_p:
			mon.atk -= min(1, mon.atk)
			print(mon.name+" is debuffed.")
	if "Buff" in totem.name:
		for hero in h_p:
			hero.skill += 1
	
