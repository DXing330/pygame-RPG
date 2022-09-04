import pygame
pygame.init()
import math
import random
import sys
import copy
from _constants import Constants
C = Constants
from _list_constants import LConstants
L = LConstants
from _basic_classes import *
from _advanced_classes import *
from pick_func import *
clock = pygame.time.Clock()


class Battle:
    def __init__(self, game: RPG_Game):
        self.game = game
        self.heroes = []
        self.allies = []
        self.equipment = []
        self.monsters = []
        self.monster_tracker = []
    
    def make_monsters(self):
        for hero in self.game.party.heroes:
            monster = Monster_NPC(hero.level, L.monster_types[random.randint(0, len(L.monster_types)-1)],
            L.elements[random.randint(0, len(L.elements)-1)])
            monster.get_stats()
            self.monsters.append(monster)
            copy_monster = copy.deepcopy(monster)
            self.monster_tracker.append(monster)

    def add_from_party(self):
        for hero in self.game.party.heroes:
            copy_hero = copy.deepcopy(hero)
            self.heroes.append(copy_hero)
        for ally in self.game.party.allies:
            copy_ally = copy.deepcopy(ally)
            self.allies.append(copy_ally)
        for equipment in self.game.party.equipment:
            copy_equipment = copy.deepcopy(equipment)
            self.equipment.append = copy.deepcopy(equipment)
        
    def hero_attack(self, hero: Hero_PC):
        pass

    def heroes_turn(self, hero: Hero_PC):
        turn = True
        while turn:
            pygame.event.clear()
            clock.tick(C.SLOW_FPS)
            keys = pygame.key.get_pressed()
            if keys.key == pygame.K_a:
                pygame.event.clear()
                turn = False
                self.hero_attack(hero)
                break

    def monsters_turn(self, monster: Monster_NPC):
        pass

    def summoned_ally_turn(self, summon: Ally_NPC):
        pass

    def battle_phase(self):
        pass
    
    def end_phase(self):
        if len(self.monsters) <= 0 and len(self.heroes) > 0:
            for hero in self.game.party.heroes:
                hero.exp += random.randint(1, hero.level)
                self.game.party.items.coins += hero.level
                for battler in self.heroes:
                    if battler.name == hero.name:
                        hero.health = min(battler.health, hero.max_health)
                        hero.mana = min(battler.mana, hero.max_mana)
                        hero.skill = min(battler.skill, hero.max_skill)
