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
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)


class RPG_Game:
    def __init__(self, party: Party_PC):
        self.party = party
        self.monsters = []
    
    def monster_maker(self):
        pass

    def battle(self):
        pass

    def home_screen(self):
        pass

    def save(self):
        pass