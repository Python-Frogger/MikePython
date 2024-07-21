import pygame

pygame.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

#define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#hide mouse cursor
pygame.mouse.set_visible(False)

#create dog
dog = pygame.transform.scale(pygame.image.load("dog.png").convert_alpha(), (160, 160))
# Set the color key for transparency
dog.set_colorkey((0, 0 , 0))
dog_rect = dog.get_rect()
dog_mask = pygame.mask.from_surface(dog)
mask_image = dog_mask.to_surface()

#create bullet and mask
bullet = pygame.Surface((20, 20))
bullet.fill(RED)
bullet_mask = pygame.mask.from_surface(bullet)

#position dog rectangle
dog_rect.topleft = (350, 250)

#game loop
run = True
while run:

  #get mouse coordinates
  pos = pygame.mouse.get_pos()

  #update background
  screen.fill(BG)

  #check mask overlap
  if dog_mask.overlap(bullet_mask, (pos[0] - dog_rect.x, pos[1] - dog_rect.y)):
    col = RED
  else:
    col = GREEN

  #draw mask image
  # screen.blit(mask_image, (0, 0))

  # draw dog
  screen.blit(dog, dog_rect)

  #draw rectangle
  bullet.fill(col)
  screen.blit(bullet, pos)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()
