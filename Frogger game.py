import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# draw rectangle
player_width = 40
player_height = 40
player_x = 75
player_y = 550
player_colour = GREEN

log_width = 80
log_height = 40
log_x = 75
log_y = 490
log_colour = BLUE

moving_log_x = 75
moving_log_y = 430
log_speed = 1/32

car_width = 60
car_height = 40
slow_car_x = 75
slow_car_y = 330
fast_car_x = 75
fast_car_y = 270
fast_car_speed_car_speed = 1/16
slow_car_speed = 1/32
fast_car_colour = RED
slow_car_colour = WHITE

end_position_width = 800
end_position_height = 210
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 0.2
    if keys[pygame.K_RIGHT]:
        player_x += 0.2
    if keys[pygame.K_UP]:
        player_y -= 0.2
    if keys[pygame.K_DOWN]:
        player_y += 0.2

    screen.fill(BG)
    pygame.draw.rect(screen, player_colour, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, log_colour, (log_x, log_y, log_width,log_height))
    pygame.draw.rect(screen, log_colour, (moving_log_x, moving_log_y, log_width, log_height))
    pygame.draw.rect(screen, slow_car_colour, (slow_car_x, slow_car_y, car_width, car_height))
    pygame.draw.rect(screen, fast_car_colour, (fast_car_x, fast_car_y, car_width, car_height))

    pygame.display.flip()