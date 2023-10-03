"""lé pengouins."""
import pygame as pg


pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

mouvements = 100
font = pg.font.Font(None, 24)
text = font.render(str(mouvements), 1, (0, 100, 255))

g = True   # tu gagnes, à voir si on garde


class Pingouin:
    """définie un pengouin."""

    def __init__(self, x, y):
        self.taille = (20, 40)
        # (width = horizontal = axe x, height = vertical = axe y)
        self.x = x
        self.y = y
        # Le point (x,y) est le point en haut à gauche de rectangle.
        self.prect = pg.Rect((self.x, self.y), self.taille)

    def touche_pas_truc(self, truc):  # fonction pareille mais pour tous objets : pingouins dans prnigouins et d'ailleurs les bords aussi (= murs ???)
        """Vérifie si le pinguoin touche le truc (le truc doit avoir x et y en paramètre)."""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        return (x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < x4[1]) or (x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < x4[1] ) or (y3[0] < y1[0] < y4[0] and y3[1] < y1[1] < y4[1] ) or (y3[0] < y2[0] < y4[0] and y3[1] < y2[1] < y4[1] )


    def touche_qui_ou(self):
        """Renvoie le mur touché par le pengouin, et sur quelle moitié de côté."""
        for mur in liste_murs:
            if not self.touche_pas_truc(mur):
                
                return mur
        return True

    @staticmethod
    def reste_mouvements():
        """Pour savoir si le joueur a encore des mouvements."""
        return mouvements > 0

    def move(self, touche):
        """Fait bouger le pengouin."""
        global mouvements
        global g
        vit = 22
        if self.touche_qui_ou() is True:
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
        #else:
            # décaler le pengouin ver là où c'est logique
        """else:
            g = False
            fon = pg.font.Font(None, 50)
            screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))"""


class Mur:
    """Un mur."""

    def __init__(self, x, y):

        self.taille = (120, 140)
        self.x = x
        self.y = y
        self.mrect = pg.Rect((x, y), self.taille)


mur1 = Mur(100, 100)
liste_murs = [mur1]
ping = Pingouin(0, 0)
runningf = True
while runningf:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            if mouvements > 0:
                ping.move(event.key)
            else:
                fon = pg.font.Font(None, 50)
                screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))
    screen.blit(background, (0, 0))
    pg.draw.rect(screen, (250, 250, 250), mur1.mrect)
    pg.draw.rect(screen, (250, 250, 250), ping.prect)
    pg.draw.rect(screen, (0, 0, 0), ping.prect, 1)
    screen.blit(font.render(str(mouvements), 1, (0, 100, 255)), (960, 0))

    pg.display.flip()
pg.quit()
