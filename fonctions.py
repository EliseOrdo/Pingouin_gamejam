import random
import sys
#import Phyphox2python as p2p
import time
from variables import *
import classes

sys.setrecursionlimit(100000000)


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
            

def creer_liste_murs(n):
    li = []
    while len(li) <= n:
        ajout = True
        m = classes.Mur(random.randint(0, fen_l-120), random.randint(0, fen_h-129), (120, 129))
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
        m = classes.Cible(random.randint(0, fen_l-40), random.randint(0, fen_h-40))
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
        m = classes.Pingouin(random.randint(0, fen_l-18), random.randint(0, fen_h-17))
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