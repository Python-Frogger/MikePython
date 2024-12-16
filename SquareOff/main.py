import pygame
import math
import random
# import asyncio
import time

# Initialize Pygame
pygame.init()
pygame.joystick.init()
pygame.mixer.init()
bullet1_sound = pygame.mixer.Sound('bullet1.ogg')
death1_sound = pygame.mixer.Sound('death1.ogg')
hurt1_sound = pygame.mixer.Sound('hurt1.ogg')
selection_music = pygame.mixer.Sound('musicinstrumental.ogg')
game1_music = pygame.mixer.Sound('musicrock.ogg')
title_screen = pygame.image.load('title_screen.png')


joysticks = []
try:
    pygame.joystick.init()
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)
    print(f"Initialized {len(joysticks)} joysticks")
except pygame.error:
    print("Joystick initialization failed")

# Set up some constants
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height)) # screen size
font = pygame.font.Font(None, 36)  # You can adjust the font size



# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)


players = [
    # player 1
    {"x": 150, "y": 450,  "gun_x": 1, "gun_y": 0, "colour": GREEN, "js_num": 0, "gravity": 0.1, "y_speed": 0,
     "fire_rate": 500, "reload_speed": 1000, "time_last_shot_fired": 0, "max_bullets": 3, "current_bullets": 3, "is_reloading": False,
    "time_start_reload": 0, "health": 100, "jump_count": 1 , "jump_force": -4, "time_last_jumped": 0, "bullet_speed": 9, "bullet_gravity": 0.2,
     "bullet_damage": 50, "speed": 2.5, "choice": False, "lives": 5, "powerup": True, "max_health": 100, "deaths": 0, "bullet_bounce" : 2, "bullet_homing" : False},
    # player 2
    {"x": 500, "y": 450,  "gun_x": -1, "gun_y": 0, "colour": BLUE, "js_num": 1, "gravity": 0.1, "y_speed": 0,
     "fire_rate": 500, "reload_speed": 1000, "time_last_shot_fired": 0, "max_bullets": 3, "current_bullets": 3, "is_reloading": False,
    "time_start_reload": 0, "health": 100, "jump_count": 1 , "jump_force": -4, "time_last_jumped": 0, "bullet_speed": 9, "bullet_gravity": 0.2,
     "bullet_damage": 50, "speed": 2.5, "choice": False, "lives": 5, "powerup": True, "max_health": 100, "deaths": 0, "bullet_bounce" : 2, "bullet_homing" : False}
]

# control for only one joystick
# Assign joysticks to players
for i, p in enumerate(players):
    if i < len(joysticks):
        p["js_num"] = i
    else:
        p["js_num"] = None  # No joystick available for this player

# Box coordinates and dimensions

# boxes = [
#     {"x": 500, "y": 500, "width": 200, "height": 100, "colour": RED},
#     {"x": 200, "y": 200, "width": 300, "height": 100, "colour": RED},
#     {"x": 200, "y": 600, "width": 200, "height": 100, "colour": RED},
#     {"x": 50, "y": 350, "width": 300, "height": 100, "colour": RED},
#     {"x": 780, "y": 0, "width": 20, "height": 800, "colour": WHITE},
#     {"x": 0, "y": 0, "width": 800, "height": 20, "colour": WHITE},
#     {"x": 0, "y": 00, "width": 20, "height": 800, "colour": WHITE},
#     {"x": 0, "y": 780, "width": 800, "height": 20, "colour": WHITE},
# ]

levels = [
    # level 1
    [
    {"x": 0, "y": 0, "width": 40, "height": 800, "colour": RED},
    {"x": 40, "y": 0, "width": 1320, "height": 40, "colour": RED},
    {"x": 1360, "y": 0, "width": 40, "height": 800, "colour": RED},
    {"x": 40, "y": 760, "width": 1320, "height": 40, "colour": RED},
    {"x": 200, "y": 160, "width": 200, "height": 80, "colour": RED},
    {"x": 1000, "y": 160, "width": 200, "height": 80, "colour": RED},
    {"x": 560, "y": 120, "width": 40, "height": 160, "colour": RED},
    {"x": 800, "y": 120, "width": 40, "height": 160, "colour": RED},
    {"x": 360, "y": 400, "width": 280, "height": 40, "colour": RED},
    {"x": 760, "y": 400, "width": 280, "height": 40, "colour": RED},
    {"x": 160, "y": 600, "width": 120, "height": 120, "colour": RED},
    {"x": 1120, "y": 600, "width": 120, "height": 120, "colour": RED},
    {"x": 440, "y": 640, "width": 520, "height": 80, "colour": RED},
    ],
    # level 2
[
    {"x": 840, "y": 200, "width": 320, "height": 120, "colour": RED},
    {"x": 1360, "y": 0, "width": 40, "height": 760, "colour": RED},
    {"x": 0, "y": 0, "width": 1360, "height": 40, "colour": RED},
    {"x": 0, "y": 40, "width": 40, "height": 760, "colour": RED},
    {"x": 40, "y": 760, "width": 1360, "height": 40, "colour": RED},
    {"x": 800, "y": 560, "width": 440, "height": 80, "colour": RED},
    {"x": 120, "y": 560, "width": 400, "height": 80, "colour": RED},
    {"x": 120, "y": 200, "width": 400, "height": 120, "colour": RED},
    {"x": 520, "y": 400, "width": 280, "height": 80, "colour": RED},
    {"x": 600, "y": 600, "width": 120, "height": 160, "colour": RED},
],
    # level 3
[
    {"x": 0, "y": 0, "width": 40, "height": 800, "colour": RED},
    {"x": 40, "y": 760, "width": 1360, "height": 40, "colour": RED},
    {"x": 1360, "y": 0, "width": 0, "height": 760, "colour": RED},
    {"x": 1360, "y": 0, "width": 40, "height": 760, "colour": RED},
    {"x": 40, "y": 0, "width": 1320, "height": 40, "colour": RED},
    {"x": 120, "y": 680, "width": 0, "height": 80, "colour": RED},
    {"x": 120, "y": 680, "width": 40, "height": 80, "colour": RED},
    {"x": 240, "y": 600, "width": 40, "height": 160, "colour": RED},
    {"x": 360, "y": 520, "width": 40, "height": 240, "colour": RED},
    {"x": 480, "y": 440, "width": 40, "height": 320, "colour": RED},
    {"x": 600, "y": 360, "width": 40, "height": 400, "colour": RED},
    {"x": 1240, "y": 680, "width": 40, "height": 80, "colour": RED},
    {"x": 1120, "y": 600, "width": 40, "height": 160, "colour": RED},
    {"x": 1000, "y": 520, "width": 40, "height": 240, "colour": RED},
    {"x": 880, "y": 440, "width": 40, "height": 320, "colour": RED},
    {"x": 760, "y": 360, "width": 40, "height": 400, "colour": RED},
    {"x": 680, "y": 480, "width": 40, "height": 280, "colour": RED},
    {"x": 120, "y": 80, "width": 160, "height": 80, "colour": RED},
    {"x": 1120, "y": 80, "width": 160, "height": 80, "colour": RED},
    {"x": 400, "y": 80, "width": 160, "height": 80, "colour": RED},
    {"x": 840, "y": 80, "width": 160, "height": 80, "colour": RED},
    {"x": 640, "y": 80, "width": 120, "height": 80, "colour": RED},
    {"x": 120, "y": 400, "width": 80, "height": 120, "colour": RED},
    {"x": 1200, "y": 400, "width": 80, "height": 120, "colour": RED},
    {"x": 240, "y": 240, "width": 160, "height": 80, "colour": RED},
    {"x": 1000, "y": 240, "width": 160, "height": 80, "colour": RED},
]
]


# Bullet coordinates and speeds
bullets = [
    {"x": 100, "y": 600, "x_speed": 7, "y_speed": -16, "gravity": 0.1, "bounce_count": 0, "active": 0, "bounce": 0.9, "colour": GREEN,
     "damage": 10, "time_created": 3000, "homing": False}
]

powerups = [
    #bounces
    ["Bounce", "More bounces for bullets"],
    ["Bullet", "Bigger magazine, less damage"],
    ["Reload", "Double fire rate, double reload speed, 75% damage"],
    ["Health", "Player Health increase, Player speed decrease"],
    ["Parkour", "Increase player speed, 80% x health"],
    ["Bullet_speed", "Increased bullet speed"],
    ["Bullet_strength", "Increase bullet damage, half bullet speed, trajectory same"],
    ["Homing", "Heat-seeking bullets, 75% bullet damage"]]
#    [{"Bullet", "Reload", "Health", "Parkour", "Bullet_speed", "Bullet_strength", "Homing"]
selected_powerups = []

gravity = 0.1

gun_angle_x = 0
gun_angle_y = 0
gun_x = 300
gun_y = 500

# print text function
def print_text(text, x, y,  colour):
    screen.blit(font.render(text, True,colour), (x, y))


def calculate_angle(x_speed, y_speed):
    # Calculate angle with 0 degrees as north (upward)
    angle_rad = math.atan2(x_speed, -y_speed)  # Note the order and negation
    angle_deg = math.degrees(angle_rad)

    # Ensure the angle is between 0 and 360 degrees
    angle_deg = (angle_deg + 360) % 360
    return angle_deg


def update_velocity(current_x_speed, current_y_speed, new_angle_degrees):
    # Calculate current speed
    current_speed = math.sqrt(current_x_speed ** 2 + current_y_speed ** 2)

    # Convert angle to radians
    new_angle_radians = math.radians(new_angle_degrees)

    # Calculate new x and y speeds
    new_x_speed = current_speed * math.sin(new_angle_radians)
    new_y_speed = -current_speed * math.cos(new_angle_radians)

    return new_x_speed, new_y_speed


stage_selection = True
pygame.mixer.music.load('musicinstrumental.mp3')
pygame.mixer.music.play(-1)

chosen_count = 2
# *** Game loop ****
running = True
# async def main():
#   global running, stage_selection, chosen_count, selected_powerups, bullets
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# loop for game lives

    if stage_selection == True:
        if not selected_powerups:
            selected_powerups = random.sample(powerups, 4)
            boxes = random.choice(levels)
        screen.blit(title_screen, (0, 0)) # plot background
        print_text(f"UP:  {selected_powerups[0][0]}: {selected_powerups[0][1]}", 100, 100, YELLOW)
        print_text(f"DOWN:  {selected_powerups[1][0]}: {selected_powerups[1][1]}", 100, 200, YELLOW)
        print_text(f"LEFT:  {selected_powerups[2][0]}: {selected_powerups[2][1]}", 100, 300, YELLOW)
        print_text(f"RIGHT:  {selected_powerups[3][0]}: {selected_powerups[3][1]}", 100, 400, YELLOW)
        # print_text("DOWN: Big Bullet: x2 damage, 1/2 bullet speed - same trajectory", 100, 200, WHITE)
        # print_text("LEFT: Super Sniper: x4 bullet speed", 100, 300, WHITE)
        # print_text("RIGHT: Parkour Pro: x2 speed inc jump, 20% less armour", 100, 400, WHITE)

#            for p in players:
#                if p["choice"] == False and p["powerup"]:
#                    joystick = joysticks[p["js_num"]]
#                    hat_x, hat_y = joystick.get_hat(0)  # Get D-pad input
#                    print(f"Joystick {p['js_num']} D-pad: ({hat_x}, {hat_y})")
#                    print (p["choice"], chosen_count)

        for p in players:
            if p["choice"] == False and p["powerup"]:
                if p["js_num"] is not None and p["js_num"] < len(joysticks):
                    joystick = joysticks[p["js_num"]]
                    try:
                        hat_x, hat_y = joystick.get_hat(0)  # Get D-pad input
                        print(f"Joystick {p['js_num']} D-pad: ({hat_x}, {hat_y})")
                    except pygame.error:
                        print(f"Error reading hat for joystick {p['js_num']}")
                        hat_x, hat_y = 0, 0
                else:
                    # No joystick for this player, maybe use keyboard input instead
                    hat_x, hat_y = 0, 0
                #print(p["choice"], chosen_count)


                if hat_x != 0 or hat_y != 0:
                    if hat_x == -1 and hat_y == 0:
                        p["choice"] = selected_powerups[2][0]
                        p["powerup"] = False
                        chosen_count -= 1
                    if hat_x == 1 and hat_y == 0:
                        p["choice"] = selected_powerups[3][0]
                        p["powerup"] = False
                        chosen_count -= 1
                    if hat_x == 0 and hat_y == 1:
                        p["choice"] = selected_powerups[0][0]
                        p["powerup"] = False
                        chosen_count -= 1
                    if hat_x == 0 and hat_y == -1:
                        p["choice"] = selected_powerups[1][0]
                        p["powerup"] = False
                        chosen_count -= 1

        # apply power ups
        # powerups = ["Bounce",
        if chosen_count == 0:
            stage_selection = False
            selected_powerups = []
            for p in players:
                if p["choice"] == "Health":
                    p["max_health"] += 100
                    p["health"] = p["max_health"]
                    p["speed"] -=1
                if p["choice"] == "Bullet_strength":
                    p["bullet_damage"] += 50
                    p["bullet_speed"] *= 0.5
                    p["bullet_gravity"] *= 0.25
                if p["choice"] == "Bullet_speed":
                    p["bullet_speed"] += 9
                if p["choice"] == "Parkour":
                    p["speed"] += 2.5
                    p["jump_force"] += -4
                    p["max_health"] *= 0.8
                    p["health"] = p["max_health"]
                if p["choice"] == "Reload":
                    p["fire_rate"] *= 0.5
                    p["reload_speed"] *= 0.5
                    p["bullet_damage"] *= 0.75
                if p["choice"] == "Bullet":
                    p["max_bullets"] += 2
                    p["bullet_damage"] *= 0.75
                    p["current_bullets"] = p["max_bullets"]
                if p["choice"] == "Bounce":
                    p["bullet_bounce"] +=3
                if p["choice"] == "Homing":
                    p["bullet_homing"] = True
                    p["bullet_damage"] *= 0.75
        pygame.display.flip()
        # await asyncio.sleep(0)

        # Cap the frame rate
        pygame.time.Clock().tick(60)
        # print("i'm running")

    if stage_selection == False:
        # gravity
        for bullet in bullets:

            if bullet["homing"] == False:
                # regular bullets
                bullet["y_speed"] = bullet["y_speed"] + bullet["gravity"]

                # Move the bullet
                bullet_x_old = bullet["x"]
                bullet_y_old = bullet["y"]

                bullet["x"] += bullet["x_speed"]
                bullet["y"] += bullet["y_speed"]

            else:
                # homing bullets


                # can't see other player?
                bullet_angle = calculate_angle(bullet["x_speed"], bullet["y_speed"])

                for p in players:
                    player_angle = calculate_angle(p["x"]-bullet["x"], p["y"]-bullet["y"])
                    if abs(bullet_angle - player_angle) <= 60:
                        # NEED TO  CHECK FOR BOXES TBC

                        bullet["x_speed"], bullet["y_speed"] = update_velocity(bullet["x_speed"], bullet["y_speed"], player_angle)



                    else:
                    # regular bullets
                        bullet["y_speed"] = bullet["y_speed"] + bullet["gravity"]

                        # Move the bullet
                        bullet_x_old = bullet["x"]
                        bullet_y_old = bullet["y"]

                        bullet["x"] += bullet["x_speed"]
                        bullet["y"] += bullet["y_speed"]

                # gotchya!


            # NEED TO ADJUST FOR CENTRE OF BULLET
            for box in boxes:
                # Collision detection
                if (box["x"] <= bullet["x"] <= box["x"] + box["width"]) and (box["y"] <= bullet["y"] <= box["y"] + box["height"]):
                    # have you hit the box?

                # have we hit from left
                    if (bullet_x_old < box["x"] and bullet["y"]>=box["y"] and bullet["y"]<=box["y"]+box["height"]):
                        bullet["x_speed"] = -bullet["bounce"] * bullet["x_speed"]
                        bullet["bounce_count"] -= 1
                        if bullet["bounce_count"] < 0:
                            bullet["active"] = 0
                        bullet["x"] = box["x"]

                # have we hit from right
                    if (bullet_x_old > box["x"] + box["width"] and bullet["y"] >= box["y"] and bullet["y"] <= box["y"] + box["height"]):
                        bullet["x_speed"] = -bullet["bounce"] * bullet["x_speed"]
                        bullet["bounce_count"] -= 1
                        if bullet["bounce_count"] < 0:
                            bullet["active"] = 0
                        bullet["x"] = box["x"] + box["width"]

                # have we hit from above
                    if (bullet_y_old < box["y"] and bullet["x"] >= box["x"] and bullet["x"] <= box["x"] + box["width"]):
                        bullet["y_speed"] = -bullet["bounce"] * bullet["y_speed"]
                        bullet["bounce_count"] -= 1
                        if bullet["bounce_count"] < 0:
                            bullet["active"] = 0
                        #print ("bullet_y_speed =", bullet["y_speed"])
                        bullet["y"] = box["y"]

                        if bullet["y_speed"] > -bullet["gravity"]:
                            print ("bullet gravity problem")
                            bullet["active"] = 0
                            # bullet_status = gone

                # have we hit from below
                    if (bullet_y_old > box["y"] + box["height"] and bullet["x"] >= box["x"] and bullet["x"] <= box["x"] + box["width"]):
                        bullet["y_speed"] = -bullet["bounce"] * bullet["y_speed"]
                        bullet["bounce_count"] -= 1
                        if bullet["bounce_count"] < 0:
                            bullet["active"] = 0
                        bullet["y"] = box["y"] + box["height"]

                # are we inside the box ie firing stupidly or other glitch
                    if  (box["x"] < bullet["x"] < box["x"] + box["width"] and box["y"] < bullet["y"] < box["y"] + box["height"]):
                        bullet["active"] = 0

            # has bullet expired?
            if pygame.time.get_ticks() - bullet["time_created"] >= 2000:
                bullet["active"] = False

        # move players and shoot
        for p in players:

            player_x_old = p["x"]
            player_y_old = p["y"]

            joystick = joysticks[p["js_num"]]
            right_analog_x = joystick.get_axis(2)
            right_analog_y = joystick.get_axis(3)
            left_analog_x = joystick.get_axis(0)
            left_analog_y = joystick.get_axis(1)
            a = joystick.get_button(0)

            # have we avoided drift?

            if abs(right_analog_x) + abs(right_analog_y) > 0.1:
                angle_radians = math.atan2(right_analog_y, right_analog_x)
                angle_degrees = math.degrees(angle_radians)
                p["gun_x"] = math.cos(angle_radians)
                p["gun_y"] = math.sin(angle_radians)

            if abs(left_analog_x) + abs(left_analog_y) > 0.1:
                p["x"] += left_analog_x * p["speed"]

            # jumped?
            if a:
                if p["jump_count"] >0:
                    if pygame.time.get_ticks() >= p["time_last_jumped"] + 500:
                        p["y_speed"] = p["jump_force"]
                        p["jump_count"] -=1
                        p["time_last_jumped"] = pygame.time.get_ticks()

            # gravity pull on players
            p["y_speed"] += p["gravity"]
            p["y"] += p["y_speed"]
            p["y"] = min(p["y"], screen_height - 14)
            p["y"] = max(p["y"],14 )
            p["x"] = max(14, p["x"])
            p["x"] = min(screen_width - 14, p["x"])


            # create new bullet
            if joystick.get_axis(5) > -1 and p["current_bullets"] > 0 and pygame.time.get_ticks() >= p["time_last_shot_fired"] + p["fire_rate"] and p["is_reloading"] == False:

                bullets = bullets + [ {"x": p["x"] + 20 * p["gun_x"], "y": p["y"] + 20 * p["gun_y"], "x_speed": p["gun_x"] * p["bullet_speed"],
                                       "y_speed": p["gun_y"] * p["bullet_speed"], "gravity": p["bullet_gravity"], "bounce_count": p["bullet_bounce"], "active": 1,
                     "bounce": 0.3, "colour": p["colour"], "damage": p["bullet_damage"], "time_created" : pygame.time.get_ticks(), "homing" : p["bullet_homing"]}
                ]

                p["current_bullets"] -= 1
                p["time_last_shot_fired"] = pygame.time.get_ticks()
                bullet1_sound.play()

            # time to reload?
            if p["is_reloading"] == False:
                if p["current_bullets"] == 0 or joystick.get_axis(4) > -1:
                    p["is_reloading"] = True
                    p["time_start_reload"] = pygame.time.get_ticks()

            # reloading complete?
            if p["is_reloading"] and pygame.time.get_ticks() >= p["time_start_reload"] + p["reload_speed"]:
                p["current_bullets"] = p["max_bullets"]
                p["is_reloading"] = False

            # collision with boxes
            for box in boxes:
                # Collision detection with box
                player_rect = pygame.Rect(p["x"] - 14, p["y"] - 14, 28, 28)
                box_rect = pygame.Rect(box["x"], box["y"], box["width"], box["height"])
                if player_rect.colliderect(box_rect):
                    # have you hit the box?

                # have we hit from left
                    if (player_x_old <= box["x"] and p["y"]>=box["y"] and p["y"]<=box["y"]+box["height"]):
                        p["x"] = box["x"]-14
                        p["jump_count"] = 1

                # have we hit from right
                    if (player_x_old >= box["x"] + box["width"] and p["y"] >= box["y"] and p["y"] <= box["y"] + box["height"]):
                        p["x"] = box["x"] + box["width"] + 14
                        p["jump_count"] = 1

                # have we hit from above
                    if (player_y_old <= box["y"] and p["x"] >= box["x"] and p["x"] <= box["x"] + box["width"]):
                        p["y_speed"] = 0
                        p["y"] = box["y"]-14
                        p["jump_count"] = 1

                # have we hit from below
                    if (player_y_old >= box["y"] + box["height"] and p["x"] >= box["x"] and p["x"] <= box["x"] + box["width"]):
                        p["y_speed"] = 0
                        p["y"] = box["y"] + box["height"]+14

            # player bullet collission
            for bullet in bullets:
                if (p["x"] - 14 <= bullet["x"] <= p["x"] + 14) and (p["y"] - 14 <= bullet["y"] <= p["y"] + 14):
                    bullet["active"] = 0
                    p["health"] -= bullet["damage"]
                    hurt1_sound.play()

        # Draw everything
        screen.fill(BG)
        for box in boxes:
            pygame.draw.rect(screen, box["colour"], (box["x"], box["y"], box["width"], box["height"]))

        # draw players
        for p in players:
            #body
            pygame.draw.rect(screen, p["colour"], (p["x"]-14, p["y"]-14,28,28))
            # gun
            pygame.draw.line(screen, (255, 255, 255), (p["x"], p["y"]), (p["x"] + 20 * p["gun_x"], p["y"] + 20 * p["gun_y"]))
            # health bar
            pygame.draw.line(screen, (0,255,0), (p["x"]-14, p["y"]-18), (p["x"]-14+p["health"]/100*26, p["y"]-18))
            # deaths

        # score
        print_text("Player 1: " + str(players[0]["deaths"]), 50, 0, WHITE)
        print_text("Player 2: " + str(players[1]["deaths"]), 200, 0, WHITE)

        for bullet in bullets:
            if bullet["active"] == 0:
                bullets.remove(bullet)
            pygame.draw.circle(screen, bullet["colour"], (bullet["x"], bullet["y"]), bullet['damage'] / 10)

        pygame.display.flip()

        # check death
        for index, p in enumerate(players):
            if p["health"] <= 0:
                death1_sound.play()
                player_number = str(index + 1)
                print(f"Player {player_number} dies")
                print_text(f"Player {player_number} dies", 300, 400, YELLOW)
                pygame.display.flip()
                pygame.time.delay(5000)
                p["powerup"] = True
                p["deaths"] += 1
                for q in players:
                    q["choice"] = False
                    q["health"] = q["max_health"]
                    q["current_bullets"] = q["max_bullets"]
                stage_selection = True
                chosen_count = 1
                players[0]["x"] = 10
                players[0]["y"] = 450
                players[1]["x"] = 500
                players[1]["y"] = 450
                for b in bullets: # remove old bullets
                    b["active"] = False

                # reset players

        # Cap the frame rate
        pygame.time.Clock().tick(60)
        # await asyncio.sleep(0)

# asyncio.run(main())
# Quit Pygame
# pygame.quit()