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
CLERIC_RAW = pygame.image.load(os.path.join("Assets", "cleric.png"))
CLERIC_IMG = pygame.transform.scale(CLERIC_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
MAGE_RAW = pygame.image.load(os.path.join("Assets", "mage.png"))
MAGE_IMG = pygame.transform.scale(MAGE_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
NINJA_RAW = pygame.image.load(os.path.join("Assets", "ninja.png"))
NINJA_IMG = pygame.transform.scale(NINJA_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
WARRIOR_RAW = pygame.image.load(os.path.join("Assets", "warrior.png"))
WARRIOR_IMG = pygame.transform.scale(WARRIOR_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
TACTICIAN_RAW = pygame.image.load(os.path.join("Assets", "tactician.png"))
TACTICIAN_IMG = pygame.transform.scale(TACTICIAN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
TOTEM_RAW = pygame.image.load(os.path.join("Assets", "totem.png"))
TOTEM_IMG = pygame.transform.scale(TOTEM_RAW, (P.SMALL_SPRITE//2, P.SMALL_SPRITE//2))
BOMB_RAW = pygame.image.load(os.path.join("Assets", "bomb.png"))
BOMB_IMG = pygame.transform.scale(BOMB_RAW, (P.SMALL_SPRITE//2, P.SMALL_SPRITE//2))
HERO_RAW = pygame.image.load(os.path.join("Assets", "hero.png"))
HERO_IMG = pygame.transform.scale(HERO_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SUMMONER_RAW = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER_IMG = pygame.transform.scale(SUMMONER_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
KNIGHT_RAW = pygame.image.load(os.path.join("Assets", "knight.png"))
KNIGHT_IMG = pygame.transform.scale(KNIGHT_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
HUNTER_RAW =pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER_IMG = pygame.transform.scale(HUNTER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
ANGEL_RAW = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL_IMG = pygame.transform.scale(ANGEL_RAW, (P.SPRITE_WIDTH//2, P.SPRITE_HEIGHT//2))
GUARDIAN_RAW = pygame.image.load(os.path.join("Assets", "chimera.png"))
GUARDIAN_IMG = pygame.transform.scale(GUARDIAN_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
MON_RAW = pygame.image.load(os.path.join("Assets", "g_mon.png"))
MON_IMG = pygame.transform.scale(MON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SLIME_RAW = pygame.image.load(os.path.join("Assets", "slime.png"))
SLIME_IMG = pygame.transform.scale(SLIME_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
BEAST_RAW = pygame.image.load(os.path.join("Assets", "beast.png"))
BEAST_IMG = pygame.transform.scale(BEAST_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
GOBLIN_RAW = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
ELEMENTAL_RAW = pygame.image.load(os.path.join("Assets", "elemental.png"))
ELEMENTAL_IMG = pygame.transform.scale(ELEMENTAL_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
DEMON_RAW = pygame.image.load(os.path.join("Assets", "demon.png"))
DEMON_IMG = pygame.transform.scale(DEMON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SKELETON_RAW = pygame.image.load(os.path.join("Assets", "skeleton.png"))
SKELETON_IMG = pygame.transform.scale(SKELETON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
TROLL_RAW = pygame.image.load(os.path.join("Assets", "troll.png"))
TROLL_IMG = pygame.transform.scale(TROLL_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
GENERAL_RAW = pygame.image.load(os.path.join("Assets", "general.png"))
GENERAL_IMG = pygame.transform.scale(GENERAL_RAW, (P.BIG_SPRITE * 2, P.BIG_SPRITE * 2))
#function that will draw parties with bosses inside them
def draw_monsters(m_p):
	width, height = WIN.get_size()
	x = 2
	y = 0
	z = 1
	for mon in m_p:
		if "Demon General" in mon.name:
			WIN.blit(GENERAL_IMG,
				 (P.BIG_SPRITE, height//2))
			x -= 1
		elif "Slime" in mon.name:
			WIN.blit(SLIME_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Beast" in mon.name:
			WIN.blit(BEAST_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Bomb" in mon.name:
			WIN.blit(BOMB_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Goblin" in mon.name:
			if "Champion" in mon.name:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
			elif "Hob" in mon.name:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SPRITE_WIDTH, P.SPRITE_WIDTH))
			else:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
			WIN.blit(GOBLIN_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Elemental" in mon.name:
			WIN.blit(ELEMENTAL_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Demon" in mon.name:
			WIN.blit(DEMON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Skeleton" in mon.name:
			WIN.blit(SKELETON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Troll" in mon.name:
			WIN.blit(TROLL_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		else:
			WIN.blit(MON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		x += 1
		if x * P.BIG_SPRITE > height - P.PADDING:
			x = 1
			y += 1
