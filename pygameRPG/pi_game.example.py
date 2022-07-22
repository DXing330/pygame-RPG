import pygame
import os
#makes font for the game to print
pygame.font.init()
HP_FONT = pygame.font.SysFont("comicsans", 20)
WIN_FONT = pygame.font.SysFont("comicsans", 100)
#constants
WIDTH = 1100
HEIGHT = 600
#makes a window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#changes the name of the window
pygame.display.set_caption("RPG")
#tuples of red green blue are used for color
FPS = 30
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CUSTOM = (100, 100, 200)
RIGHT_R = 90
LEFT_R = 270
SS_SIZE = (50, 50)
SS_WIDTH = 50
SS_HEIGHT = 50
VELOCITY = 5
BULLET_VEL = 6
BULLET_WIDTH = 5
BULLET_HEIGHT = BULLET_WIDTH
MAX_BULLETS = 100
MAX_HP = 10
BORDER_WIDTH = 10
BORDER = pygame.Rect((WIDTH - BORDER_WIDTH)//2, 0, BORDER_WIDTH, HEIGHT)
#USEREVENT adds an event defined by a number
#if they were both number 1 they would be the same event
Y_HIT = pygame.USEREVENT + 1
R_HIT = pygame.USEREVENT + 2
r_hp = MAX_HP
y_hp = MAX_HP

#imports an image into the game
Y_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
R_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
SPACE_1 = pygame.image.load(os.path.join("Assets", "space.png"))
SPACE_2 = pygame.transform.scale(SPACE_1, (WIDTH, HEIGHT))
#transforms an image
#format is pygame.transform.scale(<IMAGE>, <(WIDTH, HEIGHT)>)
#format is pygame.transform.rotate(<IMAGE>, <ANGLE>)
Y_SS_IMG = pygame.transform.scale(Y_SPACESHIP_IMAGE, SS_SIZE)
R_SS_IMG = pygame.transform.scale(R_SPACESHIP_IMAGE, SS_SIZE)
Y_SS_IMG = pygame.transform.rotate(Y_SS_IMG, RIGHT_R)
R_SS_IMG = pygame.transform.rotate(R_SS_IMG, LEFT_R)

def draw_window(red, yellow, r_b, y_b, r_hp, y_hp):
        WIN.fill(CUSTOM)
        WIN.blit(SPACE_2, (0, 0))
        #this will draw a rectangle
        pygame.draw.rect(WIN, BLACK, BORDER)
        r_hp_text = HP_FONT.render("HP: " + str(r_hp), 1, WHITE)
        y_hp_text = HP_FONT.render("HP: " + str(y_hp), 1, WHITE)
        WIN.blit(r_hp_text, (WIDTH - r_hp_text.get_width() - BORDER_WIDTH,
                             BORDER_WIDTH))
        WIN.blit(y_hp_text, (BORDER_WIDTH, BORDER_WIDTH))

        #this will draw an image
        #format is WIN.blit(<IMAGE>, <(WIDTH, HEIGHT)>)
        #yellow.x means at the x location of the yellow thing
        WIN.blit(Y_SS_IMG, (yellow.x, yellow.y))
        WIN.blit(R_SS_IMG, (red.x, red.y))
        #draw bullets as well
        for bullet in r_b:
                pygame.draw.rect(WIN, RED, bullet)
        for bullet in y_b:
                pygame.draw.rect(WIN, YELLOW, bullet)
        
        #this will update the display
        pygame.display.update()
        
def bullet_move(y_b, r_b, yellow, red):
        for bullet in y_b:
                bullet.x += BULLET_VEL
                #collide rect checks if rectangles have collided
                if red.colliderect(bullet):
                        y_b.remove(bullet)
                        pygame.event.post(pygame.event.Event(R_HIT))
                elif bullet.x >= WIDTH:
                        y_b.remove(bullet)
        for bullet in r_b:
                bullet.x -= BULLET_VEL
                if yellow.colliderect(bullet):
                        r_b.remove(bullet)
                        pygame.event.post(pygame.event.Event(Y_HIT))
                elif bullet.x <= 0:
                        r_b.remove(bullet)

def yellow_move(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:
                #move left
                yellow.x -= VELOCITY
        if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VELOCITY < BORDER.x:
                #move right
                yellow.x += VELOCITY
        if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:
                #move up
                yellow.y -= VELOCITY
        if keys_pressed[pygame.K_s]and yellow.y + yellow.height + VELOCITY < HEIGHT:
                #move down
                yellow.y += VELOCITY

def red_move(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x:
                #move left
                red.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VELOCITY < WIDTH:
                #move right
                red.x += VELOCITY
        if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:
                #move up
                red.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and red.y + red.height + VELOCITY < HEIGHT :
                #move down
                red.y += VELOCITY

def winner(text):
        draw_text = WIN_FONT.render(text, 1, WHITE)
        WIN.blit(draw_text, ((WIDTH - draw_text.get_width())//2, (HEIGHT - draw_text.get_height())//2))
        pygame.display.update()
        pygame.time.delay(5000)
        

def RPG2():
        r_hp = 10
        y_hp = 10

        #make a rectangle for the player to control
        #format is (x, y, width, height)
        red = pygame.Rect(660, 200, SS_WIDTH, SS_HEIGHT)
        yellow = pygame.Rect(330, 200, SS_WIDTH, SS_HEIGHT)
        #clock function that will keep track of time
        clock = pygame.time.Clock()
        #bullets list to keep track of bullets
        r_bullets = []
        y_bullets = []
        run = True
        while run:

                #means that the clock will run for this much time before ticking
                clock.tick(FPS)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                                pygame.quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RCTRL and len(r_bullets) < MAX_BULLETS:
                                        bullet = pygame.Rect(red.x,
                                                             red.y + red.height//2,
                                                             BULLET_WIDTH, BULLET_WIDTH)
                                        r_bullets.append(bullet)

                                if event.key == pygame.K_f and len(y_bullets) < MAX_BULLETS:
                                        bullet = pygame.Rect(yellow.x + yellow.width,
                                                             yellow.y + yellow.height//2,
                                                             BULLET_WIDTH, BULLET_WIDTH)
                                        y_bullets.append(bullet)
                        if event.type == R_HIT:
                                r_hp -= 1
                        if event.type == Y_HIT:
                                y_hp -= 1
                winner_text = ""
                if r_hp <= 0 and y_hp > 0:
                        winner_text = "Yellow Wins!"
                if y_hp <= 0 and r_hp > 0:
                        winner_text = "Red Wins!"

                if winner_text != "":
                        winner(winner_text)
                        break
                                        
                #checks the keys being pressed
                keys_pressed = pygame.key.get_pressed()
                #handles spaceship movement
                yellow_move(keys_pressed, yellow)
                red_move(keys_pressed, red)
                #handles bullet movement
                bullet_move(y_bullets, r_bullets, yellow, red)

                draw_window(red, yellow, r_bullets, y_bullets, r_hp, y_hp)
        RPG2()


if __name__ == "__RPG2__":
        RPG2()

RPG2()
