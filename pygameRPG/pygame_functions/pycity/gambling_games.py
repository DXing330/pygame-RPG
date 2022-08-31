import pygame
pygame.init()
import os
import sys
import copy
import random
import math
import draw_functions as draw_func
import card_games as card_func
import slot_games as slot_func
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
TABLE_TOP = pygame.transform.scale(TABLE_RAW, (TABLE_RAW.get_width() * 2, TABLE_RAW.get_width() * 2))
COIN_HEAD_RAW = pygame.image.load(os.path.join("Assets", "coin_head.png"))
COIN_HEAD = pygame.transform.scale(COIN_HEAD_RAW, (P.BIG_SPRITE//2, P.BIG_SPRITE//2))
COIN_TAIL_RAW = pygame.image.load(os.path.join("Assets", "coin_tail.png"))
COIN_TAIL = pygame.transform.scale(COIN_TAIL_RAW, (P.BIG_SPRITE//2, P.BIG_SPRITE//2))
DICE_1_RAW = pygame.image.load(os.path.join("Assets", "dice1.png"))
DICE_2_RAW = pygame.image.load(os.path.join("Assets", "dice2.png"))
DICE_3_RAW = pygame.image.load(os.path.join("Assets", "dice3.png"))
DICE_4_RAW = pygame.image.load(os.path.join("Assets", "dice4.png"))
DICE_5_RAW = pygame.image.load(os.path.join("Assets", "dice5.png"))
DICE_6_RAW = pygame.image.load(os.path.join("Assets", "dice6.png"))
#function that explains the rules of the game
def slot_rules():
	width, height = WIN.get_size()
	explain = True
	WIN.fill(P.BLACK)
	text = REG_FONT.render("You can bet as much as you want in increments of 10 coins.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 2))
	text = REG_FONT.render("It costs your bet to spin the wheels.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 3))
	text = REG_FONT.render("Stop the wheels whenever you want.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 4))
	text = REG_FONT.render("If a pattern lines up then you win.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 5))
	text = REG_FONT.render("Some patterns will win more than others.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 6))
	pygame.display.update()
	while explain:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				explain = False
#takes the player's bet
def slot_bet(h_bag):
	bet = 10
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("CURRENT BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If you want to bet more then RAISE, if not then STOP.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_r]:
			if (bet + 10) <= h_bag.coins:
				bet += 10
			else:
				game = False
				slot_func.slots(h_bag, bet)
		if keys[pygame.K_s]:
			game = False
			slot_func.slots(h_bag, bet)
#slot machine
def slots(h_bag, a_i):
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		coins_text = REG_FONT.render("COINS: "+str(h_bag.coins), 1, P.RED)
		WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If its your first time here, someone else can explain the RULES.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		ask_text = REG_FONT.render("Do you want to PLAY? Minimum bet is 10 coins.", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					game = False
					break
				if event.key == pygame.K_r:
					slot_rules()
				if event.key == pygame.K_p:
					slot_bet(h_bag)
#takes the player's bet
def cards_bet(h_bag):
	bet = 100
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("CURRENT BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If you want to bet more then RAISE, if not then STOP.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_r]:
			if (bet + 100) <= h_bag.coins:
				bet += 100
			else:
				game = False
				card_func.card_game(h_bag, bet)
		if keys[pygame.K_s]:
			game = False
			card_func.card_game(h_bag, bet)
#function that explains the rules of the game
def cards_rules():
	width, height = WIN.get_size()
	explain = True
	WIN.fill(P.BLACK)
	text = REG_FONT.render("You can bet as much as you want in increments of 100 coins.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 2))
	text = REG_FONT.render("You'll play against the dealer, closest to 21 points wins, if you go over then you lose.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 3))
	text = REG_FONT.render("Cards have value equal to their number, except A is worth 1 or 11 also J, Q, K are worth 10.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 4))
	text = REG_FONT.render("Everyone starts with two cards, you can get more if you want as long as you don't go over 21 points.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 5))
	text = REG_FONT.render("The dealer will stop if he has 17 points of value.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 6))
	pygame.display.update()
	while explain:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				explain = False
#function that will let the player play a knockoff version of blackjack
def cards(h_bag, a_i):
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		coins_text = REG_FONT.render("COINS: "+str(h_bag.coins), 1, P.RED)
		WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If its your first time here, someone else can explain the RULES.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		ask_text = REG_FONT.render("Do you want to PLAY? Minimum bet is 100 coins.", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					game = False
					break
				if event.key == pygame.K_r:
					cards_rules()
				if event.key == pygame.K_p:
					cards_bet(h_bag)
#function that explains the rules of the dice game
def dice_rules():
	width, height = WIN.get_size()
	explain = True
	WIN.fill(P.BLACK)
	text = REG_FONT.render("You can bet as much as you want in increments of 100 coins.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 2))
	text = REG_FONT.render("If you bet on EVENS or ODDS the payout is the same as the bet.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 3))
	text = REG_FONT.render("If you bet on BIGS you win on 4 5 or 6, payout is the same as bet.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 4))
	text = REG_FONT.render("If you bet on SMALLS you win on 1 2 or 3, payout is the same as bet.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 5))
	text = REG_FONT.render("If you bet on SINGLES you win on that roll, payout is much bigger.", 1, P.RED)
	WIN.blit(text, ((width - text.get_width())//2, P.PADDING * 6))
	pygame.display.update()
	while explain:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				explain = False
#function that takes the amount and another function that takes type of the player's bet
def dice_bet_type(h_bag, bet):
	win = None
	bigwin = None
	game = True
	wide = 0
	high = 0
	dice_img = pygame.transform.scale(DICE_6_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		WIN.blit(dice_img, ((width - dice_img.get_width())//2 + wide,
				    (height - dice_img.get_height())//2 + high))
		bet_text = REG_FONT.render("COINS: "+str(h_bag.coins)+" BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		ask_text = REG_FONT.render("What do you want to bet on?", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 3))
		options_text = REG_FONT.render("EVENS/ODDS/BIGS/SMALLS/SINGLES[1,2,3,4,5,6]", 1, P.RED)
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
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					game = False
					break
				#as long as they make a proper bet the dice will roll
				if event.key == pygame.K_e or event.key == pygame.K_o or event.key == pygame.K_b or event.key == pygame.K_s or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6:
					roll = random.randint(1, 6)
					if roll == 1:
						dice_img = pygame.transform.scale(DICE_1_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					if roll == 2:
						dice_img = pygame.transform.scale(DICE_2_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					if roll == 3:
						dice_img = pygame.transform.scale(DICE_3_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					if roll == 4:
						dice_img = pygame.transform.scale(DICE_4_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					if roll == 5:
						dice_img = pygame.transform.scale(DICE_5_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					if roll == 6:
						dice_img = pygame.transform.scale(DICE_6_RAW, (P.BIG_SPRITE//3, P.BIG_SPRITE//3))
					rotate = random.randint(1, 90)
					dice_img = pygame.transform.rotate(dice_img, rotate)
					wide = random.randint(-TABLE_TOP.get_width()//4, TABLE_TOP.get_width()//4)
					high = random.randint(-TABLE_TOP.get_height()//4, TABLE_TOP.get_height()//4)
					if event.key == pygame.K_e:
						if roll == 2 or roll == 4 or roll == 6:
							h_bag.coins += bet
							win = True
						else:
							h_bag.coins -= bet
							win = False
					elif event.key == pygame.K_o:
						if roll == 2 or roll == 4 or roll == 6:
							h_bag.coins -= bet
							win = False
						else:
							h_bag.coins += bet
							win = True
					elif event.key == pygame.K_b:
						if roll == 4 or roll == 5 or roll == 6:
							h_bag.coins += bet
							win = True
						else:
							h_bag.coins -= bet
							win = False
					elif event.key == pygame.K_s:
						if roll == 4 or roll == 5 or roll == 6:
							h_bag.coins -= bet
							win = False
						else:
							h_bag.coins += bet
							win = True
					elif event.key == pygame.K_1:
						if roll == 1:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
					elif event.key == pygame.K_2:
						if roll == 2:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
					elif event.key == pygame.K_3:
						if roll == 3:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
					elif event.key == pygame.K_4:
						if roll == 4:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
					elif event.key == pygame.K_5:
						if roll == 5:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
					elif event.key == pygame.K_6:
						if roll == 6:
							h_bag.coins += bet * 4.9
							bigwin = True
						else:
							h_bag.coins -= bet
							bigwin = False
				WIN.fill(P.BLACK)
				WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
						     (height - TABLE_TOP.get_height())//2))
				WIN.blit(dice_img, ((width - dice_img.get_width())//2 + wide,
						    (height - dice_img.get_height())//2 + high))
				if win == True:
					result_text = REG_FONT.render("Lucky you.", 1, P.GREEN)
					win = None
				if win == False:
					result_text = REG_FONT.render("Better luck next time.", 1, P.RED)
					win = None
				if bigwin == True:
					result_text = REG_FONT.render("Save some luck for the rest of us.", 1, P.GREEN)
					bigwin = None
				if bigwin == False:
					result_text = REG_FONT.render("Better luck next time.", 1, P.RED)
					bigwin = None
				WIN.blit(result_text, ((width - result_text.get_width())//2, P.PADDING * 2))
				pygame.display.update()
				pygame.time.delay(500)
def dice_bet(h_bag):
	bet = 100
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		bet_text = REG_FONT.render("CURRENT BET: "+str(bet), 1, P.RED)
		WIN.blit(bet_text, ((width - bet_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If you want to bet more then RAISE, if not then STOP.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_r]:
			if (bet + 100) <= h_bag.coins:
				bet += 100
			else:
				game = False
				dice_bet_type(h_bag, bet)
		if keys[pygame.K_s]:
			game = False
			dice_bet_type(h_bag, bet)
#dice roller simulation, slightly balanced in the house's favor
def dice(h_bag, a_i):
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		coins_text = REG_FONT.render("COINS: "+str(h_bag.coins), 1, P.RED)
		WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("If its your first time here, someone else can explain the RULES.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		ask_text = REG_FONT.render("Do you want to PLAY? Minimum bet is 100 coins.", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 4))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					game = False
					break
				if event.key == pygame.K_r:
					dice_rules()
				if event.key == pygame.K_p:
					dice_bet(h_bag)
#coin flip simulation, slightly rigged at bigger bets
def coin_flip_odds(h_bag):
	odds = 500
	if h_bag.coins >= 1000:
		odds -= round(50 * math.log10(h_bag.coins/100))
	if odds <= 0:
		odds = 250
	return odds
def coin_flip(h_bag, a_i):
	coin_img = COIN_HEAD
	game = True
	while game:
		width, height = WIN.get_size()
		WIN.fill(P.BLACK)
		WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
				     (height - TABLE_TOP.get_height())//2))
		WIN.blit(coin_img, ((width - coin_img.get_width())//2,
				    (height - coin_img.get_height())//2))
		coins_text = REG_FONT.render("COINS: "+str(h_bag.coins), 1, P.RED)
		WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 2))
		rules_text = REG_FONT.render("Simple rules, heads you win, tails you lose.", 1, P.RED)
		WIN.blit(rules_text, ((width - rules_text.get_width())//2, P.PADDING * 3))
		ask_text = REG_FONT.render("How much you want to bet? MINIMUM is 100 coins.", 1, P.RED)
		WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 4))
		option_text = REG_FONT.render("You can also bet a THOUSAND, HALF, or ALL your coins."
					      , 1, P.RED)
		WIN.blit(option_text, ((width - option_text.get_width())//2, P.PADDING * 5))
		pygame.display.update()
		pygame.event.clear()
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					game = False
					break
				if event.key == pygame.K_m:
					pygame.event.clear()
					if h_bag.coins >= 100:
						WIN.fill(P.BLACK)
						WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
								     (height - TABLE_TOP.get_height())//2))
						coin = random.randint(0, 1)
						if coin == 0:
							coin_img = COIN_HEAD
							h_bag.coins += 100
							result_text = REG_FONT.render("Lucky you.", 1, P.GREEN) 
						elif coin == 1:
							coin_img = COIN_TAIL
							h_bag.coins -= 100
							result_text = REG_FONT.render("Too bad, you lose this time."
										      , 1, P.RED)
						WIN.blit(coin_img, ((width - coin_img.get_width())//2,
								    (height - coin_img.get_height())//2))
						WIN.blit(result_text, ((width - result_text.get_width())//2, P.PADDING * 2))
						pygame.display.update()
						pygame.time.delay(250)
						
					elif h_bag.coins < 100:
						WIN.blit(BG_IMG, P.ORIGIN)
						poor_text = REG_FONT.render("Looks like you're out, better luck next time.", 1, P.RED)
						WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING * 2))
						pygame.display.update()
						pygame.time.delay(1000)
						game = False
						break
					
				if event.key == pygame.K_t:
					pygame.event.clear()
					if h_bag.coins >= 1000:
						WIN.fill(P.BLACK)
						WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
								     (height - TABLE_TOP.get_height())//2))
						coin = random.randint(1, 100)
						if coin <= 45:
							coin_img = COIN_HEAD
							h_bag.coins += 1000
							result_text = REG_FONT.render("You're pretty lucky.", 1, P.GREEN) 
						elif coin > 45:
							coin_img = COIN_TAIL
							h_bag.coins -= 1000
							result_text = REG_FONT.render("Too bad, you lose this time."
										      , 1, P.RED)
						WIN.blit(coin_img, ((width - coin_img.get_width())//2,
								    (height - coin_img.get_height())//2))
						WIN.blit(result_text, ((width - result_text.get_width())//2, P.PADDING * 2))
						pygame.display.update()
						pygame.time.delay(500)
					elif h_bag.coins < 1000:
						WIN.blit(BG_IMG, P.ORIGIN)
						poor_text = REG_FONT.render("Go back to the low roller table, you pauper.", 1, P.RED)
						WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING * 2))
						pygame.display.update()
						pygame.time.delay(500)

					
				if event.key == pygame.K_h:
					pygame.event.clear()
					WIN.fill(P.BLACK)
					WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
							     (height - TABLE_TOP.get_height())//2))
					coin = random.randint(1, 1000)
					odds = coin_flip_odds(h_bag)
					if coin <= odds:
						coin_img = COIN_HEAD
						h_bag.coins += h_bag.coins//2
						result_text = REG_FONT.render("I guess you should've gone all in instead.", 1, P.GREEN) 
					elif coin > odds:
						coin_img = COIN_TAIL
						h_bag.coins -= h_bag.coins//2
						result_text = REG_FONT.render("Ouch, well at least you still have some coins left."
									      , 1, P.RED)
					WIN.blit(coin_img, ((width - coin_img.get_width())//2,
							    (height - coin_img.get_height())//2))
					WIN.blit(result_text, ((width - result_text.get_width())//2, P.PADDING * 2))
					pygame.display.update()
					pygame.time.delay(500)
					
				if event.key == pygame.K_a:
					pygame.event.clear()
					WIN.fill(P.BLACK)
					WIN.blit(TABLE_TOP, ((width - TABLE_TOP.get_width())//2,
							     (height - TABLE_TOP.get_height())//2))
					coin = random.randint(1, 1000)
					odds = coin_flip_odds(h_bag)
					if coin <= odds:
						coin_img = COIN_HEAD
						h_bag.coins += h_bag.coins
						result_text = REG_FONT.render("Wanna try again? You seem like you're on a hot streak.",
									      1, P.GREEN) 
					elif coin > odds:
						coin_img = COIN_TAIL
						h_bag.coins -= h_bag.coins
						result_text = REG_FONT.render("Unlucky, but it could've gone either way."
									      , 1, P.RED)
					WIN.blit(coin_img, ((width - coin_img.get_width())//2,
							    (height - coin_img.get_height())//2))
					WIN.blit(result_text, ((width - result_text.get_width())//2, P.PADDING * 2))
					pygame.display.update()
					pygame.time.delay(1000)

