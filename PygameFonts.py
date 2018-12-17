import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False
black = 0, 0, 0

fontlist = pygame.font.get_fonts()

while not done:
    pygame.event.get()
    for i in fontlist:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        font = pygame.font.SysFont(i, 96)
        font.set_italic(True)
        text = font.render('D VD ', True, (0, 128, 0))
        screen.fill(black)
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()
        clock.tick(2)
    done = True
