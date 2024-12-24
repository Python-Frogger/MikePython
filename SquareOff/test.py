import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flashing Screen")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Set up the timer
flash_interval = 3000  # 3 seconds in milliseconds
last_flash_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    current_time = pygame.time.get_ticks()

    # Check if it's time to flash
    if current_time - last_flash_time >= flash_interval:
        screen.fill(WHITE)
        pygame.display.flip()
        pygame.time.delay(100)  # Flash for 100 milliseconds
        last_flash_time = current_time

    # Fill the screen with black
    screen.fill(BLACK)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
