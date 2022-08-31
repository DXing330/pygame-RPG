import pygame
import os
import sys
import copy
import random
import draw_functions as draw_func
import gambling_games as game_func
from rpg2_constants import Constants
C = Constants()
from pygconstants import PYGConstants
P = PYGConstants()
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
clock = pygame.time.Clock()
REG_FONT = pygame.font.SysFont("comicsans", 20)
BG_RAW = pygame.image.load(os.path.join("Assets", "alley.png"))
BG_IMG = pygame.transform.scale(BG_RAW, (P.WIDTH, P.HEIGHT))
#function that will let the heroes gamble away their coins
def gambling_corner(h_bag, a_i):
	choose = True
	while choose:
		width, height = WIN.get_size()
		BG_IMG = pygame.transform.scale(BG_RAW, (width, height))
		WIN.blit(BG_IMG, P.ORIGIN)
		if a_i.srank == 0:
			ask_text = REG_FONT.render("Hey, wanna play some games and make some money?", 1, P.RED)
			WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 2))
			games_text = REG_FONT.render("We got DICE, CARDS, SLOTS, Coin FLIPS, whatever you like, it'll be fun.", 1, P.RED)
			WIN.blit(games_text, ((width - games_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				choose = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					choose = False
				if event.key == pygame.K_d:
					game_func.dice(h_bag, a_i)
				if event.key == pygame.K_c:
					game_func.cards(h_bag, a_i)
				'''if event.key == pygame.K_s:
					game_func.slots(h_bag, a_i)'''
				if event.key == pygame.K_f:
					game_func.coin_flip(h_bag, a_i)
