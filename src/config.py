import pygame

#Screen
WIDTH = 960 
HEIGHT = 540
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mayhem')
screen_image= pygame.image.load("images/bg_space_seamless.png")

#Color
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLACK = (0, 0 ,0)

#Score
score_spaceship_1 = 0
score_spaceship_2 = 0