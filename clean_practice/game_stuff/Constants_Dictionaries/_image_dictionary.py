import pygame
pygame.init()
import os
from _constants import *
C = Constants()

ANGEL = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL = pygame.transform.scale(ANGEL, (C.PLAYER_SIZE//2, C.PLAYER_SIZE//2))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BEAST = pygame.image.load(os.path.join("Assets", "beast.png"))
BEAST = pygame.transform.scale(BEAST, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png"))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
BIG_GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE * 2, C.MONSTER_SIZE * 2))

class Image_Dictionary:
    def __init__(self):
        self.hero_images = {
        "Summoner" : SUMMONER,
        "Golem" : GOLEM,
        "Golem_Lord" : BIG_GOLEM
        }
        self.monster_images = {
        "Goblin" : GOBLIN,
        "Werewolf" : BEAST,
        "Wolf" : BEAST
        }
        self.ally_images = {
        "Angel" : ANGEL
        }