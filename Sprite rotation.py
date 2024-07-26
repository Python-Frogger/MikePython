import pygame
import math
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0

    def rotate(self, angle_change):
        self.angle += angle_change
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)




x = 100
y = 200

angle = -90

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.joystick.init()

# Get the number of joysticks
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    # Get the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(joystick.get_name())  # Print the joystick name

my_sprite = MySprite("cat.png", x, y)
all_sprites = pygame.sprite.Group(my_sprite)

speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    a_button_pressed = joystick.get_button(0)
    b_button_pressed = joystick.get_button(1)
    
    if a_button_pressed:
        my_sprite.rotate(2)
        angle += 2
    if b_button_pressed:
        x -= speed * math.cos(math.radians(angle))
        y += speed * math.sin(math.radians(angle))
        my_sprite.rect.x = x
        my_sprite.rect.y = y

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# speed = 1

# speed x math.cos(angle_radians)
# speed x math.sin(angle_radians)

pygame.quit()