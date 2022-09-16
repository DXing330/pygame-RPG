import sys
sys.path.append("./Constants_Dictionaries")
sys.path.append("./Object_Classes")
import pygame
pygame.init()
from _basic_classes import *
from _constants import *
from _image_dictionary import Image_Dictionary
I = Image_Dictionary()
C = Constants()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
BIG_FONT = pygame.font.SysFont("comicsans", C.BIG_FONT)
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
SMALL_FONT = pygame.font.SysFont("comicsans", C.SML_FONT)


class Draw_Screen:
    def __init__(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def add_party(self, party: Party_PC):
        self.party = party

    def draw_stats(self):
        self.party_counter = 1
        for hero in self.party.heroes:
            hero: Hero_PC
            hero_stats = hero.view_stats()
            stat_text = FONT.render(hero_stats, 1, C.WHITE)
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING,
            C.PADDING * self.party_counter))
            self.party_counter += 1
        for ally in self.party.allies:
            ally: Ally_NPC
            ally_stats = ally.view_stats()
            stat_text = FONT.render(ally_stats, 1, C.WHITE)
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING,
            C.PADDING * self.party_counter))
            self.party_counter += 1

    def draw_text(self, text: str):
        self.text = FONT.render(text, 1, C.WHITE)
        WIN.fill(C.BLACK)
        WIN.blit(self.text, ((self.width - self.text.get_width())//2, C.PADDING))
        pygame.display.update()
        pygame.time.delay(500)

    def draw_list(self, list: list):
        self.list = list
        self.object_counter = 1
        WIN.fill(C.BLACK)
        for object in self.list:
            self.text = FONT.render(object.name, 1, C.WHITE)
            WIN.blit(self.text, ((self.width - self.text.get_width())//2,
            C.PADDING * self.object_counter))
            self.object_counter += 1
        pygame.display.update()


class Draw_Allies:
    def __init__(self, allies: list):
        self.allies = allies
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_allies(self):
        self.ally_counter = 2
        for ally in self.allies:
            ally: Ally_NPC
            ally.sprite = I.ally_images.get(ally.name)
            WIN.blit(ally.sprite, (self.width - C.PADDING - (ally.sprite.get_width() * self.ally_counter/2),
            self.height//2 + ally.sprite.get_height() * (self.ally_counter)))
            self.ally_counter += 1

    def draw(self):
        self.draw_allies()
        pygame.display.update()


class Draw_Heroes:
    def __init__(self, heroes: list):
        self.heroes = heroes
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_heroes(self):
        self.hero_counter = 2
        for hero in self.heroes:
            hero: Character
            hero.sprite = I.hero_images.get(hero.name)
            # Draws the heroes in order, starting from the bottom right corner, going up diagonally.
            WIN.blit(hero.sprite, (self.width - C.PADDING - (hero.sprite.get_width() * (self.hero_counter/2)),
            (self.height - hero.sprite.get_height() * (self.hero_counter))))
            self.hero_counter += 1

    def hero_stat_text(self):
        hero_stats = self.hero.view_battle_stats()
        stat_text = SMALL_FONT.render(hero_stats, 1, C.WHITE)
        return stat_text

    def draw_heroes_stats(self):
        self.hero_counter = 2
        for hero in self.heroes:
            self.hero : Character = hero
            stat_text = self.hero_stat_text()
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING,
            C.PADDING * self.hero_counter))
            self.hero_counter += 1
            
    def draw(self):
        self.draw_heroes()
        self.draw_heroes_stats()
        pygame.display.update()

    def draw_hero_stats(self):
        stat_text = self.hero_stat_text()
        WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING,
        C.PADDING * 2))

    def draw_hero(self):
        self.hero.sprite = I.hero_images.get(self.hero.name)
        WIN.blit(self.hero.sprite, (self.width - C.PADDING - (self.hero.sprite.get_width()),
        (self.height - self.hero.sprite.get_height())))

    def draw_hero_turn_menu(self):
        attack_text = FONT.render("A: Attack", 1, C.WHITE)
        WIN.blit(attack_text, ((self.width - attack_text.get_width())//2, C.PADDING * 1))
        item_text = FONT.render("I: Use Items", 1, C.WHITE)
        WIN.blit(item_text, ((self.width - item_text.get_width())//2, C.PADDING * 2))
        if self.hero.skill > 0:
            skill_text = FONT.render("S: Use Skill", 1, C.WHITE)
            WIN.blit(skill_text, ((self.width - skill_text.get_width())//2, C.PADDING * 3))
        if self.hero.mana > 0:
            magic_text = FONT.render("M: Use Magic", 1, C.WHITE)
            WIN.blit(magic_text, ((self.width - magic_text.get_width())//2, C.PADDING * 4))

    def draw_hero_turn(self, hero: Character):
        self.hero = hero
        self.draw_hero()
        self.draw_hero_stats()
        self.draw_hero_turn_menu()
        pygame.display.update()


class Draw_Monsters:
    def __init__(self, monsters: list):
        self.monsters = monsters
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_monsters(self):
        self.monster_counter = 2
        self.height_checker = 2
        for monster in self.monsters:
            monster: Monster_NPC
            monster.sprite = I.monster_images.get(monster.name)
            WIN.blit(monster.sprite, ((monster.sprite.get_width() * (self.monster_counter/2)),
            (self.height - (monster.sprite.get_height() * (self.height_checker)))))
            self.monster_counter += 1
            self.height_checker += 1
            # If there are too many monsters then draw them in seperate rows
            if C.MONSTER_SIZE * self.height_checker >= self.height:
                self.monster_counter = 4
                self.height_checker = 2

    def draw_monster_stat(self):
            monster_stats = self.monster.view_battle_stats()
            stat_text = SMALL_FONT.render(monster_stats, 1, C.WHITE)
            return stat_text

    def draw_monster_stats(self):
        self.monster_counter = 2
        for monster in self.monsters:
            self.monster: Monster_NPC = monster
            stat_text = self.draw_monster_stat()
            WIN.blit(stat_text, (C.PADDING, C.PADDING * self.monster_counter))
            self.monster_counter += 1

    def draw(self):
        self.draw_monsters()
        self.draw_monster_stats()
        pygame.display.update()