import pygame
pygame.init()
import copy
import random
import sys
sys.path.append("../pygame_general_functions")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
				   Spell_PC, Monster_NPC, Weapon_PC,
				   Armor_PC, QuestItems_NPC, Access_NPC)
import pyparty_functions as party_func
from rpg2_constants import Constants
from rpg2_constant_lists import List_Constants
from pygconstants import PYGConstants
P = PYGConstants()
L = List_Constants()
C = Constants()
REG_FONT = pygame.font.SysFont("comicsans", 25)

#function that will make a random equipment for the player to buy
def random_equip(h_b, qi_npc, a_npc):
        e = 1
        #depending on the bosses fought, more items are available
        if h_b.dg_trophy > 1:
                e += 1
        if h_b.ah_trophy > 0:
                e += 1
        r = random.randint(0, e)
        if r == 1:
                equip = Weapon_PC("Weapon", "None", "Attack", 1, "Light", 1)
                equip_text = REG_FONT.render("This is a weapon fit for a hero!", 1, P.BLACK)
        elif r == 2:
                equip = Weapon_PC("Weapon", "None", "Command", 1, "None", 1)
                equip_text = REG_FONT.render("This is a weapon fit for a hero!", 1, P.BLACK)
        elif r == 3:
                equip = Weapon_PC("Torch", "None", "Scorch", 1, "Fire", 1)
                equip_text = REG_FONT.render("This weapon will burn bodies to ashes.", 1, P.BLACK)
        else:
                equip = Weapon_PC("Weapon", "None", "None", 0, "None", 0)
                equip_text = REG_FONT.render("This weapon has a lot of potential.", 1, P.BLACK)
        return equip, equip_text
