import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BROWN = (164, 116, 73)
GREY = (134, 136, 138)
YELLOW = (255, 255, 0)
# define player
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p_width = 40
p_height = 35
p_x = 400
p_y = 700
p_colour = RED
bullet_x = 0
bullet_y = -100
bullet_width = 10
bullet_height = 30
bullet_active = False
bullet_colour = WHITE
original = 40
alien_count = 40
alien_speed_change = 1
#define aliens
aliens = [
    {"x": 10, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 90, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 170, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 250, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 330, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 410, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 490, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 570, "y": 10, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 10, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 90, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 170, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 250, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 330, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 410, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 490, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 570, "y": 80, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 10, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 90, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 170, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 250, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 330, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 410, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 490, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 570, "y": 150, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 10, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 90, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 170, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 250, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 330, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 410, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 490, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 570, "y": 220, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 10, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 90, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 170, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 250, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 330, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 410, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 490, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
    {"x": 570, "y": 290, "width": 40, "height": 40, "colour": BLUE, "speed": 1},
]

# draw rectangle



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# joystick
    if bullet_active == False:
        bullet = []
    screen.fill(BG)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        p_x += 4.5
    if keys[pygame.K_LEFT]:
        p_x -= 4.5
    for a in aliens:
        pygame.draw.rect(screen, a["colour"], (a["x"], a["y"], a["width"], a["height"]))
    gun_point = p_x + 1 / 2 * p_width
    pygame.draw.rect(screen, p_colour, (p_x, p_y, p_width, p_height))

    pygame.draw.line(screen, YELLOW, (gun_point, p_y + 10), (gun_point, p_y - 5))

    if keys[pygame.K_SPACE]:
        if bullet_active == False:
            bullet_x = gun_point - bullet_width / 2
            bullet_y = p_y - 5
            bullet_active = True
    if bullet_active == True:
        bullet_y -= 7
        pygame.draw.rect(screen, bullet_colour, (bullet_x, bullet_y, bullet_width, bullet_height))
    if bullet_y <= 0 or bullet_y >= 770:
        bullet_active = False
    for a in aliens:
        a["x"] += 1.25 * a["speed"]
        if a["x"] >= 760 or a["x"] <= 0:
            for l in aliens:
                l["speed"] *= -1
                l["y"] += 40
                if a["y"] >= 760:
                    print("frog")
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    p_rect = pygame.Rect(p_x, p_y, p_width, p_height)
    for a in aliens:
        a_rect = pygame.Rect(a["x"], a["y"], a["width"], a["height"])
        if p_rect.colliderect(a_rect):
            print("game_over")

        if bullet_rect.colliderect(a_rect) and bullet_active == True:
            aliens.remove(a)
            alien_count -= 1
            bullet_active = False
    if alien_count == original / 2:
        if alien_speed_change > 0:
            alien_speed_change -= 1
            for a in aliens:
                a["speed"] = 1.5
    print (bullet_y)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()