import pygame
import os
import sys
import random
sys.path.append(".")
sys.path.append("../..")
sys.path.append("../../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_constants import Constants
C = Constants()
import draw_functions as draw_func
REG_FONT = pygame.font.SysFont("comicsans", 20)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
#images used
TEMPLE_RAW = pygame.image.load(os.path.join("Assets", "temple.png"))
TEMPLE_IMG = pygame.transform.scale(TEMPLE_RAW, (P.WIDTH, P.HEIGHT))
LIGHT_RAW = pygame.image.load(os.path.join("Assets", "lightray.png"))
WINGS_RAW = pygame.image.load(os.path.join("Assets", "angelwings.png"))
WINGS_IMG = pygame.transform.scale(WINGS_RAW, (P.BIG_SPRITE * 2, P.BIG_SPRITE * 2))
WINGS_IMG = pygame.transform.scale(WINGS_RAW, (P.BIG_SPRITE * 2, P.BIG_SPRITE * 2))
HATK_RAW = pygame.image.load(os.path.join("Assets", "hero_atk.png"))
HATK_IMG = pygame.transform.scale(HATK_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE//2))
MATK_RAW = pygame.image.load(os.path.join("Assets", "magic_atk.png"))
MATK_IMG = pygame.transform.scale(MATK_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE//2))
CLAWATK_RAW = pygame.image.load(os.path.join("Assets", "claw_atk.png"))
CLAWATK_IMG = pygame.transform.scale(CLAWATK_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
SLASHATK_RAW = pygame.image.load(os.path.join("Assets", "slash_atk.png"))
SLASHATK_IMG = pygame.transform.scale(SLASHATK_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
SHADATK_RAW = pygame.image.load(os.path.join("Assets", "shadow_atk.png"))
SHADATK_IMG = pygame.transform.scale(SHADATK_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
PUNCH_RAW = pygame.image.load(os.path.join("Assets", "punch_atk.png"))
PUNCH_IMG = pygame.transform.scale(PUNCH_RAW, (P.BIG_SPRITE * 2, P.BIG_SPRITE))
#function that will draw the angel's legendary action
def angel_legendary_action(angel, h_p, m_p):
	for z in range(0, 77):
		x, y = WIN.get_size()
		TEMPLE_IMG = pygame.transform.scale(TEMPLE_RAW, (x, y))
		WIN.blit(TEMPLE_IMG, P.ORIGIN)
		draw_func.draw_monsters(m_p)
		draw_func.draw_just_hero(h_p)
		#draw the light expanding each round
		LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//16, y * 2))
		#keep the light in the center
		WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//32, -y))
		#draw the angel
		WIN.blit(WINGS_IMG, (x//2 - P.BIG_SPRITE, y//2 - P.BIG_SPRITE))
		pygame.display.update()
#function that will draw the hero's attack
def hero_attack(hero, mon):
	x, y = WIN.get_size()
	draw_func.draw_monster(mon)
	attack_text = REG_FONT.render(hero.name+" attacks "+mon.name, 1, P.RED)
	WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
	if "Summoner" in hero.name or "Mage" in hero.name or "Cleric" in hero.name or "Tactician" in hero.name:
		draw_func.draw_hero(hero)
		for z in range(0, 200):
			WIN.blit(MATK_IMG, (x//2 - (z * 4), (y + P.SMALL_SPRITE)//2))
			pygame.display.update()
	elif "Hunter" in hero.name or "Warrior" in hero.name or "Hero" in hero.name:
		draw_func.draw_hero(hero)
		for z in range(0, 4):
			SLASHATK_IMAGE = pygame.transform.rotate(SLASHATK_IMG, z * random.randint(25, 75))
			WIN.blit(SLASHATK_IMAGE, (x//3, (y//2)))
			pygame.display.update()
			pygame.time.delay(125)
	elif "Knight" in hero.name:
		for z in range(0, 50):
			WIN.blit(PUNCH_IMG, (x//2 - (z * 5), (y - P.SMALL_SPRITE)//2))
			draw_func.draw_hero(hero)
			pygame.display.update()
	elif "Ninja" in hero.name:
		draw_func.draw_hero(hero)
		for z in range(0, 360):
			SHADOW_IMAGE = pygame.transform.rotate(SHADATK_IMG, z * random.randint(0, 13))
			WIN.blit(SHADOW_IMAGE, (x//3, (y//2)))
			pygame.display.update()

def monster_attack(mon, hero):
	draw_func.draw_monster(mon)
	draw_func.draw_hero(hero)
	x, y = WIN.get_size()
	attack_text = REG_FONT.render(mon.name+" attacks "+hero.name, 1, P.RED)
	WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
	for z in range(0, 2):
		SLASHATK_IMAGE = pygame.transform.rotate(CLAWATK_IMG, z * random.randint(13, 91))
		WIN.blit(SLASHATK_IMAGE, (x//2, (y//2)))
		pygame.display.update()
		pygame.time.delay(250)

def mon_atk_mon(mon, mon2):
	draw_func.draw_monster(mon)
	draw_func.draw_monster2(mon2)
	x, y = WIN.get_size()
	attack_text = REG_FONT.render(mon.name+" attacks "+mon2.name, 1, P.RED)
	WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
	if "Giant" in mon.name:
		pass
	elif "Demon" in mon.name:
		for z in range(0, 4):
			CLAWATK_IMG = pygame.transform.rotate(CLAWATK_IMG,
							      z * random.randint(13, 91))
			WIN.blit(CLAWATK_IMG, (x//2, (y//2)))
			pygame.display.update()
			pygame.time.delay(250)
	
