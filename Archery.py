""" 2D archery game
"""

import pygame, sys, math
from pygame.locals import *

pygame.init()

screen_xsize = 1440
screen_ysize = 900

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
lightyellow = (255, 255, 224)
red = (255, 0, 0)
lightgray = (211, 211, 211)
white = (255, 255, 255)
skyblue = (135, 206, 235)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_xsize, screen_ysize))
pygame.display.set_caption('Archery')


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('arrow.png')
        #self.image.set_colorkey(red)
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        '''pygame.draw.lines(self.image, black, False, [(1, 4), (49, 4), (49, 4), (45, 2), (49, 4), (45, 6)], 2)
        pygame.draw.lines(self.image, black, False, [(15, 4), (11, 1), (15, 5), (11, 8)])
        pygame.draw.lines(self.image, black, False, [(10, 4), (6, 1), (10, 5), (6, 8)])
        pygame.draw.lines(self.image, black, False, [(5, 4), (1, 1), (5, 5), (1, 8)])
        '''

    def rotate(self):
        rot = pygame.transform.rotate
        self.image = rot(self.image, 2)
        self.rect = self.image.get_rect()



all_sprites = pygame.sprite.Group()
arrow = Arrow()
all_sprites.add(arrow)

arrow.rect.x = 78
arrow.rect.y = 733

arrow_shoot = False

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                arrow_shoot = True

    screen.fill(skyblue)
    # Draw grass
    pygame.draw.rect(screen, green, (0, (screen_ysize - (screen_ysize * 0.1)), screen_xsize, (screen_ysize * 0.1)))
    # Draw target
    pygame.draw.ellipse(screen, red, ((screen_xsize * 0.8), (screen_ysize - (screen_ysize * 0.1)) - 100, 50, 100))
    pygame.draw.ellipse(screen, white, ((screen_xsize * 0.8) + 5, (screen_ysize - (screen_ysize * 0.1)) - 95, 40, 90), 5)
    pygame.draw.ellipse(screen, white, ((screen_xsize * 0.8) + 16, (screen_ysize - (screen_ysize * 0.1)) - 80, 18, 60), 5)
    # Draw legs, torso, head and left arm of archer
    pygame.draw.lines(screen, black, False,
                      [(50, screen_ysize - 90), (70, screen_ysize - 120), (90, screen_ysize - 90), (70, screen_ysize - 120),
                      (70, screen_ysize - 120), (70, screen_ysize - 180),
                       (70, screen_ysize - 160), (105, screen_ysize - 160)]
                      , 3)
    pygame.draw.circle(screen, black, (70, screen_ysize - 180), 10)
    # Draw bow
    pygame.draw.arc(screen, black, (66, screen_ysize - 210, 45, 110), -1.6, 1.6, 3)
    pygame.draw.line(screen, black, (86, screen_ysize - 210), (86, screen_ysize - 100))

    # Shoot arrow
    if arrow.rect.right < 1180 and arrow_shoot:
        arrow.rect.x += 6
        arrow.rotate()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()