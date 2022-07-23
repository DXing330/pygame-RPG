import pygame
import os
import sys
import copy
import random
sys.path.append(".")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("../../RPG2v3/RPG2v3_functions/RPG2v3_def")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_level_up_function as lvlup_func
import rpg2_player_action_function as player_act_func
import rpg2_pet_action_function as pet_func
import draw_functions as draw_func
from rpg2_constants import Constants
C = Constants()
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#images
TOWER_RAW = pygame.image.load(os.path.join("Assets", "tower.png"))
TOWER_IMG = pygame.transform.scale(TOWER_RAW, (P.WIDTH, P.HEIGHT))
#things inside the mage tower
angel = Pet_NPC("Angel", 1, 2)
new_spell = Spell_PC("new", 1, 1, None, 1)

#mage tower
def mage_tower(h_p, h_ally, h_b, h_m, h_w, h_a):
	tower = True
	while tower:
		clock.tick(P.FPS)
		WIN.fill(P.WHITE)
		WIN.blit(TOWER_IMG, P.ORIGIN)
		draw_func.draw_mage_menu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				tower = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					tower = False
