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
import slot_prizes as prize_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
clock = pygame.time.Clock()
REG_FONT = pygame.font.SysFont("comicsans", 25)
#function that will let you spin the slots
def spin_slots(h_bag, bet):
	spin = True
	spin1 = True
	spin2 = True
	spin3 = True
	spin4 = True
	spin5 = True
	line11 = None
	line12 = None
	line13 = None
	line14 = None
	line15 = None
	line21 = None
	line22 = None
	line23 = None
	line24 = None
	line25 = None
	line31 = None
	line32 = None
	line33 = None
	line34 = None
	line35 = None
	line41 = None
	line42 = None
	line43 = None
	line44 = None
	line45 = None
	line51 = None
	line52 = None
	line53 = None
	line54 = None
	line55 = None
	wheel = ['777', '777', '777', 'LUCK', 'LUCK', 'LUCK', 'LUCK', 'LUCK', 'LUCK',
		 'WILD', 'WILD', 'WILD', 'WILD', 'WILD', 'WILD', 'WILD', 'WILD', 'WILD',
		 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE', 'ACE',
		 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING', 'KING',
		 'KING', 'KING', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN',
		 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'QUEEN', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK',
		 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK', 'JACK',
		 'JACK', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN',
		 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'TEN', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE',
		 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE',
		 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE']
	random.shuffle(wheel)
	time = random.randint(0, len(wheel))
	while spin:
		width, height = WIN.get_size()
		time += 1
		if spin5 == False:
			spin = False
			prize_func.check_wheel(h_bag, bet, line11, line12, line13, line14, line15,
					       line21, line22, line23, line24, line25, line31, line32, line33, line34,
					       line35, line41, line42, line43, line44, line45, line51, line52, line53,
					       line54, line55) 
		if spin1 == True:
			line11 = wheel[((time+0)%len(wheel))]
			line12 = wheel[((time+1)%len(wheel))]
			line13 = wheel[((time+2)%len(wheel))]
			line14 = wheel[((time+3)%len(wheel))]
			line15 = wheel[((time+4)%len(wheel))]
			line21 = wheel[((time+0)%len(wheel))]
			line22 = wheel[((time+1)%len(wheel))]
			line23 = wheel[((time+2)%len(wheel))]
			line24 = wheel[((time+3)%len(wheel))]
			line25 = wheel[((time+4)%len(wheel))]
			line31 = wheel[((time+0)%len(wheel))]
			line32 = wheel[((time+1)%len(wheel))]
			line33 = wheel[((time+2)%len(wheel))]
			line34 = wheel[((time+3)%len(wheel))]
			line35 = wheel[((time+4)%len(wheel))]
			line41 = wheel[((time+0)%len(wheel))]
			line42 = wheel[((time+1)%len(wheel))]
			line43 = wheel[((time+2)%len(wheel))]
			line44 = wheel[((time+3)%len(wheel))]
			line45 = wheel[((time+4)%len(wheel))]
			line51 = wheel[((time+0)%len(wheel))]
			line52 = wheel[((time+1)%len(wheel))]
			line53 = wheel[((time+2)%len(wheel))]
			line54 = wheel[((time+3)%len(wheel))]
			line55 = wheel[((time+4)%len(wheel))]
		elif spin2 == True and spin1 == False:
			line21 = wheel[((time+0)%len(wheel))]
			line22 = wheel[((time+1)%len(wheel))]
			line23 = wheel[((time+2)%len(wheel))]
			line24 = wheel[((time+3)%len(wheel))]
			line25 = wheel[((time+4)%len(wheel))]
			line31 = wheel[((time+0)%len(wheel))]
			line32 = wheel[((time+1)%len(wheel))]
			line33 = wheel[((time+2)%len(wheel))]
			line34 = wheel[((time+3)%len(wheel))]
			line35 = wheel[((time+4)%len(wheel))]
			line41 = wheel[((time+0)%len(wheel))]
			line42 = wheel[((time+1)%len(wheel))]
			line43 = wheel[((time+2)%len(wheel))]
			line44 = wheel[((time+3)%len(wheel))]
			line45 = wheel[((time+4)%len(wheel))]
			line51 = wheel[((time+0)%len(wheel))]
			line52 = wheel[((time+1)%len(wheel))]
			line53 = wheel[((time+2)%len(wheel))]
			line54 = wheel[((time+3)%len(wheel))]
			line55 = wheel[((time+4)%len(wheel))]
		elif spin3 == True and spin2 == False:
			line31 = wheel[((time+0)%len(wheel))]
			line32 = wheel[((time+1)%len(wheel))]
			line33 = wheel[((time+2)%len(wheel))]
			line34 = wheel[((time+3)%len(wheel))]
			line35 = wheel[((time+4)%len(wheel))]
			line41 = wheel[((time+0)%len(wheel))]
			line42 = wheel[((time+1)%len(wheel))]
			line43 = wheel[((time+2)%len(wheel))]
			line44 = wheel[((time+3)%len(wheel))]
			line45 = wheel[((time+4)%len(wheel))]
			line51 = wheel[((time+0)%len(wheel))]
			line52 = wheel[((time+1)%len(wheel))]
			line53 = wheel[((time+2)%len(wheel))]
			line54 = wheel[((time+3)%len(wheel))]
			line55 = wheel[((time+4)%len(wheel))]
		elif spin4 == True and spin3 == False:
			line41 = wheel[((time+0)%len(wheel))]
			line42 = wheel[((time+1)%len(wheel))]
			line43 = wheel[((time+2)%len(wheel))]
			line44 = wheel[((time+3)%len(wheel))]
			line45 = wheel[((time+4)%len(wheel))]
			line51 = wheel[((time+0)%len(wheel))]
			line52 = wheel[((time+1)%len(wheel))]
			line53 = wheel[((time+2)%len(wheel))]
			line54 = wheel[((time+3)%len(wheel))]
			line55 = wheel[((time+4)%len(wheel))]
		elif spin5 == True and spin4 == False:
			line51 = wheel[((time+0)%len(wheel))]
			line52 = wheel[((time+1)%len(wheel))]
			line53 = wheel[((time+2)%len(wheel))]
			line54 = wheel[((time+3)%len(wheel))]
			line55 = wheel[((time+4)%len(wheel))]
		WIN.fill(P.BLACK)
		#draw every part in it's own section of the screen
		wheel11_text = REG_FONT.render(str(line11), 1, P.RED)
		WIN.blit(wheel11_text, ((width - wheel11_text.get_width())//2 - (P.PADDING * 6), height//2 + (P.PADDING * 2)))
		wheel12_text = REG_FONT.render(str(line12), 1, P.RED)
		WIN.blit(wheel12_text, ((width - wheel12_text.get_width())//2 - (P.PADDING * 6), height//2 + (P.PADDING * 1)))
		wheel13_text = REG_FONT.render(str(line13), 1, P.RED)
		WIN.blit(wheel13_text, ((width - wheel13_text.get_width())//2 - (P.PADDING * 6), height//2 + (P.PADDING * 0)))
		wheel14_text = REG_FONT.render(str(line14), 1, P.RED)
		WIN.blit(wheel14_text, ((width - wheel14_text.get_width())//2 - (P.PADDING * 6), height//2 - (P.PADDING * 1)))
		wheel15_text = REG_FONT.render(str(line15), 1, P.RED)
		WIN.blit(wheel15_text, ((width - wheel15_text.get_width())//2 - (P.PADDING * 6), height//2 - (P.PADDING * 2)))
		wheel21_text = REG_FONT.render(str(line21), 1, P.RED)
		WIN.blit(wheel21_text, ((width - wheel21_text.get_width())//2 - (P.PADDING * 3), height//2 + (P.PADDING * 2)))
		wheel22_text = REG_FONT.render(str(line22), 1, P.RED)
		WIN.blit(wheel22_text, ((width - wheel22_text.get_width())//2 - (P.PADDING * 3), height//2 + (P.PADDING * 1)))
		wheel23_text = REG_FONT.render(str(line23), 1, P.RED)
		WIN.blit(wheel23_text, ((width - wheel23_text.get_width())//2 - (P.PADDING * 3), height//2 + (P.PADDING * 0)))
		wheel24_text = REG_FONT.render(str(line24), 1, P.RED)
		WIN.blit(wheel24_text, ((width - wheel24_text.get_width())//2 - (P.PADDING * 3), height//2 - (P.PADDING * 1)))
		wheel25_text = REG_FONT.render(str(line25), 1, P.RED)
		WIN.blit(wheel25_text, ((width - wheel25_text.get_width())//2 - (P.PADDING * 3), height//2 - (P.PADDING * 2)))
		wheel31_text = REG_FONT.render(str(line31), 1, P.RED)
		WIN.blit(wheel31_text, ((width - wheel31_text.get_width())//2 - (P.PADDING * 0), height//2 + (P.PADDING * 2)))
		wheel32_text = REG_FONT.render(str(line32), 1, P.RED)
		WIN.blit(wheel32_text, ((width - wheel32_text.get_width())//2 - (P.PADDING * 0), height//2 + (P.PADDING * 1)))
		wheel33_text = REG_FONT.render(str(line33), 1, P.RED)
		WIN.blit(wheel33_text, ((width - wheel33_text.get_width())//2 - (P.PADDING * 0), height//2 + (P.PADDING * 0)))
		wheel34_text = REG_FONT.render(str(line34), 1, P.RED)
		WIN.blit(wheel34_text, ((width - wheel34_text.get_width())//2 - (P.PADDING * 0), height//2 - (P.PADDING * 1)))
		wheel35_text = REG_FONT.render(str(line35), 1, P.RED)
		WIN.blit(wheel35_text, ((width - wheel35_text.get_width())//2 - (P.PADDING * 0), height//2 - (P.PADDING * 2)))
		wheel41_text = REG_FONT.render(str(line41), 1, P.RED)
		WIN.blit(wheel41_text, ((width - wheel41_text.get_width())//2 + (P.PADDING * 3), height//2 + (P.PADDING * 2)))
		wheel42_text = REG_FONT.render(str(line42), 1, P.RED)
		WIN.blit(wheel42_text, ((width - wheel42_text.get_width())//2 + (P.PADDING * 3), height//2 + (P.PADDING * 1)))
		wheel43_text = REG_FONT.render(str(line43), 1, P.RED)
		WIN.blit(wheel43_text, ((width - wheel43_text.get_width())//2 + (P.PADDING * 3), height//2 + (P.PADDING * 0)))
		wheel44_text = REG_FONT.render(str(line44), 1, P.RED)
		WIN.blit(wheel44_text, ((width - wheel44_text.get_width())//2 + (P.PADDING * 3), height//2 - (P.PADDING * 1)))
		wheel45_text = REG_FONT.render(str(line45), 1, P.RED)
		WIN.blit(wheel45_text, ((width - wheel45_text.get_width())//2 + (P.PADDING * 3), height//2 - (P.PADDING * 2)))
		wheel51_text = REG_FONT.render(str(line51), 1, P.RED)
		WIN.blit(wheel51_text, ((width - wheel51_text.get_width())//2 + (P.PADDING * 6), height//2 + (P.PADDING * 2)))
		wheel52_text = REG_FONT.render(str(line52), 1, P.RED)
		WIN.blit(wheel52_text, ((width - wheel52_text.get_width())//2 + (P.PADDING * 6), height//2 + (P.PADDING * 1)))
		wheel53_text = REG_FONT.render(str(line53), 1, P.RED)
		WIN.blit(wheel53_text, ((width - wheel53_text.get_width())//2 + (P.PADDING * 6), height//2 + (P.PADDING * 0)))
		wheel54_text = REG_FONT.render(str(line54), 1, P.RED)
		WIN.blit(wheel54_text, ((width - wheel54_text.get_width())//2 + (P.PADDING * 6), height//2 - (P.PADDING * 1)))
		wheel55_text = REG_FONT.render(str(line55), 1, P.RED)
		WIN.blit(wheel55_text, ((width - wheel55_text.get_width())//2 + (P.PADDING * 6), height//2 - (P.PADDING * 2)))
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
					random.shuffle(wheel)
				elif spin1 == False and spin2 == True:
					spin2 = False
					random.shuffle(wheel)
				elif spin2 == False and spin3 == True:
					spin3 = False
					random.shuffle(wheel)
				elif spin3 == False and spin4 == True:
					spin4 = False
					random.shuffle(wheel)
				elif spin4 == False and spin5 == True:
					spin5 = False
#slot machine function
def slots(h_bag, bet):
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("COINS: "+str(h_bag.coins)+" BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		options_text = REG_FONT.render("SPIN/LEAVE", 1, P.RED)
		WIN.blit(options_text, ((width - options_text.get_width())//2, P.PADDING * 3))
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
					h_bag.coins -= bet
					spin_slots(h_bag, bet)

#free spins on the slot machine
def free_slots(h_bag, bet, free):
        fspin = free
        game = True
        while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("COINS: "+str(h_bag.coins)+" BET: "+str(bet), 1, P.GREEN)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		free_text = REG_FONT.render("FREE SPINS: "+str(fspin), 1, P.GREEN)
		WIN.blit(free_text, ((width - free_text.get_width())//2, P.PADDING * 3))
		options_text = REG_FONT.render("SPIN", 1, P.GREEN)
		WIN.blit(options_text, ((width - options_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		if fspin <= 0:
                        game = False
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
					fspin -= 1
					spin_slots(h_bag, bet)
