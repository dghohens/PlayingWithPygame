"""2D simulated solar system using Pygame.
"""

import pygame, sys


pygame.init()

screen_xsize = 1280
screen_ysize = 720
center = (screen_xsize//2, screen_ysize//2)

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
lightyellow = (255, 255, 224)
red = (255, 0, 0)
lightgray = (211, 211, 211)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_xsize, screen_ysize))

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Sun
    pygame.draw.circle(screen, yellow, center, 20)
    # Mercury
    pygame.draw.circle(screen, lightgray, ((screen_xsize//2) + 35, screen_ysize//2), 2)
    # Venus
    pygame.draw.circle(screen, lightyellow, ((screen_xsize//2) + 65, screen_ysize//2), 6)
    # Earth
    pygame.draw.circle(screen, blue, ((screen_xsize//2) + 95, screen_ysize//2), 8)
    # Mars
    pygame.draw.circle(screen, red, ((screen_xsize//2) + 125, screen_ysize//2), 5)
    pygame.display.flip()
    pass
