import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../../../RPG2v3/RPG2v3_functions/")
sys.path.append("../../pygame_functions/pygame_general_functions/")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Pet_NPC,
				   ItemBag_PC, Spell_PC, Weapon_PC,
				   Armor_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from rpg2_boss_constants import BOSS_CONSTANTS
B = BOSS_CONSTANTS()
import draw_functions as draw_func
import pypick_function as pick_func
#import draw_boss_functions as drawb_func
import draw_effects as drawe_func
import rpg2_monster_function as monster_func
import rpg2_player_action_function as player_act_func
import pybattle_pet_action as pet_func
import rpg2_element_function as element_func
import rpg2_monster_effect_function as me_func
import pybattle_hero_skill as hskl_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#picture for the demon lord's castle which will be the background
CASTLE_RAW = pygame.image.load(os.path.join("Assets", "throne2.png"))
CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (P.WIDTH, P.HEIGHT))

D_G = Monster_NPC("Demon General", B.DEMON_GENERAL_HEALTH, B.DEMON_GENERAL_ATK,
		  B.DEMON_GENERAL_DEFENSE, B.DEMON_GENERAL_SKILL, "Dark",
		  B.DEMON_GENERAL_DROPCHANCE)

#using items in battle
def use_item(hero, h_b, h_p, h_s, m_p):
	use = True
	while use:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
		WIN.blit(CASTLE_IMG, P.ORIGIN)
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
#hero turn
def hero_turn(hero, h_p, m_p, h_s, h_bag, h_magic, h_wpn, h_amr):
	turn = True
	while turn:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
		draw_func.draw_monsters(m_p)
		draw_func.draw_battle_menu(hero)
		draw_func.draw_hero_stats(hero)
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
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					pygame.display.update()
					drawe_func.hero_attack(hero, mon)
					break
				if event.key == pygame.K_a and len(m_p) > 1:
					turn = False
					mon = pick_func.pick_hero(m_p)
					pygame.event.clear()
					player_act_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					drawe_func.hero_attack(hero, mon)
					pygame.display.update()
					break
				if event.key == pygame.K_s:
					turn = False
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					pygame.display.update()
					hskl_func.hero_skill(hero, h_p, m_p, h_s, h_wpn, h_amr, h_bag, h_magic)
					break
				if event.key == pygame.K_m and len(h_magic) > 0:
					if hero.mana > 0:
						turn = False
						spell = pick_func.pick_hero(h_magic)
						WIN.blit(CASTLE_IMG, P.ORIGIN)
						draw_func.draw_heroes(h_p, h_s)
						draw_func.draw_monsters(m_p)
						pygame.display.update()
						hero.mana -= spell.cost
						if spell.targets > 1:
							for monster in m_p:
								new_spell_power = element_func.check_element_spell(spell, monster)
								spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
								monster.health -= spell_atk
							spell_text = REG_FONT.render(hero.name + " casts " + spell.name, 1, P.RED)
						elif spell.targets == 1:
							mon = pick_func.pick_hero(m_p)
							new_spell_power = element_func.check_element_spell(spell, monster)
							spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
							monster.health -= spell_atk
							spell_text = REG_FONT.render(hero.name + " casts " + spell.name + " on " + mon.name, 1, P.RED)
						WIN.blit(spell_text, ((x - spell_text.get_width())//2, y//3))
						pygame.display.update()
						pygame.time.delay(P.SMALLDELAY)
						break
				if event.key == pygame.K_i:
					turn = False
					use_item(hero, h_bag, h_p, h_s, m_p)
					break

#special boss actions
def dg_phase_one_action(monster, h_p, b_p, h_bag):
	x, y = WIN.get_size()
	CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
	WIN.blit(CASTLE_IMG, P.ORIGIN)
	if monster.health >= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.95:
		line_one = REG_FONT.render("Pathetic, you can't even scratch me.", 1, P.WHITE)
		line_two = REG_FONT.render("I don't know why you humans even bother to oppose me.", 1, P.WHITE)
		WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
		WIN.blit(line_two, ((x - line_two.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.time.delay(1000)
	elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.7 <= monster.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.95:
		if len(b_p) > 1:
			line_one = REG_FONT.render("Hmph, hurry up and get rid of them my guards!", 1, P.WHITE)
			WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
			for mon in b_p:
				if mon.name != "Demon General":
					mon.atk += monster.skill
		elif len(b_p) == 1:
			line_one = REG_FONT.render("Worthless guards, but no matter.  I have more.", 1, P.WHITE)
			line_two = REG_FONT.render("GUARDS!!!", 1, P.WHITE)
			WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
			WIN.blit(line_two, ((x - line_two.get_width())//2, P.PADDING * 3))
			pygame.display.update()
			pygame.time.delay(1000)
			for hero in h_p:
				mon = monster_func.random_scaled_up_monster(hero)
				b_p.append(mon)
				WIN.blit(CASTLE_IMG, P.ORIGIN)
				appear_text = REG_FONT.render(mon.name+" appears from the shadows!", 1, P.WHITE)
				WIN.blit(appear_text, ((x - appear_text.get_width())//2, P.PADDING * 2))
				draw_func.draw_monsters(b_p)
				pygame.display.update()
				pygame.time.delay(1000)
			       
	elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.5 <= monster.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.7:
		if len(b_p) > 1:
			line_one = REG_FONT.render("GUARDS! If you can't even deal with these pathetic fools, then I don't need you!", 1, P.WHITE)
			WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
			for mon in b_p:
				if mon.name != "Demon General":
					mon.atk += monster.skill
		elif len(b_p) == 1:
			line_one = REG_FONT.render("Those guards were even more worthless than you. No matter though, I have plenty more.", 1, P.WHITE)
			line_two = REG_FONT.render("GUARDS!!!!!!!!", 1, P.WHITE)
			WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
			WIN.blit(line_two, ((x - line_two.get_width())//2, P.PADDING * 3))
			pygame.display.update()
			pygame.time.delay(1000)
			for hero in h_p:
				mon = monster_func.random_scaled_monster(hero)
				b_p.append(mon)
				WIN.blit(CASTLE_IMG, P.ORIGIN)
				appear_text = REG_FONT.render(mon.name+" runs in from the hallway!", 1, P.WHITE)
				WIN.blit(appear_text, ((x - appear_text.get_width())//2, P.PADDING * 2))
				draw_func.draw_monsters(b_p)
				pygame.display.update()
				pygame.time.delay(1000)
	elif monster.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.5:
		line_one = REG_FONT.render("WORTHLESS FOOLS!", 1, P.WHITE)
		WIN.blit(line_one, ((x - line_one.get_width())//2, P.PADDING * 2))
		pygame.time.delay(1000)
		pygame.display.update()
		for num in range(0, len(b_p)):
			for mon in b_p:
				if mon.name != "Demon General":
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					drawe_func.mon_atk_mon(monster, mon)
					b_p.remove(mon)
				
#function that controls the basic battle_phase
#the boss battle phase will be a little different
#boss battles will have different phases
#this will be phase one
def dg_phase_one(h_p, b_p, h_s, h_bag, s_pc, h_w, h_a):
	bPhase1 = True
	while bPhase1:
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
		draw_func.draw_monsters(b_p)
		pygame.display.update()
		if len(h_p) == 0:
			print ("The heroes have been routed and flee back to town.")
			bPhase1 = False

		else:
			for hero in h_p:
				if "Totem" in hero.name:
					pass
				elif hero.health > 0:
					hero_turn(hero, h_p, b_p, h_s, h_bag, s_pc, h_w, h_a)
				elif hero.health <= 0:
					h_p.remove(hero)
			pet_func.ally_action(h_s, h_p, h_p)
			for num in range(0, len(b_p)):
				for monster in b_p:
					if monster.health <= 0 and monster.name != "Demon General":
						b_p.remove(monster)
			for monster in b_p:
				x, y = WIN.get_size()
				CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
				WIN.blit(CASTLE_IMG, P.ORIGIN)
				if monster.name == "Demon General" and monster.health > 0:
					dg_phase_one_action(monster, h_p, b_p, h_bag)
				elif monster.health > 0:
					hero = party_func.pick_random_healthy_hero(h_p)
					monster_func.monster_attack(monster, hero, h_a, h_p, b_p)
					drawe_func.monster_attack(monster, hero)
				elif monster.health <= 0 and monster.name != "Demon General":
					b_p.remove(monster)
			for hero in h_p:
				if hero.health <= 0:
					h_p.remove(hero)
		for mon in b_p:
			if mon.name == "Demon General" and mon.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy))/2:
				print ("Pathetic guards! ")
				bPhase1 = False
					
				
#special boss actions
def dg_phase_two_action(m_npc, h_p, b_p, h_bag, h_a):
	x, y = WIN.get_size()
	CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
	WIN.blit(CASTLE_IMG, P.ORIGIN)
	hero = party_func.pick_random_healthy_hero(h_p)
	armor = party_func.check_equipment(hero, h_a)
	new_atk = ee_func.armor_effect(m_npc, hero, armor, h_p, b_p)
	new_m_atk = element_func.check_element_monster_attack(m_npc, new_atk, armor)
	if (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.4 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.5:
		talk_text = REG_FONT.render("Even a strong bug is still just a bug. Let me show you my power!", 1, P.WHITE)
		WIN.blit(talk_text, ((x - talk_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		pygame.time.delay(500)
		if m_npc.atk < B.DEMON_GENERAL_ATK:
			m_npc.atk += (B.DEMON_GENERAL_ATK - m_npc.atk)
		m_npc.atk += m_npc.skill
		hero.health -= (new_m_atk - hero.defense - hero.defbonus)
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		drawe_func.monster_attack(m_npc, hero)
	elif (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.2 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.4:
		talk_text = REG_FONT.render("Persistent insects! ", 1, P.WHITE)
		WIN.blit(talk_text, ((x - talk_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		pygame.time.delay(500)
		hero.health -= (new_m_atk - hero.defense - hero.defbonus)
		drawe_func.monster_attack(m_npc, hero)
		hero.health -= (new_m_atk - hero.defense - hero.defbonus)
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		drawe_func.monster_attack(m_npc, hero)
	elif 0 < m_npc.health <= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy)) * 0.2:
		if m_npc.health > 1:
			print("Wretched fools, you've pushed me to my limits! ")
			print("I'll show you my final attack! ")
			m_npc.atk += m_npc.health
			m_npc.health = 1
		for x in range(0, len(h_p)):
			hero = party_func.pick_random_healthy_hero(h_p)
			hero.health -= m_npc.atk
			WIN.blit(CASTLE_IMG, P.ORIGIN)
			drawe_func.monster_attack(m_npc, hero)
			print(m_npc.name, "attacks with the last of his energy! ")
	elif m_npc.health <= 0:
		print(m_npc.name, "coughs up blood and falls to the ground.")


#this will be phase two
def dg_phase_two(h_p, b_p, new_h_s, h_bag, s_pc, h_w, h_a):
	bPhase2 = True
	while bPhase2:
		clock.tick(P.SLOWFPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_s)
		draw_func.draw_monsters(b_p)
		pygame.display.update()
		for hero in h_p:
			if hero.health <= 0:
				h_p.remove(hero)
		if len(h_p) == 0:
			print ("The heroes have been routed and flee back to town.")
			bPhase2 = False
			break
		
		else:
			for hero in h_p:
				if "Totem" in hero.name:
					pass
				elif hero.health > 0:
					hero_turn(hero, h_p, b_p, h_s, h_bag, s_pc, h_w, h_a)
				elif hero.health <= 0:
					h_p.remove(hero)
			pet_func.ally_action(h_s, h_p, h_p)
			for monster in b_p:
				x, y = WIN.get_size()
				CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
				WIN.blit(CASTLE_IMG, P.ORIGIN)
				if monster.name == "Demon General":
					dg_phase_two_action(monster, h_p, b_p, h_bag, h_a)
				else:
					b_p.remove(monster)
		for mon in b_p:
			if mon.name == "Demon General" and mon.health <= 0:
				print("You may have beaten me, but my lord will avenge me! ")
				print("You have no idea of the true terror of the demon army! ")
				bPhase2 = False
				break
		for hero in h_p:
			if hero.health <= 0:
				h_p.remove(hero)
		if len(h_p) == 0:
			bPhase2 = False
			break
#phases will change according to boss hp
def battle(h_p, b_p, h_s, h_bag, s_pc, h_w, h_a):
	#make a copy of the heroes party and the monster's party
	b_p = []
	Demon_General = copy.copy(D_G)
	Demon_General.health = round(Demon_General.health * (C.BUFF ** h_bag.dg_trophy))
	b_p.append(Demon_General)
	new_h_p = []
	new_h_s = []
	new_h_w = []
	new_h_a = []
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
	new_b_p = list(b_p)
	#boolean to loop the battle phase until it finishes
	bBattle = True
	while bBattle:
		clock.tick(P.SLOWFPS)
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		CASTLE_IMG = pygame.transform.scale(CASTLE_RAW, (x, y))
		WIN.blit(CASTLE_IMG, P.ORIGIN)
		#check to see if the battle continues
		for mon in new_b_p:
			if mon.name == "Demon General" and mon.health <= 0:
				print ("The Demonic leader has been defeated. ")
				print ("The people can breathe a sigh of relief...for now. ")
				bBattle = False
				new_b_p.remove(mon)
		if len(new_h_p) == 0:
			end_text = REG_FONT.render("The heroes have been routed and flee back to town.", 1, P.WHITE)
			WIN.blit(end_text, ((x - end_text.get_width())//2, P.PADDING * 2))
			pygame.time.delay(1000)
			pygame.display.update()
			bBattle = False
		elif len(new_b_p) == 0:
			end_text = REG_FONT.render("Back at the village you hear rumors of another general far away.", 1, P.WHITE)
			WIN.blit(end_text, ((x - end_text.get_width())//2, P.PADDING * 2))
			pygame.time.delay(1000)
			pygame.display.update()
			bBattle = False

		else:
			for mon in new_b_p:
				if mon.name == "Demon General" and mon.health >= (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy))/2:
					start_text = REG_FONT.render("Visitors? Guards, get rid of them. ", 1, P.WHITE)
					WIN.blit(start_text, ((x - start_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(new_b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					monster = monster_func.random_elite_monster()
					new_b_p.append(monster)
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					appear_text = REG_FONT.render(monster.name+" descends from beside the throne.", 1, P.WHITE)
					WIN.blit(appear_text, ((x - appear_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(new_b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					monster2 = monster_func.random_elite_monster()
					new_b_p.append(monster2)
					WIN.blit(CASTLE_IMG, P.ORIGIN)
					appear_text = REG_FONT.render(monster2.name+" descends from beside the throne.", 1, P.WHITE)
					WIN.blit(appear_text, ((x - appear_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(new_b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					dg_phase_one(new_h_p, new_b_p, new_h_s, h_bag,
						     s_pc, new_h_w, new_h_a)
				elif mon.name == "Demon General" and mon.health < (B.DEMON_GENERAL_HEALTH * (C.BUFF ** h_bag.dg_trophy))/2:
					start_text = REG_FONT.render("Enough! I'll deal with you myself! ", 1, P.WHITE)
					WIN.blit(start_text, ((x - start_text.get_width())//2, P.PADDING * 2))
					draw_func.draw_monsters(b_p)
					pygame.display.update()
					pygame.time.delay(1000)
					dg_phase_two(new_h_p, new_b_p, new_h_s, h_bag,
						     s_pc, new_h_w, new_h_a)
					
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

		if len(new_h_p) > 0:
			print ("The heroes return victorious. ")
			print ("The villagers rain praise and thanks upon them. ")
			h_bag.coins += B.DEMON_GENERAL_DROPCHANCE
			h_bag.dg_trophy += 1
