import pygame
import os
import sys
sys.path.append("../pygame_general_functions")
sys.path.append("..")
pygame.init()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import rpg2_player_action_function as player_act_func
import rpg2_pet_action_function as pet_func
import pypick_function as pick_func
import pybattle_functions as pybattle_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
#function that controls what kind of skill the hero can use
def hero_skill(hero, h_p, m_p, h_ally, h_wpn, h_amr, h_bag, h_magic):
	hero_other_stat = REG_FONT.render("SKILL: " + str(hero.skill) + " MANA: " + str(hero.mana),
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
		WIN.blit(hero_other_stat, (P.WIDTH - hero_other_stat.get_width() - P.PADDING,
					   P.PADDING + hero_other_stat.get_height() * 3))
		draw_func.draw_skill_menu(hero)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_o:
					WIN.blit(FOREST_IMG, P.ORIGIN)
					draw_func.draw_heroes(h_p, h_ally)
					draw_func.draw_monsters(m_p)
					draw_func.draw_monster_stats(m_p)
					pygame.display.update()
					turn = False
				if event.key == pygame.K_c:
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
				if event.key == pygame.K_p and "Knight" in hero.name:
					hero.name = "Defender"
					for amr in h_amr:
						if "Knight" in amr.user:
							amr.user = "Defender"
					turn = False
