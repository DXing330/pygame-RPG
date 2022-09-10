import pygame
pygame.init()
from _constants import *
C = Constants()
from _basic_classes import *


class Upgrade:
    def __init__(self, party: Party_PC):
        self.party = party

    def upgrade_ally(self):
        self.summoner_level = 1
        for hero in self.party.heroes:
            hero: Hero_PC
            if "Summoner" in hero.class_name: self.summoner_level = hero.level
        for ally in self.party.allies:
            ally: Ally_NPC
            if ally.level < self.summoner_level: ally.level = self.summoner_level