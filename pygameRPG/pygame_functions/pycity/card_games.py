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
BG_RAW = pygame.image.load(os.path.join("Assets", "alley.png"))
BG_IMG = pygame.transform.scale(BG_RAW, (P.WIDTH, P.HEIGHT))
TABLE_RAW = pygame.image.load(os.path.join("Assets", "table_top.png"))
TABLE_TOP = pygame.transform.scale(TABLE_RAW, (TABLE_RAW.get_width() * 1.5, TABLE_RAW.get_width() * 1.5))
#function that will give cards to the player
def random_card(card_deck):
	#pick a random card from the deck
	num = random.randint(0, len(card_deck) - 1)
	card = card_deck[num]
	#remove that card from the deck
	card_deck.remove(card)
	#give that card to whoever
	return card
#function that will reveal the value of a card in the dealer's hand
def get_card(hand):
	card = hand[0]
	return card
#function that will calculate the value of the player's hand
def get_value(hand):
	value = 0
	#get the value of non-"A" cards first
	for card in hand:
		if card != "A":
			if card == "J" or card == "Q" or card == "K":
				value += 10
			else:
				value += int(card)
	#then add the value of "A" cards
	for card in hand:
		if card == "A":
			if value + 11 <= 21:
				value += 11
			else:
				value += 1
	return value
			
#function that acts like blackjack
def card_game(h_bag, bet):
	card_deck = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
		     '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7',
		     '8', '8', '8', '8','9', '9', '9', '9', '10', '10', '10', '10',
		     'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
	player_hand = []
	dealer_hand = []
	player_card_one = random_card(card_deck)
	player_card_two = random_card(card_deck)
	player_hand.append(player_card_one)
	player_hand.append(player_card_two)
	dealer_card_one = random_card(card_deck)
	dealer_card_two = random_card(card_deck)
	dealer_hand.append(dealer_card_one)
	dealer_hand.append(dealer_card_two)
	game = True
	check = False
	again = False
	while game:
		value = get_value(player_hand)
		dcard = get_card(dealer_hand)
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		bet_text = REG_FONT.render("COINS: "+str(h_bag.coins)+" BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		value_text = REG_FONT.render("HAND VALUE: "+str(value), 1, P.RED)
		WIN.blit(value_text, ((width - value_text.get_width())//2, P.PADDING * 3))
		hand_text = REG_FONT.render(str(player_hand), 1, P.RED)
		WIN.blit(hand_text, ((width - hand_text.get_width())//2, P.PADDING * 4))
		dealer_card = REG_FONT.render("DEALER CARD: "+str(dcard) , 1, P.RED)
		WIN.blit(dealer_card, ((width - dealer_card.get_width())//2, P.PADDING * 5))
		options_text = REG_FONT.render("HIT/STAND", 1, P.RED)
		WIN.blit(options_text, ((width - options_text.get_width())//2, P.PADDING * 6))
		pygame.display.update()
		pygame.time.delay(500)
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
		#if the player busts then the game ends
		if value > 21:
			game = False
			again = True
			h_bag.coins -= bet
			WIN.fill(P.BLACK)
			end_text = REG_FONT.render("Looks like you bust.", 1, P.RED)
			WIN.blit(end_text, ((width - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(1000)
		#if the player gets blackjack then they win
		if value == 21 and len(player_hand) == 2:
			game = False
			again = True
			h_bag.coins += bet * 1.5
			WIN.fill(P.BLACK)
			end_text = REG_FONT.render("Lucky you, a perfect hand.", 1, P.RED)
			WIN.blit(end_text, ((width - end_text.get_width())//2, P.PADDING * 2))
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
				if event.key == pygame.K_h:
					card = random_card(card_deck)
					player_hand.append(card)
				#stand means the player stops getting cards and compares against the dealer
				if event.key == pygame.K_s:
					game = False
					check = True
	while check:
		value = get_value(player_hand)
		dvalue = get_value(dealer_hand)
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		value_text = REG_FONT.render("VALUE: "+str(value), 1, P.RED)
		WIN.blit(value_text, ((width - value_text.get_width())//2, P.PADDING * 3))
		dvalue_text = REG_FONT.render("VALUE: "+str(dvalue), 1, P.RED)
		WIN.blit(dvalue_text, ((width - dvalue_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.time.delay(500)
		if value > 21:
			check = False
			again = True
			h_bag.coins -= bet
			break
		while dvalue < 17:
			card = random_card(card_deck)
			dealer_hand.append(card)
			dvalue = get_value(dealer_hand)
			WIN.fill(P.BLACK)
			WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
					     (height - TABLE_TOP.get_height())//2))
			value_text = REG_FONT.render("VALUE: "+str(value), 1, P.RED)
			WIN.blit(value_text, ((width - value_text.get_width())//2, P.PADDING * 3))
			dvalue_text = REG_FONT.render("VALUE: "+str(dvalue), 1, P.RED)
			WIN.blit(dvalue_text, ((width - dvalue_text.get_width())//2, P.PADDING * 4))
			pygame.display.update()
			pygame.time.delay(500)
		if dvalue > 21 or dvalue < value:
			check = False
			again = True
			h_bag.coins += bet
			WIN.fill(P.BLACK)
			end_text = REG_FONT.render("You win this time.", 1, P.RED)
			WIN.blit(end_text, ((width - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(500)
		if dvalue <= 21 and dvalue > value:
			check = False
			again = True
			h_bag.coins -= bet
			WIN.fill(P.BLACK)
			end_text = REG_FONT.render("You lose this time.", 1, P.RED)
			WIN.blit(end_text, ((width - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(500)
		if dvalue <= 21 and dvalue == value:
			check = False
			again = True
			WIN.fill(P.BLACK)
			end_text = REG_FONT.render("It's a draw this time.", 1, P.RED)
			WIN.blit(end_text, ((width - end_text.get_width())//2, P.PADDING * 2))
			pygame.display.update()
			pygame.time.delay(500)
			
	while again:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		ask_text = REG_FONT.render("PLAY AGAIN/LEAVE", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.event.clear()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					again = False
				if event.key == pygame.K_p or event.key == pygame.K_a:
					card_game(h_bag, bet)
