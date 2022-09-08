import pygame
pygame.init()
import random
import json
clock = pygame.time.Clock()
from _constants import Constants
C = Constants
from _basic_classes import *


class Pick_Functions:
    def __init__(self, list: list):
        self.list = list

    def pick_randomly(self):
        if len(self.list) > 0:
            thing = None
            if len(self.list) == 1:
                thing = self.list[0]
            elif len(self.list) > 1:
                choice = random.randint(0, len(self.list)-1)
                thing = self.list[choice]
            return thing
    
    def pick(self):
        if len(self.list) > 0:
            thing = None
            if len(self.list) == 1:
                thing = self.list[0]
            else:
                pick = True
                while pick:
                    pygame.event.clear()
                    clock.tick(C.SLOW_FPS)
                    keys = pygame.key.get_pressed()
                    if keys.key == pygame.K_1:
                        thing = self.list[0]
                        pick = False
                        break
                    if keys.key == pygame.K_2:
                        thing = self.list[1]
                        pick = False
                        break
                    if keys.key == pygame.K_3:
                        if len(self.list) >= 3:
                            thing = self.list[2]
                            pick = False
                            break
                    if keys.key == pygame.K_4:
                        if len(self.list) >= 4:
                            thing = self.list[3]
                            pick = False
                            break
                    if keys.key == pygame.K_5:
                        if len(self.list) >= 5:
                            thing = self.list[4]
                            pick = False
                            break
                    if keys.key == pygame.K_6:
                        if len(self.list) >= 6:
                            thing = self.list[5]
                            pick = False
                            break
                    if keys.key == pygame.K_7:
                        if len(self.list) >= 7:
                            thing = self.list[6]
                            pick = False
                            break
                    if keys.key == pygame.K_8:
                        if len(self.list) >= 8:
                            thing = self.list[7]
                            pick = False
                            break
                    if keys.key == pygame.K_9:
                        if len(self.list) >= 9:
                            thing = self.list[8]
                            pick = False
                            break
            return thing
