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