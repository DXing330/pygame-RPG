import pygame
import os
pygame.init()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import rpg2_player_action_function as player_act_func
import rpg2_element_function as element_func
import rpg2_monster_effect_function as me_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))

#function that controls using magic
def hero_magic(hero, h_p, m_p, h_ally, h_bag, h_magic):
	magic = True
	cast = False
	spell = None
	pick = False
	mon = None
	while magic:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		draw_func.draw_spell_list(h_magic)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_1:
					spell = h_magic[0]
					cast = True
					magic = False
				if event.key == pygame.K_2 and len(h_magic) > 1:
					spell = h_magic[1]
					cast = True
					magic = False
				if event.key == pygame.K_3 and len(h_magic) > 2:
					spell = h_magic[2]
					cast = True
					magic = False
				if event.key == pygame.K_4 and len(h_magic) > 3:
					spell = h_magic[3]
					cast = True
					magic = False
				if event.key == pygame.K_5 and len(h_magic) > 4:
					spell = h_magic[4]
					cast = True
					magic = False
				if event.key == pygame.K_6 and len(h_magic) > 5:
					spell = h_magic[5]
					cast = True
					magic = False
				if event.key == pygame.K_7 and len(h_magic) > 6:
					spell = h_magic[6]
					cast = True
					magic = False
				if event.key == pygame.K_8 and len(h_magic) > 7:
					spell = h_magic[7]
					cast = True
					magic = False
				if event.key == pygame.K_9 and len(h_magic) > 8:
					spell = h_magic[8]
					cast = True
					magic = False
	while cast:
		pygame.event.clear()
		clock.tick(P.SLOWFPS)
		x, y = WIN.get_size()
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		pygame.display.update()
		if spell.targets > 1:
			for monster in m_p:
				new_spell_power = element_func.check_element_spell(spell, monster)
				spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
				monster.health -= spell_atk
			cast = False
			hero.mana -= spell.cost
			spell_text = REG_FONT.render(hero.name + " casts " + spell.name, 1, P.RED)
			x, y = WIN.get_size()
			draw_func.draw_heroes(h_p, h_ally)
			draw_func.draw_monsters(m_p)
			WIN.blit(spell_text, ((x - spell_text.get_width())//2, y//3))
			pygame.display.update()
			pygame.time.delay(P.SMALLDELAY)
		elif spell.targets == 1:
			cast = False
			pick = True
	while pick:
		draw_func.draw_monster_menu_list(m_p)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				#need a way to pick a monster
				if event.key == pygame.K_a:
					mon = m_p[0]
					pick = False
				if event.key == pygame.K_1:
					mon = m_p[0]
					pick = False
				if event.key == pygame.K_2 and len(m_p) > 1:
					mon = m_p[1]
					pick = False
				if event.key == pygame.K_3 and len(m_p) > 2:
					mon = m_p[2]
					pick = False
				if event.key == pygame.K_4 and len(m_p) > 3:
					mon = m_p[3]
					pick = False
				if event.key == pygame.K_5 and len(m_p) > 4:
					mon = m_p[4]
					pick = False
				if event.key == pygame.K_6 and len(m_p) > 5:
					mon = m_p[5]
					pick = False
				if event.key == pygame.K_7 and len(m_p) > 6:
					mon = m_p[6]
					pick = False
				if event.key == pygame.K_8 and len(m_p) > 7:
					mon = m_p[7]
					pick = False
				if event.key == pygame.K_9 and len(m_p) > 8:
					mon = m_p[8]
					pick = False
	if not pick and mon != None and spell != None:
		pygame.event.clear()
		new_spell_power = element_func.check_element_spell(spell, monster)
		spell_atk = me_func.monster_buff_check_spell(monster, hero, spell, new_spell_power)
		monster.health -= spell_atk
		hero.mana -= spell.cost
		spell_text = REG_FONT.render(hero.name + " casts " + spell.name + " on " + mon.name, 1, P.RED)
		x, y = WIN.get_size()
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		WIN.blit(spell_text, ((P.WIDTH - spell_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.time.delay(P.SMALLDELAY)
