import pygame
import os
import sys
sys.path.append(".")
pygame.font.init()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
#function that will pick from a list
def pick_hero(h_p):
	pick = True
	thing = None
	while pick:
		if len(h_p) > 1:
			WIN.fill(P.WHITE)
			x = 1
			for hero in h_p:
				hero_text = REG_FONT.render(str(x)+" : "+hero.name, 1, P.BLACK)
				WIN.blit(hero_text, ((P.WIDTH - hero_text.get_width())//2, P.PADDING * x))
				x += 1
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					pygame.event.clear()
					if event.key == pygame.K_1:
						thing = h_p[0]
						pick = False
					if event.key == pygame.K_2 and len(h_p) > 1:
						thing = h_p[1]
						pick = False
					if event.key == pygame.K_3 and len(h_p) > 2:
						thing = h_p[2]
						pick = False
					if event.key == pygame.K_4 and len(h_p) > 3:
						thing = h_p[3]
						pick = False
					if event.key == pygame.K_5 and len(h_p) > 4:
						thing = h_p[4]
						pick = False
					if event.key == pygame.K_6 and len(h_p) > 5:
						thing = h_p[5]
						pick = False
					if event.key == pygame.K_7 and len(h_p) > 6:
						thing = h_p[6]
						pick = False
					if event.key == pygame.K_8 and len(h_p) > 7:
						thing = h_p[7]
						pick = False
					if event.key == pygame.K_9 and len(h_p) > 8:
						thing = h_p[8]
						pick = False
					
		elif len(h_p) == 1:
			thing = h_p[0]
			pick = False
	if not pick:
		return thing
