import pygame
import os
import sys
import copy
sys.path.append("../pygame_general_functions")
sys.path.append("..")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
pygame.init()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_constants import Constants
C = Constants()
import pyparty_functions as party_func
import pybattle_pet_action as pet_func
import pypick_function as pick_func
import pybattle_functions as pybattle_func
import draw_functions as draw_func
import draw_animation as drawa_func
import draw_effects as drawe_func
import pyelement_function as element_func
import pyeqpeffect_function as ee_func
import pymoneffect_function as me_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
#function that observes the enemies
def observe(m_p, h_p, h_ally, h_wpn, h_amr):
	WIN.fill(P.WHITE)
	observe = True
	while observe:
		draw_func.draw_monster_stats(m_p)
		draw_func.draw_all_stats(h_p, h_ally, h_wpn, h_amr)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				observe = False
		
#function that makes a bomb
def make_bomb(hero, h_p, m_p, h_ally):
	x, y = WIN.get_size()
	WIN.fill(P.WHITE)
	pygame.display.update()
	pick = True
	while pick:
		pygame.event.clear()
		clock.tick(P.FPS)
		draw_func.draw_bomb_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_e:
					pick = False
					pygame.event.clear()
					bomb = Monster_NPC("Bomb", hero.skill, 0, 0, hero.level, "Blast", 0)
					copy_bomb = copy.copy(bomb)
					m_p.append(copy_bomb)
					break
				elif event.key == pygame.K_p:
					pick = False
					pygame.event.clear()
					bomb = Monster_NPC("Bomb", hero.skill, 0, 0, hero.level, "Poison", 0)
					copy_bomb = copy.copy(bomb)
					m_p.append(copy_bomb)
					break
					
#function that summons a totem
def summon_totem(hero, h_p, m_p, h_ally):
	x, y = WIN.get_size()
	WIN.fill(P.WHITE)
	pygame.display.update()
	pick = True
	while pick:
		pygame.event.clear()
		clock.tick(P.FPS)
		draw_func.draw_totem_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_a:
					totem = Player_PC("Attack Totem", 1, hero.skill, hero.skill,
							  hero.skill, 0, 0, 0, 0)
					copy_totem = copy.copy(totem)
					h_p.append(copy_totem)
					pick = False
					break
				if event.key == pygame.K_b:
					totem = Player_PC("Buff Totem", 1, hero.skill, hero.skill,
							  0, 0, hero.skill, 0, 0)
					copy_totem = copy.copy(totem)
					h_p.append(copy_totem)
					pick = False
					break
				if event.key == pygame.K_d:
					totem = Player_PC("Debuff Totem", 1, hero.skill, hero.skill,
							  0, 0, 0, hero.skill, 0)
					copy_totem = copy.copy(totem)
					h_p.append(copy_totem)
					pick = False
					break
				if event.key == pygame.K_h:
					totem = Player_PC("Heal Totem", 1, hero.skill, hero.skill,
							  0, hero.skill, 0, 0, 0)
					copy_totem = copy.copy(totem)
					h_p.append(copy_totem)
					pick = False
					break
					
	
#function that controls what kind of skill the hero can use
def hero_skill(hero, h_p, m_p, h_ally, h_wpn, h_amr, h_bag, h_magic):
	hero_other_stat = REG_FONT.render("SKILL: " + str(hero.skill) + " MANA: " + str(hero.mana),
					  1, P.RED)
	x, y = WIN.get_size()
	draw_func.draw_heroes(h_p, h_ally)
	draw_func.draw_monsters(m_p)
	WIN.blit(hero_other_stat, (P.WIDTH - hero_other_stat.get_width() - P.PADDING,
				   P.PADDING + hero_other_stat.get_height() * 3))
	draw_func.draw_skill_menu(hero)
	pygame.display.update()
	turn = True
	while turn:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_o:
					observe(m_p, h_p, h_ally, h_wpn, h_amr)
					if "Ninja" in hero.name:
						hero.skill += hero.level
					if "Tactician" in hero.name:
						for hero in h_p:
							if hero.name != "Totem":
								hero.skill += 1
					if "Hunter" in hero.name:
						hero.atkbonus += hero.level
						for ally in h_ally:
							if "Spirit" in ally.name:
								ally.atk += hero.level
					turn = False
					break
				elif event.key == pygame.K_c:
					if "Summoner" in hero.name:
						ally = None
						for aly in h_ally:
							if "Angel" in aly.name:
								ally = aly
						pet_func.angel_action(ally, h_p, m_p)
						pet_func.angel_action(ally, h_p, m_p)
						hero.mana += 1
						turn = False
					elif "Hunter" in hero.name:
						ally = None
						for aly in h_ally:
							if "Spirit" in aly.name:
								ally = aly
						pet_func.companion_action(ally, h_p, m_p)
						turn = False
					elif "Tactician" in hero.name:
						command = pick_func.pick_hero(h_p)
						if "Tactician" in command.name:
							pass
						else:
							pybattle_func.hero_turn(command, h_p, m_p, h_ally,
										h_bag, h_magic, h_wpn, h_amr)
						turn = False
				elif event.key == pygame.K_p and "Knight" in hero.name:
					hero.name = "Defender"
					for amr in h_amr:
						if "Knight" in amr.user:
							amr.user = "Defender"
					turn = False
				elif event.key == pygame.K_t and "Summoner" in hero.name:
					if hero.mana > len(h_p):
						hero.mana -= len(h_p)
						pygame.event.clear()
						summon_totem(hero, h_p, m_p, h_ally)
						turn = False
						break
				elif event.key == pygame.K_h:
					healee = pick_func.pick_healee(h_p)
					turn = False
					#cleric is the best at healing
					if "Cleric" in hero.name:
						healee.health += hero.mana + hero.skill + hero.level
						healee.poison -= min(hero.skill + healee.level, healee.poison)
						if hero.status != None:
							hero.status = None
					elif "Hunter" in hero.name:
						healee.poison -= min(hero.skill + healee.level, healee.poison)
					else:
						healee.health += healee.level
						healee.poison -= min(healee.level, healee.poison)
				elif event.key == pygame.K_d:
					#different heroes debuff different aspects
					mon = pick_func.pick_hero(m_p)
					turn = False
					if "Ninja" in hero.name:
						if hero.skill > mon.skill:
							mon.skill = mon.skill//C.BUFF
							hero.skill -= mon.skill
							hero.mana -= 1
						else:
							mon.skill = round(mon.skill * C.BUFF)
					elif "Knight" in hero.name or "Defender" in hero.name:
						mon.defense -= min(hero.skill, mon.defense)
					elif "Cleric" in hero.name:
						if hero.mana > 0 and hero.skill > 0:
							mon.atk -= min(hero.mana + hero.skill, mon.atk)
							hero.mana -= 1
							hero.skill -= 1
					elif "Hunter" in hero.name:
						mon.atk -= min(round(mon.poison ** C.DECREASE_EXPONENT), mon.atk)
						mon.defense -= min(round(mon.poison ** C.DECREASE_EXPONENT), mon.defense)
					else:
						mon.atk -= min(hero.level, mon.atk)
				elif event.key == pygame.K_b:
					#different heroes buff different aspects
					armor = party_func.check_equipment(hero, h_amr)
					weapon = party_func.check_equipment(hero, h_wpn)
					turn = False
					if "Ninja" in hero.name:
						if hero.mana > 0:
							hero.skill = round(hero.skill * C.BUFF)
							hero.mana -= 1
						else:
							hero.skill += hero.level
					elif "Knight" in hero.name or "Defender" in hero.name:
						hero.defbonus += hero.level//2
						if hero.skill > 0 and armor != None:
							armor.defense += 1
							armor.strength += 1
							hero.skill -= hero.defbonus//hero.level
						else:
							hero.skill += 1
						if hero.buff == None:
							hero.buff = "DEFUP"
						elif "DEFUP" not in hero.buff:
							hero.buff += " DEFUP"
						else:
							hero.defbonus += hero.level//2
					elif "Cleric" in hero.name and hero.mana > 0:
						buff = pick_func.pick_hero(h_p)
						hero.skill -= buff.atkbonus//(hero.level + hero.skill)
						buff.atkbonus += hero.level + hero.skill
						hero.mana -= 1
					elif "Summoner" in hero.name and hero.mana > 0:
						buff = pick_func.pick_hero(h_ally)
						buff.atk += hero.level
						hero.mana -= buff.atk//hero.level
					elif "Hunter" in hero.name:
						hero.atkbonus += hero.level
						if weapon != None:
							weapon.strength += 1
							weapon.atk += 1
					else:
						if hero.skill > hero.atkbonus//hero.level:
							hero.skill -= hero.atkbonus//hero.level
							if hero.buff == None:
								hero.buff = "ATKUP"
							elif "ATKUP" not in hero.buff:
								hero.buff += " ATKUP"
						else:
							hero.skill += 1
				elif event.key == pygame.K_s and "Ninja" in hero.name:
					weapon = party_func.check_equipment(hero, h_wpn)
					mon = pick_func.pick_hero(m_p)
					if weapon != None:
						mon.health -= hero.skill * weapon.atk
						hero.skill = 0
						weapon.atk = 0
					turn = False
				elif event.key == pygame.K_e and "Hunter" in hero.name:
					pygame.event.clear()
					make_bomb(hero, h_p, m_p, h_ally)
					turn = False
					break

#function that controls attacking
def player_attack(hero, m_npc, h_wpn, h_amr, h_p, m_p):
	weapon = party_func.check_equipment(hero, h_wpn)
	new_pa = ee_func.weapon_effect(m_npc, hero, weapon, h_p, m_p)
	new_atk = element_func.check_element_player_attack(hero, new_pa, m_npc, weapon)
	f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, hero, h_p, weapon, h_amr, m_p)
	if "Warrior" in hero.name and hero.level >= C.LEVEL_LIMIT:
		m_npc.health -= f_atk
		new_pa = ee_func.weapon_effect(m_npc, hero, weapon, h_p, m_p)
		new_atk = element_func.check_element_player_attack(hero, new_pa, m_npc, weapon)
		f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, hero, h_p, weapon, h_amr, m_p)
		m_npc.health -= f_atk
		new_pa = ee_func.weapon_effect(m_npc, hero, weapon, h_p, m_p)
		new_atk = element_func.check_element_player_attack(hero, new_pa, m_npc, weapon)
		f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, hero, h_p, weapon, h_amr, m_p)
		m_npc.health -= f_atk
	elif "Warrior" in hero.name or "Hero" in hero.name:
		m_npc.health -= f_atk
		new_pa = ee_func.weapon_effect(m_npc, hero, weapon, h_p, m_p)
		new_atk = element_func.check_element_player_attack(hero, new_pa, m_npc, weapon)
		f_atk = me_func.monster_def_buff_effect(m_npc, new_atk, hero, h_p, weapon, h_amr, m_p)
		m_npc.health -= f_atk
	elif "Defender" in hero.name:
		m_npc.health -= f_atk
		hero.name = "Knight"
		if weapon != None:
			if weapon.effect == "Shield":
				hero.name = "Defender"
		for amr in h_amr:
			if amr.user == "Defender":
				amr.user = hero.name
	else:
		m_npc.health -= f_atk

#using magic
def magical_attack(spell, hero, m_p):
	hero.mana -= spell.cost
	if spell.targets > 1:
		for monster in m_p:
			new_spell_power = element_func.check_element_spell(spell, monster)
			spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
			monster.health -= spell_atk
			#mages are stronger at casting magic
			if "Mage" in hero.name:
				monster.health -= max(spell_atk//2, 0)
		drawe_func.magic_attack(hero, spell, m_p)
	elif spell.targets == 1:
		mon = pick_func.pick_hero(m_p)
		new_spell_power = element_func.check_element_spell(spell, monster)
		spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
		monster.health -= spell_atk
		if "Mage" in hero.name:
			monster.health -= max(spell_atk//2, 0)
		new_m_p = []
		copy = copy.copy(mon)
		new_m_p.append(copy)
		drawe_func.magic_attack(hero, spell, new_m_p)

#hero buffs, effects that are gained in battle and lost out of battle
def hero_buff(hero, h_p, h_ally):
	#this buff will boost the hero's stats at the cost of their health
	if "Advance" in hero.buff:
		hero.health -= hero.level
		hero.atkbonus += hero.level//2
		hero.defbonus += hero.level//4
		hero.skill += hero.level//8
	if "ATKUP" in hero.buff:
		hero.atkbonus += hero.level
		#the buff is consumed upon use
		hero.buff = hero.buff.replace("ATKUP", "")
	if "DEFUP" in hero.buff:
		hero.defbonus += hero.level//4
	if "MANAUP" in hero.buff:
		hero.mana += hero.level//8
	if "SKLUP" in hero.buff:
                hero.skill += hero.level//8

#hero passive effects, like permanent buffs
def hero_passive(hero, h_p, m_p, h_ally):
	#most basic passive is regen
	if "HP+" in hero.passive:
		if hero.health < hero.maxhealth:
			hero.health += hero.level
	if "MP+" in hero.passive:
		if hero.mana < hero.maxmana:
			hero.mana += hero.level//8
	#other basic passives are stat increases
	if "ATK+" in hero.passive:
		hero.atkbonus += hero.level//2
	if "DEF+" in hero.passive:
		hero.defbonus += hero.level//4
	if "SKL+" in hero.passive:
		hero.skill += hero.level//8
	#unique summoner passive
	if "Angel+" in hero.passive:
		for ally in h_ally:
			if "Angel" in ally.name:
				ally.atk += hero.level//8
	#unique hero passive
	if "Inspire" in hero.passive:
		for h in h_p:
			num = random.randint(0, len(h_p))
			if num == 0:
				h.atkbonus += hero.level//2
				h.defbonus += hero.level//4
				h.skill += hero.level//8
#hero debuffs, gained in battle and lost out of battle
def hero_status(hero):
	if "Burn" in hero.status:
		hero.atkbonus -= hero.atkbonus//hero.skill
	if "Silence" in hero.status:
		hero.mana -= 1
	if "Curse" in hero.status:
		hero.skill -= 1
		hero.mana -= 1
