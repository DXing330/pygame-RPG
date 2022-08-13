import pygame
import os
import sys
sys.path.append("../")
sys.path.append("../pygame_general_functions")
sys.path.append("../../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
REG_FONT = pygame.font.SysFont("comicsans", 25)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
#images used
OCEAN = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\ocean.png')
WAVE1 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave1.png')
WAVE2 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave2.png')
WAVE3 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave3.png')
WAVE4 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave4.png')
WAVE5 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave5.png')
WAVE6 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave6.png')
WAVE7 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave7.png')
WAVE8 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave8.png')
WAVE9 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave9.png')
WAVE10 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave10.png')
WAVE11 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave11.png')
WAVE12 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave12.png')
WAVE13 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave13.png')
WAVE14 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave14.png')
WAVE15 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave15.png')
WAVE16 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\wave16.png')
WAVE_LIST = [WAVE1, WAVE2, WAVE3, WAVE4, WAVE5, WAVE6, WAVE7, WAVE8, WAVE9,
	     WAVE10, WAVE11, WAVE12, WAVE13, WAVE14, WAVE15, WAVE16]
FLAME = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\flames.png')
FIRE1 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire1.png')
FIRE2 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire2.png')
FIRE3 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire3.png')
FIRE4 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire4.png')
FIRE5 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire5.png')
FIRE6 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire6.png')
FIRE7 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire7.png')
FIRE8 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire8.png')
FIRE9 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire9.png')
FIRE10 = pygame.image.load(r'C:\Users\draco\Documents\RPG\pygameRPG\Assets\fire10.png')
FIRE_LIST = [FIRE1, FIRE2, FIRE3, FIRE4, FIRE5, FIRE6, FIRE7, FIRE8, FIRE9, FIRE10]
#function that draws a wave
def hero_wave_attack(hero, m_p):
	width, height = WIN.get_size()
	OCEAN_IMG = pygame.transform.scale(OCEAN, (width, height))
	for x in range(0, 17):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WAVE_IMG = pygame.transform.flip(WAVE_IMG, True, False)
		WIN.blit(OCEAN_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(20)

def enemy_wave_attack(mon, h_p):
	width, height = WIN.get_size()
	OCEAN_IMG = pygame.transform.scale(OCEAN, (width, height))
	for x in range(0, 16):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WIN.blit(OCEAN_IMG, (0, 0))
		draw_func.draw_monster(mon)
		draw_func.draw_just_hero(h_p)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(30)


def hero_fire_attack(hero, m_p):
	width, height = WIN.get_size()
	BG_IMG = pygame.transform.scale(FLAME, (width, height))
	for x in range(0, 10):
		FIRE_IMG = FIRE_LIST[x]
		FIRE_IMG = pygame.transform.scale(FIRE_IMG, (width * 0.7, height))
		WIN.blit(BG_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(FIRE_IMG, (-width * 0.15, 0))
		pygame.display.update()
		pygame.time.delay(25)
	for y in range(0, 20):
		for z in range(0, 3):
			FIRE_IMG = FIRE_LIST[z + 7]
			FIRE_IMG = pygame.transform.scale(FIRE_IMG, (width * (0.7+(y/10)), height))
			WIN.blit(BG_IMG, (0, 0))
			draw_func.draw_hero(hero)
			draw_func.draw_monsters(m_p)
			WIN.blit(FIRE_IMG, (-width * (0.15+(y/20)), 0))
			pygame.display.update()
			pygame.time.delay(20)


