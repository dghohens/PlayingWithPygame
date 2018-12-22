""" 2D archery game
"""

import pygame, sys, math

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

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    #pygame.draw.arc(screen, black, )
    pygame.display.flip()