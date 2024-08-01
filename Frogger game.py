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
river_width = 800
river_height = 90
river_x = 0
river_y = 410
river_colour = BLUE

player_width = 40
player_height = 40
player_x = 75
player_y = 550
player_colour = GREEN


standing_logs = [
    {"x": 100, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 200, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 300, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 400, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 500, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 600, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 700, "y": 460, "width": 70, "height": 40, "colour": BROWN},
    {"x": 000, "y": 460, "width": 70, "height": 40, "colour": BROWN}
]

moving_logs = [
    {"x": 100, "y": 410, "width": 80, "height": 40, "colour": BROWN, "speed": 1/32},
    {"x": 300, "y": 410, "width": 80, "height": 40, "colour": BROWN, "speed": 1/32},
    {"x": 500, "y": 410, "width": 80, "height": 40, "colour": BROWN, "speed": 1/32},
    {"x": 700, "y": 410, "width": 80, "height": 40, "colour": BROWN, "speed": 1/32}
]



fast_car_speed = 1/16
slow_car_speed = 1/32
fast_cars = [
    {"x": 75, "y": 270, "width": 60, "height": 40, "colour": RED, "speed": fast_car_speed},
    {"x": 375, "y": 270, "width": 60, "height": 40, "colour": RED, "speed": fast_car_speed},
    {"x": 575, "y": 270, "width": 60, "height": 40, "colour": RED, "speed": fast_car_speed},
    {"x": 775, "y": 270, "width": 60, "height": 40, "colour": RED, "speed": fast_car_speed}
]
slow_cars = [
    {"x": 35, "y": 330, "width": 60, "height": 40, "colour": GREY, "speed": slow_car_speed},
    {"x": 235, "y": 330, "width": 60, "height": 40, "colour": GREY, "speed": slow_car_speed},
    {"x": 435, "y": 330, "width": 60, "height": 40, "colour": GREY, "speed": slow_car_speed},
    {"x": 635, "y": 330, "width": 60, "height": 40, "colour": GREY, "speed": slow_car_speed}
]

end_position_width = 800
end_position_height = 20
end_position_x = 0
end_position_y = 210
end_position_colour = WHITE
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


    # Update moving log positions
    for log in moving_logs:
        log["x"] += log["speed"]
        if log["x"] > SCREEN_WIDTH:
            log["x"] = -log["width"]

    # Update fast car positions
    for car in fast_cars:
        car["x"] += fast_car_speed
        if car["x"] > SCREEN_WIDTH:
            car["x"] = -car["width"]

    # Update slow car positions
    for car in slow_cars:
        car["x"] += slow_car_speed
        if car["x"] > SCREEN_WIDTH:
            car["x"] = -car["width"]
    screen.fill(BG)
    pygame.draw.rect(screen, river_colour, (river_x, river_y, river_width, river_height))
    pygame.draw.rect(screen, end_position_colour, (end_position_x, end_position_y, end_position_width, end_position_height))



    # Draw standing logs
    for log in standing_logs:
        pygame.draw.rect(screen, log["colour"], (log["x"], log["y"], log["width"], log["height"]))

    # Draw moving logs
    for log in moving_logs:
        pygame.draw.rect(screen, log["colour"], (log["x"], log["y"], log["width"], log["height"]))

    pygame.draw.rect(screen, player_colour, (player_x, player_y, player_width, player_height))

    # Draw fast cars
    for car in fast_cars:
        pygame.draw.rect(screen, car["colour"], (car["x"], car["y"], car["width"], car["height"]))

    # Draw slow cars
    for car in slow_cars:
        pygame.draw.rect(screen, car["colour"], (car["x"], car["y"], car["width"], car["height"]))

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    river_rect = pygame.Rect(river_x, river_y, river_width, river_height)

    if player_rect.colliderect(river_rect):
        on_log = False
        for log in moving_logs + standing_logs:
            log_rect = pygame.Rect(log["x"], log["y"], log["width"], log["height"])
            if player_rect.colliderect(log_rect):
                on_log = True
                break
        if not on_log:
            print ("you drowned!")
            running = False
    for car in fast_cars + slow_cars:
        car_rect = pygame.Rect(car["x"], car["y"], car["width"], car["height"])
        if player_rect.colliderect(car_rect):
            print("you got run over!")
            running = False
    end_position_rect = pygame.Rect(end_position_x, end_position_y, end_position_width, end_position_height)
    if player_rect.colliderect(end_position_rect):
        print("you made it!")
        running = False


    pygame.display.flip()

pygame.quit()