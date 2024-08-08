
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up some constants
WIDTH, HEIGHT = 700, 500

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('XInput Controller Axes')

# Set up the font
font = pygame.font.Font('freesansbold.ttf', 24)

# Initialize the joystick module
pygame.joystick.init()

# Get the joystick object (assuming it's the first joystick)
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    # Read the X and Y values of the left analogue stick
    left_stick_x = joystick.get_axis(0)
    left_stick_y = joystick.get_axis(1)

    # Read the X and Y values of the right analogue stick
    right_stick_x = joystick.get_axis(2)
    right_stick_y = joystick.get_axis(3)

    # Read the Z-axis (triggers)
    triggers = joystick.get_axis(5)

    # Render the text
    left_stick_text = font.render(f"Left Stick: ({left_stick_x:.2f}, {left_stick_y:.2f})", True, BLACK)
    right_stick_text = font.render(f"Right Stick: ({right_stick_x:.2f}, {right_stick_y:.2f})", True, BLACK)
    triggers_text = font.render(f"Triggers: {triggers:.2f}", True, BLACK)

    # Draw the text onto the screen
    screen.blit(left_stick_text, (10, 10))
    screen.blit(right_stick_text, (10, 40))
    screen.blit(triggers_text, (10, 70))

    # Update the display
    pygame.display.update()

    # Limit to 60 frames per second
    pygame.time.Clock().tick(60)