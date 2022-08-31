import pygame
pygame.init()
import os
import sys
import copy
import random
import math
sys.path.append("../pygame_functions/pygame_general_functions")
sys.path.append("../pygame_functions")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
from rpg2_constants import Constants
C = Constants()
from pygconstants import PYGConstants
P = PYGConstants()
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
clock = pygame.time.Clock()
REG_FONT = pygame.font.SysFont("comicsans", 25)
#function that will determine what prize you get
def get_prize(h_bag, bet, jackpot, line1, line2, line3):
	if line1 == line2 == line3:
		if line1 == "777":
		h_bag.coins += jackpot
		elif line1 == "LUCK":
			h_bag.coins += bet * 20
		elif line1 == "WILD":
			h_bag.coins += bet * 10
		elif line1 == "Free":
			h_bag.coins += bet * 2
		elif line1 == "Jack":
			h_bag.coins += bet * 3
		elif line1 == "Queen":
			h_bag.coins += bet * 4
		elif line1 == "King":
			h_bag.coins += bet * 5
		elif line1 == "Ace":
			h_bag.coins += bet * 10
#function that will let you spin the slots
def spin_slots(h_bag, bet, jackpot):
	time = 0
	spin = True
	spin1 = True
	spin2 = True
	spin3 = True
	line1 = None
	line2 = None
	line3 = None
	wheel = ["777", "LUCK", "WILD", "Free", "Jack", "Queen", "King", "Ace", "Free", "Free"]
	while spin:
		width, heigth = WIN.get_size()
		time += 1
		if spin3 == False:
			spin = False
			get_prize(h_bag, bet, jackpot, line1, line2, line3)
		if spin1 == True:
			line1 = wheel[(time%len(wheel))]
			line2 = wheel[((time*3)%len(wheel))]
			line2 = wheel[((time*3)%len(wheel))]
		if spin2 == True and spin1 == False:
			line2 = wheel[((time*1)%len(wheel))]
			line2 = wheel[((time*3)%len(wheel))]
		if spin3 == True and spin2 == False:
			line2 = wheel[((time*1)%len(wheel))]
		wheel_text = REG_FONT.render(str(line1)+" "+str(line2)+" "+str(line3), 1, P.RED)
		WIN.blit(wheel_text, ((width - wheel_text.get_width())//2, height//2 - wheel_text.get_height()))
		pygame.display.update()
		clock.tick(15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if spin1 == True:
					spin1 = False
				elif spin1 == False and spin2 == True:
					spin2 = False
				elif spin2 == False and spin3 == True:
					spin3 = False
#slot machine function
def slots(h_bag, bet):
	jackpot = bet * 100
	game = True
	while game:
		width, heigth = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("COINS: "+str(h_bag.coins)+" BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		value_text = REG_FONT.render("JACKPOT VALUE: "+str(jackpot), 1, P.RED)
		WIN.blit(value_text, ((width - value_text.get_width())//2, P.PADDING * 3))
		options_text = REG_FONT.render("SPIN/LEAVE", 1, P.RED)
		WIN.blit(options_text, ((width - options_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		if h_bag.coins < bet:
			game = False
			WIN.fill(P.BLACK)
			poor_text = REG_FONT.render("Looks like you're out of luck for now, come back anytime.", 1, P.RED)
			WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				#hits means the player gets another card
				if event.key == pygame.K_l:
					game = False
				#stand means the player stops getting cards and compares against the dealer
				if event.key == pygame.K_s:
					pygame.event.clear()
					spin_slots(h_bag, bet, jackpot)
					jackpot += bet

