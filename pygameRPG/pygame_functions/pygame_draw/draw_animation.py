import pygame
import os
import sys
sys.path.append("../")
sys.path.append("../pygame_general_functions")
sys.path.append("../../'Assets")
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
REG_FONT = pygame.font.SysFont("comicsans", 25)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
#images used
OCEAN = pygame.image.load('Assets/animation_assets/ocean.png')
WAVE1 = pygame.image.load('Assets/animation_assets/wave1.png')
WAVE2 = pygame.image.load('Assets/animation_assets/wave2.png')
WAVE3 = pygame.image.load('Assets/animation_assets/wave3.png')
WAVE4 = pygame.image.load('Assets/animation_assets/wave4.png')
WAVE5 = pygame.image.load('Assets/animation_assets/wave5.png')
WAVE6 = pygame.image.load('Assets/animation_assets/wave6.png')
WAVE7 = pygame.image.load('Assets/animation_assets/wave7.png')
WAVE8 = pygame.image.load('Assets/animation_assets/wave8.png')
WAVE9 = pygame.image.load('Assets/animation_assets/wave9.png')
WAVE10 = pygame.image.load('Assets/animation_assets/wave10.png')
WAVE11 = pygame.image.load('Assets/animation_assets/wave11.png')
WAVE12 = pygame.image.load('Assets/animation_assets/wave12.png')
WAVE13 = pygame.image.load('Assets/animation_assets/wave13.png')
WAVE14 = pygame.image.load('Assets/animation_assets/wave14.png')
WAVE15 = pygame.image.load('Assets/animation_assets/wave15.png')
WAVE16 = pygame.image.load('Assets/animation_assets/wave16.png')
WAVE_LIST = [WAVE1, WAVE2, WAVE3, WAVE4, WAVE5, WAVE6, WAVE7, WAVE8, WAVE9,
	     WAVE10, WAVE11, WAVE12, WAVE13, WAVE14, WAVE15, WAVE16]
FLAME = pygame.image.load('Assets/animation_assets/flames.png')
FIRE1 = pygame.image.load('Assets/animation_assets/fire1.png')
FIRE2 = pygame.image.load('Assets/animation_assets/fire2.png')
FIRE3 = pygame.image.load('Assets/animation_assets/fire3.png')
FIRE4 = pygame.image.load('Assets/animation_assets/fire4.png')
FIRE5 = pygame.image.load('Assets/animation_assets/fire5.png')
FIRE6 = pygame.image.load('Assets/animation_assets/fire6.png')
FIRE7 = pygame.image.load('Assets/animation_assets/fire7.png')
FIRE8 = pygame.image.load('Assets/animation_assets/fire8.png')
FIRE9 = pygame.image.load('Assets/animation_assets/fire9.png')
FIRE10 = pygame.image.load('Assets/animation_assets/fire10.png')
FIRE_LIST = [FIRE1, FIRE2, FIRE3, FIRE4, FIRE5, FIRE6, FIRE7, FIRE8, FIRE9, FIRE10]
GROUND = pygame.image.load('Assets/animation_assets/ground.png')
EARTH1 = pygame.image.load('Assets/animation_assets/earth1.png')
EARTH2 = pygame.image.load('Assets/animation_assets/earth2.png')
EARTH3 = pygame.image.load('Assets/animation_assets/earth3.png')
EARTH4 = pygame.image.load('Assets/animation_assets/earth4.png')
EARTH5 = pygame.image.load('Assets/animation_assets/earth5.png')
EARTH6 = pygame.image.load('Assets/animation_assets/earth6.png')
EARTH7 = pygame.image.load('Assets/animation_assets/earth7.png')
EARTH8 = pygame.image.load('Assets/animation_assets/earth8.png')
EARTH9 = pygame.image.load('Assets/animation_assets/earth9.png')
EARTH10 = pygame.image.load('Assets/animation_assets/earth10.png')
EARTH11 = pygame.image.load('Assets/animation_assets/earth11.png')
EARTH12 = pygame.image.load('Assets/animation_assets/earth12.png')
EARTH13 = pygame.image.load('Assets/animation_assets/earth13.png')
EARTH14 = pygame.image.load('Assets/animation_assets/earth14.png')
EARTH15 = pygame.image.load('Assets/animation_assets/earth15.png')
EARTH16 = pygame.image.load('Assets/animation_assets/earth16.png')
EARTH17 = pygame.image.load('Assets/animation_assets/earth17.png')
EARTH18 = pygame.image.load('Assets/animation_assets/earth18.png')
EARTH_LIST = [EARTH1, EARTH2, EARTH3, EARTH4, EARTH5, EARTH6, EARTH7, EARTH8, EARTH9,
	      EARTH10, EARTH11, EARTH12, EARTH13, EARTH14, EARTH15, EARTH16, EARTH17, EARTH18]
SKY = pygame.image.load('Assets/animation_assets/sky.png')
AIR1 = pygame.image.load('Assets/animation_assets/air1.png')
AIR2 = pygame.image.load('Assets/animation_assets/air2.png')
AIR3 = pygame.image.load('Assets/animation_assets/air3.png')
AIR4 = pygame.image.load('Assets/animation_assets/air4.png')
AIR5 = pygame.image.load('Assets/animation_assets/air5.png')
AIR6 = pygame.image.load('Assets/animation_assets/air6.png')
AIR7 = pygame.image.load('Assets/animation_assets/air7.png')
AIR8 = pygame.image.load('Assets/animation_assets/air8.png')
AIR9 = pygame.image.load('Assets/animation_assets/air9.png')
AIR10 = pygame.image.load('Assets/animation_assets/air10.png')
AIR11 = pygame.image.load('Assets/animation_assets/air11.png')
AIR12 = pygame.image.load('Assets/animation_assets/air12.png')
AIR13 = pygame.image.load('Assets/animation_assets/air13.png')
AIR14 = pygame.image.load('Assets/animation_assets/air14.png')
AIR15 = pygame.image.load('Assets/animation_assets/air15.png')
AIR16 = pygame.image.load('Assets/animation_assets/air16.png')
AIR17 = pygame.image.load('Assets/animation_assets/air17.png')
AIR18 = pygame.image.load('Assets/animation_assets/air18.png')
AIR19 = pygame.image.load('Assets/animation_assets/air19.png')
AIR_LIST = [AIR1, AIR2, AIR3, AIR4, AIR5, AIR6, AIR7, AIR8,
	    AIR9, AIR10, AIR11, AIR12, AIR13, AIR14, AIR15, AIR16,
	    AIR17, AIR18, AIR19]
DARK1 = pygame.image.load('Assets/animation_assets/dark1.png')
DARK2 = pygame.image.load('Assets/animation_assets/dark2.png')
DARK3 = pygame.image.load('Assets/animation_assets/dark3.png')
DARK4 = pygame.image.load('Assets/animation_assets/dark4.png')
DARK5 = pygame.image.load('Assets/animation_assets/dark5.png')
DARK6 = pygame.image.load('Assets/animation_assets/dark6.png')
DARK7 = pygame.image.load('Assets/animation_assets/dark7.png')
DARK8 = pygame.image.load('Assets/animation_assets/dark8.png')
DARK9 = pygame.image.load('Assets/animation_assets/dark9.png')
DARK10 = pygame.image.load('Assets/animation_assets/dark10.png')
DARK11 = pygame.image.load('Assets/animation_assets/dark11.png')
DARK12 = pygame.image.load('Assets/animation_assets/dark12.png')
DARK13 = pygame.image.load('Assets/animation_assets/dark13.png')
DARK14 = pygame.image.load('Assets/animation_assets/dark14.png')
DARK15 = pygame.image.load('Assets/animation_assets/dark15.png')
DARK16 = pygame.image.load('Assets/animation_assets/dark16.png')
DARK17 = pygame.image.load('Assets/animation_assets/dark17.png')
DARK18 = pygame.image.load('Assets/animation_assets/dark18.png')
DARK19 = pygame.image.load('Assets/animation_assets/dark19.png')
DARK20 = pygame.image.load('Assets/animation_assets/dark20.png')
DARK21 = pygame.image.load('Assets/animation_assets/dark21.png')
DARK22 = pygame.image.load('Assets/animation_assets/dark22.png')
DARK23 = pygame.image.load('Assets/animation_assets/dark23.png')
DARK_LIST = [DARK1, DARK2, DARK3, DARK4, DARK5, DARK6, DARK7, DARK8,
	     DARK9, DARK10, DARK11, DARK12, DARK13, DARK14, DARK15, DARK16,
	     DARK17, DARK18, DARK19, DARK20, DARK21, DARK22, DARK23]
#function that draws a dark hole attack
def hero_dark_attack(hero, m_p, spell):
	spell_list = DARK_LIST
	width, height = WIN.get_size()
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, len(spell_list)):
		spell_img = spell_list[x]
		spell_img = pygame.transform.scale(spell_img, (width * 0.5, height))
		WIN.fill(P.BLACK)
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(spell_img, (-width * 0.1, height * 0))
		pygame.display.update()
		pygame.time.delay(10)
	for y in range(0, 18):
		for z in range(0, 13):
			spell_img = spell_list[z + 10]
			spell_img = pygame.transform.scale(spell_img, (width * (0.5 + (y/10)), height * (1 + y/10)))
			WIN.fill(P.BLACK)
			draw_func.draw_hero(hero)
			draw_func.draw_monsters(m_p)
			WIN.blit(spell_img, (-width * (0.1 + (y/20)), height * (0 - (y/20))))
			pygame.display.update()
#function that draws a whirlwind
def hero_air_attack(hero, m_p, spell):
	spell_list = AIR_LIST
	width, height = WIN.get_size()
	BG_IMG = pygame.transform.scale(SKY, (width, height))
	WIN.blit(BG_IMG, (0, 0))
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, len(spell_list)):
		spell_img = spell_list[x]
		spell_img = pygame.transform.scale(spell_img, (width * 0.5, height * 1.5))
		WIN.blit(BG_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(spell_img, (-width * 0.25, -height//20))
		WIN.blit(spell_img, (-width * 0.125, -height//20))
		WIN.blit(spell_img, (width * 0.125, -height//20))
		WIN.blit(spell_img, (width * 0, -height//20))
		pygame.display.update()
		pygame.time.delay(10)
		pygame.display.update()
		pygame.time.delay(10)
	for y in range(0, 10):
		for z in range(0, 7):
			spell_img = spell_list[z + 12]
			spell_img = pygame.transform.scale(spell_img, (width * (0.5 + (y/10)), height * 1.5))
			draw_func.draw_hero(hero)
			draw_func.draw_monsters(m_p)
			WIN.blit(spell_img, (-width * (0.25 + (y/20)), -height//20))
			WIN.blit(spell_img, (-width * (0.125 + (y/20)), -height//20))
			WIN.blit(spell_img, (width * (0.125 - (y/20)), -height//20))
			WIN.blit(spell_img, (width * (0 - (y/20)), -height//20))
			pygame.display.update()
#function that draws an earth spike
def hero_earth_attack(hero, m_p, spell):
	spell_list = EARTH_LIST
	width, height = WIN.get_size()
	BG_IMG = pygame.transform.scale(GROUND, (width, height))
	WIN.blit(BG_IMG, (0, 0))
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, len(spell_list)):
		spell_img = spell_list[x]
		spell_img = pygame.transform.scale(spell_img, (width * 0.5, height))
		WIN.blit(BG_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(spell_img, (-width * 0.125, 0))
		WIN.blit(spell_img, (-width * 0.25 , 0))
		WIN.blit(spell_img, (width * 0 , 0))
		WIN.blit(spell_img, (width * 0.125 , 0))
		pygame.display.update()
		pygame.time.delay(25)

#function that draws a wave
def hero_wave_attack(hero, m_p, spell):
	width, height = WIN.get_size()
	OCEAN_IMG = pygame.transform.scale(OCEAN, (width, height))
	WIN.blit(OCEAN_IMG, (0, 0))
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, 16):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WAVE_IMG = pygame.transform.flip(WAVE_IMG, True, False)
		WIN.blit(OCEAN_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(20)

def hero_wave_attack(hero, m_p, spell):
	width, height = WIN.get_size()
	OCEAN_IMG = pygame.transform.scale(OCEAN, (width, height))
	WIN.blit(OCEAN_IMG, (0, 0))
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, 16):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WAVE_IMG = pygame.transform.flip(WAVE_IMG, True, False)
		WIN.blit(OCEAN_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(20)
	for x in range(0, 16):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WAVE_IMG = pygame.transform.flip(WAVE_IMG, True, False)
		draw_func.draw_hero(hero)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(20)
	for x in range(0, 16):
		WAVE_IMG = WAVE_LIST[x]
		WAVE_IMG = pygame.transform.scale(WAVE_IMG, (width, height))
		WAVE_IMG = pygame.transform.flip(WAVE_IMG, True, False)
		WIN.blit(WAVE_IMG, (0, 0))
		pygame.display.update()
		pygame.time.delay(20)


def hero_fire_attack(hero, m_p, spell):
	width, height = WIN.get_size()
	BG_IMG = pygame.transform.scale(FLAME, (width, height))
	WIN.blit(BG_IMG, (0, 0))
	draw_func.draw_monsters(m_p)
	draw_func.draw_hero(hero)
	attack_text = REG_FONT.render(hero.name+" casts "+spell.name, 1, P.RED)
	WIN.blit(attack_text, ((width - attack_text.get_width())//2, P.PADDING * 2))
	pygame.display.update()
	pygame.time.delay(200)
	for x in range(0, 10):
		FIRE_IMG = FIRE_LIST[x]
		FIRE_IMG = pygame.transform.scale(FIRE_IMG, (width * 0.7, height))
		WIN.blit(BG_IMG, (0, 0))
		draw_func.draw_hero(hero)
		draw_func.draw_monsters(m_p)
		WIN.blit(FIRE_IMG, (-width * 0.15, 0))
		WIN.blit(FIRE_IMG, (-width * 0.35, 0))
		WIN.blit(FIRE_IMG, (width * 0.05, 0))
		pygame.display.update()
		pygame.time.delay(15)
	for y in range(0, 3):
		for z in range(0, 3):
			FIRE_IMG = FIRE_LIST[z + 7]
			FIRE_IMG = pygame.transform.scale(FIRE_IMG, (width * (0.7+(y/10)), height))
			WIN.blit(BG_IMG, (0, 0))
			draw_func.draw_hero(hero)
			draw_func.draw_monsters(m_p)
			WIN.blit(FIRE_IMG, (width * (0.05-(y/20)), 0))
			WIN.blit(FIRE_IMG, (-width * (0.35+(y/20)), 0))
			WIN.blit(FIRE_IMG, (-width * (0.15+(y/20)), 0))
			pygame.display.update()
			pygame.time.delay(10)


