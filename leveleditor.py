import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1400, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple CAD Program")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_GREY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Grid size
grid_size = 40

# Variables to store coordinates
first_corner = None
second_corner = None
boxes = []
preview_box = None
snap_point = None

# Function to draw the grid
def draw_grid():
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, DARK_GREY, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, DARK_GREY, (0, y), (width, y))

# Function to snap to grid
def snap_to_grid(pos):
    x, y = pos
    snapped_x = round(x / grid_size) * grid_size
    snapped_y = round(y / grid_size) * grid_size
    return snapped_x, snapped_y

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                snapped_pos = snap_to_grid(event.pos)
                if first_corner is None:
                    first_corner = snapped_pos
                else:
                    second_corner = snapped_pos
                    top_left_x = min(first_corner[0], second_corner[0])
                    top_left_y = min(first_corner[1], second_corner[1])
                    width_box = abs(second_corner[0] - first_corner[0])
                    height_box = abs(second_corner[1] - first_corner[1])
                    boxes.append(((top_left_x, top_left_y), width_box, height_box))
                    first_corner = None
                    second_corner = None
                    preview_box = None
            elif event.button == 3:  # Right mouse button
                if boxes:
                    boxes.pop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("boxes = [")
                for box in boxes:
                    print(f'    {{"x": {box[0][0]}, "y": {box[0][1]}, "width": {box[1]}, "height": {box[2]}, "colour": RED}},')
                print("]")
                boxes = []
        elif event.type == pygame.MOUSEMOTION:
            snapped_pos = snap_to_grid(event.pos)
            snap_point = snapped_pos
            if first_corner is not None:
                current_pos = snapped_pos
                top_left_x = min(first_corner[0], current_pos[0])
                top_left_y = min(first_corner[1], current_pos[1])
                width_box = abs(current_pos[0] - first_corner[0])
                height_box = abs(current_pos[1] - first_corner[1])
                preview_box = ((top_left_x, top_left_y), width_box, height_box)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Draw the boxes
    for box in boxes:
        pygame.draw.rect(screen, WHITE, (*box[0], box[1], box[2]), 2)

    # Draw the preview box
    if preview_box is not None:
        pygame.draw.rect(screen, YELLOW, (*preview_box[0], preview_box[1], preview_box[2]), 1)

    # Draw the snap point
    if snap_point is not None:
        pygame.draw.circle(screen, YELLOW, snap_point, 5)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
