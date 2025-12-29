from ursina import *
import random
from ursina.camera import Camera as UrsinaCamera # Explicitly import Camera

app = Ursina()

# --- Player 1 Setup ---
player1 = Entity(model="sphere", color=color.blue, texture="radial_gradient", position=(-5,0,0), collider='sphere')
# The global 'camera' (lowercase 'c') is the default and is always active.
# We assign its properties for Player 1.
camera.parent = player1
camera.position = (0, 1.5, -9) # Relative to player1
camera.rotation_x = 10
camera.viewport = (0, 0, 0.5, 1) # Left half of the screen

# --- Player 2 Setup ---
player2 = Entity(model="sphere", color=color.red, texture="radial_gradient", position=(5,0,0), collider='sphere')

# Create a new Camera instance for Player 2.
# By default, Ursina's scene automatically adds new Camera instances to its rendering list.
player2_camera_instance = UrsinaCamera(
    parent=player2,          # Parent it to player2 so it follows
    position=(0, 1.5, -9),   # Position relative to player2
    rotation_x=10,
    viewport=(0.5, 0, 0.5, 1) # Right half of the screen
)

# Optional: If you find only one camera rendering, it might be due to the default
# camera taking precedence. You can ensure both are active.
# Typically, setting the viewport on a new UrsinaCamera instance is enough to make it render.
# The scene.cameras list contains all active camera renderers.
# You can check scene.cameras to see if both are present after app.run() starts,
# or even print it before app.run() to debug.

ground = Entity(model='plane', scale=300, texture='grass', collider='box', y=-20)

all_boxes = []

for i in range(100):
    box = Entity(
        model='cube',
        texture='white_cube',
        position=(random.uniform(-20, 20), random.uniform(-19,20), random.uniform(0,20)),
        rotation = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360)),
        color = color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        collider='box'
    )
    all_boxes.append(box)

def update():
    # --- Player 1 Input and Movement (WASD) ---
    if held_keys['w']:
        player1.position += player1.forward * time.dt * 5
    if held_keys['s']:
        player1.rotation_x -= 1
    if held_keys['a']:
        player1.rotation_y -= 1
    if held_keys['d']:
        player1.rotation_y += 1

    # --- Player 2 Input and Movement (Arrow Keys) ---
    if held_keys['up arrow']:
        player2.position += player2.forward * time.dt * 5
    if held_keys['down arrow']:
        player2.rotation_x -= 1
    if held_keys['left arrow']:
        player2.rotation_y -= 1
    if held_keys['right arrow']:
        player2.rotation_y += 1

    # Collision detection for boxes
    for box_entity in all_boxes:
        if box_entity.enabled:
            if player1.intersects(box_entity).hit:
                print(f"Player 1 hit a box!")
                box_entity.disable()

            if player2.intersects(box_entity).hit:
                print(f"Player 2 hit a box!")
                box_entity.disable()

app.run()