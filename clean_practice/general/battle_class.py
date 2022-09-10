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
        for hero in self.party.heroes:
            monster = Advanced_Monster(L.monster_types[random.randint(0, len(L.monster_types) - 1)], hero.level,
            L.elements[random.randint(0, len(L.elements) - 1)])
            self.monsters.append(monster)
            copy_monster = copy.deepcopy(monster)
            self.monster_tracker.append(copy_monster)

    def add_from_party(self):
        for hero in self.party.heroes:
            copy_hero : Hero_PC = copy.deepcopy(hero)
            copy_hero.update_stats()
            copy_hero.update_skills()
            copy_hero.update_equipment(self.party.equipment)
            copy_hero.update_spells()
            self.heroes.append(copy_hero)
        for ally in self.party.allies:
            copy_ally : Ally_NPC = copy.deepcopy(ally)
            copy_ally.update_stats()
            self.allies.append(copy_ally)

    def update_and_draw(self):
        WIN.fill(C.BLACK)
        draw_party = Draw_Heroes(self.heroes)
        draw_allies = Draw_Allies(self.allies)
        draw_monsters = Draw_Monsters(self.monsters)
        draw_allies.draw()
        draw_party.draw()
        draw_monsters.draw()

    def start_phase(self):
        self.add_from_party()
        self.make_monsters()
        
    def hero_attack(self, hero: Character):
        pick_from = Pick_Functions(self.monsters)
        monster = pick_from.pick()
        damage = Attack_Functions(hero, monster)
        damage.calculate

    def hero_magic(self, hero: Hero_PC):
        magic = True
        for status in hero.status:
            if status.effect == "Disable" and status.effect_specifics == "Magic":
                magic = False
        if magic:
            pick_from = Pick_Functions(hero.spell_list)
            spell : Spell_PC = pick_from.pick()
            cast_spell = Spell_Functions(hero, spell, self.monsters)
            cast_spell.cast()

    def hero_skill(self, hero: Hero_PC):
        skill = True
        for status in hero.status:
            if status.effect == "Disable" and status.effect_specifics == "Skills":
                skill = False
        if skill:
            pick_from = Pick_Functions(hero.skill_list)
            used_skill : Skill_PC = pick_from.pick()
            use_skill = Skill_Functions(hero, used_skill, self.heroes, self.allies, self.monsters)
            use_skill.use()

    def heroes_turn(self, hero: Character):
        hero.status_effect()
        hero.buff_effect()
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
        if monster.turn:
            monster.choose_action(self.heroes)

    def summoned_ally_turn(self, summon: Ally_NPC):
        summon.choose_action(self.heroes, self.monsters)

    def remove_dead_characters(self):
        for monster in self.monsters:
            if monster.health <= 0:
                self.monsters.remove(monster)
        for hero in self.heroes:
            if hero.health <= 0:
                self.heroes.remove(hero)

    def battle_phase(self):
        while self.fight:
            self.standby_phase()
            for hero in self.heroes:
                self.heroes_turn(hero)
                self.standby_phase()
            for ally in self.allies:
                self.summoned_ally_turn(ally)
            self.standby_phase()
            for monster in self.monsters:
                self.monsters_turn(monster)
            self.check_end_phase()
    
    def check_end_phase(self):
        self.remove_dead_characters()
        if len(self.monsters) <= 0 or len(self.heroes) <= 0:
            self.fight = False
            self.end_phase()

    def standby_phase(self):
        self.remove_dead_characters()
        self.update_and_draw()
    
    def end_phase(self):
        if len(self.monsters) <= 0 and len(self.heroes) > 0:
            for hero in self.party.heroes:
                hero.exp += random.randint(0, hero.level)
                hero.level_up()
                self.party.items.coins += hero.level