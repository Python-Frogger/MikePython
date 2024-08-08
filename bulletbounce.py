import pygame
import math

# Initialize Pygame
pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

# Set up some constants
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG = (0, 0, 0)
BLUE = (0, 0, 255)

# Box coordinates and dimensions

boxes = [
    {"x": 500, "y": 500, "width": 200, "height": 100, "colour": RED},
    {"x": 200, "y": 200, "width": 300, "height": 100, "colour": RED},
    {"x": 200, "y": 600, "width": 200, "height": 100, "colour": RED},
    {"x": 780, "y": 0, "width": 20, "height": 800, "colour": WHITE},
    {"x": 0, "y": 0, "width": 800, "height": 20, "colour": WHITE},
    {"x": 0, "y": 00, "width": 20, "height": 800, "colour": WHITE},
    {"x": 0, "y": 780, "width": 800, "height": 20, "colour": WHITE},
]


# Bullet coordinates and speeds
bullets = [
    {"x": 100, "y": 600, "x_speed": 7, "y_speed": -16, "gravity": 0.1, "bounce_count": 0, "active": 1, "bounce": 0.9}
]

gravity = 0.1

gun_angle_x = 0
gun_angle_y = 0
gun_x = 300
gun_y = 500


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # gravity
    for bullet in bullets:
        bullet["y_speed"] = bullet["y_speed"] + bullet["gravity"]

        # Move the bullet
        bullet_x_old = bullet["x"]
        bullet_y_old = bullet["y"]

        bullet["x"] += bullet["x_speed"]
        bullet["y"] += bullet["y_speed"]



        # NEED TO ADJUST FOR CENTRE OF BULLET
        for box in boxes:
            # Collision detection
            if (box["x"] <= bullet["x"] <= box["x"] + box["width"]) and (box["y"] <= bullet["y"] <= box["y"] + box["height"]):
                # have you hit the box?

            # have we hit from left
                if (bullet_x_old < box["x"] and bullet["y"]>=box["y"] and bullet["y"]<=box["y"]+box["height"]):
                    bullet["x_speed"] = -bullet["bounce"] * bullet["x_speed"]
                    bullet["bounce_count"] += 1
                    bullet["x"] = box["x"]

            # have we hit from right
                if (bullet_x_old > box["x"] + box["width"] and bullet["y"] >= box["y"] and bullet["y"] <= box["y"] + box["height"]):
                    bullet["x_speed"] = -bullet["bounce"] * bullet["x_speed"]
                    bullet["bounce_count"] += 1
                    bullet["x"] = box["x"] + box["width"]

            # have we hit from above
                if (bullet_y_old < box["y"] and bullet["x"] >= box["x"] and bullet["x"] <= box["x"] + box["width"]):
                    bullet["y_speed"] = -bullet["bounce"] * bullet["y_speed"]
                    bullet["bounce_count"] += 1
                    #print ("bullet_y_speed =", bullet["y_speed"])
                    bullet["y"] = box["y"]
                    if bullet["y_speed"] > -bullet["gravity"]:
                        print ("bullet gravity problem")
                        bullet["active"] = 0
                        # bullet_status = gone


            # have we hit from below
                if (bullet_y_old > box["y"] + box["height"] and bullet["x"] >= box["x"] and bullet["x"] <= box["x"] + box["width"]):
                    bullet["y_speed"] = -bullet["bounce"] * bullet["y_speed"]
                    bullet["bounce_count"] += 1
                    bullet["y"] = box["y"] + box["height"]

    joystick = joysticks[0]
    right_analog_x = joystick.get_axis(2)
    right_analog_y = joystick.get_axis(3)
    left_analog_x = joystick.get_axis(0)
    left_analog_y = joystick.get_axis(1)


    # have we avoided drift?
    if abs(right_analog_x) + abs(right_analog_y) > 0.1:
        angle_radians = math.atan2(right_analog_y, right_analog_x)
        angle_degrees = math.degrees(angle_radians)
        print ("x=", right_analog_x, " y=", right_analog_y)
        print("angle degrees = ", angle_degrees)
        gun_angle_x = math.cos(angle_radians)
        gun_angle_y = math.sin(angle_radians)

    if abs(left_analog_x) + abs(left_analog_y) > 0.1:
        gun_x += left_analog_x * 2.5
        gun_y += left_analog_y * 2.5
    gun_y += gravity


    # if a pressed create new bullet
    if joystick.get_axis(5) > -1:

        bullets = bullets + [ {"x": gun_x + 20 * gun_angle_x, "y": gun_y + 20 * gun_angle_y, "x_speed": gun_angle_x * 20, "y_speed": gun_angle_y * 20, "gravity": 0.1, "bounce_count": 10, "active": 1,
             "bounce": 0.3}
        ]

    # Draw everything
    screen.fill(BG)
    for box in boxes:
        pygame.draw.rect(screen, box["colour"], (box["x"], box["y"], box["width"], box["height"]))
    for bullet in bullets:
        if bullet["active"] == 0:
            bullets.remove(bullet)
        pygame.draw.circle(screen, BLUE, (bullet["x"], bullet["y"]), 5)
        pygame.draw.rect(screen, BLUE, (gun_x-14, gun_y-14,28,28))
    pygame.draw.line(screen, (255, 255, 255), (gun_x, gun_y), (gun_x + 20 * gun_angle_x, gun_y + 20 * gun_angle_y))
    pygame.display.flip()



    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()