import pygame
pygame.init()
from _basic_classes import *
from _constants import *
from _image_dictionary import Image_Dictionary
I = Image_Dictionary()
C = Constants()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
FONT = pygame.font.SysFont("comicsans", 25)


class Draw_Party:
    def __init__(self, party: Party_PC):
        self.party = party

    def draw_heroes(self):
        for hero in self.party.heroes:
            pass


class Draw_Monsters:
    def __init__(self, monsters):
        self.monsters = monsters