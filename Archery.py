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
        self.rect = self.image.get_rect()
        self.angle = 12
        self.original_image = pygame.image.load('arrow.png')
        self.rect.x = 78
        self.rect.y = 733
        self.image = pygame.transform.rotate(self.original_image, 12)
        self.const = 0.0005

    def rotate(self):
        rot = pygame.transform.rotate
        self.rect.x += 10
        self.image = rot(self.original_image, self.angle)
        #self.rect.x = 78
        #self.rect.y = 733
        self.angle += -.25 % 360
        #self.rect = self.image.get_rect()
        self.rect.y = (self.const * ((self.rect.x - 600) ** 2)) + 600

all_sprites = pygame.sprite.Group()
arrow = Arrow()
all_sprites.add(arrow)


arrow_shoot = False

while True:
    clock.tick(60)
    print(arrow.rect.x, arrow.rect.y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                arrow_shoot = True
            if event.key == K_RETURN:
                arrow.angle = 11
                arrow.rect.x = 78
                arrow.rect.y == 733
                arrow.image = pygame.transform.rotate(arrow.original_image, arrow.angle)
                arrow_shoot = False
                all_sprites.update()
                all_sprites.draw(screen)
            if event.key == K_UP:
                arrow.const += 0.00001
            if event.key == K_DOWN:
                arrow.const -= 0.00001
            if event.key == K_ESCAPE:
                sys.exit()

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

    font = pygame.font.SysFont('arial', 12)
    text = font.render(str(arrow.const), True, black)
    screen.blit(text, (0,0))

    # Shoot arrow
    if arrow.rect.right < 1170 and arrow_shoot:
        arrow.rotate()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
