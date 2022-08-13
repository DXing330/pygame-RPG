import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../pygame_general_functions")
sys.path.append("..")
sys.path.append("../pygame_draw")
sys.path.append("../../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
				   ItemBag_PC, Spell_PC, Weapon_PC,
				   Armor_PC)
import pyparty_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
import draw_functions as draw_func
import pypick_function as pick_func
#import draw_boss_functions as drawb_func
import draw_effects as drawe_func
import pymonster_function as monster_func
import pybattle_pet_action as pet_func
import pyelement_function as element_func
import pyeqpeffect_function as ee_func
import pymoneffect_function as me_func
import pybattle_hero_skill as hskl_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 25)
#always make a clock
clock = pygame.time.Clock()
#picture for the background
ARENA_RAW = pygame.image.load(os.path.join("Assets", "swamp.png"))
ARENA_IMG = pygame.transform.scale(ARENA_RAW, (P.WIDTH, P.HEIGHT))
#this is the boss
A_H = Monster_NPC("Acid Hydra", B.A_H_HEALTH, B.A_H_ATK,
		  B.A_H_DEF, B.A_H_SKL, "Water", B.A_H_DC)
#boss spawns
def hydra_head_spawn():
	monster = Monster_NPC("Hydra Head", C.MONSTER_MAX_HP//2, 1, 1, 1, "Water", 0)
	return monster
#special actions
def ah_head_action(m_npc, h_p, b_p, h_a):
	x, y = WIN.get_size()
	ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
	WIN.blit(ARENA_IMG, P.ORIGIN)
	draw_func.draw_monster(m_npc)
	#the heads will randomly bite or buff themselves
	z = random.randint(0, 2)
	if z == 0:
		if m_npc.atk > 0:
			hero = party_func.pick_random_healthy_hero(h_p)
			monster_func.monster_attack(m_npc, hero, h_a, h_p, b_p)
			hero.poison += m_npc.atk
		else:
			m_npc.atk += m_npc.skill
			m_npc.skill += 1
			action_text = REG_FONT.render(m_npc.name+" coats its fangs with poison.", 1, P.RED)
			WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
			pygame.display.update()
			pygame.time.delay(250)
	elif z == 1:
		m_npc.atk += m_npc.skill
		m_npc.skill += 1
		action_text = REG_FONT.render(m_npc.name+" coats its fangs with poison.", 1, P.RED)
		WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
		pygame.display.update()
		pygame.time.delay(250)
	elif z == 2:
		for hero in h_p:
			hero.health -= max((m_npc.health//2 - hero.defense - hero.skill), 1)
		m_npc.health = m_npc.health//2
		drawe_func.mon_aoe(m_npc, h_p)
		action_text = REG_FONT.render(m_npc.name+" sprays its acidic blood on the heroes.", 1, P.RED)
		WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
		pygame.display.update()
		pygame.time.delay(250)

#using items in battle
def use_item(hero, h_b, h_p, h_s, m_p):
	use = True
	while use:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
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
#using magic
def magic_attack(spell, hero, m_p):
	hero.mana -= spell.cost
	if spell.targets > 1:
		for monster in m_p:
			new_spell_power = element_func.check_element_spell(spell, monster)
			spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
			monster.health -= spell_atk
		drawe_func.magic_attack(hero, spell, m_p)
	elif spell.targets == 1:
		mon = pick_func.pick_hero(m_p)
		new_spell_power = element_func.check_element_spell(spell, monster)
		spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
		monster.health -= spell_atk
		new_m_p = []
		copy = copy.copy(mon)
		new_m_p.append(copy)
		drawe_func.magic_attack(hero, spell, new_m_p)
#hero turn
def hero_turn(hero, h_p, m_p, h_s, h_bag, h_magic, h_wpn, h_amr):
	x, y = WIN.get_size()
	ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
	WIN.blit(ARENA_IMG, P.ORIGIN)
	draw_func.draw_heroes(h_p, h_s)
	draw_func.draw_monsters(m_p)
	draw_func.draw_battle_menu(hero)
	draw_func.draw_hero_stats(hero)
	turn = True
	while turn:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
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
					hskl_func.player_attack(hero, mon, h_wpn,
								      h_amr, h_p, m_p)
					WIN.blit(ARENA_IMG, P.ORIGIN)
					weapon = party_func.check_equipment(hero, h_wpn)
					drawe_func.hero_attack(hero, weapon, mon)
					pygame.display.update()
					break
				if event.key == pygame.K_a and len(m_p) > 1:
					turn = False
					mon = pick_func.pick_hero(m_p)
					pygame.event.clear()
					hskl_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
					WIN.blit(ARENA_IMG, P.ORIGIN)
					weapon = party_func.check_equipment(hero, h_wpn)
					drawe_func.hero_attack(hero, weapon, mon)
					pygame.display.update()
					break
				if event.key == pygame.K_s:
					turn = False
					WIN.blit(ARENA_IMG, P.ORIGIN)
					pygame.display.update()
					hskl_func.hero_skill(hero, h_p, m_p, h_s, h_wpn, h_amr, h_bag, h_magic)
					break
				if event.key == pygame.K_m and len(h_magic) > 0:
					if hero.mana > 0:
						turn = False
						spell = pick_func.pick_hero(h_magic)
						WIN.blit(ARENA_IMG, P.ORIGIN)
						draw_func.draw_heroes(h_p, h_s)
						draw_func.draw_monsters(m_p)
						pygame.display.update()
						hero.mana -= spell.cost
						if spell.targets > 1:
							for monster in m_p:
								new_spell_power = element_func.check_element_spell(spell, monster)
								spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
								monster.health -= spell_atk
							drawe_func.magic_attack(hero, spell, m_p)
						elif spell.targets == 1:
							mon = pick_func.pick_hero(m_p)
							new_m_p = []
							copy = copy.copy(mon)
							new_m_p.append(copy)
							new_spell_power = element_func.check_element_spell(spell, monster)
							spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
							monster.health -= spell_atk
							drawe_func.magic_attack(hero, spell, new_m_p)
						pygame.display.update()
						break
				if event.key == pygame.K_i:
					turn = False
					use_item(hero, h_bag, h_p, h_s, m_p)
					break

#special boss actions
def ah_phase_one_action(m_npc, h_p, b_p, h_bag):
	x, y = WIN.get_size()
	ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
	WIN.blit(ARENA_IMG, P.ORIGIN)
	draw_func.draw_monster(m_npc)
	draw_func.draw_just_hero(h_p)
	z = random.randint(0, 3)
	if z == 0:                       
		for hero in h_p:
			if hero.poison > 0:
				hero.health -= hero.poison
				hero.atkbonus -= min(hero.poison, hero.atkbonus)
		poison_text = REG_FONT.render(m_npc.name+" curses the acid to weaken.", 1, P.RED)
	elif z == 1:
		for hero in h_p:
			if hero.poison > 0:
				hero.health -= hero.poison
				hero.defbonus -= min(hero.poison, hero.defbonus)
		poison_text = REG_FONT.render(m_npc.name+" curses the acid to corrode.", 1, P.RED)
	elif z == 2:
		for hero in h_p:
			if hero.poison > 0:
				hero.health -= hero.poison
				hero.skill -= min(hero.poison, hero.skill)
		poison_text = REG_FONT.render(m_npc.name+" curses the acid to confuse.", 1, P.RED)
	elif z == 3:
		for hero in h_p:
			if hero.poison > 0:
				hero.health -= hero.poison
				hero.maxhealth -= hero.poison
		poison_text = REG_FONT.render(m_npc.name+" curses the acid to dissolve.", 1, P.RED)
	WIN.blit(poison_text, ((x - poison_text.get_width())//2, y//3))
	pygame.display.update()
	pygame.time.delay(P.SMALLDELAY)
	m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
	m_npc.skill += len(b_p)
	if len(b_p) <= len(h_p):
		WIN.blit(ARENA_IMG, P.ORIGIN)
		mon = hydra_head_spawn()
		b_p.append(mon)
		draw_func.draw_monsters(b_p)
		summon_text = REG_FONT.render(m_npc.name+" spawns another head!", 1, P.RED)
		WIN.blit(summon_text, ((x - summon_text.get_width())//2, y//3))
		pygame.display.update()
		pygame.time.delay(P.SMALLDELAY)
				
#function that controls the basic battle_phase
#the boss battle phase will be a little different
#boss battles will have different phases
#this will be phase one
def phase_one(h_p, b_p, h_s, h_bag, s_pc, h_w, h_a):
	bPhase1 = True
	while bPhase1:
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
		draw_func.draw_monsters(b_p)
		pygame.display.update()
		for mon in b_p:
			if mon.name == "Acid Hydra" and mon.health < (B.A_H_HEALTH * (C.BUFF ** h_bag.ah_trophy))//2:
				bPhase1 = False
				break
			
		if len(h_p) == 0:
			bPhase1 = False

		else:
			for hero in h_p:
				if hero.health > 0:
					hero_turn(hero, h_p, b_p, h_s, h_bag, s_pc, h_w, h_a)
				elif hero.health <= 0:
					h_p.remove(hero)
			pet_func.ally_action(h_s, h_p, b_p)
			for mon in b_p:
				x, y = WIN.get_size()
				ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
				WIN.blit(ARENA_IMG, P.ORIGIN)
				#cut off a head and two more appear
				if mon.health <= 0 and mon.name != "Acid Hydra":
					b_p.remove(mon)
					mon = hydra_head_spawn()
					b_p.append(mon)
					mon = hydra_head_spawn()
					b_p.append(mon)
				elif mon.health >= 0 and mon.name != "Acid Hydra":
					ah_head_action(mon, h_p, b_p, h_a)
				elif mon.health >= 0 and mon.name == "Acid Hydra":
					ah_phase_one_action(mon, h_p, b_p, h_bag)
				elif mon.health <= 0 and mon.name == "Acid Hydra":
					pass
			for hero in h_p:
				if hero.health <= 0:
					h_p.remove(hero)
		for mon in b_p:
			if mon.name == "Acid Hydra" and mon.health < (B.A_H_HEALTH * (C.BUFF ** h_bag.ah_trophy))//2:
				bPhase1 = False
				break
					
				
#special boss actions
def ah_phase_two_action(m_npc, h_p, b_p, h_bag, h_a):
	x, y = WIN.get_size()
	ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
	WIN.blit(ARENA_IMG, P.ORIGIN)
	if m_npc.health > 0 and len(b_p) > 1:
		for hero in h_p:
			WIN.blit(ARENA_IMG, P.ORIGIN)
			draw_func.draw_hero(hero)
			draw_func.draw_monster(m_npc)
			if hero.poison > 0:
				hero.health -= hero.poison
				hero.atkbonus -= min(hero.poison, hero.atkbonus)
				hero.defbonus -= min(hero.poison, hero.defbonus)
				action_text = REG_FONT.render(m_npc.name+" corrupts the poison of "+hero.name+".", 1, P.RED)
				WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
				pygame.display.update()
				pygame.time.delay(250)
			elif hero.poison <= 0:
				hero.poison += m_npc.atk
				action_text = REG_FONT.render(m_npc.name+" sprays acid on "+hero.name+".", 1, P.RED)
				WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
				pygame.display.update()
				pygame.time.delay(250)
		#the hydra also buffs itself
		m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
		m_npc.atk += m_npc.skill
		m_npc.defense += m_npc.skill
		m_npc.skill += 1
	elif m_npc.health > 0 and len(b_p) == 1:
		m_npc.atk += m_npc.skill
		m_npc.defense += m_npc.skill
		m_npc.skill += len(h_p)
		hero = party_func.pick_random_healthy_hero(h_p)
		armor = party_func.check_equipment(hero, h_a)
		new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
		new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
		hero.health -= max((new_m_atk - hero.defense - hero.defbonus), 1)
		hero.poison += m_npc.atk
		hero.health -= hero.poison
		m_npc.health += m_npc.skill + m_npc.atk
		m_npc.dropchance = m_npc.dropchance * B.A_H_DC_UP
		WIN.blit(ARENA_IMG, P.ORIGIN)
		drawe_func.monster_attack(m_npc, hero, armor)
	elif m_npc.health <= 0 and len(b_p) > 1:
		m_npc.health += max((len(b_p) * C.MONSTER_MAX_HP), ((-2)*m_npc.health))
		m_npc.atk += len(b_p) * m_npc.skill
		while len(b_p) > 1:
			for mon in b_p:
				if mon.name != "Acid Hydra":
					WIN.blit(ARENA_IMG, P.ORIGIN)
					drawe_func.mon_atk_mon(m_npc, mon)
					b_p.remove(mon)
					pygame.display.update()
					pygame.time.delay(100)
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_monsters(b_p)
		action_text = REG_FONT.render(m_npc.name+" eats it's other heads to heal!", 1, P.RED)
		WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
		pygame.display.update()
		pygame.time.delay(1000)
	elif m_npc.health <= 0 and len(b_p) == 1:
		m_npc.health += m_npc.skill
		m_npc.skill = 0
		if m_npc.health > 0:
			action_text = REG_FONT.render(m_npc.name+" manages to hang onto life by a thread!", 1, P.RED)
			WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
			pygame.display.update()
			pygame.time.delay(1000)
		elif m_npc.health <= 0:
			action_text = REG_FONT.render(m_npc.name+" finally collapses!", 1, P.RED)
			WIN.blit(action_text, ((x - action_text.get_width())//2, y//3))
			pygame.display.update()
			pygame.time.delay(1000)


#this will be phase two
def phase_two(h_p, b_p, h_s, h_bag, s_pc, h_w, h_a):
	bPhase2 = True
	while bPhase2:
		clock.tick(P.SLOWFPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
		draw_func.draw_monsters(b_p)
		pygame.display.update()
		for hero in h_p:
			if hero.health <= 0:
				h_p.remove(hero)
		if len(h_p) == 0:
			bPhase2 = False
			break
		else:
			for hero in h_p:
				if hero.health > 0:
					hero_turn(hero, h_p, b_p, h_s, h_bag, s_pc, h_w, h_a)
				elif hero.health <= 0:
					h_p.remove(hero)
			pet_func.ally_action(h_s, h_p, b_p)
			for monster in b_p:
				x, y = WIN.get_size()
				ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
				WIN.blit(ARENA_IMG, P.ORIGIN)
				if monster.name == "Acid Hydra":
					ah_phase_two_action(monster, h_p, b_p, h_bag, h_a)
				elif monster.health > 0 and monster.name != "Acid Hydra":
					ah_head_action(monster, h_p, b_p, h_a)
				elif monster.health <= 0 and monster.name != "Acid Hydra":
					b_p.remove(monster)
					mon = hydra_head_spawn()
					b_p.append(mon)
		for hero in h_p:
			if hero.health <= 0:
				h_p.remove(hero)
		if len(h_p) == 0:
			bPhase2 = False
			break
		#if the hydra is on its last head, check if the battle continues
		if len(b_p) == 1:
			for mon in b_p:
				if mon.name == "Acid Hydra":
					if mon.health <= 0:
						bPhase2 = False
						break
#phases will change according to boss hp
def battle(h_p, b_p, h_s, h_bag, s_pc, h_w, h_a):
	#make a copy of the heroes party and the monster's party
	b_p = []
	Hydra = copy.copy(A_H)
	Hydra.health = round(Hydra.health * (C.BUFF ** h_bag.ah_trophy))
	b_p.append(Hydra)
	new_h_p = []
	new_h_s = []
	new_h_w = []
	new_h_a = []
	new_b_p = []
	for hero in h_p:
		copy_hero = copy.copy(hero)
		new_h_p.append(copy_hero)
	for ally in h_s:
		copy_ally = copy.copy(ally)
		new_h_s.append(copy_ally)
	for wpn in h_w:
		copy_weapon = copy.copy(wpn)
		new_h_w.append(copy_weapon)
	for amr in h_a:
		copy_armor = copy.copy(amr)
		new_h_a.append(copy_armor)
	for mon in b_p:
		copy_mon = copy.copy(mon)
		new_b_p.append(mon)
	#boolean to loop the battle phase until it finishes
	bBattle = True
	while bBattle:
		clock.tick(P.SLOWFPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
		WIN.blit(ARENA_IMG, P.ORIGIN)
		#check to see if the battle continues
		if len(new_b_p) == 1:
			for mon in new_b_p:
				if mon.name == "Acid Hydra" and mon.health <= 0:
					bBattle = False
					end_text = REG_FONT.render("At last it seems no new heads appear.", 1, P.WHITE)
					WIN.blit(end_text, ((x - end_text.get_width())//2, P.PADDING * 2))
					pygame.display.update()
					pygame.time.delay(1000)
					#copy the end hydra to keep track of his dropchance
					fhydra = copy.copy(mon)
					b_p.append(fhydra)
					new_b_p.remove(mon)
					
		if len(new_h_p) == 0:
			end_text = REG_FONT.render("The heroes have been routed and flee back to town.", 1, P.WHITE)
			WIN.blit(end_text, ((x - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
			bBattle = False
			break
		elif len(new_b_p) == 0:
			end_text = REG_FONT.render("The swamp is relatively safe, for now.", 1, P.WHITE)
			WIN.blit(end_text, ((x - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
			bBattle = False
			break

		else:
			for mon in new_b_p:
				if mon.name == "Acid Hydra" and mon.health >= (B.A_H_HEALTH * (C.BUFF ** h_bag.ah_trophy))/2:
					start_text = REG_FONT.render("You find the massive monster in the swamp!", 1, P.WHITE)
					WIN.blit(start_text, ((x - start_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(new_b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					phase_one(new_h_p, new_b_p, new_h_s, h_bag, s_pc, new_h_w, new_h_a)
				elif mon.name == "Acid Hydra" and mon.health < (B.A_H_HEALTH * (C.BUFF ** h_bag.ah_trophy))/2:
					start_text = REG_FONT.render("The hydra's regeneration seems to be slowing!", 1, P.WHITE)
					WIN.blit(start_text, ((x - start_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					phase_two(new_h_p, new_b_p, new_h_s, h_bag, s_pc, new_h_w, new_h_a)
					
	if not bBattle:
		#adjust the hp of the heroes after battles
		for hero in h_p:
			check = None
			#knight can change names so he gets his own function
			if "Knight" in hero.name:
				for heero in new_h_p:
					if heero.name == "Defender":
						check = heero
					if "Knight" in heero.name:
						check = heero
			else:
				for heero in new_h_p:
					if hero.name == heero.name:
						check = heero
			#if there is no matching hero then the hero's health goes to zero
			if check == None:
				hero.health = 0
				hero.mana = 0
			#if there is a matching hero then the hero's health becomes equal
			elif check != None:
				hero.health = min(check.health, hero.maxhealth)
				hero.mana = min(check.mana, hero.maxmana)
		#give the heroes rewards if they win
		if len(new_h_p) > 0:
			for mon in b_p:
				h_bag.coins += round(mon.dropchance)
			h_bag.ah_trophy += 1
			h_bag.flow -= round(h_bag.ah_trophy ** C.DECREASE_EXPONENT)
			for hero in h_p:
				hero.exp += round(h_bag.ah_trophy ** C.DECREASE_EXPONENT)
			for hero in h_p:
				x, y = WIN.get_size()
				ARENA_IMG = pygame.transform.scale(ARENA_RAW, (x, y))
				WIN.blit(ARENA_IMG, P.ORIGIN)
				x = party_func.check_exp(hero)
				if x == 1:
					drawe_func.hero_level_up(hero)
