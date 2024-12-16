import pygame
import random
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BROWN = (164, 116, 73)
GREY = (134, 136, 138)
YELLOW = (255,255,0)

grid_max = 38
grid_min = 1
grid_size = grid_max-grid_min+1

pygame.font.init()
font = pygame.font.Font(None, 20)



fruit = [(19,20),(20,20),(21,20),(18,20),(22,20), (16,20),(17,20),(23,20),(24,20)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snake1 = [(5, 5), (6, 5), (7, 5), (8,5), (9,5)]
snake2 = [(35, 35), (34, 35), (33, 35), (32, 35), (31, 35)]
# draw rectangle
snake1_direction = "right"
snake2_direction = "left"
snake1_colour = RED
snake2_colour = BLUE
score1 = 0
score2 = 0

#set up clock
clock = pygame.time.Clock()
# Set the desired time interval (0.05 seconds)
time_interval = 100  # milliseconds (1 second = 1000 milliseconds)
timer = 0


pygame.init()
pygame.joystick.init()

# Get the number of joysticks
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 1:
    # Get the first joystick
    joystick1 = pygame.joystick.Joystick(0)
    joystick1.init()
    print(joystick1.get_name())  # Print the joystick name
    joystick2 = pygame.joystick.Joystick(1)
    joystick2.init()
    print(joystick2.get_name())  # Print the joystick name

else:
    print("n=Not enough joysticks")

def fill_block(x,y, colour):
    pygame.draw.rect(screen, colour, (x, y, 20, 20))

all_coordinates = [(x, y) for x in range(grid_size) for y in range(grid_size)]

def  generate_fruit(fruit_number):
    global fruit, snake1, snake2, grid_size, all_coordinates
    available_coordinates = [coord for coord in all_coordinates if coord not in snake1 and coord not in snake2 and coord not in fruit]
    random_fruit_location = random.choice(available_coordinates)
    fruit[fruit_number] = random_fruit_location
    #fruit[fruit_number][0] = random_fruit_location[0]
    #fruit[fruit_number][1] = random_fruit_location[1]
    fill_block(fruit[fruit_number][0]*20, fruit[fruit_number][1]*20 , YELLOW)
    print (fruit)


def move_snakes():
    global snake1, snake2, snake1_direction, snake2_direction, grid_max, grid_min, fruit,score1, score2

# snake1
    x, y = snake1[-1]
    if snake1_direction == "right":
        x += 1
# gone off screen?
        if x > grid_max:
            print("Player 1 off grid")
    if snake1_direction == "left":
        x -= 1
        # gone off screen?
        if x < grid_min:
            print("Player 1 off grid")
    if snake1_direction == "down":
        y += 1
        # gone off screen?
        if y > grid_max:
            print("Player 1 off grid")
    if snake1_direction == "up":
        y -= 1
        # gone off screen?
        if y < grid_min:
            print("Player 1 off grid")

# add new snake position
    fill_block(x * 20, y * 20, snake1_colour)

# collided with other snakes
    if (x, y) in snake1 or (x, y) in snake2:

        fill_block(snake1[0][0] * 20, snake1[0][1] * 20, BG)
        snake1 = snake1[1:]
        score1 -= 1

    snake1 = snake1 + [(x, y)]

# eaten fruit?
    if (x,y) in fruit:
        print("you got tangoed")
        # we know you hit a fruit. which one?
        score1 +=1
        fruit_count = 0
        for fruit_x, fruit_y in fruit:
            if (fruit_x, fruit_y) == (x,y):
                print ("you hit fruit", fruit_count)
                generate_fruit(fruit_count)
            fruit_count +=1
    else:
        fill_block(snake1[0][0]*20, snake1[0][1]*20, BG)
        snake1 = snake1[1:]



# snake2
    x, y = snake2[-1]
    if snake2_direction == "right":
        x += 1
# gone off screen?
        if x > grid_max:
            print("Player 2 loses")
    if snake2_direction == "left":
        x -= 1
        # gone off screen?
        if x < grid_min:
            print("Player 2 loses")
    if snake2_direction == "down":
        y += 1
        # gone off screen?
        if y > grid_max:
            print("Player 2 loses")
    if snake2_direction == "up":
        y -= 1
        # gone off screen?
        if y < grid_min:
            print("Player 2 loses")

# add new snake position
    fill_block(x * 20, y * 20, snake2_colour)

# collided with other snakes
    if (x, y) in snake1 or (x, y) in snake2:
        fill_block(snake2[0][0] * 20, snake2[0][1] * 20, BG)
        snake2 = snake2[1:]
        score2 -= 1


    snake2 = snake2 + [(x, y)]

# eaten fruit?
    if (x,y) in fruit:
        print("you got tangoed")
        # we know you hit a fruit. which one?
        score2 += 1

        fruit_count = 0
        for fruit_x, fruit_y in fruit:
            if (fruit_x, fruit_y) == (x,y):
                print ("you hit fruit", fruit_count)
                generate_fruit(fruit_count)
            fruit_count +=1
    else:
        fill_block(snake2[0][0]*20, snake2[0][1]*20, BG)
        snake2 = snake2[1:]



# plot first snake
for x, y in snake1:
    fill_block(x*20 , y*20, snake1_colour)
for x, y in snake2:
    fill_block(x*20 , y*20, snake2_colour)

for fruit_x, fruit_y in fruit:
    fill_block(fruit_x*20, fruit_y*20, YELLOW)

# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    timer += clock.get_time()
    if timer >= time_interval:
        timer = 0
        move_snakes()


# joystick to change direction
    x1, y1 = joystick1.get_hat(0)

    # Check D-pad directions for joystick 0
    if y1 == 1 and snake1_direction != "down":
        snake1_direction = "up"
    elif y1 == -1 and snake1_direction != "up":
        snake1_direction = "down"

    elif x1 == -1 and snake1_direction != "right":
        snake1_direction = "left"

    elif x1 == 1 and snake1_direction != "left":
        snake1_direction = "right"

    # Get the D-pad input directly for joystick 1
    x2, y2 = joystick2.get_hat(0)

    # Check D-pad directions for joystick 0
    if y2 == 1 and snake2_direction != "down":
        snake2_direction = "up"
    elif y2 == -1 and snake2_direction != "up":
        snake2_direction = "down"

    elif x2 == -1 and snake2_direction != "right":
        snake2_direction = "left"

    elif x2 == 1 and snake2_direction != "left":
        snake2_direction = "right"




#    screen.fill(BG)

    pygame.draw.rect(screen, GREY, (0, 0, 799, 799), width=20)
    # Render the scores as text
    score_text1 = font.render(f"Player 1: {score1}", True, (0, 0, 0))  # Black color
    score_text2 = font.render(f"Player 2: {score2}", True, (0, 0, 0))

    # Blit the rendered text onto the screen (top row)
    screen.blit(score_text1, (10, 00))  # Adjust the position as needed
    screen.blit(score_text2, (100,00))
    pygame.display.flip()
    clock.tick(60)  # 60 FPS (adjust as needed)

pygame.quit()