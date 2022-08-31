import pygame
import os
import sys
sys.path.append(".")
pygame.font.init()
HP_FONT = pygame.font.SysFont("comicsans", 20)
WIN_FONT = pygame.font.SysFont("comicsans", 100)

class PYGConstants:
        def __init__(self):
                self.ORIGIN = (0, 0)
                self.WIDTH = 1400
                self.HEIGHT = 750
                self.PADDING = 30
                self.SCREEN = (self.WIDTH, self.HEIGHT)
                self.FPS = 30
                self.SLOWFPS = 3
                self.TIMEDELAY = 5000
                self.SMALLDELAY = 1000
                self.RED = (255, 0, 0)
                self.GREEN = (0, 255, 0)
                self.BLUE = (0, 0, 255)
                self.YELLOW = (255, 255, 0)
                self.WHITE = (255, 255, 255)
                self.BLACK = (0, 0, 0)
                self.SPRITE_WIDTH = 80
                self.SPRITE_HEIGHT = 80
                self.BIG_SPRITE = 90
                self.SMALL_SPRITE = 70
        
