import requests
import random
import sys 
import time 
import pygame as pg
import variables as var
import classes as clas


sys.setrecursionlimit(100000000)


def acc2speed(acc: list, vit_p : list):
    #PP_ADRESS/get?&
    url = var.PP_ADDRESS + "/get?" + ("&".join(var.PP_CHANNELS))
    data = requests.get(url=url).json()
    for i, channel in enumerate(var.PP_CHANNELS):
        saute = False
        value = data["buffer"][channel]["buffer"][0]
        if(value == None): value = 0  #si value==None, on ne peut pas la mettre dans notre array acc_p
        print ('Channel is : {}, value is : {} ,index is : {}'.format(channel,value,i) )
        if(value<=-5 or value>=5):
            if(acc[i] == var.m * value/5): 
                saute = True
            else : acc[i] = var.m * value/5
        else:
            if(acc[i] == 0) :
                saute = True
            else: acc[i] = 0
        print(acc[i])
        print("pingouin : \nax : {}\nay : {}\n".format(acc[0],acc[1]))
        if not saute:
            #on n'oublie pas de séparer les cas i=0 ou 1 parce que sinon le truc fait deux fois les additions et évidemment ça part dans e130
            if i ==1 :
                vit_p[0] += min(acc[1],100)
            if i ==0 :
                vit_p[1] += min(acc[0],100)
            print("pingouin : \nvx : {}\nvy : {}\n".format(vit_p[0],vit_p[1]))
    return vit_p


def position(ping , lvit_p: list):
    if(lvit_p[0] != 0):
        ping.x += lvit_p[0]  #x = x+v
        print("ping_x : ", ping.x)
    if(lvit_p[1] != 0):
        ping.y += lvit_p[1]   
        print("ping_y : ", ping.y)
    if(ping.x >= var.fen_l- ping.taille[0]) : 
        ping.x = var.fen_l - ping.taille[0] - 1
        lvit_p[0] = 0
    elif(ping.x <= 0): 
        ping.x = 1
        lvit_p[0] = 0
    if(ping.y >= var.fen_h - ping.taille[1]) : 
        ping.y = var.fen_h - ping.taille[1] - 1
        lvit_p[1] = 0
    elif(ping.y <= 0) : 
        ping.y = 1
        lvit_p[1] = 0
    #time.sleep(0.005)
    while ping.touche_qui_ou() is True:
            print("collision")
            if(lvit_p[1] > 0): 
                ping.orientation = 'bas'
                lvit_p[1] = 0
            elif(lvit_p[1] < 0): 
                ping.orientation = 'haut'
                lvit_p[1] = 0
            print("orientation : ", ping.orientation)
            match ping.orientation :
                case 'haut':
                    ping.y += 1
                case 'bas':
                    ping.y -= 1
            if(lvit_p[0] > 0): 
                ping.orientation = 'droite'
                lvit_p[0] = 0
            elif(lvit_p[0] < 0): 
                ping.orientation = 'gauche' 
                lvit_p[0] = 0
            print("orientation : ", ping.orientation)   
            match ping.orientation:
                case 'droite':
                    ping.x -= 1
                case 'gauche':
                    ping.x += 1
            print( "avant test x : ", ping.x, " y : ", ping.y)
            if(ping.x >= var.fen_l- ping.taille[0]) : 
                ping.x = var.fen_l - ping.taille[0] - 1
                ping.orientation = 'droite' # même si on change d'orientation alors qu'on a dépasssé le cadre, on remet le bon
                lvit_p[0] = 0
            elif(ping.x <= 0): 
                ping.x = 1
                ping.orientation = 'gauche'
                lvit_p[0] = 0
            if(ping.y >= var.fen_h - ping.taille[1]) : 
                ping.y = var.fen_h - ping.taille[1] - 1
                ping.orientation = 'bas'
                lvit_p[1] = 0
            elif(ping.y <= 0) : 
                ping.y = 1
                ping.orientation = 'haut'
                lvit_p[1] = 0
            print("après tests :", ping.x, " ", ping.y)
            ping.prect = pg.Rect((ping.x, ping.y), (20, 40))
    print( "x : ", ping.x, " y : ", ping.y)
    return lvit_p


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
    var.pingcibles = 1
    var.liste_murs = creer_liste_murs(5)
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

def fin():
    url = var.PP_ADDRESS + "/get?" + ("&".join(var.PP_CHANNELS))
    data = requests.get(url=url).json()
    for i, channel in enumerate(var.PP_CHANNELS):
        saute = False
        value = data["buffer"][channel]["buffer"][0]
        if value[2] <= -5:
            pg.quit()
            return 0
        elif value[2] >= 5:
            init()
            var.fini = False
            return 1