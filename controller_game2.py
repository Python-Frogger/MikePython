import pygame
import random
import sys

pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Get the number of joysticks
num_joysticks = pygame.joystick.get_count()

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
SCREEN_HEIGHT = 800

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

# define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# hide mouse cursor
pygame.mouse.set_visible(False)

# draw rectangle
rect_width = 100
rect_height = 100
rect_x = SCREEN_WIDTH // 2 - rect_width // 2
rect_y = SCREEN_HEIGHT // 2 - rect_height // 2

# game loop
run = True
while run:
    # fill screen with black
    screen.fill(BG)

    # Check the A button state
    a_button_pressed = joystick.get_button(0)
    print(a_button_pressed)  # Print the A button state

    if a_button_pressed:
        colour = RED
    else:
        colour = GREEN

    if joystick.get_axis(1) < -0.5 and rect_y > 0:
        rect_y -= 0.5
    if joystick.get_axis(1) > 0.5 and rect_y < (SCREEN_HEIGHT-rect_width):
        rect_y += 0.5
    if joystick.get_axis(0) < -0.5 and rect_x > 0:
        rect_x -= 0.5
    if (joystick.get_axis(0) > 0.5 and rect_x < (SCREEN_WIDTH-rect_width)):
        rect_x += 0.5


    pygame.draw.rect(screen, colour, (rect_x, rect_y, rect_width, rect_height))

    # update display
    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()