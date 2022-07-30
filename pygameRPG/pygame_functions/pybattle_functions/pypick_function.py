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
	width, height = WIN.get_size()
	while pick:
		if len(h_p) == 1:
			thing = h_p[0]
			pick = False
		elif 1 < len(h_p) <= 9:
			WIN.fill(P.WHITE)
			x = 1
			for hero in h_p:
				hero_text = REG_FONT.render(str(x)+" : "+hero.name, 1, P.BLACK)
				WIN.blit(hero_text, ((width - hero_text.get_width())//2, P.PADDING * x))
				x += 1
			pygame.display.update()
		elif 9 < len(h_p):
			WIN.fill(P.WHITE)
			x = 1
			y = 1
			z = 1
			help_text = REG_FONT.render("a = 10, b = 11, etc. ", 1, P.RED)
			WIN.blit(help_text, ((width - help_text.get_width())//2, 0))
			for hero in h_p:
				hero_text = REG_FONT.render(str(z)+" : "+hero.name, 1, P.BLACK)
				WIN.blit(hero_text, (P.PADDING * y, P.PADDING * x))
				x += 1
				z += 1
				if x * P.PADDING > height - (P.PADDING * 2):
					x = 1
					y += (width//P.PADDING)//3
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
				if event.key == pygame.K_a and len(h_p) > 9:
					thing = h_p[9]
					pick = False
				if event.key == pygame.K_b and len(h_p) > 10:
					thing = h_p[10]
					pick = False
				if event.key == pygame.K_c and len(h_p) > 11:
					thing = h_p[11]
					pick = False
				if event.key == pygame.K_d and len(h_p) > 12:
					thing = h_p[12]
					pick = False
				if event.key == pygame.K_e and len(h_p) > 13:
					thing = h_p[13]
					pick = False
				if event.key == pygame.K_f and len(h_p) > 14:
					thing = h_p[14]
					pick = False
				if event.key == pygame.K_g and len(h_p) > 15:
					thing = h_p[15]
					pick = False
				if event.key == pygame.K_h and len(h_p) > 16:
					thing = h_p[16]
					pick = False
				if event.key == pygame.K_i and len(h_p) > 17:
					thing = h_p[17]
					pick = False
				if event.key == pygame.K_j and len(h_p) > 18:
					thing = h_p[18]
					pick = False
				if event.key == pygame.K_k and len(h_p) > 19:
					thing = h_p[19]
					pick = False
				if event.key == pygame.K_l and len(h_p) > 20:
					thing = h_p[20]
					pick = False
				if event.key == pygame.K_m and len(h_p) > 21:
					thing = h_p[21]
					pick = False
				if event.key == pygame.K_n and len(h_p) > 22:
					thing = h_p[22]
					pick = False
				if event.key == pygame.K_o and len(h_p) > 23:
					thing = h_p[23]
					pick = False
				if event.key == pygame.K_p and len(h_p) > 24:
					thing = h_p[24]
					pick = False
				if event.key == pygame.K_q and len(h_p) > 25:
					thing = h_p[25]
					pick = False
				if event.key == pygame.K_r and len(h_p) > 26:
					thing = h_p[26]
					pick = False
				if event.key == pygame.K_s and len(h_p) > 27:
					thing = h_p[27]
					pick = False
				if event.key == pygame.K_t and len(h_p) > 28:
					thing = h_p[28]
					pick = False
				if event.key == pygame.K_u and len(h_p) > 29:
					thing = h_p[29]
					pick = False
				if event.key == pygame.K_v and len(h_p) > 30:
					thing = h_p[30]
					pick = False
				if event.key == pygame.K_w and len(h_p) > 31:
					thing = h_p[31]
					pick = False
				if event.key == pygame.K_x and len(h_p) > 32:
					thing = h_p[32]
					pick = False
				if event.key == pygame.K_y and len(h_p) > 33:
					thing = h_p[33]
					pick = False
				if event.key == pygame.K_z and len(h_p) > 34:
					thing = h_p[34]
					pick = False

					
	if not pick:
		return thing
