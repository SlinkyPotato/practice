import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raspberry Snake')

# Set the proper color values
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
grayColor = pygame.color(150,150,150)

# Initialize Snake
snakePosition = [100,100]
snakeSegments = [[100,100], [80,100], [60,100]]
raspberryPosition = [300, 300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction

def gameOver():
    gameOverFont = pygame.fintFont('freesansbold.ttff', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, grayColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    sys.exit()

for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_RIGHT or event.key == ord('d'):
            changeDirection = 'right'
        if event.key == K_LEFT or event.key == ord('a'):
            changeDirection = 'left'
        if event.key == K_UP or event.key == ord('w'):
            changeDirection = 'up'
        if event.key == K_DOWN or event.key == ord('s'):
            changeDirection = 'down'