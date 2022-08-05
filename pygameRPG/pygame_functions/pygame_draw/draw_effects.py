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
SPACE_RAW = pygame.image.load(os.path.join("Assets", "space2.png"))
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
FANG_RAW = pygame.image.load(os.path.join("Assets", "fang_atk2.png"))
FANG_IMG = pygame.transform.scale(FANG_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
#ally actions
def spirit_companion_atk(spirit, mon):
	x, y = WIN.get_size()
	attack_text = REG_FONT.render(spirit.name+" attacks "+mon.name, 1, P.RED)
	WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
	BFANG_IMG = pygame.transform.rotate(FANG_IMG, 180)
	for z in range(0, 100):
		SPACE_IMG = pygame.transform.scale(SPACE_RAW, (x, y))
		WIN.blit(SPACE_IMG, P.ORIGIN)
		draw_func.draw_monster(mon)
		draw_func.draw_ally(spirit)
		WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
		WIN.blit(FANG_IMG, (x//3, y/(2.5 - z/200)))
		WIN.blit(BFANG_IMG, (x//3, y/(1.5 + z/200)))
		pygame.display.update()
def angel_legendary_action(angel, h_p, m_p):
	for z in range(0, 33):
		x, y = WIN.get_size()
		TEMPLE_IMG = pygame.transform.scale(TEMPLE_RAW, (x, y))
		WIN.blit(TEMPLE_IMG, P.ORIGIN)
		draw_func.draw_monsters(m_p)
		draw_func.draw_just_hero(h_p)
		#draw the light expanding each round
		LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//8, y * 2))
		#keep the light in the center
		WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//16, -y))
		#draw the angel
		WIN.blit(WINGS_IMG, (x//2 - P.BIG_SPRITE, y//2 - P.BIG_SPRITE))
		pygame.display.update()
def angel_heal_action(angel, hero):
	for z in range(0, 10):
		x, y = WIN.get_size()
		WIN.fill(P.BLACK)
		draw_func.draw_hero(hero)
		LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//16, y * 2))
		WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//32, -y))
		angel_text = REG_FONT.render(angel.name+" heals "+hero.name, 1, P.WHITE)
		WIN.blit(angel_text, ((x - angel_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		pygame.time.delay(30)
def angel_debuff_action(angel, mon):
	for z in range(0, 10):
		x, y = WIN.get_size()
		WIN.fill(P.BLACK)
		draw_func.draw_monster(mon)
		LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//16, y * 2))
		WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//32, -y))
		angel_text = REG_FONT.render(angel.name+" curses "+mon.name, 1, P.WHITE)
		WIN.blit(angel_text, ((x - angel_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		pygame.time.delay(30)
def angel_buff_action(angel, hero):
	for z in range(0, 10):
		x, y = WIN.get_size()
		WIN.fill(P.BLACK)
		draw_func.draw_hero(hero)
		LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//16, y * 2))
		WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//32, -y))
		angel_text = REG_FONT.render(angel.name+" blesses "+hero.name, 1, P.WHITE)
		WIN.blit(angel_text, ((x - angel_text.get_width())//2, P.PADDING * 2))
		pygame.display.update()
		pygame.time.delay(30)
#function that will draw the hero's attack
def hero_attack(hero, weapon, mon):
	x, y = WIN.get_size()
	draw_func.draw_monster(mon)
	attack_text = REG_FONT.render(hero.name+" attacks "+mon.name, 1, P.RED)
	WIN.blit(attack_text, ((x - attack_text.get_width())//2, P.PADDING * 2))
	if weapon != None:
		if weapon.effect == "Attack":
			pass
		else:
			effect_text = REG_FONT.render("The attack "+weapon.effect+"'s", 1, P.RED)
			WIN.blit(effect_text, ((x - effect_text.get_width())//2, P.PADDING * 3))
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

def hero_level_up(hero):
	x, y = WIN.get_size()
	draw_func.draw_hero(hero)
	level_up_text = REG_FONT.render(hero.name+" leveled up! ", 1, P.GREEN)
	WIN.blit(level_up_text, ((x - level_up_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(500)
	
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
