import pygame
pygame.init()
import random
clock = pygame.time.Clock()
from _constants import Constants
C = Constants

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
            return thing
