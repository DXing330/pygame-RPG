import random
import sys
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
from rpg2_constants import Constants
C = Constants()
#function which controls the levelling up of players
def level_up(p_pc):
        #check if the player is at the level limit
        if p_pc.level < C.LEVEL_LIMIT:
                p_pc.level += 1
                #adjust the player's stats according to their new level
                p_pc.atk += (p_pc.atk/(p_pc.level - 1))
                p_pc.defense += (p_pc.defense/(p_pc.level - 1))
                p_pc.maxhealth += (p_pc.maxhealth/(p_pc.level - 1))
                p_pc.skill += (p_pc.skill/(p_pc.level - 1))
                p_pc.maxmana += (p_pc.maxmana/(p_pc.level - 1))
        #if the player is already max level then nothing happens
        elif p_pc.level == C.LEVEL_LIMIT:
                print ("Sorry, it looks like you're already too strong.")


def exp_level_up(hero):
        x = 0
        if hero.exp >= hero.level ** C.INCREASE_EXPONENT:
                x = 1
                hero.exp -= hero.level ** C.INCREASE_EXPONENT
                hero.level += 1
                hero.maxhealth += C.LVL_UP_HP_LOW
                hero.atk += C.LVL_UP_ATK_LOW
                hero.defense += C.LVL_UP_DEF_LOW
                hero.skill += C.LVL_UP_SKL_LOW
                if "Knight" in hero.name:
                        hero.defense += C.LVL_UP_DEF_HIGH
                elif "Mage" in hero.name:
                        hero.maxmana += C.LVL_UP_MANA_HIGH
                elif "Warrior" in hero.name:
                        hero.atk += C.LVL_UP_ATK_HIGH
                elif "Cleric" in hero.name:
                        hero.maxmana += C.LVL_UP_MANA_MID
                        hero.skill += C.LVL_UP_SKL_LOW
                elif "Summoner" in hero.name:
                        hero.maxmana += C.LVL_UP_MANA_MID
                        hero.skill += C.LVL_UP_SKL_LOW
                elif "Ninja" in hero.name:
                        hero.skill += C.LVL_UP_SKL_HIGH
                elif "Hunter" in hero.name:
                        hero.skill += C.LVL_UP_SKL_MID
                        hero.atk += C.LVL_UP_ATK_LOW
                elif "Tactician" in hero.name:
                        hero.defense += C.LVL_UP_DEF_MID
                        hero.skill += C.LVL_UP_SKL_LOW
                elif "Hero" in hero.name:
                        hero.atk += C.LVL_UP_ATK_LOW
                        hero.defense += C.LVL_UP_DEF_LOW
                        hero.skill += C.LVL_UP_SKL_LOW
                        hero.maxmana += C.LVL_UP_MANA_LOW
        return x
                        
#function that levels up further
def prestige_level_up(p_pc):
        if p_pc.level < C.LEVEL_LIMIT * C.INCREASE_EXPONENT:
                p_pc.level += 1
                if "Knight" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_HIGH
                        p_pc.defense += C.LVL_UP_DEF_HIGH
                elif "Summoner" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_LOW
                        p_pc.maxmana += C.LVL_UP_MANA_MID
                elif "Mage" in p_pc.name:
                        p_pc.maxmana += C.LVL_UP_MANA_HIGH
                        p_pc.skill += C.LVL_UP_SKL_MID
                elif "Cleric" in p_pc.name:
                        p_pc.defense += C.LVL_UP_DEF_MID
                        p_pc.skill += C.LVL_UP_SKL_MID
                elif "Warrior" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.atk += C.LVL_UP_ATK_HIGH
                        p_pc.defense += C.LVL_UP_DEF_MID
                elif "Ninja" in p_pc.name:
                        p_pc.atk += C.LVL_UP_HP_LOW
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Hunter" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Tactician" in p_pc.name:
                        p_pc.defense += C.LVL_UP_DEF_LOW
                        p_pc.skill += C.LVL_UP_SKL_HIGH
                elif "Hero" in p_pc.name:
                        p_pc.maxhealth += C.LVL_UP_HP_MID
                        p_pc.atk += C.LVL_UP_ATK_HIGH
                        p_pc.defense += C.LVL_UP_DEF_MID
                        p_pc.skill += C.LVL_UP_SKL_LOW
                        p_pc.maxmana += C.LVL_UP_MANA_MID
        else:
                print ("This is the limit of what I can do for you. ")

#function that changes the player's class into a prestige class
def prestige_class(p_pc):
        if p_pc.name == "Cleric":
                p_pc.name = "High Cleric"
        elif p_pc.name == "Warrior":
                p_pc.name = "Fierce Warrior"
        elif p_pc.name == "Summoner":
                p_pc.name = "Grand Summoner"
        elif p_pc.name == "Mage":
                p_pc.name = "Arch Mage"
        elif p_pc.name == "Knight":
                p_pc.name = "Royal Knight"
        elif p_pc.name == "Ninja":
                p_pc.name = "Shadow Ninja"
        elif p_pc.name == "Tactician":
                p_pc.name = "Master Tactician"
        elif p_pc.name == "Hunter":
                p_pc.name = "Monster Hunter"
        elif p_pc.name == "Hero":
                p_pc.name = "Chosen Hero"


#functions that increase player stats
def skill_up(p_pc):
        p_pc.skill += 1
def atk_up(p_pc):
        p_pc.atkbonus += 1
def def_up(p_pc):
        p_pc.defbonus += 1
def mana_up(p_pc):
        p_pc.mana += 1
#function that will increase the pet's stage
def angel_stage_up(p_npc):
        #check if the pet is at the stage limit
        if p_npc.stage < C.STAGE_LIMIT:
                p_npc.stage += 1
                #adjust the pet's atk according to it's new level
                p_npc.atk += round(p_npc.atk * C.PET_ATK_UP)
                if p_npc.stage == 2:
                        p_npc.name = "Awoken " + p_npc.name
                elif p_npc.stage == 3:
                        p_npc.name = "Mega " + p_npc.name
                elif p_npc.stage == 4:
                        p_npc.name = "Archangel"
                elif p_npc.stage == 5:
                        p_npc.name = "Guardian Angel"
                elif p_npc.stage == 6:
                        p_npc.name = "Legendary Guardian Angel"
        #if the pet is already fully evolved then nothing happens
        elif p_npc.stage == C.STAGE_LIMIT:
                print ("Sorry, it's already too powerful.")
def spirit_stage_up(p_npc):
        if p_npc.stage < C.STAGE_LIMIT:
                p_npc.stage += 1
                p_npc.atk += round(p_npc.atk * C.PET_ATK_UP)
                if p_npc.stage == 3:
                        p_npc.name = "Awoken Spirit"
                elif p_npc.stage == 6:
                        p_npc.name = "Guardian Spirit"
def pet_atk_up(p_npc):
        if p_npc.stage == C.STAGE_LIMIT:
                p_npc.atk += 1
        else:
                print ("It's not ready yet.")
import random
import sys
sys.path.append(".")
from rpg2_classdefinitions import (Player_PC, Pet_NPC, Monster_NPC,
                                   ItemBag_PC, Spell_PC, Weapon_PC,
                                   Armor_PC)
from rpg2_constants import Constants
C = Constants()
#function that adds a hero to the hero party list
def add_to_party(h_p, p_pc):
        #if the party isn't full you can add them
        if len(h_p) < C.PARTY_LIMIT:
                h_p.append(p_pc)
        else:
                print ("The party is already full.")
#function that removes a hero from the hero party list
def remove_from_party(heroes_party):
        try:
                number = int(input("Which hero?"
                                       "(First hero is number 1, etc.)"))
                if 0 < number <= len(heroes_party):
                        heroes_party.pop(number - 1)
                else:
                        print ("That's fine if you changed your mind.")
        except (ValueError, AttributeError):
                print ("That's fine if you changed your mind.")

#function that will pick a hero from the party
def pick_hero(heroes_party):
        hero = None
        if len(heroes_party) > 1:
                try:
                        number = int(input("Which one?"
                                               "(First one is number 1, etc.)"))
                        if 0 < number <= len(heroes_party):
                                hero = heroes_party[(number - 1)]
                        else:
                                print ("That's not a real choice.")
                                hero = pick_hero(heroes_party)
                except (ValueError, AttributeError):
                        print ("That's not a real choice.")
                        hero = pick_hero(heroes_party)
        elif len(heroes_party) == 1:
                hero = heroes_party[0]
        return hero
#function that picks a random hero from the party with health > 0
def pick_random_healthy_hero(heroes_party):
        hero = None
        #if there's a defender in the party, pick him first
        for player  in heroes_party:
                if "Defender" in player.name and player.health > 0:
                        hero = player
        #if there's no defender then try to pick a random hero
        if hero == None:
                try:
                        if len(heroes_party) > 1:                                        
                                x = random.randint(0, len(heroes_party) - 1)
                                hero = heroes_party[x]
                                if hero.health <=0:
                                        hero = pick_random_healthy_hero(heroes_party)
                                return hero
                        else:
                                hero = heroes_party[0]
                                return hero

                except:
                        print ("The heroes have all been defeated.")
                        hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                        return hero
        else:
                return hero
def pet_pick_random_healthy_hero(heroes_party):
        hero = None
        try:
                if len(heroes_party) > 1:                                        
                        x = random.randint(0, len(heroes_party) - 1)
                        hero = heroes_party[x]
                        #don't pick golems
                        if hero.health <=0 or hero.name == "Totem":
                                hero = pet_pick_random_healthy_hero(heroes_party)
                        return hero
                else:
                        hero = heroes_party[0]
                        if hero.name != "Totem":
                                return hero
                        else:
                                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                                return hero

        except:
                print ("The heroes have all been defeated.")
                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                return hero
def pet_pick_random_injured_hero(heroes_party):
        hero = None
        try:
                if len(heroes_party) > 1:                                        
                        x = random.randint(0, len(heroes_party) - 1)
                        hero = heroes_party[x]
                        #only pick heroes, not golems, heros need to be injured but still conscious
                        if hero.health <=0 or hero.name == "Totem" or hero.health >= hero.maxhealth:
                                hero = pet_pick_random_healthy_hero(heroes_party)
                        return hero
                else:
                        hero = heroes_party[0]
                        if hero.name != "Totem" and hero.health > 0:
                                return hero
                        else:
                                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                                return hero

        except:
                print ("The heroes have all been defeated.")
                hero = Player_PC("nothing", 1, 0, 0, 0, 0, 0, 0, 0)
                return hero
#function that picks a random monster from the party who has been injured
def pick_random_healthy_monster(monster_party):
        try:
                if len(monster_party) > 1:
                        x = random.randint(0, len(monster_party) - 1)
                        monster = monster_party[x]
                        if monster.health <= 0:
                                monster = pick_random_healthy_monster(monster_party)
                elif len(monster_party) == 1:
                        monster = monster_party[0]
        except:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
def pet_pick_random_monster(monster_party):
        try:
                if len(monster_party) > 1:
                        x = random.randint(0, len(monster_party) - 1)
                        monster = monster_party[x]
                        #don't pick bombs
                        if monster.health <= 0 or "Bomb" in monster.name:
                                monster = pet_pick_random_monster(monster_party)
                elif len(monster_party) == 1:
                        monster = monster_party[0]
        except:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
#function that picks a monster
def pick_monster(monster_party):
        monster = None
        if len(monster_party) > 1:
                try:
                        x = int(input("Which monster?"
                                      "(First monster is number 1, etc.)"))
                        if 0 < x <= len(monster_party):
                                monster = monster_party[(x - 1)]
                        else:
                                print ("That's not a real choice.")
                                monster = pick_monster(monster_party)
                except (ValueError, AttributeError):
                        print ("That's not a real choice.")
                        monster = monster_party[0]
        elif len(monster_party) == 1:
                monster = monster_party[0]
        else:
                monster = Monster_NPC("nothing", 0, 0, 0, 0, "None", 0)
        return monster
#function that checks for equipment
def check_equipment(hero, equipment_list):
        equipment = None
        for equip in equipment_list:
                if equip.user == hero.name:
                        equipment = equip
        return equipment
#function that picks the lowest health character
def pick_lowest_health(h_p):
        #start with 100% health
        x = 100
        hro = None
        #repeat this process a few times to make sure you pick the lowest health hero
        for z in range(0, len(h_p)):
                #then check each characters health percentage
                for hero in h_p:
                        #make sure to only count health heroes
                        if hero.health > 0 and hero.name != "Totem":
                                #multiply by 100 to get an rounded percentage
                                y = round((hero.health/hero.maxhealth), 2) * 100
                                #if the percentage is lower then pick that hero
                                if y < x:
                                        x = y
                                        hro = hero
        return hro

#function that picks the highest health character
def pick_highest_health(h_p):
        #start with 0% health
        x = 0
        hro = None
        #repeat this process a few times to make sure you pick the highest health hero
        for z in range(0, len(h_p)):
                #then check each characters health percentage
                for hero in h_p:
                        #make sure to only count healthy heroes
                        if hero.health > 0 and hero.name != "Totem":
                                #multiply by 100 to get an rounded percentage
                                y = round((hero.health/hero.maxhealth), 2) * 100
                                #if the percentage is higher then pick that hero
                                if y > x:
                                        x = y
                                        hro = hero
        return hro

#function that lets a monster pick another monster to attack
def pick_different_monster(m_npc, m_p):
        target = None
        if len(m_p) > 1:
                target = pick_random_healthy_monster(m_p)
                if target == m_npc:
                        target = pick_different_monster(m_npc, m_p)
        return target

#function that heals the party to full
def recover(h_p):
        for hero in h_p:
                hero.health = hero.maxhealth
                hero.mana = hero.maxmana
