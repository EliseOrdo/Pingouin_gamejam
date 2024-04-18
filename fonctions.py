import random
import sys 
import time 
import pygame as pg
import variables as var
import classes as clas


sys.setrecursionlimit(100000000)


def coll_pote(obj: object):
    """Verifie que la cible est dans une (autre) cible."""
    for i in range(len(obj)):
        x1 = (obj[i].x, obj[i].y)
        x2 = (obj[i].x + obj[i].taille[0], obj[i].y)
        y1 = (obj[i].x, obj[i].y + obj[i].taille[1])
        y2 = (obj[i].x + obj[i].taille[0], obj[i].y + obj[i].taille[1])
        for cib in range(len(var.liste_cibles)):
            x3 = (var.liste_cibles[cib].x, var.liste_cibles[cib].y)
            x4 = (var.liste_cibles[cib].x + var.liste_cibles[cib].taille[0], var.liste_cibles[cib].y)
            y3 = (var.liste_cibles[cib].x, var.liste_cibles[cib].y + var.liste_cibles[cib].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            haut = x1[1] < 0
            bas = x3[1] > var.fen_h
            gauche = x1[0] < 0
            droite = x2[0] > var.fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
                change(var.liste_cibles, cib)

        for m in range(len(var.liste_murs)):
            x3 = (var.liste_murs[m].x, var.liste_murs[m].y)
            x4 = (var.liste_murs[m].x + var.liste_murs[m].taille[0], var.liste_murs[m].y)
            y3 = (var.liste_murs[m].x, var.liste_murs[m].y + var.liste_murs[m].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            haut = x1[1] < 0
            bas = x3[1] > var.fen_h
            gauche = x1[0] < 0
            droite = x2[0] > var.fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
                change(var.liste_murs, m)

        for p in range(len(var.liste_pingouins)):
            x3 = (var.liste_pingouins[p].x, var.liste_pingouins[p].y)
            x4 = (var.liste_pingouins[p].x + var.liste_pingouins[p].taille[0], var.liste_pingouins[p].y)
            y3 = (var.liste_pingouins[p].x, var.liste_pingouins[p].y + var.liste_pingouins[p].taille[1])
            haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
            haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
            bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
            bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
            haut = x1[1] < 0
            bas = x3[1] > var.fen_h
            gauche = x1[0] < 0
            droite = x2[0] > var.fen_l
            if haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite:
                change(var.liste_pingouins, p)


def change(liste: list, ind: int):
    """Change les coordonnees de la cible a changer."""
    if liste[ind].x >= 1000:
        liste[ind].x -= 10
    elif liste[ind].x <= 0:
        liste[ind].x += 10
    if liste[ind].y >= 800:
        liste[ind].y -= 10
    elif liste[ind].y <= 0:
        liste[ind].y -= 10

    coll_pote(var.liste_cibles)
    coll_pote(var.liste_pingouins)
    coll_pote(var.liste_murs)


def compteur_temps():
    """
    Renvoie un tuple avec en position 0 les min a afficher et en position 1 les secondes
    """
    t = int(time.time() - var.start)
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

    
def coll(obj: object, liste: list):
    x1 = (obj.x, obj.y)
    x2 = (obj.x + obj.taille[0], obj.y)
    y1 = (obj.x, obj.y + obj.taille[1])
    y2 = (obj.x + obj.taille[0], obj.y + obj.taille[1])
    for cib in range(len(liste)):
        x3 = (liste[cib].x, liste[cib].y)
        x4 = (liste[cib].x + liste[cib].taille[0], liste[cib].y)
        y3 = (liste[cib].x, liste[cib].y + liste[cib].taille[1])
        hg = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        hd = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        basg = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bd = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        if hg or basg or hd or bd:
            return True
        

def memeligne(obj1: object, obj2: object):
    y1, y2 = obj1.y, obj1.y + obj1.taille[1]
    y3, y4 = obj2.y, obj2.y + obj2.taille[1]
    haut = y1 <= y3 <= y2
    bas = y1 <= y4 <= y2
    milieu = y3 <= y1 and y4 >= y2
    return haut or bas or milieu


def animcible(cible):
    dict_obj = {"Pingouins" : [p for p in var.liste_pingouins if not memeligne(cible, p)],
                "Murs" : [m for m in var.liste_murs if not memeligne(cible, m)],
                "Cibles" : [c for c in var.liste_cibles if not memeligne(cible, c)]}
    
    dessine(dict_obj)
    var.screen.blit(var.ci1, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    var.screen.blit(var.ci2, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    var.screen.blit(var.ci3, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    var.screen.blit(var.ci4, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))
    time.sleep(0.1)

    dessine(dict_obj)
    var.screen.blit(var.cache, (cible.x, cible.y))
    pg.display.update((cible.x, cible.y, 40, 40))


def dessine(dict: dict):
    """Prend en parametre un dictionnaire de forme : 
    d = {"Pingouins" : [], "Murs" : [], "Cibles" : []}
    et dessine les objets
    """
    for pingouin in dict["Pingouins"]:
        var.screen.blit(pingouin.image, (pingouin.x, pingouin.y))
    for mur in dict["Murs"]:
        var.screen.blit(var.ice, (mur.x, mur.y))
    for cible in dict["Cibles"]:
        var.screen.blit(var.ci, (cible.x, cible.y))
            

def creer_liste_murs(n: int):
    li = []
    while len(li) <= n:
        ajout = True
        m = clas.Mur(random.randint(0, var.fen_l-120), random.randint(0, var.fen_h-129), (120, 129))
        for j in range(len(li)):
            if coll(m, li):
                ajout = False
        if ajout:
            li.append(m)
    return li

def creer_liste_cibles(n: int):
    li = []
    while len(li) < n:
        ajout = True
        m = clas.Cible(random.randint(0, var.fen_l-40), random.randint(0, var.fen_h-40))
        for j in range(len(li)):
            if coll(m, li) or coll(m, var.liste_murs):
                ajout = False
        if ajout:
            li.append(m)
    return li

def creer_liste_pingouin(n: int):
    li = []
    while len(li) < n:
        ajout = True
        m = clas.Pingouin(random.randint(0, var.fen_l-18), random.randint(0, var.fen_h-17))
        for j in range(len(li)):
            if coll(m, li) or coll(m, var.liste_murs) or coll(m, var.liste_cibles):
                ajout = False
        if ajout:
            li.append(m)
            print("coo départ : ", m.x, " ", m.y )
    return li


def init():
    var.pingcibles = 5
    """var.pin = pg.image.load("dessins/ping.png").convert_alpha()"""
    var.liste_murs = creer_liste_murs(1)
    var.liste_cibles = creer_liste_cibles(var.pingcibles)
    var.liste_pingouins = creer_liste_pingouin(var.pingcibles)
    var.dict_obj = {
                "Pingouins" : [elt for elt in var.liste_pingouins],
                "Cibles" : [elt for elt in var.liste_cibles],
                "Murs" : [elt for elt in var.liste_murs]
                }
    var.cibles_touchees = 0
    var.start = time.time()
    var.tmps = compteur_temps()
    var.fini = False