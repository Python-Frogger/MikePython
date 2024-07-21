import pygame
import random
import sys

pygame.init()
# Initialize the mixer module
pygame.mixer.init()

#Score
score = 0
time = 0

# Start the timer
start_ticks = pygame.time.get_ticks()

# Set up the font
font = pygame.font.Font(None, 36)  # You can adjust the font size

# Load the sound effect
dog_hurt_sound = pygame.mixer.Sound('doghurt.mp3')
cat_hurt_sound = pygame.mixer.Sound('cathurt.mp3')

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

number_of_dogs = 4
dog_x = [0] * number_of_dogs
dog_y = [0] * number_of_dogs
dog_x_speed = [0] * number_of_dogs
dog_y_speed = [0] * number_of_dogs
dog_active = [False] * number_of_dogs

dogs = []
dog_masks = []
for i in range(number_of_dogs):
    dog = pygame.transform.scale(pygame.image.load("dog.png").convert_alpha(), (120, 120))
    dog.set_colorkey((0, 0, 0))
    dog_rect = dog.get_rect()
    dog_mask = pygame.mask.from_surface(dog)
    dogs.append(dog)
    dog_masks.append(dog_mask)



#create dog
# dog = pygame.transform.scale(pygame.image.load("dog.png").convert_alpha(), (120, 120))
# Set the color key for transparency
# dog.set_colorkey((0, 0 , 0))
# dog_rect = dog.get_rect()
# dog_mask = pygame.mask.from_surface(dog)
# mask_image = dog_mask.to_surface()
#position dog rectangle
# dog_rect.topleft = (350, 250)
# dog_active = False


#create cat
cat = pygame.transform.scale(pygame.image.load("cat.png").convert_alpha(), (120, 120))
# Set the color key for transparency
cat.set_colorkey((0, 0 , 0))
cat_rect = cat.get_rect()
cat_mask = pygame.mask.from_surface(cat)
#cat_mask_image = cat_mask.to_surface()


#create bullet and mask
bullet = pygame.Surface((20, 20))
bullet.fill(RED)
bullet_mask = pygame.mask.from_surface(bullet)



#position cat rectangle
cat_rect.topleft = (250, 150)
cat_active = False

def create_dog(i):
    global dog_active, dog_x_speed, dog_y_speed, dog_x, dog_y
    # x is either minus dog idth or plus dogwidth
    # y is random between 0 and 800-dog height
    x = random.choice([-1, 1])
    if x == -1:
        dog_x[i] = -dogs[i].get_rect().width

        # dog_x = 0
        dog_x_speed[i] = random.uniform(0.5, 1)
        dog_y_speed[i] = random.uniform(-0.2 , 0.2)
    else:
        dog_x[i] = SCREEN_WIDTH
        dog_x_speed[i] = random.uniform(-1, -0.5)
        dog_y_speed[i] = random.uniform(-0.2 , 0.2)

    dog_y[i] = random.randint(0, SCREEN_HEIGHT - dogs[i].get_rect().height)
    dog_rect = dogs[i].get_rect()
    dog_rect.x = dog_x[i]
    dog_rect.y = dog_y[i]

    dog_active[i] = True

def create_cat():
    global cat_active, cat_x_speed, cat_y_speed, cat_x, cat_y
    # x is either minus cat idth or plus catwidth
    # y is random between 0 and 800-cat height
    x = random.choice([-1, 1])
    if x == -1:
        cat_x = -cat_rect.width
        # cat_x = 0
        cat_x_speed = random.uniform(0.5, 1)
        cat_y_speed = random.uniform(-0.2 , 0.2)
    else:
        cat_x = SCREEN_WIDTH
        cat_x_speed = random.uniform(-1, -0.5)
        cat_y_speed = random.uniform(-0.2 , 0.2)

    cat_y = random.randint(0, SCREEN_HEIGHT-cat_rect.height)
    cat_rect.x = cat_x
    cat_rect.y = cat_y

    cat_active = True
def update_dog(i):
    global dog_active, dog_x_speed, dog_y_speed, dog_x, dog_y
    dog_active[i] = True
    dog_x[i] += dog_x_speed[i]
    dog_y[i] += dog_y_speed[i]

    dog_rect = dogs[i].get_rect()
    dog_rect.x = dog_x[i]
    dog_rect.y = dog_y[i]


    # check outside zone
    if dog_rect.x < -dog_rect.width or dog_rect.x > SCREEN_WIDTH or dog_rect.y < -dog_rect.height or dog_rect.y > SCREEN_HEIGHT:
        dog_active[i] = False
     
def update_cat():
    global cat_active, cat_x_speed, cat_y_speed, cat_x, cat_y
    cat_active = True
    cat_x += cat_x_speed
    cat_y += cat_y_speed

    cat_rect.x = cat_x
    cat_rect.y = cat_y

    # check outside zone
    if cat_rect.x < -cat_rect.width or cat_rect.x > SCREEN_WIDTH or cat_rect.y < -cat_rect.height or cat_rect.y > SCREEN_HEIGHT:
        cat_active = False


#game loop
run = True
while run:
  # Calculate the elapsed time
  seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Convert milliseconds to seconds
  # Check if 60 seconds have passed
  if seconds >= 60:
      print("Time's up! Game over.")
      pygame.time.wait(5000)  # Pause the game for 5 seconds

  for i in range(number_of_dogs):
    if dog_active[i] == False:
      create_dog(i)
    else:
        update_dog(i)
        screen.blit(dogs[i], (dog_x[i], dog_y[i]))
        if dog_masks[i].overlap(bullet_mask, (pos[0] - dog_x[i], pos[1] - dog_y[i])):
            col = RED
            dog_hurt_sound.play()
            score -= 1
            dog_active[i] = False
        else:
            col = GREEN

  #   update_dog(i)
#  screen.blit(dogs[i], dogs[i].get_rect())

  if cat_active == False:
    create_cat()

  #get mouse coordinates
  pos = pygame.mouse.get_pos()

  #update background
  screen.fill(BG)

  #check dog mask overlap

  #for i in range(number_of_dogs):
  #    if dog_masks[i].overlap(bullet_mask, (pos[0] - dogs[i].get_rect().x, pos[1] - dogs[i].get_rect().y)):
  #      col = RED
  #      dog_hurt_sound.play()
  #      score -= 1
  #      dog_active[i] = False#
#
  #    else:
 #       for i in range(number_of_dogs):
    #        update_dog(i)
   #         col = GREEN

  # check cat mask overlap
  if cat_mask.overlap(bullet_mask, (pos[0] - cat_rect.x, pos[1] - cat_rect.y)):
    col = GREEN
    cat_hurt_sound.play()
    score +=1
    cat_active = False

  else:
    update_cat()
    col = RED

  #draw rectangle
  bullet.fill(col)
  screen.blit(bullet, pos)
  
  # draw dog
# if dog_active:
  for i in range(number_of_dogs):
      screen.blit(dogs[i], (dog_x[i], dog_y[i]))


  screen.blit(cat, cat_rect)
  score_text = font.render(f"Score: {score}", True, (255, 255, 255))
  screen.blit(score_text, (SCREEN_WIDTH - 150, 10))  # Adjust the position as needed
  timer_surface = font.render(f"Time: {int(seconds)}", True, (255, 255, 255))
  screen.blit(timer_surface, (400, 10))  # Adjust position as needed
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()
