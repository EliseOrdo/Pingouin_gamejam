"""les pengouins."""
import pygame as pg
import random
import sys
#import Phyphox2python as p2p
import time

sys.setrecursionlimit(100000000)

pg.init()
fen_l = 1000
fen_h = 700
screen = pg.display.set_mode((fen_l, fen_h))

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))


pin = pg.image.load("dessins/ping.png").convert_alpha()
ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()
cache = pg.image.load("dessins/snow.png").convert_alpha()
ci1 = pg.image.load("dessins/t1.png").convert_alpha()
ci2 = pg.image.load("dessins/t2.png").convert_alpha()
ci3 = pg.image.load("dessins/t3.png").convert_alpha()
ci4 = pg.image.load("dessins/t4.png").convert_alpha()

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
        """Verifie si le pingouin touche le truc (le truc doit avoir x et y en parametre).
            x1 : haut gauche de self, x2 : haut droit de self y1 bas gauche de self et y2 bas droit de self
            x3, x4, y3, y4 : meme chose pour truc"""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        haut = x1[1] < 0
        bas = y1[1] > fen_h
        gauche = x1[0] < 0
        droite = x2[0] > fen_l
        return haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite

    def touche_qui_ou(self):
        """Renvoie le mur touché par le pingouin"""
        for mur in liste_murs:
            if self.touche_truc(mur):
                return True
        return False

    def move(self, touche):
        """Fait bouger le pingouin."""
        global mouvements
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
                (self.orientation)

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
                (self.orientation)

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
                (self.orientation)

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

    def touche_cible(self, pingouin, key):
        """Renvoie vrai si le pingouin touche la cible."""
        global cibles_touchees
        global dict_obj
        if pingouin.touche_truc(self):
            self.cache = True
            if self in dict_obj['Cibles']:
                dict_obj['Cibles'].remove(self)
            cibles_touchees += 1
            pingouin.cache = True
            dict_obj['Pingouins'].remove(pingouin)
            self.anim = True
            match key:
                case pg.K_DOWN:
                    screen.blit(cache, (pingouin.x, pingouin.y - 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y - 22, 40, 40))
                case pg.K_UP:
                    screen.blit(cache, (pingouin.x, pingouin.y + 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y + 22, 40, 40))
                case pg.K_LEFT:
                    screen.blit(cache, (pingouin.x + 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x + 22, pingouin.y, 40, 40))
                case pg.K_RIGHT:
                    screen.blit(cache, (pingouin.x - 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x - 22, pingouin.y, 40, 40))
            screen.blit(ci, (self.x, self.y))
            pg.display.update(pg.Rect(self.x, self.y, 40, 40))
            animcible(self)



def coll_pote(obj):
    """Verifie que la cible est dans une (autre) cible."""
    for i in range(len(obj)):
        x1, x2 = (obj[i].x, obj[i].y), (obj[i].x + obj[i].taille[0], obj[i].y)
        y1, y2 = (obj[i].x, obj[i].y + obj[i].taille[1]), (obj[i].x + obj[i].taille[0], obj[i].y + obj[i].taille[1])
        for cib in range(len(liste_cibles)):
            x3, x4 = (liste_cibles[cib].x, liste_cibles[cib].y), (liste_cibles[cib].x + liste_cibles[cib].taille[0], liste_cibles[cib].y)
            y3, y4 = (liste_cibles[cib].x, liste_cibles[cib].y + liste_cibles[cib].taille[1]), (
                liste_cibles[cib].x + liste_cibles[cib].taille[0], liste_cibles[cib].y + liste_cibles[cib].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            haut = x1[1] < 0
            bas = x3[1] > fen_h
            gauche = x1[0] < 0
            droite = x2[0] > fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
                change(liste_cibles, cib)

        for m in range(len(liste_murs)):
            x3, x4 = (liste_murs[m].x, liste_murs[m].y), (liste_murs[m].x + liste_murs[m].taille[0], liste_murs[m].y)
            y3, y4 = (liste_murs[m].x, liste_murs[m].y + liste_murs[m].taille[1]), (liste_murs[m].x + liste_murs[m].taille[0],
                                                                                    liste_murs[m].y + liste_murs[m].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            haut = x1[1] < 0
            bas = x3[1] > fen_h
            gauche = x1[0] < 0
            droite = x2[0] > fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
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
            haut = x1[1] < 0
            bas = x3[1] > fen_h
            gauche = x1[0] < 0
            droite = x2[0] > fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
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
        

def memeligne(obj1, obj2):
    y1, y2 = (obj1.y, obj1.y + obj1.taille[1])
    y3, y4 = (obj2.y, obj2.y + obj2.taille[1])
    haut = y1 <= y3 <= y2
    bas = y1 <= y4 <= y2
    milieu = y3 <= y1 and y4 >= y2
    return haut or bas or milieu


def animcible(cible):
    dict_obj = {"Pingouins" : [p for p in liste_pingouins if not memeligne(cible, p)],
                "Murs" : [m for m in liste_murs if not memeligne(cible, m)],
                "Cibles" : [c for c in liste_cibles if not memeligne(cible, c)]}
    
    dessine(dict_obj)
    screen.blit(ci1, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    screen.blit(ci2, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    screen.blit(ci3, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    screen.blit(ci4, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    screen.blit(cache, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))


def dessine(dict):
    """Prend en parametre un dictionnaire de forme : 
    d = {"Pingouins" : [], "Murs" : [], "Cibles" : []}
    et dessine les objets
    """
    for pingouin in dict["Pingouins"]:
        screen.blit(pin, (pingouin.x, pingouin.y))
    for mur in dict["Murs"]:
        screen.blit(ice, (mur.x, mur.y))
    for cible in dict["Cibles"]:
        screen.blit(ci, (cible.x, cible.y))
            

# Fait les listes

def creer_liste_murs(n):
    li = []
    while len(li) <= n:
        ajout = True
        m = Mur(random.randint(0, fen_l-120), random.randint(0, fen_h-129), (120, 129))
        for j in range(len(li)):
            if coll(m, li):
                ajout = False
        if ajout:
            li.append(m)
    return li

def creer_liste_cibles(n):
    li = []
    while len(li) < n:
        ajout = True
        m = Cible(random.randint(0, fen_l-40), random.randint(0, fen_h-40))
        for j in range(len(li)):
            if coll(m, li) or coll(m, liste_murs):
                ajout = False
        if ajout:
            li.append(m)
    return li

def creer_liste_pingouin(n):
    li = []
    while len(li) < n:
        ajout = True
        m = Pingouin(random.randint(0, fen_l-18), random.randint(0, fen_h-17))
        for j in range(len(li)):
            if coll(m, li) or coll(m, liste_murs) or coll(m, liste_cibles):
                ajout = False
        if ajout:
            li.append(m)
    return li


def init():
    global pingcibles, liste_murs, liste_cibles, liste_pingouins, dict_obj, cibles_touchees, start, tmps, fini, pin
    pingcibles = random.randint(1, 2)
    pin = pg.image.load("dessins/ping.png").convert_alpha()
    liste_murs = creer_liste_murs(5)
    liste_cibles = creer_liste_cibles(pingcibles)
    liste_pingouins = creer_liste_pingouin(pingcibles)
    dict_obj = {
                "Pingouins" : [elt for elt in liste_pingouins],
                "Cibles" : [elt for elt in liste_cibles],
                "Murs" : [elt for elt in liste_murs]
                }
    cibles_touchees = 0
    start = time.time()
    tmps = compteur_temps()
    fini = False


runningf = True
init()
while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            if fini:
                match event.key:
                    case pg.K_o:
                        init()
                    case pg.K_n:
                        pg.quit()
            liste_pingouins[0].tourne(event.key)
            for pingind in range(len(liste_pingouins)):
                if not liste_pingouins[pingind].cache:
                    liste_pingouins[pingind].move(event.key)
            for ciblind in range(len(liste_cibles)):
                if not liste_cibles[ciblind].cache:
                    for ping in range(len(liste_pingouins)):
                        liste_cibles[ciblind].touche_cible(liste_pingouins[ping], event.key)
    # PARTIE DESSIN
    screen.blit(wallpaper, (0, 0))
    dessine(dict_obj)
    if cibles_touchees == pingcibles:
        fini = True
        text_fin = font.render("Bravo !!", 10, (0, 100, 255))
        screen.blit(text_fin, (fen_l/2-35, fen_h/2-5))
        txt = font.render("Recommencer ? (o , n)", 10, (0, 100, 255))
        screen.blit(txt, (fen_l/2 - 85, fen_h/2 + 15))
        #screen.blit(font.render(t, 10, (0,100,255)), (fen_l/2-145, fen_h/2 + 15))
        screen.blit(font.render(tmps[1], 1, (0, 100, 255)), (950, 0))
        screen.blit(font.render(tmps[0], 1, (0, 100, 255)), (895, 0))
    else:
        screen.blit(font.render(tmps[1], 1, (0, 100, 255)), (950, 0))
        screen.blit(font.render(tmps[0], 1, (0, 100, 255)), (895, 0))
        tmps = compteur_temps()
    pg.display.flip()
pg.quit()