import pygame
import random
import sys

pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Get the number of joysticks
num_joysticks = pygame.joystick.get_count()

score = 0

font = pygame.font.Font(None, 36)

# Check if there are any joysticks
if num_joysticks > 0:
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(joystick.get_name())  # Print the joystick name

# Initialize the mixer module
pygame.mixer.init()

# define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

# import sprites
background_sprite = pygame.image.load("backgroundjumping.png")
background_sprite = pygame.transform.scale(background_sprite, (800, 228))
background_x = 0
background_y = SCREEN_HEIGHT-background_sprite.get_height()
# game speed
game_speed = 1/16

# define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# hide mouse cursor
pygame.mouse.set_visible(False)

spawned_obstacle = False
obstacles = []

# draw rectangle
rect_width = 40
rect_height = 80
rect_x = 75
rect_y = 275
floor = 275
gravity = -0.00025
initial_jump_force = 0.25
force = 0
is_jumping = False
colour = GREEN
# game loop
run = True
while run:
    # fill screen with black
    screen.fill(BG)

    #draw obstacles randomly
    if not spawned_obstacle:
        obstacle_width = 40
        obstacle_height = 40
        obstacle_x = SCREEN_WIDTH + random.randint(obstacle_width, SCREEN_WIDTH - obstacle_width)



        if random.randint(1, 2) == 1:
            obstacle_y = 315
        else:
            obstacle_y = 230




        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        spawned_obstacle = True




    #update obstacle positions
    for obstacle in obstacles:
        obstacle_x -= game_speed
        if obstacle_x <= -obstacle_width:
            obstacles.remove(obstacle)
            score += 1
            game_speed += 1/64
            spawned_obstacle = False

    # plot two sprites side by side
    screen.blit(background_sprite, (background_x, background_y))
    screen.blit(background_sprite, (background_x + background_sprite.get_width(), background_y))
    background_x -= game_speed
    if background_x < 0 - background_sprite.get_width():
        background_x = 0

    # Check the A button state
    a_button_pressed = joystick.get_button(0)
    if a_button_pressed and is_jumping == False:
        is_jumping = True
        force = initial_jump_force

    if is_jumping:
        rect_y -= force
        force += gravity

    if rect_y > floor:
        rect_y = floor
        is_jumping = False


    pygame.draw.rect(screen, colour, (rect_x, rect_y, rect_width, rect_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if player_rect.colliderect(obstacle_rect):
        print("you lose")
        pygame.time.delay(5000)
    # update display
    score_surface = font.render(str(score), True, WHITE)
    screen.blit(score_surface, (600, 10))
    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()