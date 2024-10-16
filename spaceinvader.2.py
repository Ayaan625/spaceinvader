import pygame 
import os 
pygame.font.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = ((255,0,0))
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)


HEALTH_FONT = pygame.font.SysFont("Arial",40)
WINNER_FONT = pygame.font.SysFont("Airal",150)

FPS = 60
VEL = 5
BULLET_VEL = 7 
MAX_BULLET = 3

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,70

YELLOW_HIT = pygame.USERVENT + 1
RED_HIT = pygame.USERVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('images',"spaceship_yellow.png"))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('images',"spaceship_red.png"))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),270)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('images',"copy_of_space.png")),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
     WIN.blit(SPACE,(0,0))
     pygame.draw.rect(WIN,BLACK,BORDER)
     yellow_health_text = HEALTH_FONT.render("HEALTH: " + str(yellow_health),1,WHITE)
     red_health_text = HEALTH_FONT.render("HEALTH: " + str(red_health),1,WHITE)
     WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
     WIN.blit(yellow_health_text,(10,10))
     WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
     WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    for bullet in red_bullets:
      pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
      pygame.draw.rect(WIN,YELLOW,bullet)
     pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
      if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left 
            yellow.x = yellow.x - VEL

      if keys_pressed[pygame.K.d] and yellow.x + VEL + yellow.width < BORDER.x: #right
            yellow.x = yellow.x + VEL
      
      if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
            yellow.y = yellow.y - VEL

      if keys_pressed[pygame.K_s] and yellow.y +VEL + yellow.height < HEIGHT-15: #right
            yellow.y = yellow.y + VEL

def red_handle_movement(keys_pressed,red):
      if keys_pressed[pygame.K_a] and red.x - VEL > 0: #left 
            red.x = red.x - VEL

      if keys_pressed[pygame.K.d] and red.x + VEL + red.width < BORDER.x: #right
            red.x = red.x + VEL
      
      if keys_pressed[pygame.K_w] and red.y - VEL > 0: #up
            red.y = red.y - VEL

      if keys_pressed[pygame.K_s] and red.y +VEL + red.height < HEIGHT-15: #right
            red.y = red.y + VEL

def handle_bullets(yellow_bullets,red_bullets,yellow_red)
      for bullet in yellow_bullets:
            bullet.x = bullet.x + BULLET_VEL
            if red.colliderect(bullet):
                  pygame.event.post(pygame.event.EVENT(RED_HIT))
                  yellow_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                  yellow_bullets.remove(bullet)
        
      for bullet in red_bullets:
            bullet.x = bullet.x + BULLET_VEL
            if yellow.colliderect(bullet):
                  pygame.event.post(pygame.event.EVENT(YELLOW_HIT))
                  red_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                  red_bullets.remove(bullet)
          