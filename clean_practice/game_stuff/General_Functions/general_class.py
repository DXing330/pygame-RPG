import pygame
pygame.init()
import random
clock = pygame.time.Clock()
from _draw_classes import *


class Pick_Functions:
    def __init__(self, list: list):
        self.list = list

    def draw_general_list(self):
        pick_menu = Draw_Screen()
        pick_menu.draw_list(self.list)

    def draw_skill_list(self):
        pick_menu = Draw_Screen()
        pick_menu.draw_skill_list(self.list)

    def pick_randomly(self):
        thing = self.list[random.randint(0, len(self.list) - 1)]
        return thing
    
    def pick_from_list(self, pick_randomly = False):
        if len(self.list) <= 0:
            thing = None
            return thing
        if len(self.list) == 1:
            thing = self.list[0]
            return thing
        if pick_randomly == True:
            return self.pick_randomly()
        pick = True
        while pick:
            pygame.event.clear()
            clock.tick(C.SLOW_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        thing = self.list[0]
                        pick = False
                        break
                    if event.key == pygame.K_2:
                        thing = self.list[1]
                        pick = False
                        break
                    if event.key == pygame.K_3 and len(self.list) >= 3:
                        thing = self.list[2]
                        pick = False
                        break
                    if event.key == pygame.K_4 and len(self.list) >= 4:
                        thing = self.list[3]
                        pick = False
                        break
                    if event.key == pygame.K_5 and len(self.list) >= 5:
                        thing = self.list[4]
                        pick = False
                        break
                    if event.key == pygame.K_6 and len(self.list) >= 6:
                        thing = self.list[5]
                        pick = False
                        break
                    if event.key == pygame.K_7 and len(self.list) >= 7:
                        thing = self.list[6]
                        pick = False
                        break
                    if event.key == pygame.K_8 and len(self.list) >= 8:
                        thing = self.list[7]
                        pick = False
                        break
                    if event.key == pygame.K_9 and len(self.list) >= 9:
                        thing = self.list[8]
                        pick = False
                        break
        return thing

    def pick(self, pick_randomly=False):
        self.draw_general_list()
        return self.pick_from_list(pick_randomly)

    def pick_skill(self):
        self.draw_skill_list()
        return self.pick_from_list()
