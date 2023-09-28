import pygame as pg


pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

mouvements = 10
font = pg.font.Font(None, 24)
text = font.render(str(mouvements), 1, (0, 100, 255))

g = True


class Pingouin:
    def __init__(self, x, y):
        self.taille = (100, 200)
        self.x = x
        self.y = y
        self.prect = pg.Rect((x, y), (20, 40))

    @staticmethod
    def peut_bouger():
        return mouvements > 0

    def move(self, touche):
        global mouvements
        global g
        vit = 22
        if self.peut_bouger():
            if touche == pg.K_UP:
                self.y -= vit
                mouvements -= 1
            elif touche == pg.K_DOWN:
                self.y += vit
                mouvements -= 1
            elif touche == pg.K_RIGHT:
                self.x += vit
                mouvements -= 1
            elif touche == pg.K_LEFT:
                self.x -= vit
                mouvements -= 1
            self.prect = pg.Rect((self.x, self.y), (20, 40))
        else:
            g = False
            fon = pg.font.Font(None, 50)
            screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))

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
    screen.blit(font.render(str(mouvements), 1, (0, 100, 255)), (960, 0))
    if not g:
        fon = pg.font.Font(None, 50)
        screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))
    pg.display.flip()
