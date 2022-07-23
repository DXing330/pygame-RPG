import pygame
import os
import sys
import json
import copy
import random
sys.path.append(".")
sys.path.append("./pygame_functions")
sys.path.append("./RPG2v3/RPG2v3_functions")
sys.path.append("./RPG2v3/RPG2v3_functions/RPG2v3_quest")
sys.path.append("./RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("./RPG2v3/RPG2v3_functions/RPG2v3_battle")
sys.path.append("./RPG2v3/RPG2v3_functions/bossbattles")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, ItemBag_PC,
                                   Spell_PC, Monster_NPC, Weapon_PC,
                                   Armor_PC, QuestItems_NPC, Access_NPC)
import rpg2_city_function as city_func
import rpg2_party_management_functions as party_func
import rpg2_monster_function as monster_func
import rpg2_battle_phase_function as battle_func
import rpg2_player_action_function as player_act_func
import rpg2_mage_tower_function as magetower_func
import rpg2_save_function as save_func
import rpg2_random_boss_function as boss_func
import rpg2_monster_hunter_guild as mh_func
import rpg2_quest_function as quest_func
import rpg2_tavern as tavern_func
from rpg2_constants import Constants
C = Constants()
from rpg2_constant_lists import List_Constants
L = List_Constants()
from rpg2_constant_quests import Q_Constants
Q = Q_Constants()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_functions as draw_func
import pybattle_functions as pybattle_func
import pycity_functions as pycity_func
#clock
clock = pygame.time.Clock()
#makes fonts
pygame.font.init()
#makes sound
pygame.mixer.init()
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#images used
PLAINS_RAW = pygame.image.load(os.path.join("Assets", "plains.png"))
PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (P.WIDTH, P.HEIGHT))
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
SPACE_RAW = pygame.image.load(os.path.join("Assets", "space.png"))
SPACE_IMG = pygame.transform.scale(SPACE_RAW, (P.WIDTH, P.HEIGHT))


#function will make the plains background        
def draw_plains():
        WIN.fill(P.WHITE)
        WIN.blit(PLAINS_IMG, P.ORIGIN)
        draw_func.draw_menu()
        pygame.display.update()

def RPG(h_party, h_magic, h_bag, h_ally, h_wpn, h_amr, quest, access):
        m_p = []
        game = True
        while game:
                clock.tick(P.SLOWFPS)
                draw_plains()
                draw_func.draw_heroes(h_party, h_ally)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game = False
                                pygame.quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_a:
                                        for hero in h_party:
                                                mon = monster_func.random_scaled_monster(hero)
                                                m_p.append(mon)
                                        pybattle_func.battle(h_party, m_p, h_ally, h_bag,
                                                             h_magic, h_wpn, h_amr)
                                if event.key == pygame.K_c:
                                        pycity_func.city(h_party, h_bag, h_wpn, h_amr)
                                if event.key == pygame.K_r:
                                        save_func.write_to_files(h_party, h_magic,
                                                                 h_bag, h_ally,
                                                                 h_wpn, h_amr,
                                                                 quest, access,
                                                                 "RPG2_ \n ")
                                if event.key == pygame.K_s:
                                        game = False
                                        pygame.quit()
                                        

def Start():
        #inital variables
        heroes_party = []
        heroes_magic = []
        heroes_allies = []
        heroes_bag = ItemBag_PC(1, 1, 1, 50)
        heroes_weapons = []
        heroes_armor = []
        q_items = QuestItems_NPC()
        a_items = Access_NPC()
        hero = Player_PC("Hero", 1, 15, 15, 5, 4, 2, 2, 2)
        hero_sword = Weapon_PC("LS", "Hero", "Attack", 1, "Light", 1)
        hero_armor = Armor_PC("LA", "Hero", "Block", 1, "Light", 1)
        start = True
        while start:
                clock.tick(P.FPS)
                start_text = REG_FONT.render("CONTINUE/START? C/S? ", 1, P.WHITE)
                WIN.fill(P.BLACK)
                WIN.blit(SPACE_IMG, P.ORIGIN)
                WIN.blit(start_text, ((P.WIDTH - start_text.get_width())//2,
                                      P.PADDING))
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                start = False
                                pygame.quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_s:
                                        party_func.add_to_party(heroes_party, hero)
                                        heroes_weapons.append(hero_sword)
                                        heroes_armor.append(hero_armor)
                                        start = False
                                        
                                if event.key == pygame.K_c:
                                        heroes_list, heroes_magic_list, items_bag_obj, allies, weapons, armor, quest, access = save_func.read()
                                        heroes_party = heroes_list
                                        heroes_magic = heroes_magic_list
                                        heroes_bag = items_bag_obj
                                        heroes_allies = allies
                                        heroes_weapons = weapons
                                        heroes_armor = armor
                                        q_items = quest
                                        a_items = access
                                        start = False
                                        
        RPG(heroes_party, heroes_magic, heroes_bag, heroes_allies,
            heroes_weapons, heroes_armor, q_items, a_items)

Start()
                                        
        
