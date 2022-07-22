import pygame
import os
import sys
import json
sys.path.append(".")
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
HERO_RAW = pygame.image.load(os.path.join("Assets", "hero.png"))
HERO_IMG = pygame.transform.scale(HERO_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SUMMONER_RAW = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER_IMG = pygame.transform.scale(SUMMONER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
KNIGHT_RAW = pygame.image.load(os.path.join("Assets", "knight.png"))
KNIGHT_IMG = pygame.transform.scale(KNIGHT_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
HUNTER_RAW =pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER_IMG = pygame.transform.scale(HUNTER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
ANGEL_RAW = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL_IMG = pygame.transform.scale(ANGEL_RAW, (P.SPRITE_WIDTH//2, P.SPRITE_HEIGHT//2))

#function that will draw characters in battle
def draw_heroes(h_p, h_ally):
        for player in h_p:
                if "Hunter" in player.name:
                        WIN.blit(HUNTER_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 4),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 4)))
                if "Hero" in player.name:
                        WIN.blit(HERO_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 2),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 2)))
                if "Summoner" in player.name:
                        WIN.blit(SUMMONER_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 3),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))
                if "Knight" in player.name:
                        WIN.blit(KNIGHT_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 5),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 5)))
                
        for aly in h_ally:
                if "Angel" in aly.name:
                        WIN.blit(ANGEL_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 2),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))

        pygame.display.update()
                

#function that will control the battle
def battle(h_p, m_p, h_ally, h_bag,
           h_magic, h_wpn, h_amr):
        clock = pygame.time.Clock()
        battle = True
        while battle:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(FOREST_IMG, P.ORIGIN)
                draw_heroes(h_p, h_ally)
                draw_battle_menu(h_p, m_p, h_ally, h_magic,
                                 h_wpn, h_amr)
                pygame.display.update()
                
#function will list options for the player
def draw_menu():
        attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
        WIN.blit(attack_text, (P.WIDTH//2 - attack_text.get_width(), P.PADDING))
        save_text = REG_FONT.render("RECORD journey: R", 1, P.BLACK)
        WIN.blit(save_text, (P.WIDTH//2 - save_text.get_width(),
                             P.PADDING + save_text.get_height()))
        city_text = REG_FONT.render("return to CITY: C", 1, P.BLACK)
        WIN.blit(city_text, (P.WIDTH//2 - city_text.get_width(),
                             P.PADDING + city_text.get_height() * 2))
        

#function will make the plains background        
def draw_plains():
        WIN.fill(P.WHITE)
        WIN.blit(PLAINS_IMG, P.ORIGIN)
        draw_menu()
        pygame.display.update()
        
#function that will make the city
def city(h_p, h_b, h_w, h_a):
        clock = pygame.time.Clock()
        city = True
        while city:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                pygame.display.update()
                
        
def RPG(h_party, h_magic, h_bag, h_ally, h_wpn, h_amr, quest, access):
        clock = pygame.time.Clock()
        m_p = []
        game = True
        while game:
                clock.tick(P.FPS)
                draw_plains()
                draw_heroes(h_party, h_ally)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game = False
                                pygame.quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_a:
                                        for hero in h_party:
                                                mon = monster_func.random_scaled_monster(hero)
                                                m_p.append(mon)
                                        battle(h_party, m_p, h_ally, h_bag,
                                               h_magic, h_wpn, h_amr)
                                if event.key == pygame.K_c:
                                        city(h_party, h_bag, h_wpn, h_amr)
                                if event.key == pygame.K_r:
                                        save_func.write_to_files(h_party, h_magic,
                                                                 h_bag, h_ally,
                                                                 h_wpn, h_amr,
                                                                 quest, access,
                                                                 "RPG2_ \n ")

                



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
                start_text = REG_FONT.render("CONTINUE/START? C/S? ", 1, P.WHITE)
                WIN.fill(P.BLACK)
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
                                        
        

