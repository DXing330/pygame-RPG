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
import rpg2_player_action_function as player_act_func
import rpg2_pet_action_function as pet_func
import draw_functions as draw_func
#always define the window you're drawing on
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#also need any specific images
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
#function that will make the city
def city(h_p, h_b, h_w, h_a):
        city = True
        while city:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_city_menu()
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                city = False
                                pygame.quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_i:
                                        inn(h_p, h_b, h_w, h_a)
                                if event.key == pygame.K_l:
                                        city = False
                                if event.key == pygame.K_s:
                                        equipment_store(h_b, h_w, h_a)
                                if event.key == pygame.K_p:
                                        practice_arena(h_p, h_b)
