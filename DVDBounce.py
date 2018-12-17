""" Recreating the bouncing DVD screensaver like it is here: https://youtu.be/QOtuX0jL85Y
"""

import random
import pygame
import sys

random.seed

pygame.init()
screenx = 640
screeny = 480

screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('DVD Bounce Screensaver')
clock = pygame.time.Clock()

black = 0, 0, 0
r = 127
g = 127
b = 127

font = pygame.font.SysFont('arial', 96)
font.set_italic(True)
text = font.render('D VD ', True, (r, g, b))

box_x = 250
box_y = 250
box_xdir = 3
box_ydir = 3


def boundcheck(xpos, ypos, xsize, ysize, xscreen, yscreen):
    xbound = xscreen - xsize
    ybound = yscreen - ysize
    if xpos >= xbound:
        xpos = xbound
        box_xdir = -1* box_xdir

    elif xpos <= 0:
        xpos = 0
        box_xdir = -1 * box_xdir

    if ypos >= ybound:
        box_y = 390
        box_ydir = -1* box_ydir

    elif ypos <= 0:
        box_y = 0
        box_ydir = -1 * box_ydir

def colorchange(rcol, gcol, bcol):
    rcol = random.randint(0, 255)
    gcol = random.randint(0, 255)
    bcol = random.randint(0, 255)
    return rcol, gcol, bcol

def redirecter(xdir, ydir, xchange = False, ychange = False):
    if xchange == True:
        xdir = -1 * xdir
    if ychange == True:
        ydir = -1 * ydir
    return xdir, ydir


while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    box_x += box_xdir
    box_y += box_ydir

    pygame.draw.rect(screen, (r,g,b), (box_x, box_y, 120, 90))
    pygame.display.flip()
    pass