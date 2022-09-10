import pygame
pygame.init()
from _basic_classes import *
from advanced_monster_class import *
from _constants import *
from _image_dictionary import Image_Dictionary
I = Image_Dictionary()
C = Constants()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
FONT = pygame.font.SysFont("comicsans", 25)


class Draw_Home_Screen:
    def __init__(self, party: Party_PC):
        self.party = party
        self.width = WIN.get_width()
        self.height = WIN.get_height()

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


class Draw_Allies:
    def __init__(self, allies: list):
        self.allies = allies
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_allies(self):
        self.ally_counter = 2
        for ally in self.allies:
            ally: Ally_NPC
            ally.sprite = I.ally_images.get(ally.race)
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

    def draw_heroes_stats(self):
        self.hero_counter = 2
        for hero in self.heroes:
            hero: Character
            hero_stats = hero.view_battle_stats()
            stat_text = FONT.render(hero_stats, 1, C.WHITE)
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING,
            C.PADDING * self.hero_counter))
            self.hero_counter += 1
            

    def draw(self):
        self.draw_heroes()
        self.draw_heroes_stats()
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
            monster.sprite = I.monster_images.get(monster.race)
            WIN.blit(monster.sprite, ((monster.sprite.get_width() * (self.monster_counter/2)),
            (self.height - (monster.sprite.get_height() * (self.height_checker)))))
            self.monster_counter += 1
            self.height_checker += 1
            # If there are too many monsters then draw them in seperate rows
            if C.MONSTER_SIZE * self.height_checker >= self.height:
                self.monster_counter = 4
                self.height_checker = 2

    def draw_monster_stats(self):
        self.monster_counter = 2
        for monster in self.monsters:
            monster: Monster_NPC
            monster_stats = monster.view_battle_stats()
            stat_text = FONT.render(monster_stats, 1, C.WHITE)
            WIN.blit(stat_text, (C.PADDING, C.PADDING * self.monster_counter))
            self.monster_counter += 1

    def draw(self):
        self.draw_monsters()
        self.draw_monster_stats()
        pygame.display.update()