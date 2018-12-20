"""2D simulated solar system using Pygame.
"""

import pygame, sys, math


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

mercury_radius = 80
mercury_xpos = 80
mercury_ypos = 1
mercury_ypositive = True

venus_radius = 170
venus_xpos = 170
venus_ypos = 1
venus_ypositive = True

earth_radius = 240
earth_xpos = 240
earth_ypos = 1
earth_ypositive = True

mars_radius = 350
mars_xpos = 350
mars_ypos = 0
mars_degree = 0

moon_radius = 25
moon_xpos = 25
moon_ypos = 1
moon_ypositive = True


def planetmove(rad, xpos, ypos, ypositive):
    nearend = rad - abs(xpos)

    if nearend <= 4 and ypositive:
        xpos -= 0.4
    elif nearend <= 4 and ypositive is False:
        xpos += 0.4
    elif ypositive:
        xpos -= 1
    else:
        xpos += 1

    if xpos >= rad:
        xpos = rad
    elif xpos <= -rad:
        xpos = -rad

    ypos = ((rad ** 2) - (xpos ** 2)) ** (1 / 2)

    if ypositive is False:
        ypos = -1 * ypos
    return xpos, ypos

def degreemove(angle, radius):
    angle += 1
    xpos = math.cos(math.radians(angle)) * radius
    ypos = math.sin(math.radians(angle)) * radius
    return angle, xpos, ypos


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if mercury_ypos == 0:
        if mercury_ypositive:
            mercury_ypositive = False
        elif mercury_ypositive is False:
            mercury_ypositive = True
    mercury_pos = planetmove(mercury_radius, mercury_xpos, mercury_ypos, mercury_ypositive)
    mercury_xpos = mercury_pos[0]
    mercury_ypos = mercury_pos[1]

    if venus_ypos == 0:
        if venus_ypositive:
            venus_ypositive = False
        elif venus_ypositive is False:
            venus_ypositive = True
    venus_pos = planetmove(venus_radius, venus_xpos, venus_ypos, venus_ypositive)
    venus_xpos = venus_pos[0]
    venus_ypos = venus_pos[1]

    if earth_ypos == 0:
        if earth_ypositive:
            earth_ypositive = False
        elif earth_ypositive is False:
            earth_ypositive = True
    earth_pos = planetmove(earth_radius, earth_xpos, earth_ypos, earth_ypositive)
    earth_xpos = earth_pos[0]
    earth_ypos = earth_pos[1]

    '''if mars_ypos == 0:
        if mars_ypositive:
            mars_ypositive = False
        elif mars_ypositive is False:
            mars_ypositive = True
    mars_pos = planetmove(mars_radius, mars_xpos, mars_ypos, mars_ypositive)
    mars_xpos = mars_pos[0]
    mars_ypos = mars_pos[1]
    '''

    mars_pos = degreemove(mars_degree, mars_radius)
    mars_degree = mars_pos[0]
    mars_xpos = mars_pos[1]
    mars_ypos = mars_pos[2]

    if int(moon_ypos) == 0:
        if moon_ypositive:
            moon_ypositive = False
        elif moon_ypositive is False:
            moon_ypositive = True
    moon_pos = planetmove(moon_radius, moon_xpos, moon_ypos, moon_ypositive)
    moon_xpos = moon_pos[0]
    moon_ypos = moon_pos[1]

    # Sun
    pygame.draw.circle(screen, yellow, center, 40)
    # Mercury
    pygame.draw.circle(screen, lightgray, ((screen_xsize//2) + int(mercury_xpos), (screen_ysize//2) - int(mercury_ypos)), 4)
    # Venus
    pygame.draw.circle(screen, lightyellow, ((screen_xsize//2) + int(venus_xpos), (screen_ysize//2) - int(venus_ypos)), 12)
    # Earth
    pygame.draw.circle(screen, blue, ((screen_xsize//2) + int(earth_xpos), (screen_ysize//2) - int(earth_ypos)), 16)
    # Mars
    pygame.draw.circle(screen, red, ((screen_xsize//2) + int(mars_xpos), (screen_ysize//2) - int(mars_ypos)), 10)
    # Moon
    pygame.draw.circle(screen, lightgray, ((screen_xsize//2) + int(moon_xpos) + int(earth_xpos), (screen_ysize//2) - int(moon_ypos) - int(earth_ypos)), 3)
    pygame.display.flip()
    pass
