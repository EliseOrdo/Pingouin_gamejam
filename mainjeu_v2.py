"""lé pengouins."""
import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

mouvements = 0
font = pg.font.Font(None, 24)
text = font.render(str(mouvements), 1, (0, 100, 255))

g = True  # tu gagnes, à voir si on garde


class Pingouin:
    """définie un pingouin."""

    def __init__(self, x, y):
        self.taille = (20, 40)
        # (width = horizontal = axe x, height = vertical = axe y)
        self.x = x
        self.y = y
        # Le point (x,y) est le point en haut à gauche de rectangle.
        self.prect = pg.Rect((self.x, self.y), self.taille)
        self.cache = False

    def touche_truc(self, truc):
        """Vérifie si le pinguoin touche le truc (le truc doit avoir x et y en paramètre)."""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        g = 0 > x1[0]
        h = 0 > x1[1]
        d = 1000 < x2[0]
        b = 800 < y1[1]
        return hg or basg or hd or bd or g or h or d or b

    def touche_qui_ou(self):
        """Renvoie le mur touché par le pingouin, et sur quelle moitié de côté."""
        for mur in liste_murs:
            # print(self.x, sel
            if self.touche_truc(mur):
                # print('A')
                return True
        return False

    @staticmethod
    def perdu():
        """Le text quand c'est perdu."""
        fon = pg.font.Font(None, 50)
        screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))

    def move(self, touche):
        """Fait bouger le pingouin."""
        global mouvements
        global g
        vit = 22
        if self.touche_qui_ou() is False:
            if touche == pg.K_UP:
                self.y -= vit

            elif touche == pg.K_DOWN:
                self.y += vit
            elif touche == pg.K_RIGHT:
                self.x += vit
            elif touche == pg.K_LEFT:
                self.x -= vit

            self.prect = pg.Rect((self.x, self.y), (20, 40))

        while self.touche_qui_ou() is True:
            if touche == pg.K_UP:
                self.y += 1
            elif touche == pg.K_DOWN:
                self.y -= 1
            elif touche == pg.K_RIGHT:
                self.x -= 1
            elif touche == pg.K_LEFT:
                self.x += 1
            self.prect = pg.Rect((self.x, self.y), (20, 40))

        """else:
            g = False
            fon = pg.font.Font(None, 50)
            screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))"""


class Mur:
    """Un mur."""

    def __init__(self, x, y, taille):
        self.taille = taille
        self.x = x
        self.y = y
        self.mrect = pg.Rect((x, y), self.taille)
        self.couleur = (250, 250, 250)


class Cible:
    """Je propose que l but soit d'aller dans l'eau, genre pour chercher du poisson."""

    def __init__(self, x, y):
        self.taille = (40, 40)
        self.x = x
        self.y = y
        self.crect = pg.Rect((x, y), self.taille)
        # nouveau
        self.couleur = (140, 220, 250)
        self.cache = False

    # nouveau
    def touche_cible(self, pingouin):
        """Renvoie vrai si le pingouin touche la cible."""
        if pingouin.touche_truc(self):
            self.cache = True
            ping.cache = True

    # nouveau
    def coll_cibles(self):
        """Vérifie que la cible est dans une (autre) cible."""
        for cible in liste_cibles:
            x1, x2 = (cible.x, cible.y), (cible.x + cible.taille[0], cible.y)
            y1, y2 = (cible.x, cible.y + cible.taille[1]), (cible.x + cible.taille[0], cible.y + cible.taille[1])
            for truc in liste_cibles:
                x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
                y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
                hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
                hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
                basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
                bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
                if hg or basg or hd or bd:
                    self.change(truc)
            for truc in liste_murs:
                x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
                y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
                hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
                hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
                basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
                bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
                if hg or basg or hd or bd:
                    self.change(truc)
            for truc in liste_pingouins:
                x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
                y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
                hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
                hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
                basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
                bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
                if hg or basg or hd or bd:
                    self.change(truc)

    # nouveau
    def change(self, cible):
        """Change les coordonnées de la cible à changer."""
        if cible.x >= 100:
            cible.x += 10
        else:
            cible.x -= 10
        if cible.y >= 800:
            cible.y += 10
        else:
            cible.y -= 800
        self.coll_cibles()


pingcibles = random.randint(0, 15)
# cible1 = Cible(230, 240)
# mur1 = Mur(100, 100)
liste_murs = [Mur(random.randint(0, 800), random.randint(0, 1000), (120, 140)) for j in range(random.randint(1, 15))]
# ping = Pingouin(0, 0)
liste_pingouins = [Pingouin(random.randint(0, 800), random.randint(0, 1000)) for k in range(pingcibles)]
liste_cibles = [Cible(random.randint(0, 800), random.randint(0, 1000)) for i in range(pingcibles)]
runningf = True
while runningf:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            mouvements += 1
            for pingouin in liste_pingouins:
                if not pingouin.cache:
                    pingouin.move(event.key)
            for cible in liste_cibles:
                if not cible.cache:
                    for ping in liste_pingouins:
                        cible.touche_cible(ping)
    screen.blit(background, (0, 0))
    # pg.draw.rect(screen, cible1.couleur, cible1.crect)
    for cible in liste_cibles:
        if not cible.cache:
            pg.draw.rect(screen, cible.couleur, cible.crect)
    # pg.draw.rect(screen, (250, 250, 250), mur1.mrect)
    for mur in liste_murs:
        pg.draw.rect(screen, mur.couleur, mur.mrect)
    # pg.draw.rect(screen, (250, 250, 250), ping.prect)
    # pg.draw.rect(screen, (0, 0, 0), ping.prect, 1)
    for ping in liste_pingouins:
        if not ping.cache:
            pg.draw.rect(screen, (250, 250, 250), ping.prect)
            pg.draw.rect(screen, (0, 0, 0), ping.prect, 1)
    screen.blit(font.render(str(mouvements), 1, (0, 100, 255)), (960, 0))

    pg.display.flip()
pg.quit()
