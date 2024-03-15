"""les pengouins."""
import pygame as pg
import random
import sys

#sys.setrecursionlimit(100000000)

pg.init()
screen = pg.display.set_mode((1000, 800))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

mouvements = 0
font = pg.font.Font(None, 24)
text = font.render(str(mouvements), 1, (0, 100, 255))


class Pingouin:
    """definie un pingouin."""

    def __init__(self, x, y):
        self.taille = (18, 17)
        # (width = horizontal = axe x, height = vertical = axe y)
        self.x = x
        self.y = y
        # Le point (x,y) est le point en haut a gauche de rectangle.
        self.prect = pg.Rect((self.x, self.y), self.taille)
        self.cache = False
        self.orientation = 'haut'

    def touche_truc(self, truc):
        """Verifie si le pinguoin touche le truc (le truc doit avoir x et y en parametre)."""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        h = 0 > x1[1]
        ga = 0 > x1[0]
        d = y2[0] > 1000
        b = y1[1] > 800
        return hg or basg or hd or bd or h or ga or d or b

    def touche_qui_ou(self):
        """Renvoie le mur touche par le pingouin, et sur quelle moitie de cote."""
        for mur in liste_murs:
            if self.touche_truc(mur):
                return True
        return False

    @staticmethod
    def perdu():
        """Le texte quand c'est perdu."""
        fon = pg.font.Font(None, 50)
        screen.blit(fon.render("PERDUUUU", 1, (0, 100, 255)), (425, 350))

    def move(self, touche):
        """Fait bouger le pingouin."""
        global mouvements
        global g
        global pin
        vit = 22
        if self.touche_qui_ou() is False:
            
            #Mouvement
            if touche == pg.K_UP:
                self.y -= vit
            elif touche == pg.K_DOWN:
                self.y += vit
            elif touche == pg.K_RIGHT:
                self.x += vit
            elif touche == pg.K_LEFT:
                self.x -= vit
            
            #Rotation
            if self.orientation == 'haut':
                if touche == pg.K_RIGHT:
                    self.orientation = 'droite'
                    pin = pg.transform.rotate(pin, -90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_DOWN:
                    self.orientation = 'bas'
                    pin = pg.transform.rotate(pin, 180)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_LEFT:
                    self.orientation = 'gauche'
                    pin = pg.transform.rotate(pin, 90)
                    screen.blit(pin, (self.x, self.y))
            
            elif self.orientation == 'droite':
                if touche == pg.K_UP:
                    self.orientation = 'haut'
                    pin = pg.transform.rotate(pin, 90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_DOWN:
                    self.orientation = 'bas'
                    pin = pg.transform.rotate(pin, -90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_LEFT:
                    self.orientation = 'gauche'
                    pin = pg.transform.rotate(pin, 180)
                    screen.blit(pin, (self.x, self.y))

            elif self.orientation == 'gauche':
                if touche == pg.K_UP:
                    self.orientation = 'haut'
                    pin = pg.transform.rotate(pin, -90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_DOWN:
                    self.orientation = 'bas'
                    pin = pg.transform.rotate(pin, 90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_RIGHT:
                    self.orientation = 'droite'
                    pin = pg.transform.rotate(pin, 180)
                    screen.blit(pin, (self.x, self.y))

            if self.orientation == 'bas':
                if touche == pg.K_RIGHT:
                    self.orientation = 'droite'
                    pin = pg.transform.rotate(pin, 90)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_UP:
                    self.orientation = 'haut'
                    pin = pg.transform.rotate(pin, 180)
                    screen.blit(pin, (self.x, self.y))
                elif touche == pg.K_LEFT:
                    self.orientation = 'gauche'
                    pin = pg.transform.rotate(pin, -90)
                    screen.blit(pin, (self.x, self.y))

            self.prect = pg.Rect((self.x, self.y), (20, 40))
            print(self.orientation)
            

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


class Mur:
    """Un mur."""

    def __init__(self, x, y, taille):
        self.taille = taille
        self.x = x
        self.y = y
        self.couleur = (250, 250, 250)


class Cible:
    """Je propose que le but soit d'aller dans l'eau, genre pour chercher du poisson."""

    def __init__(self, x, y):
        self.taille = (40, 40)
        self.x = x
        self.y = y
        self.couleur = (140, 220, 250)
        self.cache = False

    def touche_cible(self, pingouin):
        """Renvoie vrai si le pingouin touche la cible."""
        if pingouin.touche_truc(self):
            self.cache = True
            pingouin.cache = True


def coll_pote(obj):
    """Verifie que la cible est dans une (autre) cible."""
    for i in range(len(obj)):
        x1, x2 = (obj[i].x, obj[i].y), (obj[i].x + obj[i].taille[0], obj[i].y)
        y1, y2 = (obj[i].x, obj[i].y + obj[i].taille[1]), (obj[i].x + obj[i].taille[0], obj[i].y + obj[i].taille[1])
        for cib in range(len(liste_cibles)):
            x3, x4 = (liste_cibles[cib].x, liste_cibles[cib].y), (
                liste_cibles[cib].x + liste_cibles[cib].taille[0], liste_cibles[cib].y)
            y3, y4 = (liste_cibles[cib].x, liste_cibles[cib].y + liste_cibles[cib].taille[1]), (
                liste_cibles[cib].x + liste_cibles[cib].taille[0], liste_cibles[cib].y + liste_cibles[cib].taille[1])
            hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if hg or basg or hd or bd:
                change(liste_cibles, cib)
        for c in range(len(liste_murs)):
            x3, x4 = (liste_murs[c].x, liste_murs[c].y), (liste_murs[c].x + liste_murs[c].taille[0], liste_murs[c].y)
            y3, y4 = (liste_murs[c].x, liste_murs[c].y + liste_murs[c].taille[1]), (
                liste_murs[c].x + liste_murs[c].taille[0], liste_murs[c].y + liste_murs[c].taille[1])
            hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if hg or basg or hd or bd:
                change(liste_murs, c)
        for truc in range(len(liste_pingouins)):
            x3, x4 = (liste_pingouins[truc].x, liste_pingouins[truc].y), (
                liste_pingouins[truc].x + liste_pingouins[truc].taille[0], liste_pingouins[truc].y)
            y3, y4 = (liste_pingouins[truc].x, liste_pingouins[truc].y + liste_pingouins[truc].taille[1]), (
                liste_pingouins[truc].x + liste_pingouins[truc].taille[0],
                liste_pingouins[truc].y + liste_pingouins[truc].taille[1])
            hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if hg or basg or hd or bd:
                change(liste_pingouins, truc)


def change(liste, ind):
    """Change les coordonnees de la cible a changer."""
    if liste[ind].x >= 1000:
        liste[ind].x -= 10
    elif liste[ind].x <= 0:
        liste[ind].x += 10
    if liste[ind].y >= 800:
        liste[ind].y -= 10
    elif liste[ind].y <= 0:
        liste[ind].y -= 10

    coll_pote(liste_cibles)

    coll_pote(liste_pingouins)

    coll_pote(liste_murs)


# pingcibles = random.randint(1, 10)
pingcibles = 1

pin = pg.image.load("dessins/ping.png").convert_alpha()
ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()

# Fait les listes

liste_murs = [Mur(random.randint(0, 800), random.randint(0, 1000), (119, 129)) for j in range(random.randint(1, 2))]
liste_pingouins = [Pingouin(random.randint(0, 800), random.randint(0, 1000)) for k in range(pingcibles)]
liste_cibles = [Cible(random.randint(0, 800), random.randint(0, 1000)) for i in range(pingcibles)]
coll_pote(liste_pingouins)
coll_pote(liste_murs)
coll_pote(liste_cibles)

runningf = True
while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            mouvements += 1
            for pingind in range(len(liste_pingouins)):
                if not liste_pingouins[pingind].cache:
                    liste_pingouins[pingind].move(event.key)
            for ciblind in range(len(liste_cibles)):
                if not liste_cibles[ciblind].cache:
                    for ping in range(len(liste_pingouins)):
                        liste_cibles[ciblind].touche_cible(liste_pingouins[ping])
    # PARTIE DESSIN
    screen.blit(wallpaper, (0, 0))
    for ciblind in liste_cibles:
        if not ciblind.cache:
            screen.blit(ci, (ciblind.x, ciblind.y))
    for murind in range(len(liste_murs)):
        screen.blit(ice, (liste_murs[murind].x, liste_murs[murind].y))
    for pingind in range(len(liste_pingouins)):
        if not liste_pingouins[pingind].cache:
            screen.blit(pin, (liste_pingouins[pingind].x, liste_pingouins[pingind].y))
    screen.blit(font.render(str(mouvements), 1, (0, 100, 255)), (960, 0))
    pg.display.flip()
pg.quit()
