"""les pengouins."""
import pygame as pg
import random
import sys
import time
import numpy

sys.setrecursionlimit(100000000)

pg.init()
fen_l = 1000
fen_h = 800
screen = pg.display.set_mode((fen_l, fen_h))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))


pin = pg.image.load("dessins/ping.png").convert_alpha()
ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()

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
        """Verifie si le pingouin touche le truc (le truc doit avoir x et y en parametre)."""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        return haut_gauche or bas_gauche or haut_droit or bas_droit

    def touche_qui_ou(self):
        """Renvoie le mur touche par le pingouin, et sur quelle moitie de cote."""
        for mur in liste_murs:
            if self.touche_truc(mur):
                touche = True
        for pin in liste_pingouins:
            if self.touche_truc(pin):
                touche = True
        return touche

    def move(self, touche):
        """Fait bouger le pingouin."""
        global mouvements
        global pin
        vit = 22
        if self.touche_qui_ou() is False:
            #Mouvement

            match touche:
                case pg.K_UP:
                    self.y -= vit
                case pg.K_DOWN:
                    self.y += vit
                case pg.K_RIGHT:
                    self.x += vit
                case pg.K_LEFT:
                    self.x -= vit
                

            
        while self.touche_qui_ou() is True:
            match touche :
                case pg.K_UP:
                    self.y += 1
                case pg.K_DOWN:
                    self.y -= 1
                case pg.K_RIGHT:
                    self.x -= 1
                case pg.K_LEFT:
                    self.x += 1
            self.prect = pg.Rect((self.x, self.y), (20, 40))

    def tourne(self, touche):
        
        global pin
        
        #Rotation
        match self.orientation:
            case 'haut':
                match touche :
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                print(self.orientation)
            
            case 'droite':
                match touche:
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                print(self.orientation)

            case 'gauche':
                match touche:
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                print(self.orientation)

            case 'bas':
                match touche :
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                print(self.orientation)

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
        self.anim = False

    def touche_cible(self, pingouin):
        """Renvoie vrai si le pingouin touche la cible."""
        global cibles_touchees
        if pingouin.touche_truc(self):
            self.cache = True
            cibles_touchees += 1
            pingouin.cache = True
            self.anim = True
            # But : soit mettre le pingouin au centre de la cible puis le faire disparaitre
            # Met le pingouin au centre de la cible
            screen.blit(cache, (pingouin.x, pingouin.y))
            screen.blit(ci, (self.x, self.y))
            pg.display.update(pg.Rect(pingouin.x, pingouin.y, 40, 40))
            print(pingouin.x, pingouin.y)
            print(self.x, self.y)
            pg.display.update(pg.Rect(self.x, self.y, 40, 40))



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
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if haut_gauche or bas_gauche or haut_droit or bas_droit:
                change(liste_cibles, cib)

        for m in range(len(liste_murs)):
            x3, x4 = (liste_murs[m].x, liste_murs[m].y), (liste_murs[m].x + liste_murs[m].taille[0], liste_murs[m].y)
            y3, y4 = (liste_murs[m].x, liste_murs[m].y + liste_murs[m].taille[1]), (liste_murs[m].x + liste_murs[m].taille[0],
                                                                                    liste_murs[m].y + liste_murs[m].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if haut_gauche or bas_gauche or haut_droit or bas_droit:
                change(liste_murs, m)

        for p in range(len(liste_pingouins)):
            x3, x4 = ((liste_pingouins[p].x, liste_pingouins[p].y),
                      (liste_pingouins[p].x + liste_pingouins[p].taille[0], liste_pingouins[p].y))
            y3, y4 = ((liste_pingouins[p].x, liste_pingouins[p].y + liste_pingouins[p].taille[1]),
                      (liste_pingouins[p].x + liste_pingouins[p].taille[0], liste_pingouins[p].y + liste_pingouins[p].taille[1]))
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            if haut_gauche or bas_gauche or haut_droit or bas_droit:
                change(liste_pingouins, p)


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



# pg.Rect.colliderect(Rect) pour collisions entre 2 rectangles pas penchés

def compteur_temps():
    """
    Renvoie un tuple avec en position 0 les min a afficher et en position 1 les secondes
    """
    global start
    t = int(time.time() - start)
    sec = str(t%60) + ' sec'
    if t%60 < 10 :
        sec = '0' + sec
    min = ''
    if t >= 60 :
        if t < 600 : 
            min = '0' + str(t//60) + ' min'
        else :
            min = str(t//60) + ' min'
    return (min, sec)


"""def collautres(obj , liste):
    if len(liste)<=1:
        return False
    for elt in liste[1::]:
        if pg.Rect(obj.x,obj.y,obj.taille).colliderect(elt):
            return True
    return False"""
    
def coll(obj, liste):
    x1, x2 = (obj.x, obj.y), (obj.x + obj.taille[0], obj.y)
    y1, y2 = (obj.x, obj.y + obj.taille[1]), (obj.x + obj.taille[0], obj.y + obj.taille[1])
    for cib in range(len(liste)):
        x3, x4 = (liste[cib].x, liste[cib].y), (
            liste[cib].x + liste[cib].taille[0], liste[cib].y)
        y3, y4 = (liste[cib].x, liste[cib].y + liste[cib].taille[1]), (
            liste[cib].x + liste[cib].taille[0], liste[cib].y + liste[cib].taille[1])
        hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        if hg or basg or hd or bd:
            #change(liste_cibles, cib)
            return True


# pingcibles = random.randint(1, 10)
pingcibles = 17

pin = pg.image.load("dessins/ping.png").convert_alpha()
cache = pg.image.load("dessins/snow.png").convert_alpha()
ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()
ci1 = pg.image.load("dessins/t1.png").convert_alpha()
ci2 = pg.image.load("dessins/t2.png").convert_alpha()
ci3 = pg.image.load("dessins/t3.png").convert_alpha()
ci4 = pg.image.load("dessins/t4.png").convert_alpha()

# Fait les listes

liste_murs = [Mur(random.randint(0, 800), random.randint(0, 1000), (119, 129)) for j in range(random.randint(1, 2))]
liste_pingouins = [Pingouin(random.randint(0, 800), random.randint(0, 1000)) for k in range(pingcibles)]
liste_cibles = [Cible(random.randint(0, 800), random.randint(0, 1000)) for i in range(pingcibles)]
coll_pote(liste_pingouins)
coll_pote(liste_murs)
coll_pote(liste_cibles)

cibles_touchees = 0

runningf = True
while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:

            liste_pingouins[0].tourne(event.key)
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
        if ciblind.anim:
            screen.blit(ci1, (ciblind.x, ciblind.y))
            pg.display.update((ciblind.x, ciblind.y, 40, 40))
            time.sleep(0.2)
            screen.blit(ci2, (ciblind.x, ciblind.y))
            pg.display.update((ciblind.x, ciblind.y, 40, 40))
            time.sleep(0.2)
            screen.blit(ci3, (ciblind.x, ciblind.y))
            pg.display.update((ciblind.x, ciblind.y, 40, 40))
            time.sleep(0.2)
            screen.blit(ci4, (ciblind.x, ciblind.y))
            pg.display.update((ciblind.x, ciblind.y, 40, 40))
            time.sleep(0.2)
            screen.blit(cache, (ciblind.x, ciblind.y))
            pg.display.update((ciblind.x, ciblind.y, 40, 40))
            ciblind.anim = False
    for murind in range(len(liste_murs)):
        screen.blit(ice, (liste_murs[murind].x, liste_murs[murind].y))
    for pingind in range(len(liste_pingouins)):
        if not liste_pingouins[pingind].cache:
            screen.blit(pin, (liste_pingouins[pingind].x, liste_pingouins[pingind].y))
    #screen.blit(font.render(str(mouvements), 1, (0, 100, 255)), (960, 0))
    if cibles_touchees == pingcibles:
        text_fin = font.render("Bravo !!", 10, (0, 100, 255))
        screen.blit(text_fin, (fen_l/2-35, fen_h/2-5))
        #screen.blit(font.render(t, 10, (0,100,255)), (fen_l/2-145, fen_h/2 + 15))
    screen.blit(font.render(compteur_temps()[1], 1, (0, 100, 255)), (950, 0))
    screen.blit(font.render(compteur_temps()[0], 1, (0, 100, 255)), (895, 0))
    pg.display.flip()
pg.quit()