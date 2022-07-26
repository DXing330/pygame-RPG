import pygame
import os
import sys
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
#function that will draw the angel's legendary action
def angel_legendary_action(angel, h_p, m_p):
        for z in range(0, 120):
                #first make the window blank
                WIN.fill(P.WHITE)
                #then draw in the angelic background
                x, y = WIN.get_size()
                TEMPLE_IMG = pygame.transform.scale(TEMPLE_RAW, (x, y))
                WIN.blit(TEMPLE_IMG, P.ORIGIN)
                #then draw in the heroes and monsters
                draw_func.draw_monsters(m_p)
                draw_func.draw_just_hero(h_p)
                #draw the light expanding each round
                LIGHT_IMG = pygame.transform.scale(LIGHT_RAW, (x * (z + 1)//64, y * 2))
                #keep the light in the center
                WIN.blit(LIGHT_IMG, (x//2 - (x * (z + 1))//128, -y))
                #draw the angel
                WIN.blit(WINGS_IMG, (x//2 - P.BIG_SPRITE, y//2 - P.BIG_SPRITE))
                pygame.display.update()
