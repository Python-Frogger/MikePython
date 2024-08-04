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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# draw rectangle



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# joystick

    screen.fill(BG)



    pygame.display.flip()

pygame.quit()