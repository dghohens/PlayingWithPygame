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

font = pygame.font.SysFont('arial', 48)
font.set_italic(True)
text = font.render('D VD ', True, (r, g, b))

box_x = 250
box_y = 250
box_xdir = 3
box_ydir = 3
box_xsize = 120
box_ysize = 90

def boundcheck(xpos, ypos, xsize, ysize, xscreen, yscreen):
    xbound = xscreen - xsize
    ybound = yscreen - (ysize - 20)
    xchange = False
    ychange = False

    if xpos >= xbound:
        xpos = xbound
        xchange = True

    elif xpos <= 0:
        xpos = 0
        xchange = True

    if ypos >= ybound:
        ypos = ybound
        ychange = True

    elif ypos <= -7:
        ypos = -7
        ychange = True

    return xpos, ypos, xchange, ychange

def colorchange():
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

    bounds = boundcheck(box_x, box_y, box_xsize, box_ysize, screenx, screeny)
    box_x = bounds[0]
    box_y = bounds[1]

    if bounds[2] == True or bounds[3] == True:
        redir = redirecter(box_xdir, box_ydir, bounds[2], bounds[3])
        box_xdir = redir[0]
        box_ydir = redir[1]
        randcolor = colorchange()
        r = randcolor[0]
        g = randcolor[1]
        b = randcolor[2]

    pygame.draw.ellipse(screen, (r, g, b), (box_x, box_y + (box_ysize//2), box_xsize, box_ysize//4))
    pygame.draw.ellipse(screen, black, (box_x + (box_xsize//3) + (box_xsize//20), box_y + (box_ysize//2) + (box_ysize//20), box_xsize//4, box_ysize//8))
    text = font.render('D VD ', True, (r, g, b))
    screen.blit(text, (box_x, box_y))
    pygame.display.flip()
    pass
