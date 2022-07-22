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
#need additional images for the inn, equipment store and practice arena
#store the starter characters incase the player recruits them
summoner = Player_PC("Summoner", 1, 10, 10, 2, 2, 2, 2, 2)
cleric = Player_PC("Cleric", 1, 10, 10, 3, 3, 2, 3, 3)
mage = Player_PC("Mage", 1, 10, 10, 2, 2, 2, 5, 5)
warrior = Player_PC("Warrior", 1, 15, 15, 5, 3, 2, 0, 0)
ninja = Player_PC("Ninja", 1, 15, 15, 3, 3, 5, 2, 2)
knight = Player_PC("Knight", 1, 20, 20, 3, 4, 2, 0, 0)
tactician = Player_PC("Tactician", 1, 10, 10, 1, 1, 5, 0, 0)
#function that removes party members
def remove_party(h_p):
        remove = True
        while remove:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_prremove_menu(h_p)
                pygame.display.update()
                if len(h_p) <= 1:
                        remove = False
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_l:
                                        remove = False
                                if event.key == pygame.K_1 or event.key == pygame.K_a:
                                        h_p.pop(0)
                                if event.key == pygame.K_2 or event.key == pygame.K_s:
                                        h_p.pop(1)
                                if event.key == pygame.K_3:
                                        h_p.pop(2)
                                if event.key == pygame.K_4:
                                        h_p.pop(3)
                
#function that manages adjusting party members
def reorder_party(h_p):
        reorder = True
        while reorder:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_prreorder_menu(h_p)
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_l:
                                        reorder = False
                                if event.key == pygame.K_1 or event.key == pygame.K_a:
                                        hero = h_p[0]
                                        copy_hero = copy.copy(hero)
                                        h_p.remove(hero)
                                        h_p.append(copy_hero)
                                if event.key == pygame.K_2 or event.key == pygame.K_s:
                                        hero = h_p[1]
                                        copy_hero = copy.copy(hero)
                                        h_p.remove(hero)
                                        h_p.append(copy_hero)
                                if event.key == pygame.K_3:
                                        hero = h_p[2]
                                        copy_hero = copy.copy(hero)
                                        h_p.remove(hero)
                                        h_p.append(copy_hero)
                                if event.key == pygame.K_4:
                                        hero = h_p[3]
                                        copy_hero = copy.copy(hero)
                                        h_p.remove(hero)
                                        h_p.append(copy_hero)
                
#function that manages adjusting heroes and armor
def private_room(h_p, h_w, h_a):
        room = True
        while room:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_proom_menu()
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_l:
                                        room = False
                                if event.key == pygame.K_p:
                                        reorder_party(h_p)
                                if event.key == pygame.K_r:
                                        remove_party(h_p)
                                if event.key == pygame.K_w:
                                        reorder_weapons(h_p, h_w)
                                if event.key == pygame.K_a:
                                        reorder_armors(h_p, h_a)
                
#function that controls adding heroes to the party
def recruit(h_p):
        recruit = True
        while recruit:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_recruit_menu(h_p)
                pygame.display.update()
                knght = None
                smner = None
                tact = None
                #check for duplicates
                for hero in h_p:
                        if "Knight" in hero.name:
                                knght = hero
                        if "Summoner" in hero.name:
                                smner = hero
                        if "Tactician" in hero.name:
                                tact = hero
                        if len(h_p) >= C.PARTY_LIMT:
                                recruit = False
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_l:
                                        recruit = False
                                #should show character and text after successful recruit
                                if event.key == pygame.K_s and smner == None:
                                        new_hero = copy.copy(summoner)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_k and knght == None:
                                        new_hero = copy.copy(knight)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_t and tact == None:
                                        new_hero = copy.copy(tactician)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_w:
                                        new_hero = copy.copy(warrior)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_c:
                                        new_hero = copy.copy(cleric)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_m:
                                        new_hero = copy.copy(mage)
                                        party_func.add_to_party(h_p, new_hero)
                                if event.key == pygame.K_n:
                                        new_hero = copy.copy(ninja)
                                        party_func.add_to_party(h_p, new_hero)
                                
#function that controls the inn of the city
def inn(h_p, h_b, h_w, h_a):
        inn = True
        while inn:
                clock.tick(P.FPS)
                WIN.fill(P.WHITE)
                WIN.blit(CITY_IMG, P.ORIGIN)
                draw_func.draw_inn_menu()
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_s:
                                        for hero in h_p:
                                                hero.health = hero.maxhealth
                                                hero.mana = hero.maxmana
                                        h_b.coins -= min(len(h_p), h_b.coins)
                                        inn = False
                                if event.key == pygame.K_l:
                                        inn = False
                                if event.key == pygame.K_p:
                                        private_room(h_p, h_w, h_a)
                                if event.key == pygame.K_r and len(h_p) < C.PARTY_LIMIT:
                                        recruit(h_p)
		
	
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
