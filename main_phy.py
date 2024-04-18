"""les pengouins."""

import pygame as pg
import variables as var
import fonctions as func
import Phyphox2python as p2p


pg.init()
pg.font.init()


runningf = True

func.init()

while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        
    #Boucle pour le mouvement
    vitesse = p2p.acc2speed(p2p.acc, p2p.vit_p)  
    print("vitesse : ",vitesse[0]," et ", vitesse[1]) 
    for pingind in range(len(var.liste_pingouins)):
        if not var.liste_pingouins[pingind].cache:
            vitesse = p2p.position(var.liste_pingouins[pingind], vitesse)
            if abs(vitesse[0] < abs(vitesse[1])):
                if vitesse[1] > 0:
                    var.liste_pingouins[pingind].tourne('bas')
                elif vitesse[1] < 0:
                    var.liste_pingouins[pingind].tourne('haut')
            else:
                if vitesse[0] < 0:
                    var.liste_pingouins[pingind].tourne('gauche')
                elif vitesse[0] > 0:
                    var.liste_pingouins[pingind].tourne('droite')                   
            print("position ", "indice ",pingind)
    for ciblind in range(len(var.liste_cibles)):
        if not var.liste_cibles[ciblind].cache:
            for ping in range(len(var.liste_pingouins)):
                if var.liste_cibles[ciblind].touche_cible(var.liste_pingouins[ping]):
                    func.animcible(var.liste_cibles[ciblind])            

    # PARTIE DESSIN
    var.screen.blit(var.wallpaper, (0, 0))
    func.dessine(var.dict_obj)
    if var.cibles_touchees == var.pingcibles:
        var.fini = True
        text_fin = var.font.render("Bravo !!", 10, (0, 100, 255))
        txt = var.font.render("Recommencer ?", 10, (0, 100, 255))
        t = var.font.render("monter : oui, descendre : non", 10, (0, 100, 255))
        var.screen.blit(text_fin, (var.fen_l/2-35, var.fen_h/2-5))
        var.screen.blit(txt, (var.fen_l/2 - 70, var.fen_h/2 + 15))
        var.screen.blit(t, (var.fen_l/2-120, var.fen_h/2 + 35))
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
    else:
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
        var.tmps = func.compteur_temps()
    pg.display.flip()
pg.quit()