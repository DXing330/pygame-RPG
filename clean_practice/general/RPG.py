import math
import json
import random
import copy
import pygame
pygame.init()
from _constants import *
C = Constants()
from _basic_classes import *
from ally_classes import *
from general_class import *
from save_class import *
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)

class RPG_Game:
    def __init__(self):
        self.party = None

    def add_party(self, party: Party_PC):
        self.party = party

    def new_game(self):
        party = Party_PC()
        hero = Hero_PC("Summoner", 1, 0)
        party.add_hero(hero)
        ally = Angel_NPC("Angel", 1)
        party.add_ally(ally)
        self.add_party(party)
    
    def load_game(self):
        load_game = Save_Functions()
        load_game.load()
        self.party = load_game.party

    def save_game(self):
        save_game = Save_Functions()
        save_game.add_party(self.party)
        save_game.save()

    def Start(self):
        start = True
        while start:
            WIN.fill((0, 0, 0))
            pygame.display.update()
            pygame.event.clear()
            clock.tick(C.SLOW_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_n:
                        start = False
                        self.new_game()
                        print ("new")
                        self.Game()
                    if event.key == pygame.K_l:
                        self.load_game()
                        print ("loaded")
                        self.Game()

    def Game(self):
        game = True
        while game:
            WIN.fill((0, 0, 0))
            pygame.display.update()
            pygame.event.clear()
            clock.tick(C.SLOW_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game = False
                        pygame.quit()
                    if event.key == pygame.K_r:
                        self.save_game()
                        print ("saved")

def Start_Game():
    start = True
    Game = RPG_Game()
    Game.Start()

Start_Game()