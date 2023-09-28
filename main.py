import pygame as pg
import time

pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))


class Pingouin:
    def __init__(self, x, y):
        self.taille = (100, 200)
        self.x = x
        self.y = y
        self.prect = pg.Rect((x, y), (20, 40))

    def move(self, touche):
        vit = 22
        if touche == pg.K_UP:
            self.y -= vit
        elif touche == pg.K_DOWN:
            self.y += vit
        elif touche == pg.K_RIGHT:
            self.x += vit
        elif touche == pg.K_LEFT:
            self.x -= vit
        self.prect = pg.Rect((self.x, self.y), (20, 40))


ping = Pingouin(0, 0)
runningf = True
while runningf:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            ping.move(event.key)
    screen.blit(background, (0, 0))
    pg.draw.rect(screen, (250, 250, 250), ping.prect)
    pg.draw.rect(screen, (0, 0, 0), ping.prect, 1)
    #time.sleep(0.5)
    pg.display.flip()
