import pygame
pygame.init()
import random
import sys
sys.path.append("../../../RPG2v3/RPG2v3_functions/RPG2v3_def")
sys.path.append("..")
sys.path.append("../pygame_draw")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC)
import rpg2_party_management_functions as party_func
from rpg2_constants import Constants
C = Constants()
from pygconstants import PYGConstants
P = PYGConstants()
import draw_effects as draw_func
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
REG_FONT = pygame.font.SysFont("comicsans", 20)
#always make a clock
clock = pygame.time.Clock()
#function that controls what the pet will do during battle
#need to input the pet and both parties
def angel_random_action(p_npc, h_p, m_p):
        z = random.randint(0, p_npc.stage)
        if z == 0:
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.poison -= min(p_npc.stage, hero.poison)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.poison -= min(p_npc.stage, hero.poison)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
        elif z == 1:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.health -= max((p_npc.atk - monster.defense), 1)
                hero = party_func.pet_pick_random_injured_hero(h_p)
                hero.poison -= min(p_npc.stage, hero.poison)
                hero.health = min((hero.health + round(p_npc.atk ** C.PET_HP_BUFF)), hero.maxhealth)
        elif z == 2:
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
        elif z == 3:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
        elif z == 4:
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                hero = party_func.pet_pick_random_healthy_hero(h_p)
                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
        elif z == 5:
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                monster = party_func.pick_random_healthy_monster(m_p)
                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
        elif z >= 6:
                draw_func.angel_legendary_action(p_npc, h_p, m_p)
                for hero in h_p:
                        if hero.name != "Totem":
                                hero.poison -= min(p_npc.stage, hero.poison)
                                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                                hero.health = min(hero.health + round(p_npc.atk ** C.PET_HP_BUFF), hero.maxhealth)
                                
                for monster in m_p:
                        monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                        monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)

def angel_action(p_npc, h_p, m_p):
        for hero in h_p:
                if "Summoner" in hero.name:
                        angel_random_action(p_npc, h_p, m_p)
                elif "Hero" in hero.name:
                        hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                        hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                        hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                        hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                        hero.poison -= min(p_npc.stage, hero.poison)                        
                elif "Totem" in hero.name:
                        if hero.atk > 0:
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.health -= max((p_npc.atk - monster.defense), 1)
                        elif hero.skill > 0:
                                hero = party_func.pet_pick_random_healthy_hero(h_p)
                                hero.maxhealth += round(p_npc.atk ** C.PET_HP_BUFF)
                                hero.atkbonus += round(p_npc.atk ** C.PET_ATK_BUFF)
                                hero.defbonus += round(p_npc.atk ** C.PET_DEF_BUFF)
                                hero.skill += round(p_npc.atk ** C.PET_SKILL_BUFF)
                        elif hero.defense > 0:
                                hero = party_func.pet_pick_random_injured_hero(h_p)
                                hero.poison -= min(p_npc.stage, hero.poison)
                                hero.health = min((hero.health + p_npc.atk), hero.maxhealth)
                        elif hero.mana > 0:
                                monster = party_func.pick_random_healthy_monster(m_p)
                                monster.atk = max(monster.atk - round(p_npc.atk ** C.PET_ATK_BUFF), 0)
                                monster.defense = max(monster.defense - round(p_npc.atk ** C.PET_DEF_BUFF), 0)
                else:
                        x = random.randint(0, C.PET_ACTION_UP * len(h_p) * len(m_p))
                        if x == 0:
                                angel_random_action(p_npc, h_p, m_p)

#companions actions
def companion_action(p_npc, h_p, m_p):
        for hero in h_p:
                if "Hunter" in hero.name:
                        x = random.randint(0, p_npc.stage)
                        if x < 3:
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
                        elif x < 6:
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
                        else:
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
                                mon = party_func.pet_pick_random_monster(m_p)
                                mon.poison += p_npc.atk//p_npc.stage
                                mon.health -= mon.poison
