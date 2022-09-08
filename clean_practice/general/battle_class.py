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
from ally_classes import *
from _advanced_classes import *
from damage_class import *
from general_class import *
clock = pygame.time.Clock()


class Battle:
    def __init__(self, game: RPG_Game):
        self.game = game
        self.heroes = []
        self.allies = []
        self.monsters = []
        self.monster_tracker = []
        self.fight = True
    
    def make_monsters(self):
        for hero in self.game.party.heroes:
            monster = Monster_NPC(hero.level, L.monster_types[random.randint(0, len(L.monster_types)-1)],
            L.elements[random.randint(0, len(L.elements)-1)])
            monster.update_stats()
            self.monsters.append(monster)
            copy_monster = copy.deepcopy(monster)
            self.monster_tracker.append(monster)

    def add_from_party(self):
        for hero in self.game.party.heroes:
            copy_hero : Hero_PC = copy.deepcopy(hero)
            copy_hero.update_stats()
            copy_hero.update_skills()
            self.heroes.append(copy_hero)
        for ally in self.game.party.allies:
            copy_ally : Ally_NPC = copy.deepcopy(ally)
            copy_ally.update_stats()
            self.allies.append(copy_ally)

    def start_phase(self):
        self.add_from_party()
        self.make_monsters()
        
    def hero_attack(self, hero: Hero_PC):
        pick_from = Pick_Functions(self.monsters)
        monster = pick_from.pick()
        damage = Damage_Functions(hero, monster)
        damage.calculate

    def hero_skill(self, hero: Hero_PC):
        pick_from = Pick_Functions(hero.skill_list)
        used_skill : Skill_PC = pick_from.pick()
        if hero.skill > used_skill.cost:
            hero.skill -= used_skill.cost

    def heroes_turn(self, hero: Hero_PC):
        hero.status_effect()
        hero.buff_effect()
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
            if keys.key == pygame.K_s:
                if len(hero.skill_list) > 0:
                    pygame.event.clear()
                    turn = False
                    self.hero_skill(hero)
                    break

    def monsters_turn(self, monster: Monster_NPC):
        monster.status_effect()
        monster.buff_effect()
        pick_from = Pick_Functions(self.heroes)
        hero = pick_from.pick_randomly()
        damage = Damage_Functions(monster, hero)
        damage.calculate

    def remove_dead_characters(self):
        for monster in self.monsters:
            if monster.health <= 0:
                self.monsters.remove(monster)
        for hero in self.heroes:
            if hero.health <= 0:
                self.heroes.remove(hero)

    def summoned_ally_turn(self, summon: Ally_NPC):
        summon.choose_action(self.heroes, self.monsters)

    def battle_phase(self):
        while self.fight:
            self.check_end_phase
            for hero in self.heroes:
                self.heroes_turn(hero)
            self.check_end_phase
            for ally in self.allies:
                self.summoned_ally_turn(ally)
            self.check_end_phase
            for monster in self.monsters:
                self.monsters_turn(monster)
            self.check_end_phase
    
    def check_end_phase(self):
        self.remove_dead_characters
        if len(self.monsters) <= 0 or len(self.heroes) <= 0:
            self.fight = False
            self.end_phase()
    
    def end_phase(self):
        if len(self.monsters) <= 0 and len(self.heroes) > 0:
            for hero in self.game.party.heroes:
                hero.exp += random.randint(1, hero.level)
                hero.level_up()
                self.game.party.items.coins += hero.level
