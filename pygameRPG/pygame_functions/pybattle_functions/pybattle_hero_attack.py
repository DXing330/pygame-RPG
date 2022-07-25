import pygame
import os
pygame.init()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import rpg2_player_action_function as player_act_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
#function that controls a hero attacking a monster
def hero_attack(hero, h_p, m_p, h_ally, h_wpn, h_amr):
	#the game will wait while the hero picks
	pick = True
	mon = None
	hero_stat_text = REG_FONT.render("Hero: " + str(hero.name) + " ATK: " + str(hero.atk) + " ATKBONUS: " + str(hero.atkbonus)
					 , 1, P.RED)
	print (str(hero.stats()))
	while pick:
		WIN.fill(P.WHITE)
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		draw_func.draw_monster_menu_list(m_p)
		WIN.blit(hero_stat_text, (P.WIDTH - hero_stat_text.get_width() - P.PADDING,
					  P.PADDING + hero_stat_text.get_height()))
		pygame.display.update()
		clock.tick(P.FPS)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				#need a way to pick a monster
				if event.key == pygame.K_a:
					mon = m_p[0]
					#after you pick then the function will stop looping
					pick = False
					break
				if event.key == pygame.K_1:
					mon = m_p[0]
					pick = False
					break
				if event.key == pygame.K_2 and len(m_p) > 1:
					mon = m_p[1]
					pick = False
					break
				if event.key == pygame.K_3 and len(m_p) > 2:
					mon = m_p[2]
					pick = False
					break
				if event.key == pygame.K_4 and len(m_p) > 3:
					mon = m_p[3]
					pick = False
					break
				if event.key == pygame.K_5 and len(m_p) > 4:
					mon = m_p[4]
					pick = False
					break
				if event.key == pygame.K_6 and len(m_p) > 5:
					mon = m_p[5]
					pick = False
					break
				if event.key == pygame.K_7 and len(m_p) > 6:
					mon = m_p[6]
					pick = False
					break
				if event.key == pygame.K_8 and len(m_p) > 7:
					mon = m_p[7]
					pick = False
					break
				if event.key == pygame.K_9 and len(m_p) > 8:
					mon = m_p[8]
					pick = False
					break
	if not pick:
		pygame.event.clear()
		player_act_func.player_attack(hero, mon, h_wpn, h_amr, h_p, m_p)
		attack_text = REG_FONT.render(hero.name + " attacks " + mon.name, 1, P.RED)
		x, y = WIN.get_size()
		FOREST_IMG = pygame.transform.scale(FOREST_RAW, (x, y))
		WIN.blit(FOREST_IMG, P.ORIGIN)
		draw_func.draw_heroes(h_p, h_ally)
		draw_func.draw_monsters(m_p)
		WIN.blit(attack_text, ((P.WIDTH - attack_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.time.delay(P.SMALLDELAY)
