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
mercury_degree = 0
mercury_degree_change = 0.81818

venus_radius = 170
venus_degree = 0
venus_degree_change = 0.32

earth_radius = 240
earth_degree = 0
earth_degree_change = 0.19672

mars_radius = 350
mars_degree = 0
mars_degree_change = 0.1048

moon_radius = 25
moon_degree = 0
moon_degree_change = 2.66667

def degreemove(angle, radius, angle_change):
    angle += angle_change
    xpos = math.cos(math.radians(angle)) * radius
    ypos = math.sin(math.radians(angle)) * radius
    return angle, xpos, ypos


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    mercury_pos = degreemove(mercury_degree, mercury_radius, mercury_degree_change)
    mercury_degree = mercury_pos[0]
    mercury_xpos = mercury_pos[1]
    mercury_ypos = mercury_pos[2]

    venus_pos = degreemove(venus_degree, venus_radius, venus_degree_change)
    venus_degree = venus_pos[0]
    venus_xpos = venus_pos[1]
    venus_ypos = venus_pos[2]

    earth_pos = degreemove(earth_degree, earth_radius, earth_degree_change)
    earth_degree = earth_pos[0]
    earth_xpos = earth_pos[1]
    earth_ypos = earth_pos[2]

    mars_pos = degreemove(mars_degree, mars_radius, mars_degree_change)
    mars_degree = mars_pos[0]
    mars_xpos = mars_pos[1]
    mars_ypos = mars_pos[2]

    moon_pos = degreemove(moon_degree, moon_radius, moon_degree_change)
    moon_degree = moon_pos[0]
    moon_xpos = moon_pos[1]
    moon_ypos = moon_pos[2]

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
