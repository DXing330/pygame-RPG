import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Object_Classes")
sys.path.append("./General_Functions")
sys.path.append("./Battle_Functions")
import pygame
pygame.init()
import random
import copy
from _constants import Constants
C = Constants
from _list_constants import LConstants
L = LConstants
from _basic_classes import *
from ally_classes import *
from advanced_monster_class import *
M = Monster_Groups()
from damage_class import *
from skill_class import *
from general_class import *
from _draw_classes import *
clock = pygame.time.Clock()


class Battle:
    def __init__(self, party: Party_PC):
        self.party = party
        self.heroes = []
        self.allies = []
        self.monsters = []
        self.monster_tracker = []
        self.fight = True
    
    def make_monsters(self):
        self.level_tracker = 0
        for hero in self.party.battle_party:
            # Check the difficulty of the battle by seeing the heroes levels
            self.level_tracker += hero.level
        # Randomize the difficulty.
        self.difficulty = random.randint(self.level_tracker//2, self.level_tracker)
        # Then generate the monster party based on the difficulty.
        self.monsters = []
        while len(self.monsters) <= 0:
            monster_list = M.MONSTER_GROUPS.get(self.difficulty)
            if monster_list != None:
                for monster in monster_list:
                    copy_monster = copy.copy(monster)
                    self.monsters.append(copy_monster)
            self.difficulty -= 1
        for monster in self.monsters:
            monster.update_for_battle()
            copy_monster = copy.deepcopy(monster)
            self.monster_tracker.append(copy_monster)


    def add_monsters(self, monsters: list):
        self.monsters = monsters
        self.monster_tracker = copy.deepcopy(monsters)
        self.add_from_party()
        self.battle_phase()

    def add_from_party(self):
        for hero in self.party.battle_party:
            copy_hero : Hero_PC = copy.deepcopy(hero)
            self.heroes.append(copy_hero)
        for ally in self.party.allies:
            copy_ally : Ally_NPC = copy.deepcopy(ally)
            copy_ally.update_stats()
            self.allies.append(copy_ally)

    def update_and_draw(self):
        WIN.fill(C.BLACK)
        self.draw_battle = Draw_Battle()
        self.draw_battle.add_heroes(self.heroes)
        self.draw_battle.add_monsters(self.monsters)
        self.draw_battle.add_allies(self.allies)
        self.draw_battle.draw_allies.draw()
        self.draw_battle.draw_heroes.draw()
        self.draw_battle.draw_monsters.draw()

    def start_phase(self):
        self.add_from_party()
        self.make_monsters()
        self.battle_phase()
        
    def hero_attack(self, hero: Character):
        pick_from = Pick_Functions(self.monsters)
        monster: Monster_NPC = pick_from.pick()
        damage = Attack_Functions(hero, monster)
        damage.calculate()

    def hero_magic(self, hero: Character):
        if hero.magic:
            pick_from = Pick_Functions(hero.spell_list)
            spell : Spell_PC = pick_from.pick()
            cast_spell = Spell_Functions(hero, spell, self.monsters)
            cast_spell.cast()

    def hero_skill(self, hero: Hero_PC):
        if hero.skills:
            pick_from = Pick_Functions(hero.skill_list)
            used_skill : Skill_PC = pick_from.pick_skill()
            use_skill = Skill_Functions(hero, used_skill, self.heroes,
            self.allies, self.monsters, pick_randomly = False)
            use_skill.use()

    def heroes_turn(self, hero: Character):
        hero.status_effect()
        hero.buff_effect()
        WIN.fill(C.BLACK)
        self.draw_battle.draw_monsters.draw()
        self.draw_battle.draw_heroes.draw_hero_turn(hero)
        while hero.turn:
            pygame.event.clear()
            clock.tick(C.SLOW_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fight = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_a:
                        pygame.event.clear()
                        hero.turn = False
                        self.hero_attack(hero)
                        break
                    if event.key == pygame.K_s:
                        if len(hero.skill_list) >= 1:
                            pygame.event.clear()
                            hero.turn = False
                            self.hero_skill(hero)
                            break
                    if event.key == pygame.K_m:
                        if len(hero.spell_list) >= 1:
                            pygame.event.clear()
                            hero.turn = False
                            self.hero_magic(hero)
                            break

    def monsters_turn(self, monster: Advanced_Monster):
        monster.status_effect()
        monster.buff_effect()
        monster.passive_skill_effect(self.heroes, self.monsters)
        if monster.turn:
            monster.choose_action(self.heroes, self.monsters)

    def summoned_ally_turn(self, summon: Ally_NPC):
        summon.choose_action(self.heroes, self.monsters)

    def remove_dead_characters(self):
        for monster in self.monsters:
            if monster.health <= 0:
                monster.death_action(self.heroes, self.monsters)
                self.monsters.remove(monster)
        for hero in self.heroes:
            if hero.health <= 0:
                self.heroes.remove(hero)

    def battle_phase(self):
        while self.fight:
            self.standby_phase()
            for hero in self.heroes:
                if len(self.monsters) > 0:
                    self.heroes_turn(hero)
                    self.standby_phase()
            for ally in self.allies:
                self.summoned_ally_turn(ally)
            self.standby_phase()
            for monster in self.monsters:
                if len(self.heroes) > 0:
                    self.monsters_turn(monster)
            self.check_end_phase()
    
    def check_end_phase(self):
        self.remove_dead_characters()
        self.update_and_draw()
        if len(self.monsters) <= 0 or len(self.heroes) <= 0:
            self.fight = False
            self.end_phase()

    def standby_phase(self):
        self.remove_dead_characters()
        self.update_and_draw()
    
    def end_phase(self):
        for hero in self.party.battle_party:
            hero : Hero_PC
            hero.update_after_battle(self.heroes)
        if len(self.monsters) <= 0 and len(self.heroes) > 0:
            for hero in self.party.heroes:
                hero: Hero_PC
                hero.exp += random.randint(0, hero.level//2)
                hero.level_up()
                self.party.items.coins += random.randint(0, hero.level)
            for ally in self.party.allies:
                ally: Ally_NPC
                ally.update_level(self.party)