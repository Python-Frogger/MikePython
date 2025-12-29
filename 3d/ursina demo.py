

from ursina import *
import random
import time

app = Ursina()

player = Entity(model="sphere", color=color.white, texture="radial_gradient", position=(0,0,0), collider='sphere')
camera.parent = player  # Make the camera a child of the player
camera.position = (0, 1.5, -9) # Position the camera relative to the player (x, y, z)
camera.rotation_x = 10 # Angle the camera down slightly

ground = Entity(model='plane', scale=300, texture='grass', collider='box', y=-20)
last_fired = 0

all_bullets = []
all_boxes = [] # Make sure you have this list to store your boxes
def create_bullet(x, y, z, a, b, c):
    global bullet
    bullet = Entity(
        model='sphere',
        texture='white_cube',  # <--- ADD THIS LINE
        position=(x, y, z),
        rotation=(a, b, c),
        color= color.green,
        collider='sphere',
        scale = 0.3# <--- ADD THIS LINE: Give each box a collider
    )
    all_bullets.append(bullet)

for i in range(100):
    box = Entity(
        model='cube',
        texture='white_cube',  # <--- ADD THIS LINE
        position=(random.uniform(-20, 20), random.uniform(-19,20), random.uniform(0,20)),
        rotation = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360)),
        color = color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        collider='box'  # <--- ADD THIS LINE: Give each box a collider
    )
    all_boxes.append(box) # Add the box to your list


def update():
    global last_fired
    # Player movement (W key for forward)
#    if held_keys['w']:
        # Move the player forward relative to its own facing direction
    player.position += player.forward * time.dt * 5  # '5' is movement speed
    for bullet in all_bullets:
        bullet.position += bullet.forward * time.dt * 50
    if held_keys['d']:
        player.rotation_y +=1

    if held_keys['a']:
        player.rotation_y -=1

    #if held_keys['s']:
        # Move the player forward relative to its own facing direction
        #player.position += player.forward * time.dt * -5  # '5' is movement speed
    if held_keys['s']:
        player.rotation_x += 1
    if held_keys['w']:
        player.rotation_x -= 1
    if held_keys['space'] and time.time() - last_fired >= 0.2:
        create_bullet(player.x, player.y, player.z, player.rotation_x, player.rotation_y, player.rotation_z)
        last_fired = time.time()

    # The camera automatically moves with the player because it's a child.
    # Its relative position (0, 1.5, -5) is maintained.

    # Collision detection for boxes
    for box_entity in all_boxes:  # Iterate through the list of ALL boxes
        if box_entity.enabled:# Only check collision if the box is still active/enabled
            for bullet in all_bullets:
                if bullet.intersects(box_entity).hit:
                    bullet.disable()
                    box_entity.disable()
            if player.intersects(box_entity).hit:  # <--- THIS IS THE SYNTAX for collision
                print(f"Game over")  # Optional: print a message
                #box_entity.disable()  # <--- THIS IS THE SYNTAX to make it disappear
                # Use .destroy() to completely remove it.
                # Use .disable() to just hide it temporarily

app.run()
