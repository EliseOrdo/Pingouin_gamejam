import pygame as pg

pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

runningf = True
while runningf:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
    screen.blit(background, (0, 0))
    pg.display.flip()
