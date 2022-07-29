import pygame
import os
pygame.init()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import draw_effects as drawe_func
import pypick_function as pick_func
import rpg2_player_action_function as player_act_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
#function that controls a hero attacking a monster
def hero_attack(hero, h_p, m_p, h_ally, h_wpn, h_amr):
	mon = pick_func.pick_hero(m_p)
	pygame.event.clear()
	player_act_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
	x, y = WIN.get_size()
	FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
	WIN.blit(FOREST_IMG, P.ORIGIN)
	drawe_func.hero_attack(hero, mon)
	pygame.display.update()
