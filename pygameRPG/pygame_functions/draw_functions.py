import pygame
import os
import sys
sys.path.append("..")
from pygconstants import PYGConstants
P = PYGConstants()
REG_FONT = pygame.font.SysFont("comicsans", 20)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
#images used
PLAINS_RAW = pygame.image.load(os.path.join("Assets", "plains.png"))
PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (P.WIDTH, P.HEIGHT))
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
HERO_RAW = pygame.image.load(os.path.join("Assets", "hero.png"))
HERO_IMG = pygame.transform.scale(HERO_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SUMMONER_RAW = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER_IMG = pygame.transform.scale(SUMMONER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
KNIGHT_RAW = pygame.image.load(os.path.join("Assets", "knight.png"))
KNIGHT_IMG = pygame.transform.scale(KNIGHT_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
HUNTER_RAW =pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER_IMG = pygame.transform.scale(HUNTER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
ANGEL_RAW = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL_IMG = pygame.transform.scale(ANGEL_RAW, (P.SPRITE_WIDTH//2, P.SPRITE_HEIGHT//2))
MON_RAW = pygame.image.load(os.path.join("Assets", "g_mon.png"))
MON_IMG = pygame.transform.scale(MON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
#function that will draw characters in battle
def draw_heroes(h_p, h_ally):
        for player in h_p:
                if "Hunter" in player.name:
                        WIN.blit(HUNTER_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 2),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 4)))
                if "Hero" in player.name:
                        WIN.blit(HERO_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 1),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 2)))
                if "Summoner" in player.name:
                        WIN.blit(SUMMONER_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 1.5),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))
                if "Knight" in player.name:
                        WIN.blit(KNIGHT_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 2.5),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 5)))
                
        for aly in h_ally:
                if "Angel" in aly.name:
                        WIN.blit(ANGEL_IMG,
                                 (P.WIDTH - (P.SPRITE_WIDTH * 2),
                                 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))

        pygame.display.update()
#function that will draw monsters in battle
def draw_monsters(m_p):
        x = 2
        for mon in m_p:
                WIN.blit(MON_IMG,
                         (P.PADDING//2 * x,
                          P.HEIGHT - (P.SPRITE_HEIGHT * x)))
                x += 1
                
#function that lists what monsters there are
def draw_monster_menu_list(m_p):
        x = 2
        for mon in m_p:
                mon_info = REG_FONT.render(str(mon.name), 1, P.BLACK)
                WIN.blit(mon_info, (P.WIDTH//2 - mon_info.get_width(), P.PADDING * x))
                x += 2
#function that will draw the options in battle
def draw_battle_menu(h_p, m_p, h_ally, h_m, h_w, h_a):
        attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
        WIN.blit(attack_text, (P.WIDTH//2 - attack_text.get_width(), P.PADDING))
        run_text = REG_FONT.render("RUN away: R", 1, P.RED)
        WIN.blit(run_text, (P.WIDTH//2 - run_text.get_width(),
                            P.PADDING * 2))

#function will list options for the player
def draw_menu():
        attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
        WIN.blit(attack_text, (P.WIDTH//2 - attack_text.get_width(), P.PADDING))
        save_text = REG_FONT.render("RECORD journey: R", 1, P.BLACK)
        WIN.blit(save_text, (P.WIDTH//2 - save_text.get_width(),
                             P.PADDING * 2))
        city_text = REG_FONT.render("return to CITY: C", 1, P.BLACK)
        WIN.blit(city_text, (P.WIDTH//2 - city_text.get_width(),
                             P.PADDING * 3))
