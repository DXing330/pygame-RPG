import pygame
import os
import sys
sys.path.append("../../pygameRPG/Assets")
from pygconstants import PYGConstants
P = PYGConstants()
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
x, y = WIN.get_size()
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 24)
#always make a clock
clock = pygame.time.Clock()
ROAD_RAW = pygame.image.load(os.path.join("Assets", "roadside.png"))
ROAD_IMG = pygame.transform.scale(ROAD_RAW, (P.WIDTH, P.HEIGHT))
def explain_guild():
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	explain_text1 = REG_FONT.render("The hunter's guild?", 1, P.BLACK)
	explain_text2 = REG_FONT.render("You must be skilled if they let you join them.", 1, P.BLACK)
	explain_text3 = REG_FONT.render("They're a group of strong people working together to fight monsters.", 1, P.BLACK)
	explain_text4 = REG_FONT.render("If you're a member then you should have access to their services.", 1, P.BLACK)
	explain_text5 = REG_FONT.render("I heard that as you get higher ranks you get more services from them.", 1, P.BLACK)
	explain_text6 = REG_FONT.render("I heard that they have some special enchantments for equipment.", 1, P.BLACK)
	explain_text7 = REG_FONT.render("I heard they can also upgrade or even combine your equipment.", 1, P.BLACK)
	explain_text8 = REG_FONT.render("You can also sell old equipment to them, they'll always find a use for it.", 1, P.BLACK)
	explain_text9 = REG_FONT.render("There's a rumor that the grandmasters there can teach you new skills too.", 1, P.BLACK)
	WIN.blit(explain_text1, ((width - explain_text1.get_width())//2, P.PADDING * 1))
	WIN.blit(explain_text2, ((width - explain_text2.get_width())//2, P.PADDING * 2))
	WIN.blit(explain_text3, ((width - explain_text3.get_width())//2, P.PADDING * 3))
	WIN.blit(explain_text4, ((width - explain_text4.get_width())//2, P.PADDING * 4))
	WIN.blit(explain_text5, ((width - explain_text5.get_width())//2, P.PADDING * 5))
	WIN.blit(explain_text6, ((width - explain_text6.get_width())//2, P.PADDING * 6))
	WIN.blit(explain_text7, ((width - explain_text7.get_width())//2, P.PADDING * 7))
	WIN.blit(explain_text8, ((width - explain_text8.get_width())//2, P.PADDING * 8))
	WIN.blit(explain_text9, ((width - explain_text9.get_width())//2, P.PADDING * 9))
	pygame.display.update()
	explain = True
	while explain:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				explain = False
				width, height = WIN.get_size()
				ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
				WIN.blit(ROAD_IMG, (0, 0))
				greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
				choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
				WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
				WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
				pygame.display.update()
def explain_purpose():
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	explain_text1 = REG_FONT.render("Why are you here?.", 1, P.BLACK)
	explain_text2 = REG_FONT.render("Sorry I don't know that.", 1, P.BLACK)
	explain_text3 = REG_FONT.render("But if you're here then why not help people?", 1, P.BLACK)
	explain_text4 = REG_FONT.render("It's a dangerous world recently, monsters are everywhere.", 1, P.BLACK)
	explain_text5 = REG_FONT.render("It only seems to be getting worse as time goes on.", 1, P.BLACK)
	explain_text6 = REG_FONT.render("No matter how many we kill, more and stronger one just keep coming.", 1, P.BLACK)
	explain_text7 = REG_FONT.render("If you want a grand goal, then try to find out why.", 1, P.BLACK)
	explain_text8 = REG_FONT.render("If you want a grander goal, then try to stop them for good.", 1, P.BLACK)
	WIN.blit(explain_text1, ((width - explain_text1.get_width())//2, P.PADDING * 1))
	WIN.blit(explain_text2, ((width - explain_text2.get_width())//2, P.PADDING * 2))
	WIN.blit(explain_text3, ((width - explain_text3.get_width())//2, P.PADDING * 3))
	WIN.blit(explain_text4, ((width - explain_text4.get_width())//2, P.PADDING * 4))
	WIN.blit(explain_text5, ((width - explain_text5.get_width())//2, P.PADDING * 5))
	WIN.blit(explain_text6, ((width - explain_text6.get_width())//2, P.PADDING * 6))
	WIN.blit(explain_text7, ((width - explain_text7.get_width())//2, P.PADDING * 7))
	WIN.blit(explain_text8, ((width - explain_text8.get_width())//2, P.PADDING * 8))
	pygame.display.update()
	explain = True
	while explain:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				explain = False
				width, height = WIN.get_size()
				ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
				WIN.blit(ROAD_IMG, (0, 0))
				greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
				choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
				WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
				WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
				pygame.display.update()
def explain_wizards():
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	explain_text1 = REG_FONT.render("Wizards sure do love TOWERs.", 1, P.BLACK)
	explain_text2 = REG_FONT.render("Wizards don't really fight but they can help you in other ways.", 1, P.BLACK)
	explain_text3 = REG_FONT.render("Some of them will sell you books that will teach you NEW MAGIC.", 1, P.BLACK)
	explain_text4 = REG_FONT.render("Some of them will help you SUMMON a SPIRIT ALLY.", 1, P.BLACK)
	explain_text5 = REG_FONT.render("Some of them will help you ENCHANT your EQUIPMENT.", 1, P.BLACK)
	explain_text6 = REG_FONT.render("And of course some will help TRAIN your MAGIC.", 1, P.BLACK)
	WIN.blit(explain_text1, ((width - explain_text1.get_width())//2, P.PADDING * 1))
	WIN.blit(explain_text2, ((width - explain_text2.get_width())//2, P.PADDING * 2))
	WIN.blit(explain_text3, ((width - explain_text3.get_width())//2, P.PADDING * 3))
	WIN.blit(explain_text4, ((width - explain_text4.get_width())//2, P.PADDING * 4))
	WIN.blit(explain_text5, ((width - explain_text5.get_width())//2, P.PADDING * 5))
	WIN.blit(explain_text6, ((width - explain_text6.get_width())//2, P.PADDING * 6))
	pygame.display.update()
	explain = True
	while explain:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				explain = False
				width, height = WIN.get_size()
				ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
				WIN.blit(ROAD_IMG, (0, 0))
				greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
				choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
				WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
				WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
				pygame.display.update()
def explain_cities():
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	explain_text1 = REG_FONT.render("Lots of people gather at cities.", 1, P.BLACK)
	explain_text2 = REG_FONT.render("It's safe enough that people can settle down and set up shops.", 1, P.BLACK)
	explain_text3 = REG_FONT.render("You can buy POTIONs or WEAPONs and ARMOR there.", 1, P.BLACK)
	explain_text4 = REG_FONT.render("If you're tired you can usually find an INN to rest at.", 1, P.BLACK)
	explain_text5 = REG_FONT.render("Lots of people go to inns making you can meet some NEW ALLIES there.", 1, P.BLACK)
	explain_text6 = REG_FONT.render("They also having TRAINING ARENAs to help you practice.", 1, P.BLACK)
	WIN.blit(explain_text1, ((width - explain_text1.get_width())//2, P.PADDING * 1))
	WIN.blit(explain_text2, ((width - explain_text2.get_width())//2, P.PADDING * 2))
	WIN.blit(explain_text3, ((width - explain_text3.get_width())//2, P.PADDING * 3))
	WIN.blit(explain_text4, ((width - explain_text4.get_width())//2, P.PADDING * 4))
	WIN.blit(explain_text5, ((width - explain_text5.get_width())//2, P.PADDING * 5))
	WIN.blit(explain_text6, ((width - explain_text6.get_width())//2, P.PADDING * 6))
	pygame.display.update()
	explain = True
	while explain:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				explain = False
				width, height = WIN.get_size()
				ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
				WIN.blit(ROAD_IMG, (0, 0))
				greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
				choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
				WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
				WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
				pygame.display.update()
def explain_heroes():
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	hero_text1 = REG_FONT.render("Lots of people going around calling themselves heroes nowadays.", 1, P.BLACK)
	hero_text2 = REG_FONT.render("Usually they specialize in just a few things though.", 1, P.BLACK)
	hero_text3 = REG_FONT.render("Like WARRIORs are good at hitting things hard and fast.", 1, P.BLACK)
	hero_text4 = REG_FONT.render("MAGEs are good at casting spells that hit lots of things.", 1, P.BLACK)
	hero_text5 = REG_FONT.render("CLERICs are good at empowering allies and weakening enemies.", 1, P.BLACK)
	hero_text6 = REG_FONT.render("SUMMONERs are good at commanding spirits to assist them to do all sorts of things.", 1, P.BLACK)
	hero_text7 = REG_FONT.render("KNIGHTs are good at defending their allies.", 1, P.BLACK)
	hero_text8 = REG_FONT.render("TACTICIANs are good at coordinating their allies.", 1, P.BLACK)
	hero_text9 = REG_FONT.render("NINJAs are good for hitting hard but they run out of steam fast.", 1, P.BLACK)
	WIN.blit(hero_text1, ((width - hero_text1.get_width())//2, P.PADDING * 1))
	WIN.blit(hero_text2, ((width - hero_text2.get_width())//2, P.PADDING * 2))
	WIN.blit(hero_text3, ((width - hero_text3.get_width())//2, P.PADDING * 3))
	WIN.blit(hero_text4, ((width - hero_text4.get_width())//2, P.PADDING * 4))
	WIN.blit(hero_text5, ((width - hero_text5.get_width())//2, P.PADDING * 5))
	WIN.blit(hero_text6, ((width - hero_text6.get_width())//2, P.PADDING * 6))
	WIN.blit(hero_text7, ((width - hero_text7.get_width())//2, P.PADDING * 7))
	WIN.blit(hero_text8, ((width - hero_text8.get_width())//2, P.PADDING * 8))
	WIN.blit(hero_text9, ((width - hero_text9.get_width())//2, P.PADDING * 9))
	pygame.display.update()
	explain = True
	while explain:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				explain = False
				width, height = WIN.get_size()
				ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
				WIN.blit(ROAD_IMG, (0, 0))
				greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
				choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
				WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
				WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
				pygame.display.update()
	
def ask(access):
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	greeting = REG_FONT.render("What do you want to talk about?", 1, P.BLACK)
	if access.rank == 0:
		choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / LEAVE.", 1, P.BLACK)
	elif access.rank > 0:
		choice = REG_FONT.render("PURPOSE / HEROES / CITIES / WIZARDS / GUILD / LEAVE.", 1, P.BLACK)
	WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
	WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	ask = True
	while ask:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					ask = False
					width, height = WIN.get_size()
					ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
					WIN.blit(ROAD_IMG, (0, 0))
					greeting = REG_FONT.render("Hello, have we met before?", 1, P.BLACK)
					greeting2 = REG_FONT.render("Sorry, my memory has gone hazy with age.", 1, P.BLACK)
					greeting3 = REG_FONT.render("I still remember lots of things though.", 1, P.BLACK)
					choice = REG_FONT.render("TALK or LEAVE?", 1, P.BLACK)
					WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
					WIN.blit(greeting2, ((width - greeting2.get_width())//2, P.PADDING * 2))
					WIN.blit(greeting3, ((width - greeting3.get_width())//2, P.PADDING * 3))
					WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 4))
					pygame.display.update()
				if event.key == pygame.K_h:
					explain_heroes()
				if event.key == pygame.K_c:
					explain_cities()
				if event.key == pygame.K_w:
					explain_wizards()
				if event.key == pygame.K_p:
					explain_purpose()
				if event.key == pygame.K_g and access.rank > 0:
					explain_guild()
def old_warrior(access):
	width, height = WIN.get_size()
	ROAD_IMG = pygame.transform.scale(ROAD_RAW, (width, height))
	WIN.blit(ROAD_IMG, (0, 0))
	greeting = REG_FONT.render("Hello, have we met before?", 1, P.BLACK)
	greeting2 = REG_FONT.render("Sorry, my memory has gone hazy with age.", 1, P.BLACK)
	greeting3 = REG_FONT.render("I still remember lots of things though.", 1, P.BLACK)
	choice = REG_FONT.render("TALK or LEAVE?", 1, P.BLACK)
	WIN.blit(greeting, ((width - greeting.get_width())//2, P.PADDING * 1))
	WIN.blit(greeting2, ((width - greeting2.get_width())//2, P.PADDING * 2))
	WIN.blit(greeting3, ((width - greeting3.get_width())//2, P.PADDING * 3))
	WIN.blit(choice, ((width - choice.get_width())//2, P.PADDING * 4))
	talk = True
	while talk:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				talk = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				pygame.event.clear()
				if event.key == pygame.K_l:
					talk = False
				if event.key == pygame.K_t:
					print ("t")
					ask(access)
