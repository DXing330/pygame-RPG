import pygame
import os
import sys
import copy
sys.path.append("../pygame_general_functions")
sys.path.append("..")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_battle")
pygame.init()
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_constants import Constants
C = Constants()
import pyparty_functions as party_func
import pybattle_pet_action as pet_func
import pypick_function as pick_func
import pybattle_functions as pybattle_func
import draw_functions as draw_func
import draw_animation as drawa_func
import draw_effects as drawe_func
import pyelement_function as element_func
import pyeqpeffect_function as ee_func
import pymoneffect_function as me_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
clock = pygame.time.Clock()
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
